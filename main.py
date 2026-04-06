# Archivo principal - Redirige a la arquitectura hexagonal
# Este archivo mantiene compatibilidad hacia atrás mientras migramos

from app.main import app

# Re-exportar la aplicación para compatibilidad
__all__ = ["app"]

if __name__ == "__main__":
    # Ejecutar usando la nueva arquitectura
    from app.main import app as hexagonal_app
    import uvicorn
    from app.config import settings

    uvicorn.run(
        "app.main:hexagonal_app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload
    )
