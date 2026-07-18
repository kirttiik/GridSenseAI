from uuid import UUID

from fastapi import APIRouter, Depends, Path, Query

from app.api.dependencies import get_assets_service
from app.schemas.assets import PowerPlantResponse, SubstationResponse, TransmissionLineResponse
from app.schemas.responses import PaginatedResponse, SuccessResponse
from app.services.assets_service import AssetsService

router = APIRouter()


@router.get("/plants", response_model=PaginatedResponse[PowerPlantResponse])
async def get_power_plants(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    assets_service: AssetsService = Depends(get_assets_service),
):
    """
    Fetch all power plants with pagination.
    """
    skip = (page - 1) * page_size
    data = await assets_service.get_power_plants(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/plants/{id}", response_model=SuccessResponse[PowerPlantResponse])
async def get_power_plant(
    id: UUID = Path(...), assets_service: AssetsService = Depends(get_assets_service)
):
    """
    Fetch a single power plant by ID.
    """
    data = await assets_service.get_power_plant(id)
    return SuccessResponse(data=data)


@router.get("/substations", response_model=PaginatedResponse[SubstationResponse])
async def get_substations(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    assets_service: AssetsService = Depends(get_assets_service),
):
    """
    Fetch all substations with pagination.
    """
    skip = (page - 1) * page_size
    data = await assets_service.get_substations(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/transmission-lines", response_model=PaginatedResponse[TransmissionLineResponse])
async def get_transmission_lines(
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    assets_service: AssetsService = Depends(get_assets_service),
):
    """
    Fetch all transmission lines with pagination.
    """
    skip = (page - 1) * page_size
    data = await assets_service.get_transmission_lines(skip=skip, limit=page_size)
    return PaginatedResponse(data=data, total=len(data), page=page, size=page_size)


@router.get("/operators", response_model=SuccessResponse[list[dict]])
async def get_operators(assets_service: AssetsService = Depends(get_assets_service)):
    """
    Fetch all operators (placeholder endpoint mapping to reference operators usually).
    """
    return SuccessResponse(data=[])


@router.get("/renewable-parks", response_model=SuccessResponse[list[dict]])
async def get_renewable_parks(assets_service: AssetsService = Depends(get_assets_service)):
    """
    Fetch all renewable parks (placeholder).
    """
    return SuccessResponse(data=[])
