import logging
import uuid
from typing import List, Dict, Any
from datetime import datetime

from app.sdk.energy_atlas.client import BaseClient
from app.models.energy.carbon_data import CarbonIntensity
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

logger = logging.getLogger(__name__)

class CarbonIngestionService:
    """Service to ingest carbon intensity data into PostgreSQL."""
    
    def __init__(self, atlas_client, session: AsyncSession):
        self.atlas = atlas_client
        self.session = session
    
    async def run(self) -> int:
        records_processed = 0
        logger.info("Starting carbon ingestion...")
        
        try:
            resp = await self.atlas.carbon.get_intensity()
            records = self._map_carbon(resp.data)
            if records:
                # Deduplicate by ID
                records = list({r["id"]: r for r in records}.values())
                
                stmt = insert(CarbonIntensity).values(records)
                stmt = stmt.on_conflict_do_update(
                    index_elements=['id'],
                    set_={
                        'value_gco2_kwh': stmt.excluded.value_gco2_kwh
                    }
                )
                await self.session.execute(stmt)
                records_processed += len(records)
                logger.info(f"Ingested {len(records)} Carbon Intensity records.")
                
        except Exception as e:
            logger.error(f"Error during carbon ingestion: {e}")
            raise
            
        return records_processed
        
    def _generate_deterministic_id(self, timestamp: datetime, region: str) -> uuid.UUID:
        key = f"{timestamp.isoformat()}_{region}"
        return uuid.uuid5(uuid.NAMESPACE_OID, key)
        
    def _map_carbon(self, data: Any) -> List[Dict[str, Any]]:
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
            val = item.get("value_gco2_kwh") or item.get("intensity") or 0.0
            
            records.append({
                "id": self._generate_deterministic_id(dt, region),
                "timestamp": dt,
                "region": region,
                "value_gco2_kwh": float(val)
            })
            
        return records
