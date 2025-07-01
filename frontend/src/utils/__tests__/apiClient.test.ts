import { apiClient, ApiError } from '../apiClient';
import { auth } from '../../firebase/config';
import { getApiBaseUrl } from '../../config/api';

// Mock Firebase and Config modules
jest.mock('../../firebase/config', () => ({
  auth: {
    currentUser: null, // Default to no user
  },
}));

jest.mock('../../config/api', () => ({
  getApiBaseUrl: jest.fn(() => 'http://localhost:8123/api/v1'), // Mock API base URL
}));

// Mock global fetch
global.fetch = jest.fn();

describe('apiClient', () => {
  beforeEach(() => {
    // Reset mocks before each test
    (fetch as jest.Mock).mockClear();
    // Reset auth.currentUser for each test, can be overridden within tests
    auth.currentUser = null;
    // Reset getIdToken mock if it was set on a specific user object
    if (auth.currentUser && (auth.currentUser as any).getIdToken) {
        delete (auth.currentUser as any).getIdToken;
    }
  });

  // Test F_AC1
  test('F_AC1: sends token and default Content-Type if user is logged in for POST', async () => {
    const mockUser = {
      getIdToken: jest.fn(async () => 'test_token_123'),
    };
    auth.currentUser = mockUser as any; // Type assertion for simplicity in mock

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: 'success' }),
    });

    const postData = { key: 'value' };
    await apiClient('/test-endpoint', { method: 'POST', body: JSON.stringify(postData) });

    expect(fetch).toHaveBeenCalledTimes(1);
    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:8123/api/v1/test-endpoint',
      expect.objectContaining({
        method: 'POST',
        headers: expect.objectContaining({
          'Authorization': 'Bearer test_token_123',
          'Content-Type': 'application/json',
        }),
        body: JSON.stringify(postData),
      })
    );
    expect(mockUser.getIdToken).toHaveBeenCalledTimes(1);
  });

  // Test F_AC1 (variant for GET to ensure Content-Type is not added by default)
  test('F_AC1_GET: sends token but not default Content-Type for GET', async () => {
    const mockUser = {
      getIdToken: jest.fn(async () => 'test_token_get'),
    };
    auth.currentUser = mockUser as any;

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: 'success' }),
    });

    await apiClient('/test-get-endpoint', { method: 'GET' });

    expect(fetch).toHaveBeenCalledTimes(1);
    const fetchCallArgs = (fetch as jest.Mock).mock.calls[0];
    const headers = fetchCallArgs[1].headers as Headers; // apiClient creates Headers object
    expect(headers.get('Authorization')).toBe('Bearer test_token_get');
    expect(headers.has('Content-Type')).toBe(false); // Should not have Content-Type for GET
    expect(mockUser.getIdToken).toHaveBeenCalledTimes(1);
  });


  // Test F_AC2
  test('F_AC2: does NOT send token if user is not logged in', async () => {
    auth.currentUser = null; // Ensure no user

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: 'success' }),
    });

    await apiClient('/test-endpoint');

    expect(fetch).toHaveBeenCalledTimes(1);
    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:8123/api/v1/test-endpoint',
      expect.objectContaining({
        headers: expect.not.objectContaining({
          'Authorization': expect.any(String),
        }),
      })
    );
  });

  // Test F_AC3
  test('F_AC3: handles successful JSON response', async () => {
    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: 'done' }),
    });

    const result = await apiClient('/success');
    expect(result).toEqual({ message: 'done' });
  });

  // Test F_AC4
  test('F_AC4: handles 204 No Content response', async () => {
    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      status: 204,
      // json: async () => Promise.reject(new Error("Should not call json() for 204")) // fetch itself won't have json method for 204
    });

    const result = await apiClient('/no-content');
    expect(result).toBeNull();
  });

  // Test F_AC5
  test('F_AC5: throws ApiError on HTTP error with JSON response', async () => {
    const errorDetail = { detail: 'Bad Request Details' };
    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: false,
      status: 400,
      json: async () => errorDetail,
      statusText: 'Bad Request',
    });

    try {
      await apiClient('/error-json');
      fail('ApiError was not thrown'); // Should not reach here
    } catch (error) {
      expect(error).toBeInstanceOf(ApiError);
      const apiError = error as ApiError;
      expect(apiError.status).toBe(400);
      expect(apiError.message).toBe('Bad Request Details');
      expect(apiError.errorData).toEqual(errorDetail);
    }
  });

  test('F_AC5_NonJSON: throws ApiError on HTTP error with non-JSON response', async () => {
    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: false,
      status: 500,
      json: async () => { throw new Error("Simulating JSON parse error"); }, // Simulate JSON parsing failure
      statusText: 'Internal Server Error',
    });

    try {
      await apiClient('/error-non-json');
      fail('ApiError was not thrown');
    } catch (error) {
      expect(error).toBeInstanceOf(ApiError);
      const apiError = error as ApiError;
      expect(apiError.status).toBe(500);
      expect(apiError.message).toBe('Internal Server Error'); // Falls back to statusText
      expect(apiError.errorData).toBeUndefined();
    }
  });

  // Test F_AC6
  test('F_AC6: correctly sets Content-Type for POST with token', async () => {
    const mockUser = {
      getIdToken: jest.fn(async () => 'a_token'),
    };
    auth.currentUser = mockUser as any;

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: 'success' }),
    });

    await apiClient('/test-post', { method: 'POST', body: JSON.stringify({ key: 'value' }) });

    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:8123/api/v1/test-post',
      expect.objectContaining({
        headers: expect.objectContaining({
          'Content-Type': 'application/json',
          'Authorization': 'Bearer a_token',
        }),
      })
    );
  });

  // Test F_AC7
  test('F_AC7: does not override existing Content-Type', async () => {
    const mockUser = {
      getIdToken: jest.fn(async () => 'a_token'),
    };
    auth.currentUser = mockUser as any;

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: 'success' }),
    });

    await apiClient('/test-post-custom-type', {
      method: 'POST',
      body: 'text data',
      headers: {'Content-Type': 'text/plain'}
    });

    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:8123/api/v1/test-post-custom-type',
      expect.objectContaining({
        headers: expect.objectContaining({
          'Content-Type': 'text/plain', // Should preserve this
          'Authorization': 'Bearer a_token',
        }),
      })
    );
  });

  test('F_AC_IdTokenError: handles error when getIdToken fails', async () => {
    const mockUser = {
      getIdToken: jest.fn(async () => { throw new Error("Token fetch failed"); }),
    };
    auth.currentUser = mockUser as any;

    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    (fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ data: 'success' }),
    });

    await apiClient('/test-endpoint');

    expect(fetch).toHaveBeenCalledTimes(1);
    // Check that Authorization header was NOT set
    const fetchCallArgs = (fetch as jest.Mock).mock.calls[0];
    const headers = fetchCallArgs[1].headers as Headers;
    expect(headers.has('Authorization')).toBe(false);
    expect(consoleErrorSpy).toHaveBeenCalledWith('Error getting ID token:', expect.any(Error));

    consoleErrorSpy.mockRestore();
  });

});
