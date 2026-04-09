from typing import List
from datetime import datetime
from app.domain.entities.favorite import Favorite
from app.ports.repositories.favorite_repository import FavoriteRepositoryPort

class FavoriteRepositoryMock(FavoriteRepositoryPort):
    """Adaptador Mock en memoria para el repositorio de favoritos."""
    
    def __init__(self):
        self._favorites: List[Favorite] = []
        self._next_id = 1

    async def add_favorite(self, user_id: int, book_id: int) -> Favorite:
        fav = Favorite(
            id=self._next_id, 
            user_id=user_id, 
            book_id=book_id, 
            created_at=datetime.now()
        )
        self._favorites.append(fav)
        self._next_id += 1
        return fav

    async def remove_favorite(self, user_id: int, book_id: int) -> bool:
        initial_length = len(self._favorites)
        self._favorites = [f for f in self._favorites if not (f.user_id == user_id and f.book_id == book_id)]
        return len(self._favorites) < initial_length

    async def get_user_favorites(self, user_id: int) -> List[Favorite]:
        return [f for f in self._favorites if f.user_id == user_id]

    async def is_favorite(self, user_id: int, book_id: int) -> bool:
        return any(f.user_id == user_id and f.book_id == book_id for f in self._favorites)
