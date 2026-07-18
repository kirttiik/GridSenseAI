import json
import re
from typing import Any

from sqlalchemy.orm import DeclarativeBase, declared_attr

from app.db.metadata import mapper_registry


def camel_to_snake(name: str) -> str:
    """Converts CamelCase class names to snake_case table names."""
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy declarative models.
    Provides automatic __tablename__ generation, common utilities for serialization,
    and ties into the enterprise naming conventions via mapper_registry.
    """

    registry = mapper_registry

    # We enforce that all subclasses must define their own PK (UUID or Composite),
    # so we do not define `id: Any` here globally to prevent inheritance collisions
    # on tables with composite natural keys.

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Automatically generate table names by converting the class name to snake_case.
        """
        return camel_to_snake(cls.__name__)

    def to_dict(self, exclude: list[str] | None = None) -> dict[str, Any]:
        """
        Converts the SQLAlchemy model instance into a Python dictionary.
        Ignores internal SQLAlchemy state.

        Args:
            exclude: List of column names to omit (e.g. ['password_hash'])
        """
        exclude = exclude or []
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
            if column.name not in exclude
        }

    def update_from_dict(self, data: dict[str, Any]) -> None:
        """
        Dynamically updates model attributes from a dictionary.
        Only updates attributes that map to actual table columns.
        """
        for key, value in data.items():
            if hasattr(self, key) and key in self.__table__.columns.keys():
                setattr(self, key, value)

    def as_json(self, exclude: list[str] | None = None) -> str:
        """
        Serializes the model to a JSON string.
        (Note: Complex types like datetimes may need custom JSON encoding).
        """
        return json.dumps(self.to_dict(exclude=exclude), default=str)

    def __repr__(self) -> str:
        """Provides a clean string representation for debugging."""
        columns = [f"{col.name}={getattr(self, col.name)}" for col in self.__table__.columns]
        return f"<{self.__class__.__name__}({', '.join(columns)})>"
