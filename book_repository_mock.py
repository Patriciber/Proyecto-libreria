from typing import List, Optional
from app.domain.entities.book import Book
from app.ports.repositories.book_repository import BookRepositoryPort

class BookRepositoryMock(BookRepositoryPort):
    """
    Adaptador mock del repositorio de libros.
    Implementa BookRepositoryPort usando datos en memoria.
    Útil para desarrollo, testing y demos.
    """

    def __init__(self):
        self._books = [
            Book(
                id=1, title="Horizonte Perdido", author="Elena Vargas",
                rating=4.8, pages=342, duration="12h 30m",
                category="ciencia_ficcion", price=0.0, is_premium=False,
                cover_style="mockup-1", icon="ri-planet-line",
                description="En un futuro donde la humanidad se ha expandido por las estrellas...",
                is_favorite=False
            ),
            Book(
                id=2, title="Código Limpio", author="David Chen",
                rating=4.9, pages=464, duration="15h 10m",
                category="tecnologia", price=14.99, is_premium=True,
                cover_style="mockup-2", icon="ri-macbook-line",
                description="Todo desarrollador necesita saber cómo escribir buen código...",
                is_favorite=True
            ),
            Book(
                id=3, title="Reino de Sombras", author="Marc Sterling",
                rating=4.5, pages=512, duration="18h 00m",
                category="fantasia", price=9.99, is_premium=False,
                cover_style="mockup-3", icon="ri-sword-line",
                description="Una guerra mágica amenaza con destruir el continente...",
                is_favorite=False
            ),
            Book(
                id=4, title="La Mente Humana", author="Dra. Sarah Jenkins",
                rating=4.7, pages=280, duration="09h 45m",
                category="autoayuda", price=0.0, is_premium=False,
                cover_style="mockup-4", icon="ri-psychotherapy-line",
                description="Descubre cómo funciona el cerebro y optimiza tus pensamientos.",
                is_favorite=False
            ),
            Book(
                id=5, title="Amor en Tiempos Cuánticos", author="Lucía M.",
                rating=4.6, pages=310, duration="10h 20m",
                category="romance", price=4.99, is_premium=False,
                cover_style="mockup-5", icon="ri-empathize-line",
                description="Dos científicos descubren que el amor puede viajar entre universos.",
                is_favorite=False
            ),
            Book(
                id=6, title="El Enigma del Sótano", author="R. K. Black",
                rating=4.4, pages=390, duration="11h 15m",
                category="misterio", price=0.0, is_premium=True,
                cover_style="mockup-1", icon="ri-search-eye-line",
                description="Un detective retirado debe resolver un último caso.",
                is_favorite=True
            ),
            Book(
                id=7, title="Amanecer en Marte", author="Noah Briggs",
                rating=4.3, pages=296, duration="11h 05m",
                category="ciencia_ficcion", price=12.49, is_premium=False,
                cover_style="mockup-2", icon="ri-rocket-line",
                description="La primera colonia humana en Marte enfrenta desafíos internos y externos.",
                is_favorite=False
            ),
            Book(
                id=8, title="Secretos del Palacio", author="Ana Ríos",
                rating=4.2, pages=422, duration="14h 40m",
                category="historia", price=7.50, is_premium=False,
                cover_style="mockup-3", icon="ri-book-line",
                description="Una biografía histórica de una reina olvidada por los libros de texto.",
                is_favorite=False
            ),
            Book(
                id=9, title="Negocios sin Fronteras", author="Carlos Mateo",
                rating=4.8, pages=215, duration="08h 20m",
                category="negocios", price=19.99, is_premium=True,
                cover_style="mockup-4", icon="ri-briefcase-4-line",
                description="Estrategias para escalar startups globales desde cero.",
                is_favorite=True
            ),
            Book(
                id=10, title="Misterio en la Ciudadela", author="Lena Torres",
                rating=4.6, pages=374, duration="13h 00m",
                category="misterio", price=5.99, is_premium=False,
                cover_style="mockup-5", icon="ri-search-eye-line",
                description="Un peligroso secreto emerge de las profundidades de una antigua citadela.",
                is_favorite=False
            ),
            Book(
                id=11, title="Espejos del Alma", author="Mariana López",
                rating=4.7, pages=260, duration="09h 10m",
                category="autoayuda", price=0.0, is_premium=False,
                cover_style="mockup-1", icon="ri-heart-line",
                description="Guía práctica para la autoconexión y el equilibrio emocional.",
                is_favorite=False
            ),
            Book(
                id=12, title="Viaje a la Creatividad", author="Tomás Pérez",
                rating=4.9, pages=298, duration="10h 40m",
                category="tecnologia", price=11.35, is_premium=False,
                cover_style="mockup-2", icon="ri-lightbulb-line",
                description="Cómo usar tecnología para potenciar ideas innovadoras en tu carrera.",
                is_favorite=False
            ),
        ]

    def get_all_books(self) -> List[Book]:
        return self._books.copy()

    def get_books_by_category(self, category: str) -> List[Book]:
        return [book for book in self._books if book.category == category]

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self._books if book.id == book_id), None)

    def search_books(self, query: str) -> List[Book]:
        query_lower = query.lower()
        return [
            book for book in self._books
            if (query_lower in book.title.lower() or
                query_lower in book.author.lower() or
                query_lower in book.description.lower())
        ]

    def get_featured_books(self, limit: int = 3) -> List[Book]:
        sorted_books = sorted(self._books, key=lambda x: x.rating, reverse=True)
        return sorted_books[:limit]