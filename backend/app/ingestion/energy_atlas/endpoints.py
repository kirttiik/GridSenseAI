from app.ingestion.energy_atlas.client import EnergyAtlasClient
from app.ingestion.energy_atlas.schemas import (
    CarbonResponse,
    DemandResponse,
    GenericAtlasResponse,
    GridFrequencyResponse,
    MarketResponse,
)

# Singleton client instance
_client = EnergyAtlasClient()


async def get_grid_frequency() -> GridFrequencyResponse:
    data = await _client.request("GET", "/api/intelligence/grid-frequency")
    return GridFrequencyResponse(**data)


async def get_demand_timeseries() -> DemandResponse:
    data = await _client.request("GET", "/api/intelligence/demand-timeseries")
    return DemandResponse(**data)


async def get_market_latest(market_type: str = "DAM") -> MarketResponse:
    data = await _client.request(
        "GET", "/developer/v1/market/iex/latest", params={"market_type": market_type}
    )
    return MarketResponse(**data)


async def get_carbon_intensity() -> CarbonResponse:
    data = await _client.request("GET", "/api/intelligence/carbon-intensity")
    return CarbonResponse(**data)


async def get_power_plants() -> GenericAtlasResponse:
    data = await _client.request("GET", "/api/intelligence/power-plants")
    return GenericAtlasResponse(**data)


async def get_transmission_edges() -> GenericAtlasResponse:
    data = await _client.request("GET", "/api/edges")
    return GenericAtlasResponse(**data)


async def get_substations_nodes() -> GenericAtlasResponse:
    data = await _client.request("GET", "/api/nodes")
    return GenericAtlasResponse(**data)


async def get_investments() -> GenericAtlasResponse:
    data = await _client.request("GET", "/api/intelligence/energy-investments")
    return GenericAtlasResponse(**data)
