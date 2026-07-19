from typing import Any

from pydantic import BaseModel, ConfigDict


class AnalyticsResponse(BaseModel):
    summary: dict[str, Any]
    metrics: list[dict[str, Any]]
    metadata: dict[str, Any] | None = None

    model_config = ConfigDict(from_attributes=True)


class TrendResponse(BaseModel):
    trend_type: str
    series_data: list[dict[str, Any]]
    average: float | None = None
    peak: float | None = None

    model_config = ConfigDict(from_attributes=True)


class SummaryResponse(BaseModel):
    total: float
    unit: str
    breakdown: list[dict[str, Any]] | None = None

    model_config = ConfigDict(from_attributes=True)

class AnalyticsFilter(BaseModel):
    start_date: str | None = None
    end_date: str | None = None
    state: str | None = None
    region: str | None = None
    fuel: str | None = None
    market_type: str | None = None
    resolution: str = "daily"  # hourly, daily, monthly
