import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

ENERGY_ATLAS_API_KEY = os.getenv("ENERGY_ATLAS_API_KEY")
ENERGY_ATLAS_BASE_URL = os.getenv("ENERGY_ATLAS_BASE_URL", "https://api.energymap.in")
ENERGY_ATLAS_TIMEOUT = int(os.getenv("ENERGY_ATLAS_TIMEOUT", 30))
