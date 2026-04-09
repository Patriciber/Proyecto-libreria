from dataclasses import dataclass
from datetime import datetime

@dataclass
class Favorite:
    """Entidad pura de dominio que representa la relación de un usuario con un libro favorito."""
    id: int
    user_id: int
    book_id: int
    created_at: datetime
