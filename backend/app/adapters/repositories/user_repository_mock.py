from typing import List, Optional
from app.domain.entities.user import User, UserInDB
from app.ports.repositories.user_repository import UserRepositoryPort
from app.adapters.security.security_adapter import SecurityAdapter

class UserRepositoryMock(UserRepositoryPort):
    """
    Implementación Mock del repositorio de usuarios.
    Contiene usuarios predefinidos para pruebas de seguridad.
    """
    
    def __init__(self, security_adapter: SecurityAdapter):
        self.security = security_adapter
        # Usuarios iniciales con contraseñas hasheadas
        self._users = [
            UserInDB(
                id=1,
                username="admin",
                email="admin@lumiere.com",
                full_name="Administrator",
                role="admin",
                is_active=True,
                password_hash=self.security.get_password_hash("admin123")
            ),
            UserInDB(
                id=2,
                username="user",
                email="user@lumiere.com",
                full_name="Standard User",
                role="user",
                is_active=True,
                password_hash=self.security.get_password_hash("user123")
            )
        ]

    async def get_by_username(self, username: str) -> Optional[UserInDB]:
        return next((u for u in self._users if u.username == username), None)

    async def get_by_id(self, user_id: int) -> Optional[User]:
        user_db = next((u for u in self._users if u.id == user_id), None)
        if user_db:
            return User(
                id=user_db.id,
                username=user_db.username,
                email=user_db.email,
                full_name=user_db.full_name,
                role=user_db.role,
                is_active=user_db.is_active
            )
        return None

    async def save(self, user: UserInDB) -> UserInDB:
        if user.id is None:
            max_id = max((u.id for u in self._users), default=0)
            user.id = max_id + 1
            
        existing = await self.get_by_username(user.username)
        if existing:
            self._users.remove(existing)
        self._users.append(user)
        return user
