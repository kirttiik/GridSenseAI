import asyncio
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.db.session import AsyncSessionLocal
from sqlalchemy import text

async def check_db():
    async with AsyncSessionLocal() as session:
        res = await session.execute(text("SELECT count(*) FROM grid_status"))
        print(f"Grid status count: {res.scalar()}")

if __name__ == "__main__":
    asyncio.run(check_db())
