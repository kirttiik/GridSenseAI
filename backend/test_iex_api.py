import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.sdk.energy_atlas import EnergyAtlasClient

async def main():
    client = EnergyAtlasClient()
    try:
        resp = await client.iex.get_dam(limit=5)
        print("Response data:", resp.data)
        print("Response meta:", resp.meta)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
