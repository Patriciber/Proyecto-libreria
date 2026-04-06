import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """Fixture para obtener un TestClient de FastAPI."""
    with TestClient(app) as c:
        yield c

@pytest.fixture
def auth_headers(client):
    """Fixture para obtener headers de autenticación (opcional)."""
    # En el futuro, este fixture puede manejar el login automático para tests protegidos
    return {}
