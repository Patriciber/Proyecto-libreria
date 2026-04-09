from pydantic import BaseModel, EmailStr
from typing import List

class AuthorResponse(BaseModel):
    """Modelo de respuesta para un autor."""
    id: int
    name: str
    last_name: str
    email: str
    full_name: str

    class Config:
        from_attributes = True

class AuthorListResponse(BaseModel):
    """Modelo de respuesta para una lista de autores."""
    authors: List[AuthorResponse]
