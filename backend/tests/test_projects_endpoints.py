import pytest
from fastapi.testclient import TestClient
from http import HTTPStatus
from unittest.mock import patch, AsyncMock, MagicMock

# Import the main FastAPI application
from backend.src.agent.app import app

# Define a sample project structure based on Project Pydantic model (from useProjects.ts)
# This helps in creating mock return values for the database.
SAMPLE_PROJECT_DATA = {
    "id": 1,
    "name": "Test Project 1",
    "description": "A project for testing",
    "github_repo_url": "https://github.com/test/project1",
    "github_repo_id": "repo_123",
    "github_metadata": {"stars": 10},
    "repository_analysis": "Initial analysis done.",
    "status": "active",
    "priority": "high",
    "team": "Alpha Team",
    "user_id": "owner_uid", # This will be crucial for ownership tests
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z",
}

client = TestClient(app)

# --- Tests for GET /api/v1/projects/{project_id} ---

@patch('firebase_admin.auth.verify_id_token')
@patch('backend.src.api.projects_endpoints.get_db_connection')
async def test_get_specific_project_valid_token_owner(
    mock_get_db_connection: MagicMock,
    mock_verify_id_token: MagicMock
):
    """Test accessing a specific project with a valid token of the project owner."""
    mock_verify_id_token.return_value = {'uid': 'owner_uid', 'email': 'owner@example.com'}

    # Configure the mock database connection and cursor
    mock_conn = AsyncMock()
    mock_get_db_connection.return_value.__aenter__.return_value = mock_conn

    # fetchrow should return a dict-like object if row_factory is set, or a tuple/list
    # For simplicity, assume it returns a dict matching SAMPLE_PROJECT_DATA
    mock_conn.fetchrow.return_value = dict(SAMPLE_PROJECT_DATA)

    response = client.get("/api/v1/projects/1", headers={"Authorization": "Bearer validtoken"})

    assert response.status_code == HTTPStatus.OK
    project_data = response.json()
    assert project_data["id"] == SAMPLE_PROJECT_DATA["id"]
    assert project_data["name"] == SAMPLE_PROJECT_DATA["name"]
    assert project_data["user_id"] == "owner_uid"
    mock_verify_id_token.assert_called_once_with("validtoken")
    mock_get_db_connection.assert_called_once() # Ensure DB connection was attempted
    mock_conn.fetchrow.assert_called_once_with(
        "SELECT * FROM projects WHERE id = $1 AND user_id = $2", 1, "owner_uid"
    )

@patch('firebase_admin.auth.verify_id_token')
@patch('backend.src.api.projects_endpoints.get_db_connection')
async def test_get_specific_project_forbidden_wrong_user(
    mock_get_db_connection: MagicMock,
    mock_verify_id_token: MagicMock
):
    """Test accessing a specific project with a valid token of a NON-owner user."""
    mock_verify_id_token.return_value = {'uid': 'other_uid', 'email': 'other@example.com'}

    mock_conn = AsyncMock()
    mock_get_db_connection.return_value.__aenter__.return_value = mock_conn
    # Simulate project exists but is owned by 'owner_uid', so fetchrow for 'other_uid' returns None
    mock_conn.fetchrow.return_value = None

    response = client.get("/api/v1/projects/1", headers={"Authorization": "Bearer validtoken_otheruser"})

    # The current implementation of get_project in projects_endpoints.py first checks ownership
    # by user_id in the query. If no row is returned, it means either project doesn't exist OR
    # it's not owned by this user. Both result in a 404 from that perspective.
    # A true 403 would require fetching the project first, then checking user_id.
    # Given the current SQL `SELECT * FROM projects WHERE id = $1 AND user_id = $2`,
    # a non-matching user_id will result in fetchrow returning None, leading to a 404.
    # If the logic were: 1. Fetch project by ID. 2. Check user_id. Then 403 would be more direct.
    # For now, we expect 404 based on the combined query.
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "Project not found or not owned by user"
    mock_verify_id_token.assert_called_once_with("validtoken_otheruser")
    mock_conn.fetchrow.assert_called_once_with(
        "SELECT * FROM projects WHERE id = $1 AND user_id = $2", 1, "other_uid"
    )


def test_get_specific_project_no_token():
    """Test accessing a specific project without an Authorization token."""
    response = client.get("/api/v1/projects/1")
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()["detail"] == "Authorization header is missing"


@patch('firebase_admin.auth.verify_id_token')
@patch('backend.src.api.projects_endpoints.get_db_connection')
async def test_get_specific_project_not_found(
    mock_get_db_connection: MagicMock,
    mock_verify_id_token: MagicMock
):
    """Test accessing a non-existent project with a valid token."""
    mock_verify_id_token.return_value = {'uid': 'any_uid', 'email': 'any@example.com'}

    mock_conn = AsyncMock()
    mock_get_db_connection.return_value.__aenter__.return_value = mock_conn
    mock_conn.fetchrow.return_value = None # Simulate project not found

    response = client.get("/api/v1/projects/999", headers={"Authorization": "Bearer validtoken"})

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "Project not found or not owned by user"
    mock_verify_id_token.assert_called_once_with("validtoken")
    mock_conn.fetchrow.assert_called_once_with(
        "SELECT * FROM projects WHERE id = $1 AND user_id = $2", 999, "any_uid"
    )

