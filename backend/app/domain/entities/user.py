from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """Entidad de dominio que representa un usuario del sistema."""
    id: int
    username: str
    email: str
    full_name: str
    role: str
    is_active: bool

@dataclass
class UserInDB(User):
    """Extiende la entidad User para incluir el hash de la contraseña (solo para uso interno/DB)."""
    password_hash: str
