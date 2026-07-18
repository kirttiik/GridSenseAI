from typing import Any

from pydantic import BaseModel, Field


class GridFrequencyData(BaseModel):
    timestamp: str
    frequency_hz: float
    region: str | None = None


class GridFrequencyResponse(BaseModel):
    success: bool
    data: list[GridFrequencyData] = Field(default_factory=list)


class DemandData(BaseModel):
    timestamp: str
    state: str
    demand_mw: float
    peak_demand_mw: float | None = None


class DemandResponse(BaseModel):
    success: bool
    data: list[DemandData] = Field(default_factory=list)


class MarketData(BaseModel):
    timestamp: str
    market_type: str
    mcp_rs_mwh: float
    mcv_mw: float


class MarketResponse(BaseModel):
    success: bool
    data: list[MarketData] = Field(default_factory=list)


class CarbonData(BaseModel):
    timestamp: str
    state: str
    intensity_gco2_kwh: float


class CarbonResponse(BaseModel):
    success: bool
    data: list[CarbonData] = Field(default_factory=list)


class GenericAtlasResponse(BaseModel):
    success: bool
    data: Any
