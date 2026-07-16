from fastapi import APIRouter, status

from app.core.constants import API_V1_PREFIX, HEALTHY_STATUS, ROOT_MESSAGE, SERVICE_NAME
from app.core.config import get_settings

router = APIRouter(prefix=API_V1_PREFIX)


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health check",
    tags=["system"],
)
async def health_check() -> dict[str, str]:
    settings = get_settings()
    return {
        "status": HEALTHY_STATUS,
        "service": SERVICE_NAME,
        "version": settings.app_version,
    }


root_router = APIRouter()


@root_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Root endpoint",
    tags=["system"],
)
async def read_root() -> dict[str, str]:
    return {"message": ROOT_MESSAGE}
