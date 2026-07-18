import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.sdk.energy_atlas import EnergyAtlasClient

async def main():
    client = EnergyAtlasClient()
    try:
        print("\nTesting iex.get_dam()...")
        dam = await client.iex.get_dam()
        print(f"DAM: {len(dam.data) if isinstance(dam.data, list) else dam.data}")
        if isinstance(dam.data, list) and dam.data:
            print(f"DAM Sample: {dam.data[0]}")
            
        print("\nTesting weather (no SDK endpoint, how did weather work?)...")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(main())
