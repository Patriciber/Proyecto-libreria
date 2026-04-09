from typing import Optional
from datetime import timedelta
from app.domain.entities.user import User, UserInDB
from app.models.user_schema import UserCreate
from app.ports.repositories.user_repository import UserRepositoryPort
from app.adapters.security.security_adapter import SecurityAdapter
from app.config import settings

class AuthService:
    """Servicio de aplicación para gestionar la autenticación y seguridad."""
    
    def __init__(self, user_repository: UserRepositoryPort, security_adapter: SecurityAdapter):
        self.user_repo = user_repository
        self.security = security_adapter
        
    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Verifica las credenciales del usuario y lo devuelve si son correctas."""
        user_db = await self.user_repo.get_by_username(username)
        if not user_db:
            return None
        
        if not self.security.verify_password(password, user_db.password_hash):
            return None
            
        return User(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email,
            full_name=user_db.full_name,
            role=user_db.role,
            is_active=user_db.is_active
        )

    def create_token_for_user(self, user: User) -> str:
        """Genera un token JWT para el usuario proporcionado."""
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token = self.security.create_access_token(
            data={"sub": user.username, "role": user.role},
            expires_delta=access_token_expires
        )
        return access_token

    async def get_user_from_token(self, token: str) -> Optional[User]:
        """Valida un token y devuelve el usuario asociado."""
        payload = self.security.decode_token(token)
        if not payload:
            return None
        
        username: str = payload.get("sub")
        if not username:
            return None
            
        user_db = await self.user_repo.get_by_username(username)
        if not user_db:
            return None
            
        return User(
            id=user_db.id,
            username=user_db.username,
            email=user_db.email,
            full_name=user_db.full_name,
            role=user_db.role,
            is_active=user_db.is_active
        )

    async def register_user(self, user_data: UserCreate) -> User:
        """Registra un nuevo usuario en el sistema."""
        # Verificar si ya existe
        existing = await self.user_repo.get_by_username(user_data.username)
        if existing:
            raise ValueError(f"El usuario '{user_data.username}' ya está registrado")
        
        # Hashear contraseña
        hashed_password = self.security.get_password_hash(user_data.password)
        
        # Crear entidad UserInDB
        new_user_db = UserInDB(
            id=None,  # El repositorio asignará el ID si es Mock o DB real
            username=user_data.username,
            email=user_data.email,
            full_name=user_data.full_name,
            role="user",
            is_active=True,
            password_hash=hashed_password
        )
        
        # Guardar en repositorio
        saved_user_db = await self.user_repo.save(new_user_db)
        
        return User(
            id=saved_user_db.id,
            username=saved_user_db.username,
            email=saved_user_db.email,
            full_name=saved_user_db.full_name,
            role=saved_user_db.role,
            is_active=saved_user_db.is_active
        )
