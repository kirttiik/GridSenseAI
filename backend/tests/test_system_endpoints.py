from fastapi.testclient import TestClient

from app.main import create_app


def test_root_endpoint() -> None:
    client = TestClient(create_app())

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to GridSense AI Backend"}


def test_health_endpoint() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "GridSense AI Backend",
        "version": "1.0.0",
    }
