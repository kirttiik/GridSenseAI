import asyncio
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.session import AsyncSessionLocal
from app.services.ingestion.sync_manager import SyncManager

async def main():
    try:
        async with AsyncSessionLocal() as session:
            manager = SyncManager(session)
            print("Running SyncManager...")
            result = await manager.run_sync()
            await session.commit()
            print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
