from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ForecastResponse(BaseModel):
    model_id: UUID
    model_name: str
    target_date: str
    predicted_values: list[dict[str, Any]]
    accuracy_metrics: dict[str, float] | None = None

    model_config = ConfigDict(from_attributes=True)


class ForecastGenerateRequest(BaseModel):
    model_name: str
    target_date: str
