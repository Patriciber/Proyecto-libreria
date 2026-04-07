"""
Contenedor de dependencias para inyección de dependencias.
Centraliza la creación y configuración de todos los servicios.
"""
from typing import Generator
from app.domain.services.book_service import BookService
from app.domain.services.auth_service import AuthService
from app.ports.repositories.book_repository import BookRepositoryPort
from app.ports.repositories.user_repository import UserRepositoryPort
from app.adapters.repositories.book_repository_mock import BookRepositoryMock
from app.adapters.repositories.user_repository_mock import UserRepositoryMock
from app.adapters.repositories.favorite_repository_mock import FavoriteRepositoryMock
from app.adapters.security.security_adapter import SecurityAdapter
from app.ports.repositories.favorite_repository import FavoriteRepositoryPort
from app.domain.services.favorite_service import FavoriteService

class DependencyContainer:
    """Contenedor de dependencias para la aplicación."""

    def __init__(self):
        self._book_repository: BookRepositoryPort = None
        self._user_repository: UserRepositoryPort = None
        self._book_service: BookService = None
        self._auth_service: AuthService = None
        self._security_adapter: SecurityAdapter = None
        self._favorite_repository: FavoriteRepositoryPort = None
        self._favorite_service: FavoriteService = None

    @property
    def security_adapter(self) -> SecurityAdapter:
        """Lazy initialization del adaptador de seguridad."""
        if self._security_adapter is None:
            self._security_adapter = SecurityAdapter()
        return self._security_adapter

    @property
    def book_repository(self) -> BookRepositoryPort:
        """Lazy initialization del repositorio de libros."""
        if self._book_repository is None:
            self._book_repository = BookRepositoryMock()
        return self._book_repository

    @property
    def user_repository(self) -> UserRepositoryPort:
        """Lazy initialization del repositorio de usuarios."""
        if self._user_repository is None:
            self._user_repository = UserRepositoryMock(self.security_adapter)
        return self._user_repository

    @property
    def book_service(self) -> BookService:
        """Lazy initialization del servicio de libros."""
        if self._book_service is None:
            self._book_service = BookService(self.book_repository)
        return self._book_service

    @property
    def auth_service(self) -> AuthService:
        """Lazy initialization del servicio de autenticación."""
        if self._auth_service is None:
            self._auth_service = AuthService(self.user_repository, self.security_adapter)
        return self._auth_service

    @property
    def favorite_repository(self) -> FavoriteRepositoryPort:
        """Lazy initialization del repositorio de favoritos."""
        if self._favorite_repository is None:
            self._favorite_repository = FavoriteRepositoryMock()
        return self._favorite_repository
        
    @property
    def favorite_service(self) -> FavoriteService:
        """Lazy initialization del servicio de favoritos."""
        if self._favorite_service is None:
            self._favorite_service = FavoriteService(self.favorite_repository, self.book_repository)
        return self._favorite_service

# Instancia global del contenedor
container = DependencyContainer()

def get_book_service() -> BookService:
    """Factory function para obtener el servicio de libros."""
    return container.book_service

def get_auth_service() -> AuthService:
    """Factory function para obtener el servicio de autenticación."""
    return container.auth_service

def get_book_repository() -> BookRepositoryPort:
    """Factory function para obtener el repositorio de libros."""
    return container.book_repository

def get_user_repository() -> UserRepositoryPort:
    """Factory function para obtener el repositorio de usuarios."""
    return container.user_repository

def get_favorite_service() -> FavoriteService:
    """Factory function para obtener el servicio de favoritos."""
    return container.favorite_service