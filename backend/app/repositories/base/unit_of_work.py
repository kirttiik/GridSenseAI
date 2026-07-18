from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

# The domain repositories will be imported locally in __init__ to prevent circular imports.
from .exceptions import TransactionError
from .exceptions import TransactionError


class UnitOfWork:
    """
    Context manager for database transactions and repository aggregation.
    Ensures that all operations within the context block are committed atomically,
    or rolled back if an exception occurs.
    """

    def __init__(self, session: AsyncSession):
        self._session = session

        from ..assets_repository import AssetsRepository
        from ..energy_repository import EnergyRepository
        from ..grid_repository import GridRepository
        from ..ingestion_repository import IngestionRepository
        from ..market_repository import MarketRepository
        from ..ml_repository import MlRepository
        from ..operations_repository import OperationsRepository
        from ..reference_repository import ReferenceRepository

        # Initialize Repositories
        self.reference = ReferenceRepository(self._session)
        self.assets = AssetsRepository(self._session)
        self.energy = EnergyRepository(self._session)
        self.grid = GridRepository(self._session)
        self.market = MarketRepository(self._session)
        self.operations = OperationsRepository(self._session)
        self.ingestion = IngestionRepository(self._session)
        self.ml = MlRepository(self._session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            await self.rollback()
            raise TransactionError(f"Transaction failed: {exc_val}")

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()


async def get_uow(session: AsyncSession = Depends(get_db)) -> AsyncGenerator[UnitOfWork, None]:
    """
    FastAPI dependency for injecting the Unit of Work.
    """
    async with UnitOfWork(session) as uow:
        yield uow
