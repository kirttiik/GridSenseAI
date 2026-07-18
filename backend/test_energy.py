import asyncio
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.session import AsyncSessionLocal
from app.sdk.energy_atlas import EnergyAtlasClient
from app.services.ingestion.energy_ingestion import EnergyIngestionService

async def main():
    try:
        async with AsyncSessionLocal() as session:
            client = EnergyAtlasClient()
            service = EnergyIngestionService(client, session)
            
            print("Fetching energy data...")
            await service.run()
            await session.commit()
            await client.close()
            print("Done")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
