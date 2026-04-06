from hypothesis import given, strategies as st
from app.adapters.repositories.book_repository_mock import BookRepositoryMock

def test_search_always_returns_list():
    """Test básico: La búsqueda siempre debe devolver una lista, sin importar la query."""
    repo = BookRepositoryMock()
    
    # Probamos con strings aleatorios generados por Hypothesis
    @given(st.text())
    def run_property_test(query):
        results = repo.search_books(query)
        assert isinstance(results, list)
        # El resultado no debería ser mayor que el total de libros
        assert len(results) <= len(repo._books)

    run_property_test()

def test_featured_books_limit_property():
    """Hypothesis valida que el límite pedido nunca sea excedido."""
    repo = BookRepositoryMock()
    
    @given(st.integers(min_value=0, max_value=100))
    def run_limit_test(limit):
        featured = repo.get_featured_books(limit)
        assert len(featured) <= limit
        # Pero tampoco puede devolver más de lo que hay en el repo
        assert len(featured) <= len(repo._books)

    run_limit_test()
