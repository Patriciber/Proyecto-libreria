from pydantic import BaseModel, Field
from typing import Optional

class BookResponse(BaseModel):
    """Modelo de respuesta para la API de libros. Sincronizado con la Entidad de Dominio."""
    id: int
    title: str
    author: str
    rating: float = Field(ge=0, le=5, description="Rating between 0 and 5")
    pages: int = Field(gt=0, description="Number of pages must be positive")
    duration: str
    category: str
    price: float = Field(ge=0, description="Price cannot be negative")
    is_premium: bool
    cover_style: str
    icon: str
    description: str
    content: str
    is_favorite: bool
    cover: Optional[str] = None

    class Config:
        from_attributes = True

class NewsletterSubscriptionRequest(BaseModel):
    """Modelo de solicitud para suscripción al newsletter."""
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class NewsletterSubscriptionResponse(BaseModel):
    """Modelo de respuesta para suscripción al newsletter."""
    status: str
    message: str