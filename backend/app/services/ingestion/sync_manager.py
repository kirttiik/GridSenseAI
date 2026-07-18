import logging
import time
from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.sdk.energy_atlas import EnergyAtlasClient
from app.services.ingestion.energy_ingestion import EnergyIngestionService
from app.services.ingestion.grid_ingestion import GridIngestionService
from app.services.ingestion.market_ingestion import MarketIngestionService
from app.services.ingestion.weather_ingestion import WeatherIngestionService
from app.services.ingestion.ai_ingestion import AiIngestionService

logger = logging.getLogger(__name__)

# Module-level variable to store last sync time in-memory
LAST_SYNC_TIME = None

class SyncManager:
    """Orchestrates the data ingestion across all domains."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def run_sync(self) -> Dict[str, Any]:
        global LAST_SYNC_TIME
        
        start_time = time.time()
        logger.info("Initiating manual synchronization...")
        
        result = {
            "status": "success",
            "energy_records": 0,
            "weather_records": 0,
            "grid_records": 0,
            "market_records": 0,
            "errors": []
        }
        
        try:
            atlas = EnergyAtlasClient()
            # 1. Energy
            try:
                energy_svc = EnergyIngestionService(atlas, self.session)
                result["energy_records"] = await energy_svc.run()
            except Exception as e:
                logger.error(f"Energy sync failed: {e}")
                result["errors"].append(f"Energy sync failed: {str(e)}")
            
            # 2. Grid
            try:
                grid_svc = GridIngestionService(atlas, self.session)
                result["grid_records"] = await grid_svc.run()
            except Exception as e:
                logger.error(f"Grid sync failed: {e}")
                result["errors"].append(f"Grid sync failed: {str(e)}")
                
            # 3. Market
            try:
                market_svc = MarketIngestionService(atlas, self.session)
                result["market_records"] = await market_svc.run()
            except Exception as e:
                logger.error(f"Market sync failed: {e}")
                result["errors"].append(f"Market sync failed: {str(e)}")
                
            # 4. Weather (no-op)
            try:
                weather_svc = WeatherIngestionService(atlas, self.session)
                result["weather_records"] = await weather_svc.run()
            except Exception as e:
                logger.error(f"Weather sync failed: {e}")
                
            # 5. AI Insight (no-op)
            try:
                ai_svc = AiIngestionService(atlas, self.session)
                await ai_svc.run()
            except Exception as e:
                logger.error(f"AI sync failed: {e}")
                
            await atlas.close()
            
        except Exception as e:
            logger.error(f"Global sync failure: {e}")
            result["status"] = "error"
            result["errors"].append(str(e))
        
        end_time = time.time()
        logger.info(f"Synchronization complete in {end_time - start_time:.2f} seconds.")
        
        if not result["errors"]:
            LAST_SYNC_TIME = end_time
            
        return result
