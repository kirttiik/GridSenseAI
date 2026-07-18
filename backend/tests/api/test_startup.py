from fastapi.testclient import TestClient

from app.main import app


def test_app_startup_metadata():
    """Test that application metadata and openapi configurations are wired up correctly."""
    assert app.title == "GridSense AI"
    assert app.description == "GridSense AI Core Backend API for Energy Intelligence"
    assert app.contact["email"] == "support@gridsense.io"
    assert app.license_info["name"] == "Proprietary"


def test_openapi_schema():
    """Verify that OpenAPI schema can be generated without errors (this implicitly tests all routers and response models)."""
    client = TestClient(app)
    response = client.get("/api/v1/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "openapi" in schema
    assert "info" in schema
    assert schema["info"]["title"] == "GridSense AI"
    assert "/api/v1/health/live" in schema["paths"]
    assert "/api/v1/energy/" in schema["paths"]
