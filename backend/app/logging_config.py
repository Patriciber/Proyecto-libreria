"""
Configuración centralizada de logging para la aplicación.
"""
import logging
import sys
from pathlib import Path
from app.config import settings

def setup_logging():
    """Configura el sistema de logging de la aplicación."""

    # Crear directorio de logs si no existe
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Configuración del logger raíz
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # Log a archivo
            logging.FileHandler(log_dir / "lumiere.log", encoding='utf-8'),
            # Log a consola
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Configurar niveles específicos para módulos
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("fastapi").setLevel(logging.WARNING)
    logging.getLogger("app").setLevel(logging.DEBUG)

    # Logger específico de la aplicación
    logger = logging.getLogger("lumiere")
    logger.info(f"Iniciando {settings.app_name} v{settings.version}")

    return logger

# Logger global de la aplicación
logger = setup_logging()