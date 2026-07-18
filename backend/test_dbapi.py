import asyncio
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.session import AsyncSessionLocal
from app.sdk.energy_atlas import EnergyAtlasClient
from app.services.ingestion.energy_ingestion import EnergyIngestionService
from sqlalchemy.exc import DBAPIError

async def main():
    try:
        async with AsyncSessionLocal() as session:
            client = EnergyAtlasClient()
            service = EnergyIngestionService(client, session)
            await service.run()
            await session.commit()
            await client.close()
    except DBAPIError as e:
        print("DBAPI ERROR ORIG:", repr(e.orig))
        print("DBAPI ERROR STATEMENT:", e.statement)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
