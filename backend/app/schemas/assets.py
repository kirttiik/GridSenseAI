from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PowerPlantResponse(BaseModel):
    id: UUID
    name: str
    region_id: UUID
    state_id: UUID
    operator_id: UUID
    fuel_type_id: UUID
    energy_source_id: UUID
    installed_capacity_mw: float
    latitude: float | None = None
    longitude: float | None = None
    status: str

    model_config = ConfigDict(from_attributes=True)


class SubstationResponse(BaseModel):
    id: UUID
    name: str
    region_id: UUID
    state_id: UUID
    voltage_level_id: UUID
    capacity_mva: float | None = None
    status: str

    model_config = ConfigDict(from_attributes=True)


class TransmissionLineResponse(BaseModel):
    id: UUID
    name: str
    region_id: UUID
    voltage_level_id: UUID
    length_ckm: float | None = None
    status: str

    model_config = ConfigDict(from_attributes=True)


class OperatorResponse(BaseModel):
    id: UUID
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True)
