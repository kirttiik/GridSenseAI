import logging
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

class WeatherIngestionService:
    """No-op service since weather data does not exist in Energy Atlas."""
    
    def __init__(self, atlas_client, session: AsyncSession):
        self.atlas = atlas_client
        self.session = session
    
    async def run(self) -> int:
        logger.info("Skipping weather ingestion (no Weather API in Energy Atlas).")
        return 0
