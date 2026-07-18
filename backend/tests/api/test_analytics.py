from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_analytics_service
from app.main import app
from app.services.analytics_service import AnalyticsService


@pytest.fixture
def override_analytics_service():
    mock_service = AsyncMock(spec=AnalyticsService)

    mock_service.capacity_summary.return_value = {"total_installed_mw": 350000}
    mock_service.market_statistics.return_value = {"market_share_rtm": 15.0}

    app.dependency_overrides[get_analytics_service] = lambda: mock_service
    yield mock_service
    app.dependency_overrides = {}


def test_get_generation_summary(override_analytics_service):
    client = TestClient(app)
    response = client.get("/api/v1/analytics/generation-summary")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["total"] == 150000
    assert data["data"]["unit"] == "MW"


def test_get_capacity_utilization(override_analytics_service):
    client = TestClient(app)
    response = client.get("/api/v1/analytics/capacity-utilization")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["total"] == 350000


def test_get_market_summary(override_analytics_service):
    client = TestClient(app)
    response = client.get("/api/v1/analytics/market-summary")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["summary"]["market_share_rtm"] == 15.0
