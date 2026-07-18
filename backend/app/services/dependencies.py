from fastapi import Depends

from app.repositories.base.unit_of_work import UnitOfWork, get_uow

from .analytics_service import AnalyticsService
from .assets_service import AssetsService
from .energy_service import EnergyService
from .forecast_service import ForecastService
from .grid_service import GridService
from .ingestion_service import IngestionService
from .market_service import MarketService
from .operations_service import OperationsService

# These imports will work once the domain services are created
from .reference_service import ReferenceService


def get_reference_service(uow: UnitOfWork = Depends(get_uow)) -> ReferenceService:
    return ReferenceService(uow)


def get_assets_service(uow: UnitOfWork = Depends(get_uow)) -> AssetsService:
    return AssetsService(uow)


def get_energy_service(uow: UnitOfWork = Depends(get_uow)) -> EnergyService:
    return EnergyService(uow)


def get_grid_service(uow: UnitOfWork = Depends(get_uow)) -> GridService:
    return GridService(uow)


def get_market_service(uow: UnitOfWork = Depends(get_uow)) -> MarketService:
    return MarketService(uow)


def get_operations_service(uow: UnitOfWork = Depends(get_uow)) -> OperationsService:
    return OperationsService(uow)


def get_ingestion_service(uow: UnitOfWork = Depends(get_uow)) -> IngestionService:
    return IngestionService(uow)


def get_forecast_service(uow: UnitOfWork = Depends(get_uow)) -> ForecastService:
    return ForecastService(uow)


def get_analytics_service(uow: UnitOfWork = Depends(get_uow)) -> AnalyticsService:
    return AnalyticsService(uow)
