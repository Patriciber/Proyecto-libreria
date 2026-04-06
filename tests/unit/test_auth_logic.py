import pytest
from unittest.mock import MagicMock
from app.domain.services.auth_service import AuthService
from app.domain.entities.user import User, UserInDB
from app.ports.repositories.user_repository import UserRepositoryPort
from app.adapters.security.security_adapter import SecurityAdapter

@pytest.fixture
def mock_repo():
    return MagicMock(spec=UserRepositoryPort)

@pytest.fixture
def mock_security():
    return MagicMock(spec=SecurityAdapter)

@pytest.fixture
def auth_service(mock_repo, mock_security):
    return AuthService(mock_repo, mock_security)

def test_authenticate_user_success(auth_service, mock_repo, mock_security):
    # Setup
    user_db = UserInDB(
        id=1, username="testuser", email="test@test.com", 
        full_name="Test User", role="user", is_active=True,
        password_hash="hashed_pass"
    )
    mock_repo.get_by_username.return_value = user_db
    mock_security.verify_password.return_value = True

    # Execute
    user = auth_service.authenticate_user("testuser", "correct_pass")

    # Assert
    assert user is not None
    assert user.username == "testuser"
    mock_repo.get_by_username.assert_called_once_with("testuser")
    mock_security.verify_password.assert_called_once_with("correct_pass", "hashed_pass")

def test_authenticate_user_fail_wrong_pass(auth_service, mock_repo, mock_security):
    # Setup
    user_db = UserInDB(
        id=1, username="testuser", email="test@test.com", 
        full_name="Test User", role="user", is_active=True,
        password_hash="hashed_pass"
    )
    mock_repo.get_by_username.return_value = user_db
    mock_security.verify_password.return_value = False

    # Execute
    user = auth_service.authenticate_user("testuser", "wrong_pass")

    # Assert
    assert user is None
