import httpx
import asyncio
from datetime import datetime

async def test():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.energymap.in/developer/v1/market/iex/latest?market_type=DAM&limit=100", headers={"X-API-Key": "iea_live_QVopDNVE9M9LMpVZC0aTSBDtcLeG3a2-"})
        data = r.json().get("data", [])
        print("Raw data count:", len(data))
        if data:
            item = data[0]
            print("First item:", item)
            price = item.get("price_inr") or item.get("price") or item.get("mcp_rs_mwh") or 0.0
            volume = item.get("volume_mwh") or item.get("volume") or item.get("mcv_mw") or None
            print(f"Mapped price: {price}")
            print(f"Mapped volume: {volume}")

asyncio.run(test())
