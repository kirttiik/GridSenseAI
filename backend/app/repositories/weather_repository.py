from sqlalchemy.ext.asyncio import AsyncSession

from app.models.operations.weather_data import WeatherData
from .base.generic_repository import GenericRepository


class WeatherRepository(GenericRepository[WeatherData]):
    """Repository for MVP WeatherData model."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, WeatherData)
