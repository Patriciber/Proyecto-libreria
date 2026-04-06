from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    """Prueba que el endpoint /health responda correctamente."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "service" in data
    assert "books_available" in data
