import time
from fastapi import APIRouter
from sqlalchemy import text

from app.core.settings import settings
from app.db.session import AsyncSessionLocal
from app.schemas.responses import HealthResponse
from app.services.ingestion.sync_manager import LAST_SYNC_TIME
import httpx

router = APIRouter()

@router.get("", response_model=HealthResponse)
async def health_check():
    """Basic health check that the application is running."""
    return HealthResponse(
        status="ok",
        environment=settings.ENVIRONMENT.value,
        version=settings.VERSION,
        database="unknown",
        energy_atlas_api="unknown",
        last_sync_time=LAST_SYNC_TIME,
        uptime_seconds=time.time() - settings.START_TIME,
    )

@router.get("/live", response_model=HealthResponse)
async def liveness_probe():
    """Liveness probe for Kubernetes."""
    return HealthResponse(
        status="ok",
        environment=settings.ENVIRONMENT.value,
        version=settings.VERSION,
        database="unknown",
        energy_atlas_api="unknown",
        last_sync_time=LAST_SYNC_TIME,
        uptime_seconds=time.time() - settings.START_TIME,
    )

@router.get("/ready", response_model=HealthResponse)
async def readiness_probe():
    """Readiness probe that checks backing services (e.g. Database and API)."""
    db_status = "ok"
    api_status = "ok"
    status = "ok"
    
    counts = {
        "energy_data": 0,
        "weather_data": 0,
        "grid_status": 0,
        "market_data": 0,
        "ai_insight": 0
    }
    
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
            
            # Fetch table counts
            for table in counts.keys():
                try:
                    res = await session.execute(text(f"SELECT COUNT(1) FROM {table}"))
                    counts[table] = res.scalar() or 0
                except Exception:
                    pass
    except Exception:
        db_status = "error"
        status = "error"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            # simple ping to a known fast endpoint or base URL
            res = await client.get(f"{settings.ENERGY_ATLAS_BASE_URL}/health")
            if res.status_code >= 500:
                api_status = "error"
    except Exception:
        api_status = "error"
        # We don't necessarily fail readiness if Energy Atlas is down, 
        # but we reflect it in the API status.

    return HealthResponse(
        status=status,
        environment=settings.ENVIRONMENT.value,
        version=settings.VERSION,
        database=db_status,
        energy_atlas_api=api_status,
        last_sync_time=LAST_SYNC_TIME,
        uptime_seconds=time.time() - settings.START_TIME,
        energy_records=counts["energy_data"],
        weather_records=counts["weather_data"],
        grid_records=counts["grid_status"],
        market_records=counts["market_data"],
        ai_insight_records=counts["ai_insight"],
    )
