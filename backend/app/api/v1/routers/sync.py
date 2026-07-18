import logging
from typing import Dict, Any
from fastapi import APIRouter, Depends

from app.db.session import AsyncSessionLocal
from app.services.ingestion.sync_manager import SyncManager

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("", response_model=Dict[str, Any])
async def trigger_sync():
    """
    Manually triggers the ingestion pipeline to fetch from Energy Atlas
    and synchronize to the PostgreSQL database.
    """
    try:
        async with AsyncSessionLocal() as session:
            manager = SyncManager(session)
            result = await manager.run_sync()
            await session.commit()
            return result
    except Exception as e:
        logger.error(f"Failed to execute manual sync: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
