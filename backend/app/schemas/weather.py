from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class WeatherDataResponse(BaseModel):
    id: UUID
    timestamp: datetime
    region: str
    temperature_c: float
    solar_irradiance_wm2: float
    wind_speed_ms: float
    humidity_pct: float
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
