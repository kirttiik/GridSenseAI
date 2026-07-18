import enum


class JobStatus(str, enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class RefreshType(str, enum.Enum):
    STATIC = "STATIC"
    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"


class MarketType(str, enum.Enum):
    DAM = "DAM"
    RTM = "RTM"
    GDAM = "GDAM"


class FuelCategory(str, enum.Enum):
    THERMAL = "THERMAL"
    RENEWABLE = "RENEWABLE"
    HYDRO = "HYDRO"
    NUCLEAR = "NUCLEAR"
    OTHER = "OTHER"


class PlantStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    DECOMMISSIONED = "DECOMMISSIONED"
    MAINTENANCE = "MAINTENANCE"
    PLANNED = "PLANNED"


class OwnershipType(str, enum.Enum):
    CENTRAL = "CENTRAL"
    STATE = "STATE"
    PRIVATE = "PRIVATE"


class SourceSystem(str, enum.Enum):
    ENERGY_ATLAS = "EnergyAtlas"
    GRID_INDIA = "GridIndia"
    CEA = "CEA"
    POSOCO = "POSOCO"
    MANUAL = "Manual"
    FORECAST = "Forecast"
