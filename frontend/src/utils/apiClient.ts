import { auth } from '../firebase/config';
import { getApiBaseUrl } from '../config/api';

interface ApiErrorData {
  message?: string;
  detail?: string | Array<{ loc: string[]; msg: string; type: string }>; // For FastAPI validation errors
  // Add other potential error structures if known
}

export class ApiError extends Error {
  status: number;
  errorData?: ApiErrorData;

  constructor(message: string, status: number, errorData?: ApiErrorData) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.errorData = errorData;
    Object.setPrototypeOf(this, ApiError.prototype);
  }
}

export const apiClient = async <T = any>(url: string, options: RequestInit = {}): Promise<T> => {
  const headers = new Headers(options.headers || {});
  let idToken: string | null = null;

  if (auth.currentUser) {
    try {
      idToken = await auth.currentUser.getIdToken();
      headers.set('Authorization', `Bearer ${idToken}`);
    } catch (error) {
      console.error('Error getting ID token:', error);
      // Optionally, you could throw a specific error here or handle it based on requirements
    }
  }

  const method = options.method?.toUpperCase();
  if (idToken && (method === 'POST' || method === 'PUT' || method === 'PATCH')) {
    if (!headers.has('Content-Type')) {
      headers.set('Content-Type', 'application/json');
    }
  }

  const fullUrl = `${getApiBaseUrl()}${url}`;

  const fetchOptions: RequestInit = {
    ...options,
    headers,
  };

  const response = await fetch(fullUrl, fetchOptions);

  if (!response.ok) {
    let errorData: ApiErrorData | null = null;
    let errorMessage = `Request failed with status ${response.status}`;
    try {
      errorData = await response.json();
      if (errorData) {
        if (typeof errorData.detail === 'string') {
          errorMessage = errorData.detail;
        } else if (Array.isArray(errorData.detail)) {
          // Handle FastAPI validation errors specifically if needed
          errorMessage = errorData.detail.map(err => `${err.loc.join('.')} - ${err.msg}`).join('; ');
        } else if (errorData.message) {
          errorMessage = errorData.message;
        }
      }
    } catch (e) {
      // Parsing JSON failed, use statusText or default message
      errorMessage = response.statusText || errorMessage;
    }
    throw new ApiError(errorMessage, response.status, errorData || undefined);
  }

  // Handle cases where response might be empty (e.g., 204 No Content)
  if (response.status === 204) {
    return Promise.resolve(null as any); // Or undefined, depending on how you want to handle it
  }

  return response.json();
};
