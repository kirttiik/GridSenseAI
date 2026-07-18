from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MarketDataResponse(BaseModel):
    id: UUID
    timestamp: datetime
    region: str
    market_type: str
    price_inr: float
    volume_mwh: float | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
