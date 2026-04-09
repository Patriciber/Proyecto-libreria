from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuración centralizada de la aplicación."""

    # API Settings
    app_name: str = "Lumière Digital Library API"
    version: str = "1.0.0"
    description: str = "API para la biblioteca digital Lumière"

    # Server Settings
    host: str = "127.0.0.1"
    port: int = 8080
    reload: bool = True

    # CORS Settings
    cors_origins: list = [
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]
    cors_allow_credentials: bool = True
    cors_allow_methods: list = ["*"]
    cors_allow_headers: list = ["*"]

    # Database Settings (para futuro uso)
    database_url: str = "sqlite:///./lumiere.db"

    # Security Settings
    secret_key: str = "lumiere-secret-key-2026-very-secure"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = False

# Instancia global de configuración
settings = Settings()