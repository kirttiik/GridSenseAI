import pytest
from fastapi.testclient import TestClient
from app.main import app

def test_health_check_basic():
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "uptime_seconds" in data
    assert data["database"] == "unknown"

def test_liveness_probe():
    client = TestClient(app)
    response = client.get("/api/v1/health/live")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"

@pytest.mark.asyncio
def test_readiness_probe():
    # Note: If the DB is not fully running, this may return 200 with db="error"
    client = TestClient(app)
    response = client.get("/api/v1/health/ready")
    assert response.status_code == 200
    data = response.json()
    # It checks the DB, so it should be ok or error depending on the local env.
    assert data["database"] in ["ok", "error"]
