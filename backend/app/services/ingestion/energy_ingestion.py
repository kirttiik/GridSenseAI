import logging
import uuid
from typing import List, Dict, Any
from datetime import datetime

from app.sdk.energy_atlas.client import BaseClient
from app.models.energy.energy_data import EnergyData
from app.repositories.energy_repository import EnergyRepository
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)

class EnergyIngestionService:
    """Service to ingest energy data (demand, generation) into PostgreSQL."""
    
    def __init__(self, atlas_client, session: AsyncSession):
        self.atlas = atlas_client
        self.repo = EnergyRepository(session)
    
    async def run(self) -> int:
        records_processed = 0
        logger.info("Starting energy ingestion...")
        
        try:
            # 1. Fetch Demand
            demand_resp = await self.atlas.demand.get_timeseries(limit=100)
            demand_records = self._map_demand(demand_resp.data)
            if demand_records:
                demand_records = list({r["id"]: r for r in demand_records}.values())
                await self.repo.upsert(["id"], demand_records)
                records_processed += len(demand_records)
                logger.info(f"Ingested {len(demand_records)} demand records.")
            
            # 2. Fetch Generation (Fuel Mix)
            gen_resp = await self.atlas.generation.get_generation(limit=100)
            gen_records = self._map_generation(gen_resp.data)
            if gen_records:
                gen_records = list({r["id"]: r for r in gen_records}.values())
                await self.repo.upsert(["id"], gen_records)
                records_processed += len(gen_records)
                logger.info(f"Ingested {len(gen_records)} generation records.")
                
        except Exception as e:
            logger.error(f"Error during energy ingestion: {e}")
            raise  # Let the error bubble up so test scripts can see it!
            
        return records_processed

    def _generate_deterministic_id(self, timestamp: datetime, region: str, source_type: str) -> uuid.UUID:
        key = f"{timestamp.isoformat()}_{region}_{source_type}"
        return uuid.uuid5(uuid.NAMESPACE_OID, key)
        
    def _map_demand(self, data: Any) -> List[Dict[str, Any]]:
        records = []
        if not data or not isinstance(data, list):
            return records
            
        for item in data:
            if not isinstance(item, dict):
                continue
                
            region = item.get("state", "INDIA")
            points = item.get("points", [])
            
            for pt in points:
                timestamp_str = pt.get("timestamp")
                if not timestamp_str:
                    continue
                    
                try:
                    dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
                except ValueError:
                    continue
                    
                demand_val = pt.get("demand_mw") or pt.get("value") or 0.0
                
                records.append({
                    "id": self._generate_deterministic_id(dt, region, "Demand"),
                    "timestamp": dt,
                    "region": region,
                    "source_type": "Demand",
                    "value_mw": float(demand_val)
                })
                
        return records
        
    def _map_generation(self, data: Any) -> List[Dict[str, Any]]:
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
            
            # The API returns a flat list where each record has a fuel_type
            fuel_type = item.get("fuel_type")
            
            if fuel_type:
                fuel_name = str(fuel_type).capitalize()
                gen_val = item.get("generation_mw") or item.get("value") or 0.0
                records.append({
                    "id": self._generate_deterministic_id(dt, region, fuel_name),
                    "timestamp": dt,
                    "region": region,
                    "source_type": fuel_name,
                    "value_mw": float(gen_val)
                })
            else:
                fuel_mix = item.get("fuel_mix", {})
                if isinstance(fuel_mix, dict) and fuel_mix:
                    for fuel, val in fuel_mix.items():
                        fuel_name = str(fuel).capitalize()
                        records.append({
                            "id": self._generate_deterministic_id(dt, region, fuel_name),
                            "timestamp": dt,
                            "region": region,
                            "source_type": fuel_name,
                            "value_mw": float(val)
                        })
                else:
                    gen_val = item.get("generation_mw") or item.get("value") or 0.0
                    records.append({
                        "id": self._generate_deterministic_id(dt, region, "Generation (Total)"),
                        "timestamp": dt,
                        "region": region,
                        "source_type": "Generation (Total)",
                        "value_mw": float(gen_val)
                    })
                
        return records

