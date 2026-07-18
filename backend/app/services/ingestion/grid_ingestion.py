import logging
import uuid
from typing import List, Dict, Any
from datetime import datetime

from app.sdk.energy_atlas.client import BaseClient
from app.models.grid.grid_status import GridStatus
from app.repositories.grid_repository import GridRepository
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

class GridIngestionService:
    """Service to ingest grid status (frequency) into PostgreSQL."""
    
    def __init__(self, atlas_client, session: AsyncSession):
        self.atlas = atlas_client
        self.repo = GridRepository(session)
    
    async def run(self) -> int:
        records_processed = 0
        logger.info("Starting grid ingestion...")
        
        try:
            # 1. Fetch grid frequency
            grid_resp = await self.atlas.grid.get_frequency(limit=100)
            grid_records = self._map_grid(grid_resp.data)
            
            if grid_records:
                grid_records = list({r["id"]: r for r in grid_records}.values())
                await self.repo.upsert(["id"], grid_records)
                records_processed += len(grid_records)
                logger.info(f"Ingested {len(grid_records)} grid frequency records.")
                
        except Exception as e:
            logger.error(f"Error during grid ingestion: {e}")
            raise
            
        return records_processed
        
    def _generate_deterministic_id(self, timestamp: datetime, region: str) -> uuid.UUID:
        key = f"{timestamp.isoformat()}_{region}"
        return uuid.uuid5(uuid.NAMESPACE_OID, key)
        
    def _map_grid(self, data: Any) -> List[Dict[str, Any]]:
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
            freq = item.get("frequency_hz") or item.get("frequency") or 50.0
            stability = item.get("stability_index") or 1.0
            voltage = item.get("voltage_kv") or None
            
            records.append({
                "id": self._generate_deterministic_id(dt, region),
                "timestamp": dt,
                "region": region,
                "frequency_hz": float(freq),
                "stability_index": float(stability),
                "voltage_kv": float(voltage) if voltage is not None else None
            })
            
        return records
