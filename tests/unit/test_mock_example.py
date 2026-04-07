import pytest
import respx
from httpx import Response
from unittest.mock import MagicMock
from app.domain.services.auth_service import AuthService
from app.ports.repositories.user_repository import UserRepositoryPort
from app.adapters.security.security_adapter import SecurityAdapter

def test_auth_service_with_mocker(mocker):
    """Ejemplo de uso de pytest-mock (mocker) para simular dependencias."""
    mock_repo = mocker.Mock(spec=UserRepositoryPort)
    mock_security = mocker.Mock(spec=SecurityAdapter)
    
    service = AuthService(mock_repo, mock_security)
    
    # Configuramos el mock
    mock_repo.get_by_username.return_value = None
    
    # Ejecutamos
    result = service.authenticate_user("usuario_inexistente", "password")
    
    # Verificamos
    assert result is None
    # Eliminado: mock_repo.get_by_username.assert_called_once_with("usuario_inexistente")
    # (Anti-patrón 3: Over-spec, comprobamos el estado observable, no la llamada interna)
@respx.template
def test_external_api_mocking():
    """Ejemplo de cómo simular respuestas HTTP externas usando respx."""
    # Simulamos una llamada a nuestra propia API (o una externa)
    route = respx.get("http://127.0.0.1:8080/api/books").mock(
        return_value=Response(200, json=[{"id": 1, "title": "Mock Book"}])
    )
    
    import httpx
    response = httpx.get("http://127.0.0.1:8080/api/books")
    
    assert response.status_code == 200
    assert response.json()[0]["title"] == "Mock Book"
    assert route.called
