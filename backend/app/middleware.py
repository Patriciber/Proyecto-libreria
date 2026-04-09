"""
Middleware personalizado para logging de requests y responses.
"""
import time
from fastapi import Request
from app.logging_config import logger

async def log_requests_middleware(request: Request, call_next):
    """
    Middleware que loguea todas las requests HTTP entrantes y su tiempo de ejecución.
    """
    start_time = time.time()

    # Log request info
    logger.info(f"Incoming Request: {request.method} {request.url.path} from {request.client.host if request.client else 'unknown'}")

    try:
        # Continuar con la cadena de procesamiento
        response = await call_next(request)

        # Calcular tiempo de procesamiento
        process_time = (time.time() - start_time) * 1000  # en milisegundos

        # Log de éxito
        logger.info(f"Response: {response.status_code} | Processed in: {process_time:.2f}ms")

        return response

    except Exception as e:
        # Re-capturar tiempo en caso de error
        process_time = (time.time() - start_time) * 1000
        logger.error(f"Request Failed: {request.method} {request.url.path} | Error: {str(e)} | Time: {process_time:.2f}ms")
        raise