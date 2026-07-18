import asyncio
import os
import sys

# Ensure backend directory is in the python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.sdk.energy_atlas import EnergyAtlasClient

async def main():
    print("Instantiating EnergyAtlasClient...")
    try:
        # Pass a mock API key in env if it's missing just for this script
        os.environ["ENERGY_ATLAS_API_KEY"] = os.environ.get("ENERGY_ATLAS_API_KEY", "test-key")
        client = EnergyAtlasClient()
        print("Success! Available modules:")
        print(" - grid:", client.grid)
        print(" - demand:", client.demand)
        print(" - generation:", client.generation)
        print(" - carbon:", client.carbon)
        print(" - iex:", client.iex)
        print(" - assets:", client.assets)
        print(" - operations:", client.operations)
        await client.close()
    except Exception as e:
        print("Failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
