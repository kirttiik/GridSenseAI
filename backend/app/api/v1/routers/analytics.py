from fastapi import APIRouter, Depends

from app.api.dependencies import get_analytics_service
from app.schemas.analytics import AnalyticsResponse, SummaryResponse, TrendResponse
from app.schemas.responses import SuccessResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter()


@router.get("/generation-summary", response_model=SuccessResponse[SummaryResponse])
async def get_generation_summary(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    """
    Fetch generation summary.
    """
    # Assuming some orchestrations or simple proxy
    return SuccessResponse(data=SummaryResponse(total=150000, unit="MW"))


@router.get("/demand-summary", response_model=SuccessResponse[SummaryResponse])
async def get_demand_summary(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch demand summary.
    """
    return SuccessResponse(data=SummaryResponse(total=145000, unit="MW"))


@router.get("/grid-summary", response_model=SuccessResponse[AnalyticsResponse])
async def get_grid_summary(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch grid summary.
    """
    return SuccessResponse(data=AnalyticsResponse(summary={"status": "Optimal"}, metrics=[]))


@router.get("/market-summary", response_model=SuccessResponse[AnalyticsResponse])
async def get_market_summary(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch market summary.
    """
    data = await analytics_service.market_statistics()
    return SuccessResponse(data=AnalyticsResponse(summary=data, metrics=[]))


@router.get("/carbon-summary", response_model=SuccessResponse[SummaryResponse])
async def get_carbon_summary(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch carbon summary.
    """
    data = await analytics_service.carbon_summary()
    return SuccessResponse(
        data=SummaryResponse(
            total=data.get("avg_carbon_intensity", 0.0), unit=data.get("unit", "gCO2/kWh")
        )
    )


@router.get("/weather-summary", response_model=SuccessResponse[AnalyticsResponse])
async def get_weather_summary(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch weather summary.
    """
    return SuccessResponse(data=AnalyticsResponse(summary={"temperature_avg": 30.5}, metrics=[]))


@router.get("/state-comparison", response_model=SuccessResponse[AnalyticsResponse])
async def get_state_comparison(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    """
    Fetch state comparison.
    """
    data = await analytics_service.top_generating_states()
    return SuccessResponse(data=AnalyticsResponse(summary={}, metrics=data))


@router.get("/renewable-mix", response_model=SuccessResponse[AnalyticsResponse])
async def get_renewable_mix(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch renewable mix.
    """
    data = await analytics_service.renewable_mix()
    return SuccessResponse(data=AnalyticsResponse(summary=data, metrics=[]))


@router.get("/fuel-mix", response_model=SuccessResponse[AnalyticsResponse])
async def get_fuel_mix(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch fuel mix.
    """
    return SuccessResponse(data=AnalyticsResponse(summary={}, metrics=[]))


@router.get("/capacity-utilization", response_model=SuccessResponse[SummaryResponse])
async def get_capacity_utilization(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    """
    Fetch capacity utilization.
    """
    data = await analytics_service.capacity_summary()
    return SuccessResponse(
        data=SummaryResponse(total=data.get("total_installed_mw", 0.0), unit="MW")
    )


@router.get("/trends", response_model=SuccessResponse[list[TrendResponse]])
async def get_trends(analytics_service: AnalyticsService = Depends(get_analytics_service)):
    """
    Fetch analytical trends.
    """
    return SuccessResponse(data=[TrendResponse(trend_type="Generation", series_data=[])])


@router.get("/top-performing-states", response_model=SuccessResponse[AnalyticsResponse])
async def get_top_performing_states(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    """
    Fetch top performing states.
    """
    data = await analytics_service.top_generating_states()
    return SuccessResponse(data=AnalyticsResponse(summary={}, metrics=data))


@router.get("/top-generating-plants", response_model=SuccessResponse[AnalyticsResponse])
async def get_top_generating_plants(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    """
    Fetch top generating plants.
    """
    return SuccessResponse(data=AnalyticsResponse(summary={}, metrics=[]))


@router.get("/operator-performance", response_model=SuccessResponse[AnalyticsResponse])
async def get_operator_performance(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    """
    Fetch operator performance.
    """
    data = await analytics_service.top_generating_companies()
    return SuccessResponse(data=AnalyticsResponse(summary={}, metrics=data))
