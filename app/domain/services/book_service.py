from typing import List, Optional
from app.domain.entities.book import Book
from app.domain.exceptions import BookNotFoundError, RepositoryError
from app.ports.repositories.book_repository import BookRepositoryPort
from app.logging_config import logger

class BookService:
    """
    Servicio de dominio para libros.
    Contiene toda la lógica de negocio relacionada con libros.
    No depende de frameworks externos ni de detalles de infraestructura.
    """

    def __init__(self, book_repository: BookRepositoryPort):
        self._book_repository = book_repository
        self._logger = logger
    async def get_books(self, category: Optional[str] = None, search: Optional[str] = None) -> List[Book]:
        """
        Obtiene libros con filtros opcionales.
        Lógica de negocio: combina filtros de categoría y búsqueda.
        """
        try:
            self._logger.debug(f"Getting books with category={category}, search={search}")

            if search:
                books = await self._book_repository.search_books(search)
                self._logger.info(f"Found {len(books)} books matching search '{search}'")
            else:
                books = await self._book_repository.get_all_books()

            if category and category != "all":
                books = [book for book in books if book.category == category]
                self._logger.debug(f"Filtered to {len(books)} books in category '{category}'")

            return books

        except Exception as e:
            self._logger.error(f"Error retrieving books: {str(e)}")
            raise RepositoryError(f"Failed to retrieve books: {str(e)}")

    async def get_book(self, book_id: int) -> Book:
        """Obtiene un libro específico."""
        try:
            self._logger.debug(f"Getting book with id {book_id}")
            book = await self._book_repository.get_book_by_id(book_id)

            if not book:
                self._logger.warning(f"Book with id {book_id} not found")
                raise BookNotFoundError(book_id)

            return book

        except BookNotFoundError:
            raise  # Re-lanzar excepciones de dominio
        except Exception as e:
            self._logger.error(f"Error retrieving book {book_id}: {str(e)}")
            raise RepositoryError(f"Failed to retrieve book {book_id}: {str(e)}")

    async def get_featured_books(self, limit: int = 3) -> List[Book]:
        """Obtiene libros destacados ordenados por rating."""
        try:
            self._logger.debug(f"Getting {limit} featured books")
            books = await self._book_repository.get_featured_books(limit)
            self._logger.info(f"Retrieved {len(books)} featured books")
            return books

        except Exception as e:
            self._logger.error(f"Error retrieving featured books: {str(e)}")
            raise RepositoryError(f"Failed to retrieve featured books: {str(e)}")

    async def get_books_by_reading_time(self, time_category: str) -> List[Book]:
        """
        Obtiene libros filtrados por tiempo de lectura.
        Lógica de negocio específica de la aplicación.
        """
        try:
            self._logger.debug(f"Getting books by reading time category: {time_category}")
            all_books = await self._book_repository.get_all_books()
            filtered_books = [book for book in all_books if book.get_reading_time_category() == time_category]
            self._logger.info(f"Found {len(filtered_books)} books in reading time category '{time_category}'")
            return filtered_books

        except Exception as e:
            self._logger.error(f"Error filtering books by reading time: {str(e)}")
            raise RepositoryError(f"Failed to filter books by reading time: {str(e)}")

    async def get_free_books(self) -> List[Book]:
        """Obtiene solo libros gratuitos."""
        try:
            self._logger.debug("Getting free books")
            all_books = await self._book_repository.get_all_books()
            free_books = [book for book in all_books if book.is_free()]
            self._logger.info(f"Found {len(free_books)} free books")
            return free_books

        except Exception as e:
            self._logger.error(f"Error retrieving free books: {str(e)}")
            raise RepositoryError(f"Failed to retrieve free books: {str(e)}")

    async def get_premium_books(self) -> List[Book]:
        """Obtiene solo libros premium."""
        try:
            self._logger.debug("Getting premium books")
            all_books = await self._book_repository.get_all_books()
            premium_books = [book for book in all_books if not book.is_free()]
            self._logger.info(f"Found {len(premium_books)} premium books")
            return premium_books

        except Exception as e:
            self._logger.error(f"Error retrieving premium books: {str(e)}")
            raise RepositoryError(f"Failed to retrieve premium books: {str(e)}")