import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.session import AsyncSessionLocal
from app.sdk.energy_atlas import EnergyAtlasClient
from app.services.ingestion.grid_ingestion import GridIngestionService

async def main():
    async with AsyncSessionLocal() as session:
        client = EnergyAtlasClient()
        service = GridIngestionService(client, session)
        
        print("Fetching grid data...")
        await service.run()
        await session.commit()
        await client.close()
        print("Done")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
