from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class IncidentResponse(BaseModel):
    id: UUID
    title: str
    description: str | None = None
    region_id: UUID
    severity: str
    status: str
    start_time: datetime
    end_time: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class OutageResponse(BaseModel):
    id: UUID
    equipment_type: str
    equipment_id: UUID
    reason: str | None = None
    status: str
    start_time: datetime
    end_time: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
