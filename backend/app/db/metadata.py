from sqlalchemy.orm import registry

from app.db.naming import metadata

# Create a central SQLAlchemy registry mapping to our custom metadata.
# This registry manages all ORM mappers and is used by the DeclarativeBase.
mapper_registry = registry(metadata=metadata)
