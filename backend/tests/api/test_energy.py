import uuid
from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_energy_service
from app.main import app
from app.models.user import User
from app.security.permissions.deps import get_current_active_user
from app.services.energy_service import EnergyService


@pytest.fixture
def override_user():
    user = User(id="c31671fc-a7ad-45ea-9005-4c0cfb638c03", is_active=True)
    app.dependency_overrides[get_current_active_user] = lambda: user
    yield user
    app.dependency_overrides = {}


# Mock Data
MOCK_UUID = uuid.uuid4()
mock_energy_data = [
    {
        "timestamp": "2026-07-17T10:00:00Z",
        "fuel_type_id": str(MOCK_UUID),
        "date_key": 20260717,
        "generation_mw": 1200.5,
    }
]


@pytest.fixture
def override_energy_service():
    mock_service = AsyncMock(spec=EnergyService)

    # Setup mock returns
    mock_service.get_current_generation.return_value = mock_energy_data
    mock_service.get_generation_history.return_value = mock_energy_data
    mock_service.get_generation_summary.return_value = {"total_generation_mw": 50000}

    app.dependency_overrides[get_energy_service] = lambda: mock_service
    yield mock_service
    app.dependency_overrides = {}


def test_get_current_generation(override_energy_service, override_user):
    client = TestClient(app)
    response = client.get("/api/v1/energy/current")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["data"]) == 1
    assert data["data"][0]["generation_mw"] == 1200.5


def test_get_generation_summary(override_energy_service, override_user):
    client = TestClient(app)
    response = client.get("/api/v1/energy/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["total_generation_mw"] == 50000
