import abc
import logging
from typing import Any

from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


class BaseLoader(abc.ABC):
    """
    Abstract base class for Loading transformed data into the database.
    """

    @property
    @abc.abstractmethod
    def index_elements(self) -> list[str]:
        """
        List of column names used as unique keys for UPSERT.
        """
        pass

    @abc.abstractmethod
    async def load(self, uow: UnitOfWork, records: list[dict[str, Any]]) -> int:
        """
        Loads the records using the appropriate repository.
        Returns the number of rows successfully inserted/updated.
        """
        pass
