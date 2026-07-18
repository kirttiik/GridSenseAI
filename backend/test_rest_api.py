import os
import sys
import asyncio

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from httpx import AsyncClient, ASGITransport
from app.main import app

async def main():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        print("Testing /api/v1/energy/current")
        r_energy = await client.get("/api/v1/energy/current")
        print("Status:", r_energy.status_code)
        print("Data count:", len(r_energy.json().get("data", [])) if r_energy.status_code == 200 else 0)
        
        print("\nTesting /api/v1/grid/current")
        r_grid = await client.get("/api/v1/grid/current")
        print("Status:", r_grid.status_code)
        print("Data count:", len(r_grid.json().get("data", [])) if r_grid.status_code == 200 else 0)
        
        print("\nTesting /api/v1/market/current")
        r_market = await client.get("/api/v1/market/current")
        print("Status:", r_market.status_code)
        print("Data count:", len(r_market.json().get("data", [])) if r_market.status_code == 200 else 0)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
