import time

from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.settings import settings
from app.logging.logger import logger

# Create the async engine with robust connection pooling tailored for PostgreSQL
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=settings.DEBUG,  # Print SQL statements in debug mode
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=10,  # Number of persistent connections
    max_overflow=20,  # Allow temporary burst connections
    pool_timeout=30,  # Seconds to wait before giving up on getting a connection
    pool_recycle=1800,  # Recycle connections after 30 minutes to prevent stale drops
)


@event.listens_for(engine.sync_engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    context._query_start_time = time.time()


@event.listens_for(engine.sync_engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total_time = (time.time() - context._query_start_time) * 1000
    if total_time > 100:  # Log slow queries (> 100ms)
        logger.warning(f"Slow Query Detected: {total_time:.2f}ms - {statement}")
    else:
        logger.debug(f"Query Executed: {total_time:.2f}ms - {statement}")
