from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RegionResponse(BaseModel):
    id: UUID
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True)


class StateResponse(BaseModel):
    id: UUID
    region_id: UUID
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True)


class FuelTypeResponse(BaseModel):
    id: UUID
    code: str
    name: str
    category: str

    model_config = ConfigDict(from_attributes=True)


class EnergySourceResponse(BaseModel):
    id: UUID
    code: str
    name: str
    is_renewable: bool

    model_config = ConfigDict(from_attributes=True)
