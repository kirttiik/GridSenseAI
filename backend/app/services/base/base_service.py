import logging

from app.repositories.base.unit_of_work import UnitOfWork
from app.services.exceptions import ResourceNotFound

logger = logging.getLogger(__name__)


class BaseService:
    """
    Abstract BaseService for all domain services.
    Encapsulates the UnitOfWork and provides shared orchestration functionality.
    """

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_or_404(self, repository, id: str):
        """Helper to fetch from a generic repository or raise a Service exception."""
        entity = await repository.get_by_id(id)
        if not entity:
            raise ResourceNotFound(f"Resource with ID {id} not found.")
        return entity
