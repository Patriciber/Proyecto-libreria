from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.middleware.base import BaseHTTPMiddleware
import os

from app.config import settings
from app.logging_config import logger
from app.container import container
from app.middleware import log_requests_middleware
from app.routers.books import router as books_router
from app.routers.newsletter import router as newsletter_router
from app.routers.auth import router as auth_router
from app.routers.favorites import router as favorites_router

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description
)

app.middleware("http")(log_requests_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

# Incluir routers de la API primero
app.include_router(books_router)
app.include_router(newsletter_router)
app.include_router(auth_router)
app.include_router(favorites_router)

# Ruta para el análisis interactivo
@app.get("/analisis")
async def read_analisis():
    """Sirve el dashboard de análisis interactivo."""
    return FileResponse("docs/analisis_final_interactivo.html")

@app.get("/health")
async def health_check():
    """Endpoint de health check simplificado para monitoreo."""
    return {"status": "healthy"}

@app.get("/api/v1/status")
async def get_system_status():
    """Ruta detallada para testeo manual de Backend y Frontend."""
    try:
        book_repo = container.book_repository
        user_repo = container.user_repository
        
        # Detectar el modo (Mock o Real) basado en el tipo de adaptador
        is_mock = "Mock" in str(type(book_repo))
        
        return {
            "status": "online",
            "environment": "development",
            "version": settings.version,
            "architecture": "hexagonal",
            "persistence": {
                "mode": "Mock (In-Memory)" if is_mock else "SQL Database",
                "database_mode_config": settings.database_mode
            },
            "data_count": {
                "books": len(await book_repo.get_all_books()),
                "users": len(await user_repo.get_all()) if hasattr(user_repo, 'get_all') else "N/A"
            },
            "security": {
                "auth_enabled": True,
                "jwt_algorithm": settings.algorithm
            }
        }
    except Exception as e:
        logger.error(f"Error en status endpoint: {e}")
        return {"status": "error", "message": str(e)}

# Servir archivos estáticos del frontend (index.html, styles.css, script.js)
# NOTA: Esto debe ir DESPUÉS de las rutas de la API
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload
    )