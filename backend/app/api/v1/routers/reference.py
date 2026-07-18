from fastapi import APIRouter, Depends, Query

from app.api.dependencies import get_reference_service
from app.schemas.reference import (
    EnergySourceResponse,
    FuelTypeResponse,
    RegionResponse,
    StateResponse,
)
from app.schemas.responses import PaginatedResponse, SuccessResponse
from app.services.reference_service import ReferenceService

router = APIRouter()


@router.get("/regions", response_model=PaginatedResponse[RegionResponse])
async def get_regions(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    reference_service: ReferenceService = Depends(get_reference_service),
):
    """
    Fetch all regions.
    """
    skip = (page - 1) * page_size
    data = await reference_service.get_regions(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/states", response_model=PaginatedResponse[StateResponse])
async def get_states(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    reference_service: ReferenceService = Depends(get_reference_service),
):
    """
    Fetch all states.
    """
    skip = (page - 1) * page_size
    data = await reference_service.get_states(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/fuel-types", response_model=PaginatedResponse[FuelTypeResponse])
async def get_fuel_types(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    reference_service: ReferenceService = Depends(get_reference_service),
):
    """
    Fetch all fuel types.
    """
    skip = (page - 1) * page_size
    data = await reference_service.get_fuel_types(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/energy-sources", response_model=PaginatedResponse[EnergySourceResponse])
async def get_energy_sources(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    reference_service: ReferenceService = Depends(get_reference_service),
):
    """
    Fetch all energy sources.
    """
    skip = (page - 1) * page_size
    data = await reference_service.get_energy_sources(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/operators", response_model=SuccessResponse[list[dict]])
async def get_operators(reference_service: ReferenceService = Depends(get_reference_service)):
    """
    Fetch all operators.
    """
    # Placeholder for operators reference lookup
    return SuccessResponse(data=[])


@router.get("/market-types", response_model=SuccessResponse[list[dict]])
async def get_market_types(reference_service: ReferenceService = Depends(get_reference_service)):
    """
    Fetch all market types.
    """
    # Placeholder for market types
    return SuccessResponse(data=[])


@router.get("/voltage-levels", response_model=SuccessResponse[list[dict]])
async def get_voltage_levels(reference_service: ReferenceService = Depends(get_reference_service)):
    """
    Fetch all voltage levels.
    """
    # Placeholder for voltage levels
    return SuccessResponse(data=[])
