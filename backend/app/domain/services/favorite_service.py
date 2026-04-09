from typing import List, Dict
from app.domain.entities.favorite import Favorite
from app.ports.repositories.favorite_repository import FavoriteRepositoryPort
from app.ports.repositories.book_repository import BookRepositoryPort
from app.domain.exceptions import BookNotFoundError

class FavoriteService:
    """
    Servicio de Dominio para manejar la lógica de negocio de los Favoritos.
    Orquesta llamadas entre distintos repositorios a través de sus puertos.
    """
    def __init__(self, favorite_repo: FavoriteRepositoryPort, book_repo: BookRepositoryPort):
        self.favorite_repo = favorite_repo
        self.book_repo = book_repo

    async def toggle_favorite(self, user_id: int, book_id: int) -> Dict[str, str]:
        """
        Agrega a favoritos o lo quita si ya estaba agregado.
        Aplica la regla de negocio de verificar primero si el libro existe en el catálogo.
        """
        # Verificar existencia del libro
        book = await self.book_repo.get_book_by_id(book_id)
        if not book:
            raise BookNotFoundError(f"El libro con ind {book_id} no existe en el catálogo.")

        # Alternar
        is_fav = await self.favorite_repo.is_favorite(user_id, book_id)
        if is_fav:
            await self.favorite_repo.remove_favorite(user_id, book_id)
            return {"status": "removed", "message": "Libro quitado de favoritos", "book_id": str(book_id)}
        else:
            await self.favorite_repo.add_favorite(user_id, book_id)
            return {"status": "added", "message": "Libro añadido a favoritos", "book_id": str(book_id)}

    async def get_user_favorite_books(self, user_id: int) -> List[dict]:
        """
        Devuelve no sólo la relación, sino la información de los libros favoritos.
        """
        favorites = await self.favorite_repo.get_user_favorites(user_id)
        books = []
        for fav in favorites:
            book = await self.book_repo.get_book_by_id(fav.book_id)
            if book:
                books.append(book)
        return books
