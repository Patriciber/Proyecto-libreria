"""
Middleware personalizado para logging de requests y responses.
"""
import time
from fastapi import Request, Response
from app.logging_config import logger

async def log_requests_middleware(request: Request, call_next):
    """
    Middleware que loguea todas las requests HTTP entrantes.
    """
    start_time = time.time()

    # Log request
    logger.info(f"Request: {request.method} {request.url} from {request.client.host}")

    try:
        # Procesar la request
        response = await call_next(request)

        # Calcular tiempo de procesamiento
        process_time = time.time() - start_time

        # Log response
        logger.info(".2f")

        return response

    except Exception as e:
        # Log errores
        process_time = time.time() - start_time
        logger.error(".2f")
        raise