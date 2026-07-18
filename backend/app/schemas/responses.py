from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    """Standard success response wrapper."""

    success: bool = True
    data: T


class ErrorResponse(BaseModel):
    """Standard error response."""

    success: bool = False
    error: str = Field(description="Error message")
    code: str | None = Field(default=None, description="Internal error code if applicable")


class PaginatedResponse(BaseModel, Generic[T]):
    """Standard paginated response wrapper."""

    success: bool = True
    data: list[T]
    total: int = Field(description="Total number of items")
    page: int = Field(default=1, description="Current page number")
    size: int = Field(default=100, description="Page size limit")


class MessageResponse(BaseModel):
    """Standard generic message response."""

    success: bool = True
    message: str


class HealthResponse(BaseModel):
    """Health status response."""

    status: str = Field(..., description="Overall health status (e.g., 'ok', 'error')")
    environment: str = Field(..., description="Current deployment environment")
    version: str = Field(..., description="API version")
    database: str = Field(default="unknown", description="Database connectivity status")
    energy_atlas_api: str = Field(default="unknown", description="Energy Atlas API connectivity status")
    last_sync_time: float | None = Field(default=None, description="Timestamp of the last successful sync")
    uptime_seconds: float | None = Field(default=None, description="Application uptime in seconds")
    
    # Table counts
    energy_records: int = Field(default=0, description="Total EnergyData records")
    weather_records: int = Field(default=0, description="Total WeatherData records")
    grid_records: int = Field(default=0, description="Total GridStatus records")
    market_records: int = Field(default=0, description="Total MarketData records")
    ai_insight_records: int = Field(default=0, description="Total AIInsight records")
