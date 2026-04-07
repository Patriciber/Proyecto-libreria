import pytest
from datetime import datetime
from freezegun import freeze_time
from unittest.mock import AsyncMock
from app.domain.entities.favorite import Favorite
from app.domain.services.favorite_service import FavoriteService

"""
Nivel 2 — Los 5 anti-patrones a evitar en Testing:
1. Mockear lo que no es IO: lógica pura no debería necesitar mocks.
2. Parchear el sitio incorrecto: test que no controla la dependencia real.
3. Over-spec: asserts de llamadas demasiado exactos (frágiles).
4. Testear implementación en vez de comportamiento (se rompe con refactors sanos).
5. Mocks globales compartidos entre tests (contaminación).

Señal roja: si al cambiar nombres internos (refactor) se rompen 30 tests, tu suite está acoplada a implementación. El mocking está "demasiado cerca".
"""

# 1. Demostración de freezegun (Control del Tiempo)
@freeze_time("2026-04-07 12:00:00")
def test_favorite_creation_time():
    """Prueba que asegura predecibilidad de tiempo usando freezegun."""
    fav = Favorite(id=1, user_id=10, book_id=100, created_at=datetime.now())
    # El tiempo está congelado, por lo que datetime.now() siempre devolverá esta constancia exacta
    assert fav.created_at.year == 2026
    assert fav.created_at.month == 4
    assert fav.created_at.day == 7
    assert fav.created_at.hour == 12

# 2. Demostración de unittest.mock / pytest-mock (Fixture Mocker)
@pytest.mark.asyncio
async def test_favorite_service_with_mocker(mocker):
    """
    Prueba que simula dependencias completas del repositorio 
    sin tocar la implementación real usando pytest-mock.
    """
    # Creamos 'spies' / mocks de los puertos usando mocker
    mock_favorite_repo = mocker.AsyncMock()
    mock_book_repo = mocker.AsyncMock()

    # Configuramos el comportamiento esperado del mock: El libro existe
    mock_book_repo.get_book_by_id.return_value = {"id": 1, "title": "Libro Simulado"}
    # El usuario no tiene favoritos aún
    mock_favorite_repo.is_favorite.return_value = False

    # Inyectamos los mocks en el servicio
    service = FavoriteService(mock_favorite_repo, mock_book_repo)
    
    result = await service.toggle_favorite(user_id=10, book_id=1)

    # Aserciones: Verificamos qué pasó dentro de la lógica del negocio
    assert result["status"] == "added"
    
    # Verificamos que el servicio "llamó" a la base de datos simulada
    mock_book_repo.get_book_by_id.assert_called_once_with(1)
    mock_favorite_repo.add_favorite.assert_called_once_with(10, 1)

# Se aplicaría la misma lógica con "responses" o "respx" para 
# pruebas de integración HTTP externas, y "fakeredis" cuando activemos la caché.
