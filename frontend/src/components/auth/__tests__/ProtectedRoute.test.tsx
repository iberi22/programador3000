import React from 'react';
import { render, screen, act } from '@testing-library/react';
import { MemoryRouter, Routes, Route, useLocation } from 'react-router-dom';
import ProtectedRoute from '../ProtectedRoute';
import useAuth from '../../../hooks/useAuth'; // The hook to be mocked

// Mock the useAuth hook
jest.mock('../../../hooks/useAuth');

// Mock child component
const MockChildComponent = () => <div>Child Content</div>;
const MockLoginPage = () => {
  const location = useLocation();
  return (
    <div>
      Login Page
      {location.state?.from?.pathname && <span data-testid="from-pathname">{location.state.from.pathname}</span>}
    </div>
  );
};


describe('ProtectedRoute', () => {
  const mockUseAuth = useAuth as jest.Mock; // Typecast for easier mock usage

  beforeEach(() => {
    // Reset any previous mock implementations
    mockUseAuth.mockReset();
  });

  // Test F_PR1
  test('F_PR1: Authenticated user sees children', () => {
    mockUseAuth.mockReturnValue({
      currentUser: { uid: 'test-user', email: 'test@example.com' }, // Provide a mock user object
      loading: false,
    });

    render(
      <MemoryRouter initialEntries={['/protected']}>
        <Routes>
          <Route path="/protected" element={<ProtectedRoute><MockChildComponent /></ProtectedRoute>} />
        </Routes>
      </MemoryRouter>
    );

    expect(screen.getByText('Child Content')).toBeInTheDocument();
  });

  // Test F_PR2 & F_PR4 combined (redirect and location state)
  test('F_PR2 & F_PR4: Unauthenticated user is redirected to login, preserving original location', () => {
    mockUseAuth.mockReturnValue({
      currentUser: null,
      loading: false,
    });

    render(
      <MemoryRouter initialEntries={['/protected-path']}>
        <Routes>
          <Route
            path="/protected-path"
            element={
              <ProtectedRoute>
                <MockChildComponent />
              </ProtectedRoute>
            }
          />
          <Route path="/login" element={<MockLoginPage />} />
        </Routes>
      </MemoryRouter>
    );

    // Check that child content is NOT rendered
    expect(screen.queryByText('Child Content')).not.toBeInTheDocument();

    // Check that Login Page content IS rendered
    expect(screen.getByText('Login Page')).toBeInTheDocument();

    // Check that the "from" location was passed in state
    const fromPathnameSpan = screen.getByTestId('from-pathname');
    expect(fromPathnameSpan).toHaveTextContent('/protected-path');
  });

  // Test F_PR3
  test('F_PR3: Shows loader while auth state is loading', () => {
    mockUseAuth.mockReturnValue({
      currentUser: null,
      loading: true,
    });

    render(
      <MemoryRouter initialEntries={['/protected']}>
        <Routes>
          <Route path="/protected" element={<ProtectedRoute><MockChildComponent /></ProtectedRoute>} />
        </Routes>
      </MemoryRouter>
    );

    // Check that child content is NOT rendered
    expect(screen.queryByText('Child Content')).not.toBeInTheDocument();

    // Check for loader (Lucide's Loader2 has class 'animate-spin' by default from ProtectedRoute.tsx)
    // We can also check for a specific data-testid if we added one to the loader div in ProtectedRoute
    const loader = document.querySelector('.animate-spin'); // Less ideal, direct DOM query
    expect(loader).toBeInTheDocument();
    // A better way if you control ProtectedRoute: add a test-id to the loader's container
    // For example, if ProtectedRoute had <div data-testid="loading-spinner">...</div>
    // expect(screen.getByTestId('loading-spinner')).toBeInTheDocument();
  });

  // Test for requiredRole (though not fully implemented in ProtectedRoute.tsx, we can test the structure)
  test('Authenticated user with requiredRole (not implemented) still sees children', () => {
    mockUseAuth.mockReturnValue({
      currentUser: { uid: 'test-user-role', email: 'role@example.com', role: 'admin' }, // Assuming role might exist
      loading: false,
    });

    render(
      <MemoryRouter initialEntries={['/admin']}>
        <Routes>
          <Route
            path="/admin"
            element={
              <ProtectedRoute requiredRole="admin">
                <MockChildComponent />
              </ProtectedRoute>
            }
          />
           <Route path="/unauthorized" element={<div>Unauthorized Page</div>} />
        </Routes>
      </MemoryRouter>
    );
    // Since role check is commented out in ProtectedRoute, it should render children
    expect(screen.getByText('Child Content')).toBeInTheDocument();
  });
});
