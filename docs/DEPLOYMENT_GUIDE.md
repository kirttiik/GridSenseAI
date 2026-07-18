# Deployment Guide

GridSense AI is designed to be easily deployable using Docker or native Python environments.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ENVIRONMENT` | Deployment environment (`development`, `staging`, `production`) | `development` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+asyncpg://postgres:postgres@localhost:5432/gridsense` |
| `SECRET_KEY` | Secret used for signing JWT tokens | (Must provide in production) |
| `ALGORITHM` | JWT Algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry | `1440` |
| `ALLOWED_API_KEYS` | Comma separated list of active API keys | |
| `LOG_LEVEL` | Application logging level | `INFO` |

## Pre-Requisites

1. PostgreSQL database running.
2. Python 3.10+ (if deploying natively).

## Startup Procedure

### 1. Database Migrations
Always ensure the database schema is up-to-date before booting the application.
```bash
alembic upgrade head
```

### 2. Seeding (First Run Only)
If this is a fresh database, run the seeders to populate reference data and user roles.
```bash
python scripts/seed_database.py
```

### 3. Application Startup
Use a production-grade ASGI server like Uvicorn (with Gunicorn workers in production).

**Development:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Production:**
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Docker Deployment
Alternatively, use the provided `Dockerfile` and `docker-compose.yml`.
```bash
docker-compose up --build -d
```
The application will automatically run migrations and boot.
