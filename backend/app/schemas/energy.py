from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EnergyDataResponse(BaseModel):
    id: UUID
    timestamp: datetime
    region: str
    source_type: str
    value_mw: float
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
