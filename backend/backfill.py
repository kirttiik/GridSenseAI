import asyncio
import logging
import time
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal
from app.sdk.energy_atlas import EnergyAtlasClient
from app.services.ingestion.energy_ingestion import EnergyIngestionService
from app.services.ingestion.grid_ingestion import GridIngestionService
from app.services.ingestion.market_ingestion import MarketIngestionService
from app.services.ingestion.carbon_ingestion import CarbonIngestionService

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def backfill():
    atlas = EnergyAtlasClient()
    
    async with AsyncSessionLocal() as session:
        # We need to temporarily patch the run methods to fetch more data
        # Energy
        energy_svc = EnergyIngestionService(atlas, session)
        demand_resp = await atlas.demand.get_timeseries(limit=5000)
        demand_records = energy_svc._map_demand(demand_resp.data)
        if demand_records:
            demand_records = list({r["id"]: r for r in demand_records}.values())
            await energy_svc.repo.upsert(["id"], demand_records)
            logger.info(f"Ingested {len(demand_records)} demand records.")
            
        gen_resp = await atlas.generation.get_generation(limit=5000)
        gen_records = energy_svc._map_generation(gen_resp.data)
        if gen_records:
            gen_records = list({r["id"]: r for r in gen_records}.values())
            await energy_svc.repo.upsert(["id"], gen_records)
            logger.info(f"Ingested {len(gen_records)} generation records.")

        # Grid
        grid_svc = GridIngestionService(atlas, session)
        freq_resp = await atlas.grid.get_frequency(limit=5000)
        freq_records = grid_svc._map_grid(freq_resp.data)
        if freq_records:
            freq_records = list({r["id"]: r for r in freq_records}.values())
            await grid_svc.repo.upsert(["id"], freq_records)
            logger.info(f"Ingested {len(freq_records)} grid frequency records.")

        # Market
        market_svc = MarketIngestionService(atlas, session)
        dam_resp = await atlas.iex.get_dam(limit=5000)
        dam_records = market_svc._map_market(dam_resp.data, "DAM")
        if dam_records:
            dam_records = list({r["id"]: r for r in dam_records}.values())
            await market_svc.repo.upsert(["id"], dam_records)
            logger.info(f"Ingested {len(dam_records)} DAM records.")
            
        rtm_resp = await atlas.iex.get_rtm(limit=5000)
        rtm_records = market_svc._map_market(rtm_resp.data, "RTM")
        if rtm_records:
            rtm_records = list({r["id"]: r for r in rtm_records}.values())
            await market_svc.repo.upsert(["id"], rtm_records)
            logger.info(f"Ingested {len(rtm_records)} RTM records.")
            
        # Carbon
        carbon_svc = CarbonIngestionService(atlas, session)
        carbon_resp = await atlas.carbon.get_carbon_intensity(limit=5000)
        carbon_records = carbon_svc._map_carbon(carbon_resp.data)
        if carbon_records:
            carbon_records = list({r["id"]: r for r in carbon_records}.values())
            from sqlalchemy.dialects.postgresql import insert
            from app.models.energy.carbon_data import CarbonIntensity
            stmt = insert(CarbonIntensity).values(carbon_records)
            stmt = stmt.on_conflict_do_update(
                index_elements=['id'],
                set_={
                    'value_gco2_kwh': stmt.excluded.value_gco2_kwh
                }
            )
            await session.execute(stmt)
            await session.commit()
            logger.info(f"Ingested {len(carbon_records)} Carbon records.")

    await atlas.close()

if __name__ == "__main__":
    asyncio.run(backfill())
