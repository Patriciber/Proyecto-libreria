from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.models.book import BookResponse
from app.domain.services.book_service import BookService
from app.domain.exceptions import BookNotFoundError, RepositoryError
from app.container import get_book_service
from app.routers.auth import get_current_user
from app.domain.entities.user import User
from app.logging_config import logger

router = APIRouter(prefix="/api/books", tags=["books"])

@router.get("/", response_model=List[BookResponse])
async def get_books(
    category: Optional[str] = Query(None, description="Filter by category"),
    search: Optional[str] = Query(None, description="Search in title, author or description"),
    book_service: BookService = Depends(get_book_service)
):
    """
    Obtiene todos los libros con filtros opcionales.

    - **category**: Filtrar por categoría específica
    - **search**: Buscar en título, autor o descripción
    """
    try:
        logger.info(f"API call: get_books with category={category}, search={search}")
        books = await book_service.get_books(category=category, search=search)
        return books
    except RepositoryError as e:
        logger.error(f"Repository error in get_books: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in get_books: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int,
    book_service: BookService = Depends(get_book_service)
):
    """
    Obtiene un libro específico por su ID.

    - **book_id**: ID único del libro
    """
    try:
        logger.info(f"API call: get_book with id {book_id}")
        book = await book_service.get_book(book_id)
        return book
    except BookNotFoundError as e:
        logger.warning(f"Book not found: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except RepositoryError as e:
        logger.error(f"Repository error in get_book: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in get_book: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/featured/", response_model=List[BookResponse])
async def get_featured_books(
    limit: int = Query(3, ge=1, le=10, description="Number of featured books to return"),
    book_service: BookService = Depends(get_book_service)
):
    """
    Obtiene libros destacados ordenados por rating.

    - **limit**: Número de libros a retornar (1-10)
    """
    try:
        logger.info(f"API call: get_featured_books with limit {limit}")
        return await book_service.get_featured_books(limit)
    except RepositoryError as e:
        logger.error(f"Repository error in get_featured_books: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in get_featured_books: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/free/", response_model=List[BookResponse])
async def get_free_books(
    book_service: BookService = Depends(get_book_service)
):
    """Obtiene todos los libros gratuitos."""
    try:
        logger.info("API call: get_free_books")
        return await book_service.get_free_books()
    except RepositoryError as e:
        logger.error(f"Repository error in get_free_books: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in get_free_books: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/premium/", response_model=List[BookResponse])
async def get_premium_books(
    current_user: User = Depends(get_current_user),
    book_service: BookService = Depends(get_book_service)
):
    """Obtiene todos los libros premium. Requiere autenticación."""
    try:
        logger.info("API call: get_premium_books")
        return await book_service.get_premium_books()
    except RepositoryError as e:
        logger.error(f"Repository error in get_premium_books: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in get_premium_books: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")