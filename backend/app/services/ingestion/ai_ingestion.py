import logging
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

class AiIngestionService:
    """No-op service since AI Insight data does not exist in Energy Atlas natively."""
    
    def __init__(self, atlas_client, session: AsyncSession):
        self.atlas = atlas_client
        self.session = session
    
    async def run(self) -> int:
        logger.info("Skipping AI insight ingestion (No AI endpoint in Energy Atlas).")
        return 0
