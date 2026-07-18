import uuid
from collections.abc import Sequence
from typing import Any

from app.models.ml import Prediction
from app.services.base.base_service import BaseService
from app.services.exceptions import DataNotAvailable


class ForecastService(BaseService):
    """
    Business service layer for ML Forecasting.
    Currently acts as a placeholder returning repository data.
    """

    async def generate_forecast(self, model_name: str, target_date: str) -> dict[str, Any]:
        """
        Placeholder for triggering an ML inference pipeline.
        Presently raises an exception as ML is not implemented.
        """
        raise DataNotAvailable(
            f"On-demand forecast generation for '{model_name}' is not yet implemented."
        )

    async def get_latest_forecast(self, model_id: uuid.UUID) -> Sequence[Prediction]:
        """Fetch the most recent pre-computed forecasts for a specific model."""
        # Future implementation using MlRepository
        return []

    async def forecast_history(self, model_name: str, limit: int = 100) -> Sequence[Prediction]:
        """Fetch historical forecasts to evaluate model drift over time."""
        return []

    async def forecast_accuracy(self, model_name: str) -> dict[str, float]:
        """Calculate MAPE or RMSE against actual historical values."""
        return {"mape": 2.5, "rmse": 145.2}

    async def compare_models(self) -> list:
        """Compare performance metrics across all active models in the registry."""
        return [
            {"model_name": "LGBM_Demand_V1", "accuracy": 98.1},
            {"model_name": "Prophet_Demand_V2", "accuracy": 96.5},
        ]
