import logging
import uuid
from typing import List, Dict, Any
from datetime import datetime

from app.sdk.energy_atlas.client import BaseClient
from app.models.market.market_data import MarketData
from app.repositories.market_repository import MarketRepository
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

class MarketIngestionService:
    """Service to ingest market data (DAM, RTM) into PostgreSQL."""
    
    def __init__(self, atlas_client, session: AsyncSession):
        self.atlas = atlas_client
        self.repo = MarketRepository(session)
    
    async def run(self) -> int:
        records_processed = 0
        logger.info("Starting market ingestion...")
        
        try:
            # 1. Fetch DAM
            dam_resp = await self.atlas.iex.get_dam(limit=100)
            dam_records = self._map_market(dam_resp.data, "DAM")
            if dam_records:
                dam_records = list({r["id"]: r for r in dam_records}.values())
                await self.repo.upsert(["id"], dam_records)
                records_processed += len(dam_records)
                logger.info(f"Ingested {len(dam_records)} DAM records.")
            
            # 2. Fetch RTM
            rtm_resp = await self.atlas.iex.get_rtm(limit=100)
            rtm_records = self._map_market(rtm_resp.data, "RTM")
            if rtm_records:
                rtm_records = list({r["id"]: r for r in rtm_records}.values())
                await self.repo.upsert(["id"], rtm_records)
                records_processed += len(rtm_records)
                logger.info(f"Ingested {len(rtm_records)} RTM records.")
                
        except Exception as e:
            logger.error(f"Error during market ingestion: {e}")
            raise
            
        return records_processed
        
    def _generate_deterministic_id(self, timestamp: datetime, region: str, market_type: str) -> uuid.UUID:
        key = f"{timestamp.isoformat()}_{region}_{market_type}"
        return uuid.uuid5(uuid.NAMESPACE_OID, key)
        
    def _map_market(self, data: Any, market_type: str) -> List[Dict[str, Any]]:
        records = []
        if not data or not isinstance(data, list):
            return records
            
        for item in data:
            if not isinstance(item, dict):
                continue
            
            timestamp_str = item.get("timestamp")
            if not timestamp_str:
                continue
                
            try:
                dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
            except ValueError:
                continue
                
            region = item.get("region", "INDIA")
            price = item.get("price_inr") or item.get("price") or item.get("mcp_rs_mwh") or 0.0
            volume = item.get("volume_mwh") or item.get("volume") or item.get("mcv_mw") or None
            
            records.append({
                "id": self._generate_deterministic_id(dt, region, market_type),
                "timestamp": dt,
                "region": region,
                "market_type": market_type,
                "price_inr": float(price),
                "volume_mwh": float(volume) if volume is not None else None
            })
            
        return records
