from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.author import AuthorResponse
from app.ports.repositories.author_repository import AuthorRepositoryPort
from app.container import get_author_repository

router = APIRouter(prefix="/api/authors", tags=["Authors"])

@router.get("/", response_model=List[AuthorResponse])
async def get_authors(
    repository: AuthorRepositoryPort = Depends(get_author_repository)
):
    """
    Obtener todos los autores del catálogo.
    """
    authors = await repository.get_all()
    return authors

@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author(
    author_id: int,
    repository: AuthorRepositoryPort = Depends(get_author_repository)
):
    """
    Obtener un autor por su ID.
    """
    author = await repository.get_by_id(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return author
