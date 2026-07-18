import asyncio
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.session import AsyncSessionLocal
from app.sdk.energy_atlas import EnergyAtlasClient
from app.services.ingestion.market_ingestion import MarketIngestionService

async def main():
    try:
        async with AsyncSessionLocal() as session:
            client = EnergyAtlasClient()
            service = MarketIngestionService(client, session)
            print("Fetching market data...")
            result = await service.run()
            await session.commit()
            await client.close()
            print(f"Records ingested: {result}")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
