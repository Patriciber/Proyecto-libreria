from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.user import User, UserInDB

class UserRepositoryPort(ABC):
    """Puerto (contrato) para el repositorio de usuarios."""
    
    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[UserInDB]:
        """Obtiene un usuario (incluyendo password_hash) por su nombre de usuario."""
        pass
    
    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        """Obtiene un usuario público (sin password_hash) por su ID."""
        pass

    @abstractmethod
    async def save(self, user: UserInDB) -> UserInDB:
        """Guarda o actualiza un usuario en el sistema."""
        pass
