from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIInsightResponse(BaseModel):
    id: UUID
    timestamp: datetime
    region: str
    title: str
    summary: str
    severity: str
    confidence: int
    recommendation: str | None = None
    target_timeframe: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
