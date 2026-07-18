import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Add backend to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.session import AsyncSessionLocal
from app.services.ingestion.sync_manager import SyncManager

logging.basicConfig(level=logging.INFO)

async def test_sync():
    print("Testing sync manager...")
    async with AsyncSessionLocal() as session:
        manager = SyncManager(session)
        result = await manager.run_sync()
        await session.commit()
        print("Sync result:")
        print(result)

if __name__ == "__main__":
    asyncio.run(test_sync())
