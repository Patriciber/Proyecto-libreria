"""
Excepciones personalizadas del dominio.
Define errores específicos de negocio que pueden ocurrir en la aplicación.
"""

class DomainException(Exception):
    """Excepción base para errores del dominio."""
    pass

class BookNotFoundError(DomainException):
    """Excepción cuando un libro no es encontrado."""
    def __init__(self, book_id: int):
        self.book_id = book_id
        super().__init__(f"Book with id {book_id} not found")

class InvalidBookDataError(DomainException):
    """Excepción para datos de libro inválidos."""
    def __init__(self, message: str):
        super().__init__(f"Invalid book data: {message}")

class NewsletterSubscriptionError(DomainException):
    """Excepción para errores en suscripción al newsletter."""
    def __init__(self, email: str, reason: str = None):
        self.email = email
        message = f"Failed to subscribe {email}"
        if reason:
            message += f": {reason}"
        super().__init__(message)

class RepositoryError(DomainException):
    """Excepción base para errores de repositorio."""
    pass

class DatabaseConnectionError(RepositoryError):
    """Excepción para errores de conexión a base de datos."""
    def __init__(self, message: str = "Database connection failed"):
        super().__init__(message)