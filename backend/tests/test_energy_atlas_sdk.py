import httpx
import pytest
import respx

from app.ingestion.energy_atlas.endpoints import get_grid_frequency
from app.ingestion.energy_atlas.schemas import GridFrequencyResponse

pytestmark = pytest.mark.asyncio


@respx.mock
async def test_get_grid_frequency_success():
    # Mock the API response
    mock_data = {
        "success": True,
        "data": [{"timestamp": "2023-01-01T00:00:00Z", "frequency_hz": 50.05, "region": "North"}],
    }

    respx.get("https://api.energymap.in/api/intelligence/grid-frequency").mock(
        return_value=httpx.Response(200, json=mock_data)
    )

    response = await get_grid_frequency()

    # Validate schema parsing
    assert isinstance(response, GridFrequencyResponse)
    assert response.success is True
    assert len(response.data) == 1
    assert response.data[0].frequency_hz == 50.05
    assert response.data[0].region == "North"


@respx.mock
async def test_get_grid_frequency_retry_on_429():
    # We mock the route to return 429 first, then 200 success on the second attempt
    mock_success_data = {"success": True, "data": []}

    route = respx.get("https://api.energymap.in/api/intelligence/grid-frequency")
    route.side_effect = [
        httpx.Response(429, json={"error": "Rate limit exceeded"}),
        httpx.Response(200, json=mock_success_data),
    ]

    response = await get_grid_frequency()

    # Verify the SDK successfully parsed the eventual 200 response
    assert response.success is True
    # Verify the SDK actually attempted the request twice (1 fail, 1 success) due to tenacity retries
    assert route.call_count == 2
