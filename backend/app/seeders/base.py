import abc
import logging

from app.repositories.base.unit_of_work import UnitOfWork

logger = logging.getLogger(__name__)


class BaseSeeder(abc.ABC):
    """
    Abstract Base Class for all seeders.
    """

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Name of the seeder."""
        pass

    @property
    @abc.abstractmethod
    def priority(self) -> int:
        """
        Execution priority. Lower number = earlier execution.
        0-9: Core Reference Enums
        10-19: Geography & Time
        20-29: Companies & Source Systems
        30-39: Ingestion & Metadata
        40-49: Sample Assets
        50-59: Sample Energy Data
        """
        pass

    @property
    def environments(self) -> list[str]:
        """
        Environments where this seeder should run.
        Defaults to all environments.
        """
        return ["development", "testing", "staging", "production"]

    @abc.abstractmethod
    async def execute(self, uow: UnitOfWork) -> None:
        """
        Execute the seed logic.
        Must be implemented by all seeders.
        """
        pass
