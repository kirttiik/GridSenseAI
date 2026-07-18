from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class GridStatusResponse(BaseModel):
    id: UUID
    timestamp: datetime
    region: str
    frequency_hz: float
    stability_index: float
    voltage_kv: float | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
