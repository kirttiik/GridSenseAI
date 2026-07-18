import uuid
from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_assets_service
from app.main import app
from app.services.assets_service import AssetsService
from app.services.exceptions import ResourceNotFound

MOCK_UUID = uuid.uuid4()
mock_plants = [
    {
        "id": str(MOCK_UUID),
        "name": "Test Plant",
        "region_id": str(uuid.uuid4()),
        "state_id": str(uuid.uuid4()),
        "operator_id": str(uuid.uuid4()),
        "fuel_type_id": str(uuid.uuid4()),
        "energy_source_id": str(uuid.uuid4()),
        "installed_capacity_mw": 1000.0,
        "status": "ACTIVE",
    }
]


@pytest.fixture
def override_assets_service():
    mock_service = AsyncMock(spec=AssetsService)

    # Setup mock returns
    mock_service.get_power_plants.return_value = mock_plants
    mock_service.get_power_plant.return_value = mock_plants[0]

    # Setup 404 behavior for specific mocked calls later
    def mock_get_plant_side_effect(plant_id):
        if str(plant_id) == str(MOCK_UUID):
            return mock_plants[0]
        raise ResourceNotFound("Power plant not found")

    mock_service.get_power_plant.side_effect = mock_get_plant_side_effect

    app.dependency_overrides[get_assets_service] = lambda: mock_service
    yield mock_service
    app.dependency_overrides = {}


def test_get_power_plants(override_assets_service):
    client = TestClient(app)
    response = client.get("/api/v1/assets/plants")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["total"] == 1
    assert data["data"][0]["name"] == "Test Plant"


def test_get_power_plant_found(override_assets_service):
    client = TestClient(app)
    response = client.get(f"/api/v1/assets/plants/{MOCK_UUID}")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["name"] == "Test Plant"


def test_get_power_plant_not_found(override_assets_service):
    client = TestClient(app)
    random_uuid = uuid.uuid4()
    response = client.get(f"/api/v1/assets/plants/{random_uuid}")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert data["error"] == "Power plant not found"
    assert data["code"] == "RESOURCE_NOT_FOUND"
