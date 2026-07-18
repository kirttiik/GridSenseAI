import os


class SDKConfig:
    """Configuration for the Energy Atlas SDK."""

    @property
    def api_key(self) -> str:
        key = os.getenv("ENERGY_ATLAS_API_KEY")
        if not key:
            raise ValueError("ENERGY_ATLAS_API_KEY environment variable is missing.")
        return key

    @property
    def base_url(self) -> str:
        return os.getenv("ENERGY_ATLAS_BASE_URL", "https://api.energymap.in")

    @property
    def timeout(self) -> float:
        return float(os.getenv("EA_TIMEOUT", "30.0"))

    @property
    def connect_timeout(self) -> float:
        return float(os.getenv("EA_CONNECT_TIMEOUT", "10.0"))

    @property
    def read_timeout(self) -> float:
        return float(os.getenv("EA_READ_TIMEOUT", "30.0"))

    @property
    def max_retries(self) -> int:
        return int(os.getenv("EA_MAX_RETRIES", "3"))

    @property
    def backoff_factor(self) -> float:
        return float(os.getenv("EA_BACKOFF_FACTOR", "2.0"))

    @property
    def max_backoff(self) -> float:
        return float(os.getenv("EA_MAX_BACKOFF", "60.0"))


config = SDKConfig()
