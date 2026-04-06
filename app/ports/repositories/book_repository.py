from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.book import Book

class BookRepositoryPort(ABC):
    """
    Puerto (contrato) para el repositorio de libros.
    Define las operaciones que debe ofrecer cualquier implementación
    de repositorio de libros, independientemente de la tecnología.
    """

    @abstractmethod
    async def get_all_books(self) -> List[Book]:
        """Obtiene todos los libros disponibles."""
        pass

    @abstractmethod
    async def get_books_by_category(self, category: str) -> List[Book]:
        """Obtiene libros filtrados por categoría."""
        pass

    @abstractmethod
    async def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Obtiene un libro específico por su ID."""
        pass

    @abstractmethod
    async def search_books(self, query: str) -> List[Book]:
        """Busca libros por título, autor o descripción."""
        pass

    @abstractmethod
    async def get_featured_books(self, limit: int = 3) -> List[Book]:
        """Obtiene libros destacados (mejores ratings)."""
        pass