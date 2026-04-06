from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    """Entidad de dominio puro para representar un libro."""
    id: int
    title: str
    author: str
    rating: float
    pages: int
    duration: str
    category: str
    price: float
    is_premium: bool
    cover_style: str
    icon: str
    description: str
    content: str  # Nuevo campo para el contenido completo
    is_favorite: bool

    def __post_init__(self):
        """Validaciones de negocio básicas."""
        if self.rating < 0 or self.rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        if self.pages <= 0:
            raise ValueError("Pages must be positive")
        if self.price < 0:
            raise ValueError("Price cannot be negative")

    def is_free(self) -> bool:
        """Regla de negocio: determina si el libro es gratuito."""
        return self.price == 0

    def get_reading_time_category(self) -> str:
        """Categoriza el tiempo de lectura."""
        try:
            hours = int(self.duration.split('h')[0])
            if hours < 5:
                return "corta"
            elif hours < 12:
                return "media"
            else:
                return "larga"
        except (ValueError, IndexError):
            return "desconocida"