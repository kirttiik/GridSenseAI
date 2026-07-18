from fastapi import APIRouter, Depends

from app.api.dependencies import get_operations_service
from app.schemas.operations import IncidentResponse, OutageResponse
from app.schemas.responses import SuccessResponse
from app.services.operations_service import OperationsService

router = APIRouter()


@router.get("/incidents", response_model=SuccessResponse[list[IncidentResponse]])
async def get_incidents(operations_service: OperationsService = Depends(get_operations_service)):
    """
    Fetch grid operations incidents.
    """
    # Assuming future implementation inside the service
    return SuccessResponse(data=[])


@router.get("/outages", response_model=SuccessResponse[list[OutageResponse]])
async def get_outages(operations_service: OperationsService = Depends(get_operations_service)):
    """
    Fetch equipment outages.
    """
    # Assuming future implementation inside the service
    return SuccessResponse(data=[])


@router.get("/maintenance", response_model=SuccessResponse[list[dict]])
async def get_maintenance(operations_service: OperationsService = Depends(get_operations_service)):
    """
    Fetch maintenance schedules.
    """
    return SuccessResponse(data=[])


@router.get("/alerts", response_model=SuccessResponse[list[dict]])
async def get_alerts(operations_service: OperationsService = Depends(get_operations_service)):
    """
    Fetch operation alerts.
    """
    return SuccessResponse(data=[])


@router.get("/posoco-psp", response_model=SuccessResponse[list[dict]])
async def get_posoco_psp(operations_service: OperationsService = Depends(get_operations_service)):
    """
    Fetch POSOCO Daily Power Supply Position data.
    """
    # Using existing service method
    data = await operations_service.get_posoco_daily_psp()
    return SuccessResponse(data=data)
