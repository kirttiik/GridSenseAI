from uuid import UUID

from fastapi import APIRouter, Depends, Query

from app.api.dependencies import get_forecast_service
from app.schemas.forecast import ForecastGenerateRequest, ForecastResponse
from app.schemas.responses import PaginatedResponse, SuccessResponse
from app.services.forecast_service import ForecastService

router = APIRouter()


@router.get("/latest", response_model=SuccessResponse[list[ForecastResponse]])
async def get_latest_forecast(
    model_id: UUID = Query(...), forecast_service: ForecastService = Depends(get_forecast_service)
):
    """
    Fetch the most recent pre-computed forecasts for a specific model.
    """
    data = await forecast_service.get_latest_forecast(model_id)
    # The current ForecastService returns empty list `[]`
    # Mapping requires transformation if it returned actual Prediction models
    return SuccessResponse(data=[])


@router.get("/history", response_model=PaginatedResponse[ForecastResponse])
async def get_forecast_history(
    model_name: str = Query(...),
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    forecast_service: ForecastService = Depends(get_forecast_service),
):
    """
    Fetch historical forecasts to evaluate model drift over time.
    """
    data = await forecast_service.forecast_history(model_name, limit=page_size)
    return PaginatedResponse(data=[], total=0, page=page, size=page_size)


@router.get("/accuracy", response_model=SuccessResponse[dict])
async def get_forecast_accuracy(
    model_name: str = Query(...), forecast_service: ForecastService = Depends(get_forecast_service)
):
    """
    Calculate MAPE or RMSE against actual historical values.
    """
    data = await forecast_service.forecast_accuracy(model_name)
    return SuccessResponse(data=data)


@router.get("/models", response_model=SuccessResponse[list[dict]])
async def compare_models(forecast_service: ForecastService = Depends(get_forecast_service)):
    """
    Compare performance metrics across all active models in the registry.
    """
    data = await forecast_service.compare_models()
    return SuccessResponse(data=data)


@router.get("/summary", response_model=SuccessResponse[dict])
async def get_forecast_summary(forecast_service: ForecastService = Depends(get_forecast_service)):
    """
    Fetch forecast summary.
    """
    return SuccessResponse(data={"status": "Operational"})


@router.get("/trends", response_model=SuccessResponse[list[dict]])
async def get_forecast_trends(forecast_service: ForecastService = Depends(get_forecast_service)):
    """
    Fetch forecast trends.
    """
    return SuccessResponse(data=[])


@router.post("/generate", response_model=SuccessResponse[dict])
async def generate_forecast(
    request: ForecastGenerateRequest,
    forecast_service: ForecastService = Depends(get_forecast_service),
):
    """
    Trigger an on-demand forecast generation pipeline.
    """
    data = await forecast_service.generate_forecast(request.model_name, request.target_date)
    return SuccessResponse(data=data)
