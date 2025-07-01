import pytest
from fastapi import FastAPI, Depends, HTTPException
from fastapi.testclient import TestClient
from http import HTTPStatus
from unittest.mock import patch, MagicMock

# Assuming firebase_admin is initialized elsewhere or not strictly needed for these mocks to work
# If firebase_admin.initialize_app() is needed, it should be handled in a conftest.py or test setup
try:
    from firebase_admin import auth as firebase_auth
    from firebase_admin.auth import ExpiredIdTokenError, InvalidIdTokenError
except ImportError:
    # Create mock classes if firebase_admin is not installed in the test environment
    # This allows tests to be defined, though they might not run correctly without proper mocking setup
    class ExpiredIdTokenError(Exception):
        pass
    class InvalidIdTokenError(Exception):
        pass

    firebase_auth = MagicMock()
    firebase_auth.ExpiredIdTokenError = ExpiredIdTokenError
    firebase_auth.InvalidIdTokenError = InvalidIdTokenError
    firebase_auth.verify_id_token = MagicMock()


# Code to be tested
from backend.src.auth.firebase import FirebaseAuthMiddleware, get_current_user, User

# --- Test FastAPI App Setup ---
def create_test_app():
    app = FastAPI()

    # Apply the middleware
    # For testing, we might not need to initialize Firebase Admin app if we mock verify_id_token
    # However, the middleware itself might try to import firebase_admin.auth
    app.add_middleware(FirebaseAuthMiddleware)

    @app.get("/test-protected", response_model=User)
    async def test_protected_route(current_user: User = Depends(get_current_user)):
        if not current_user: # Should not happen if middleware and Depends work
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="User not found in request state")
        return current_user

    @app.get("/unprotected")
    async def unprotected_route():
        return {"message": "This is an unprotected route"}

    return app

client = TestClient(create_test_app())

# --- Test Cases ---

@patch('firebase_admin.auth.verify_id_token')
def test_b1_valid_token(mock_verify_id_token: MagicMock):
    """Test B1: Valid token allows access to protected route."""
    sample_decoded_token = {'uid': 'test_uid_123', 'email': 'test@example.com', 'name': 'Test User'}
    mock_verify_id_token.return_value = sample_decoded_token

    response = client.get("/test-protected", headers={"Authorization": "Bearer faketoken"})

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'uid': 'test_uid_123', 'email': 'test@example.com', 'name': 'Test User', 'picture': None, 'email_verified': False} # Matches User model defaults
    mock_verify_id_token.assert_called_once_with("faketoken")

def test_b2_missing_token():
    """Test B2: Missing token results in Unauthorized."""
    response = client.get("/test-protected")

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()['detail'] == "Authorization header is missing"

@patch('firebase_admin.auth.verify_id_token')
def test_b4_invalid_token_value_error(mock_verify_id_token: MagicMock):
    """Test B4: Invalid token (ValueError from verify_id_token) results in Unauthorized."""
    mock_verify_id_token.side_effect = ValueError("Simulated bad token format or signature")

    response = client.get("/test-protected", headers={"Authorization": "Bearer invalidtoken"})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()['detail'] == "Invalid authentication token: Simulated bad token format or signature"
    mock_verify_id_token.assert_called_once_with("invalidtoken")

@patch('firebase_admin.auth.verify_id_token')
def test_b4_invalid_token_invalid_id_token_error(mock_verify_id_token: MagicMock):
    """Test B4 (alternative): Invalid token (InvalidIdTokenError from verify_id_token) results in Unauthorized."""
    # Use the actual InvalidIdTokenError if available, otherwise the mocked one
    actual_invalid_id_token_error = getattr(firebase_auth, 'InvalidIdTokenError', InvalidIdTokenError)
    mock_verify_id_token.side_effect = actual_invalid_id_token_error("Token is invalid for other reasons")

    response = client.get("/test-protected", headers={"Authorization": "Bearer anotherinvalidtoken"})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()['detail'] == "Invalid authentication token: Token is invalid for other reasons"
    mock_verify_id_token.assert_called_once_with("anotherinvalidtoken")


@patch('firebase_admin.auth.verify_id_token')
def test_b_expired_token(mock_verify_id_token: MagicMock):
    """Test B_Expired: Expired token results in Unauthorized."""
    # Use the actual ExpiredIdTokenError if available, otherwise the mocked one
    actual_expired_id_token_error = getattr(firebase_auth, 'ExpiredIdTokenError', ExpiredIdTokenError)
    mock_verify_id_token.side_effect = actual_expired_id_token_error("Simulated token has expired")

    response = client.get("/test-protected", headers={"Authorization": "Bearer expiredtoken"})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()['detail'] == "Authentication token has expired: Simulated token has expired"
    mock_verify_id_token.assert_called_once_with("expiredtoken")

def test_unprotected_route_no_token():
    """Test that an unprotected route can be accessed without a token."""
    response = client.get("/unprotected")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "This is an unprotected route"}

def test_unprotected_route_with_valid_token(mock_verify_id_token: MagicMock = None): # Allow mock to be passed if needed by other setups
    """Test that an unprotected route can be accessed even with a valid token."""
    # This test doesn't strictly need a mock if the route doesn't use Depends(get_current_user)
    # or if the middleware doesn't block requests with valid tokens to public routes.
    # However, if other tests patch verify_id_token globally, this ensures it's fine.
    if mock_verify_id_token: # If a mock is passed (e.g. from a class-level patch)
        sample_decoded_token = {'uid': 'test_uid_public', 'email': 'public@example.com'}
        mock_verify_id_token.return_value = sample_decoded_token

    response = client.get("/unprotected", headers={"Authorization": "Bearer sometoken"})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "This is an unprotected route"}

@patch('firebase_admin.auth.verify_id_token')
def test_malformed_bearer_token(mock_verify_id_token: MagicMock):
    """Test that a malformed Bearer token is rejected."""
    response = client.get("/test-protected", headers={"Authorization": "Bearer"}) # Missing token part
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "Malformed Authorization header" in response.json()['detail']
    mock_verify_id_token.assert_not_called()

    response = client.get("/test-protected", headers={"Authorization": "NotBearer faketoken"})
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "Malformed Authorization header" in response.json()['detail']
    mock_verify_id_token.assert_not_called()

    response = client.get("/test-protected", headers={"Authorization": "Bearer token1 token2"}) # Too many parts
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "Malformed Authorization header" in response.json()['detail']
    mock_verify_id_token.assert_not_called()

# It might be useful to also test the get_current_user dependency directly,
# but testing it through the middleware and a protected route is a good integration test.

# Example of how to initialize firebase_admin if it's strictly necessary for some tests
# and not handled by a global conftest.py
#
# import firebase_admin
# from firebase_admin import credentials
#
# @pytest.fixture(scope="session", autouse=True)
# def initialize_firebase_for_tests():
#     """Initialize Firebase Admin SDK for the test session if not already initialized."""
#     if not firebase_admin._apps:
#         # Use a mock credential if you don't want to use a real service account in tests
#         # For CI environments, you might use environment variables for a service account
#         cred = MagicMock(spec=credentials.Certificate)
#         firebase_admin.initialize_app(cred, name="pytest_firebase_app")
#     yield
#     # Teardown if necessary, though typically not for firebase_admin
#
# Note: The above fixture is commented out as for these specific tests with patching verify_id_token,
# full Firebase app initialization might not be required. If FirebaseAuthMiddleware or get_current_user
# had side effects relying on firebase_admin.get_app(), then it would be more critical.
# The try-except for firebase_admin imports also helps in environments where it might not be installed.
