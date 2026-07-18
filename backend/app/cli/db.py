import argparse
import asyncio
import logging

from app.bootstrap.initializer import (
    initialize_database,
    rebuild_database,
    reset_migrations,
    run_migrations,
)
from app.bootstrap.seed_manager import SeedManager
from app.bootstrap.verification import verify_database

logger = logging.getLogger(__name__)


def run_cli():
    parser = argparse.ArgumentParser(description="GridSense AI Database Management CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init-db
    parser_init = subparsers.add_parser("init-db", help="Initialize the database (migrate + seed)")
    parser_init.add_argument("--env", type=str, default="development", help="Environment to use")

    # seed-db
    parser_seed = subparsers.add_parser("seed-db", help="Run database seeders")
    parser_seed.add_argument("--env", type=str, default="development", help="Environment to use")
    parser_seed.add_argument(
        "--dry-run", action="store_true", help="Run in dry-run mode (no commits)"
    )

    # verify-db
    parser_verify = subparsers.add_parser(
        "verify-db", help="Verify database structure and seed data"
    )

    # reset-db
    parser_reset = subparsers.add_parser(
        "reset-db", help="Drop all tables (Alembic downgrade base)"
    )

    # rebuild-db
    parser_rebuild = subparsers.add_parser("rebuild-db", help="Reset and then Initialize database")
    parser_rebuild.add_argument("--env", type=str, default="development", help="Environment to use")

    # migrate
    parser_migrate = subparsers.add_parser("migrate", help="Run alembic upgrade head")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    if args.command == "init-db":
        asyncio.run(initialize_database(environment=args.env))
    elif args.command == "seed-db":
        manager = SeedManager(environment=args.env)
        asyncio.run(manager.execute(dry_run=args.dry_run))
    elif args.command == "verify-db":
        asyncio.run(verify_database())
    elif args.command == "reset-db":
        reset_migrations()
    elif args.command == "rebuild-db":
        asyncio.run(rebuild_database(environment=args.env))
    elif args.command == "migrate":
        run_migrations()
