#!/usr/bin/env python
"""
GridSense AI Management CLI.
Entrypoint for database operations, seeding, and initialization.
"""
import sys
import os

# Add the project root to the python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.cli.db import run_cli

if __name__ == "__main__":
    run_cli()
