import abc
import logging
from typing import Any

from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


class BaseTransformer(abc.ABC):
    """
    Abstract base class for transforming Validated datasets.
    Handles lookups, FK resolutions, and unit normalization.
    """

    @abc.abstractmethod
    async def transform(
        self, uow: UnitOfWork, valid_records: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Takes validated records and returns the final mapped records ready for the Loader.
        Requires UnitOfWork to fetch reference data if needed.
        """
        pass