# --- Tests for GET /api/v1/projects ---

def test_get_projects_no_token():
    """Test accessing the list of projects without an Authorization token."""
    response = client.get("/api/v1/projects")
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()["detail"] == "Authorization header is missing"

@patch('firebase_admin.auth.verify_id_token')
@patch('backend.src.api.projects_endpoints.get_db_connection')
async def test_get_projects_valid_token(
    mock_get_db_connection: MagicMock,
    mock_verify_id_token: MagicMock
):
    """Test accessing the list of projects with a valid token."""
    mock_verify_id_token.return_value = {'uid': 'test_user_projects_uid', 'email': 'user@example.com'}

    mock_conn = AsyncMock()
    mock_get_db_connection.return_value.__aenter__.return_value = mock_conn

    # Simulate fetch returning a list of projects
    # Each project in the list should be a dict-like object
    mock_conn.fetch.return_value = [
        dict(SAMPLE_PROJECT_DATA, id=1, user_id='test_user_projects_uid'),
        dict(SAMPLE_PROJECT_DATA, id=2, name="Project Alpha", user_id='test_user_projects_uid')
    ]

    response = client.get("/api/v1/projects", headers={"Authorization": "Bearer validtoken"})

    assert response.status_code == HTTPStatus.OK
    projects_list = response.json()
    assert isinstance(projects_list, list)
    assert len(projects_list) == 2
    assert projects_list[0]["name"] == SAMPLE_PROJECT_DATA["name"]
    assert projects_list[1]["name"] == "Project Alpha"
    mock_verify_id_token.assert_called_once_with("validtoken")
    # Check if the SQL query in the endpoint was called with the correct user_id
    # Example: mock_conn.fetch.assert_called_once_with("SELECT * FROM projects WHERE user_id = $1 ORDER BY updated_at DESC", "test_user_projects_uid")
    # The exact query depends on the implementation of list_projects endpoint
    args, _ = mock_conn.fetch.call_args
    assert "SELECT * FROM projects WHERE user_id = $1" in args[0] # Check the query string
    assert args[1] == "test_user_projects_uid" # Check the user_id parameter

@patch('firebase_admin.auth.verify_id_token')
@patch('backend.src.api.projects_endpoints.get_db_connection')
async def test_get_projects_valid_token_no_projects(
    mock_get_db_connection: MagicMock,
    mock_verify_id_token: MagicMock
):
    """Test accessing the list of projects with a valid token when user has no projects."""
    mock_verify_id_token.return_value = {'uid': 'new_user_uid', 'email': 'new@example.com'}

    mock_conn = AsyncMock()
    mock_get_db_connection.return_value.__aenter__.return_value = mock_conn
    mock_conn.fetch.return_value = [] # Simulate no projects found for this user

    response = client.get("/api/v1/projects", headers={"Authorization": "Bearer validtoken_newuser"})

    assert response.status_code == HTTPStatus.OK
    projects_list = response.json()
    assert isinstance(projects_list, list)
    assert len(projects_list) == 0
    mock_verify_id_token.assert_called_once_with("validtoken_newuser")
    args, _ = mock_conn.fetch.call_args
    assert "SELECT * FROM projects WHERE user_id = $1" in args[0]
    assert args[1] == "new_user_uid"

# TODO: Add tests for POST, PUT, DELETE for projects, ensuring auth and ownership where applicable.
# For POST, check that user_id from token is used.
# For PUT/DELETE, check that user_id from token matches project's user_id.

# Example of a test for POST /api/v1/projects
@patch('firebase_admin.auth.verify_id_token')
@patch('backend.src.api.projects_endpoints.get_db_connection')
async def test_create_project_valid_token(
    mock_get_db_connection: MagicMock,
    mock_verify_id_token: MagicMock
):
    """Test creating a new project with a valid token."""
    user_uid = 'creator_uid'
    mock_verify_id_token.return_value = {'uid': user_uid, 'email': 'creator@example.com'}

    mock_conn = AsyncMock()
    mock_get_db_connection.return_value.__aenter__.return_value = mock_conn

    new_project_data_from_db = {
        "id": 2, "name": "Newly Created Project", "description": "Desc",
        "user_id": user_uid, "status": "pending", "priority": "medium",
        "created_at": "2024-01-02T10:00:00Z", "updated_at": "2024-01-02T10:00:00Z"
        # Fill other fields as per your model defaults or what the DB returns
    }
    mock_conn.fetchrow.return_value = new_project_data_from_db

    project_payload = {"name": "Newly Created Project", "description": "Desc"}
    response = client.post("/api/v1/projects",
                           headers={"Authorization": "Bearer validtoken_creator"},
                           json=project_payload)

    assert response.status_code == HTTPStatus.CREATED
    created_project = response.json()
    assert created_project["name"] == project_payload["name"]
    assert created_project["user_id"] == user_uid # Crucial check

    # Check that the insert query was called with the correct user_id
    args, _ = mock_conn.fetchrow.call_args
    # Example: INSERT INTO projects (name, description, user_id, status, priority) VALUES ($1, $2, $3, $4, $5) RETURNING *
    assert "INSERT INTO projects" in args[0]
    assert project_payload["name"] in args # Check name is in query args
    assert user_uid in args # Check user_id is in query args
    mock_verify_id_token.assert_called_once_with("validtoken_creator")
