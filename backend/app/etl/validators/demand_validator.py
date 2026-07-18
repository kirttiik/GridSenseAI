from datetime import datetime

from pydantic import BaseModel, Field

from app.etl.base.base_validator import BaseValidator


class DemandRecordSchema(BaseModel):
    """Pydantic schema for raw Demand data."""

    timestamp: datetime
    state_abbreviation: str = Field(..., min_length=2, max_length=10)
    demand_mw: float = Field(..., ge=0, description="Demand must be positive")


class DemandValidator(BaseValidator):
    @property
    def schema(self) -> type[BaseModel]:
        return DemandRecordSchema
