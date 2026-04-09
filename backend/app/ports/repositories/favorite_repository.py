from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.favorite import Favorite

class FavoriteRepositoryPort(ABC):
    """
    Puerto de salida (Outbound Port) para el Repositorio de Favoritos.
    Define el contrato que cualquier adaptador de base de datos deberá cumplir.
    """
    
    @abstractmethod
    async def add_favorite(self, user_id: int, book_id: int) -> Favorite:
        """Añade un libro a los favoritos del usuario."""
        pass

    @abstractmethod
    async def remove_favorite(self, user_id: int, book_id: int) -> bool:
        """Remueve un libro de los favoritos del usuario. Retorna true si fue exitoso."""
        pass

    @abstractmethod
    async def get_user_favorites(self, user_id: int) -> List[Favorite]:
        """Obtiene la lista de favoritos de un usuario."""
        pass

    @abstractmethod
    async def is_favorite(self, user_id: int, book_id: int) -> bool:
        """Verifica si un libro está en los favoritos del usuario."""
        pass
