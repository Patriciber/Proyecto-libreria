from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    """Esquema para la creación de un nuevo usuario."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=3, max_length=100)

class UserResponse(BaseModel):
    """Esquema para la respuesta pública de un usuario (seguro)."""
    id: int
    username: str
    email: EmailStr
    full_name: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True
