from fastapi import APIRouter, Depends

from app.api.v1.routers import (
    dashboard,
    energy,
    grid,
    health,
    market,
    sync,
    weather,
    insights,
)

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["Health"])

api_router.include_router(
    dashboard.router, prefix="/dashboard", tags=["Dashboard"]
)
api_router.include_router(
    energy.router, prefix="/energy", tags=["Energy"]
)
api_router.include_router(
    market.router, prefix="/market", tags=["Market"]
)
api_router.include_router(
    grid.router, prefix="/grid", tags=["Grid"]
)
api_router.include_router(
    weather.router, prefix="/weather", tags=["Weather"]
)
api_router.include_router(
    insights.router, prefix="/insights", tags=["Insights"]
)
api_router.include_router(
    sync.router, prefix="/sync", tags=["Sync"]
)
