class RepositoryError(Exception):
    """Base exception for all repository-related errors."""

    pass


class EntityNotFound(RepositoryError):
    """Raised when an entity is not found in the database."""

    pass


class DuplicateEntity(RepositoryError):
    """Raised when attempting to create an entity that already exists."""

    pass


class OptimisticLockError(RepositoryError):
    """Raised when an optimistic concurrency check fails."""

    pass


class TransactionError(RepositoryError):
    """Raised when a unit of work transaction fails."""

    pass


class QueryError(RepositoryError):
    """Raised when a complex query fails to execute."""

    pass


class IntegrityError(RepositoryError):
    """Raised when a database integrity constraint is violated."""

    pass
