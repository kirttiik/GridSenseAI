from collections.abc import Sequence
from typing import Any, Generic, TypeVar

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Base

from .exceptions import EntityNotFound

ModelType = TypeVar("ModelType", bound=Base)


class GenericRepository(Generic[ModelType]):
    """
    Generic repository providing standard CRUD and bulk operations
    using SQLAlchemy 2.0 syntax. Strongly typed.
    """

    def __init__(self, session: AsyncSession, model_class: type[ModelType]):
        self._session = session
        self.model_class = model_class

    async def get_by_id(self, id: Any) -> ModelType | None:
        return await self._session.get(self.model_class, id)

    async def get_by_id_or_fail(self, id: Any) -> ModelType:
        entity = await self.get_by_id(id)
        if not entity:
            raise EntityNotFound(f"{self.model_class.__name__} with ID {id} not found.")
        return entity

    async def get_all(self, skip: int = 0, limit: int = 100) -> Sequence[ModelType]:
        stmt = select(self.model_class).offset(skip).limit(limit)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def create(self, entity: ModelType) -> ModelType:
        self._session.add(entity)
        await self._session.flush()
        return entity

    async def bulk_create(self, entities: list[ModelType]) -> None:
        self._session.add_all(entities)
        await self._session.flush()

    async def update(self, entity: ModelType) -> ModelType:
        # Implicitly updated if attached to session
        await self._session.flush()
        return entity

    async def delete(self, entity: ModelType) -> None:
        await self._session.delete(entity)
        await self._session.flush()

    async def count(self) -> int:
        stmt = select(func.count()).select_from(self.model_class)
        result = await self._session.execute(stmt)
        return result.scalar_one()

    async def upsert(self, index_elements: list[str], values: list[dict[str, Any]]) -> None:
        """
        Perform a bulk PostgreSQL UPSERT (ON CONFLICT DO UPDATE).
        Requires PostgreSQL dialects.
        """
        if not values:
            return

        # Batch the values to avoid 'too many SQL variables' error
        batch_size = 500
        for i in range(0, len(values), batch_size):
            batch = values[i:i + batch_size]
            stmt = insert(self.model_class).values(batch)

            # Build dictionary for update (excluding the unique constraints)
            update_dict = {c.name: c for c in stmt.excluded if c.name not in index_elements}

            stmt = stmt.on_conflict_do_update(index_elements=index_elements, set_=update_dict)

            await self._session.execute(stmt)
            
        await self._session.flush()
