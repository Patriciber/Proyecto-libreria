from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from app.container import get_favorite_service
from app.domain.services.favorite_service import FavoriteService
from app.routers.auth import get_current_user
from app.domain.entities.user import User
from app.domain.exceptions import BookNotFoundError
from app.models.book import BookResponse

router = APIRouter(prefix="/api/favorites", tags=["favorites"])

@router.post("/{book_id}", response_model=Dict[str, str])
async def toggle_favorite(
    book_id: int,
    current_user: User = Depends(get_current_user),
    favorite_service: FavoriteService = Depends(get_favorite_service)
):
    """
    Añade un libro a favoritos, o lo quita si ya estaba añadido.
    Aplica las reglas de negocio verificando que el libro exista.
    """
    try:
        result = await favorite_service.toggle_favorite(current_user.id, book_id)
        return result
    except BookNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[BookResponse])
async def get_user_favorites(
    current_user: User = Depends(get_current_user),
    favorite_service: FavoriteService = Depends(get_favorite_service)
):
    """
    Obtiene todos los libros marcados como favoritos por el usuario actual.
    """
    try:
        books = await favorite_service.get_user_favorite_books(current_user.id)
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
