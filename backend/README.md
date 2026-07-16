# GridSense AI Backend

Production-ready FastAPI foundation for GridSense AI Sprint 1.

## Scope

Sprint 1 includes only the backend foundation:

- FastAPI application factory
- Pydantic Settings configuration
- Environment variable management
- Structured logging
- SQLAlchemy 2.x async database session setup
- Alembic migration setup
- PostgreSQL connection configuration
- CORS configuration
- `GET /`
- `GET /health`
- Docker and Render-ready deployment configuration

Sprint 1 intentionally excludes authentication, business logic, Energy Atlas integration, dashboard APIs, models, scheduler jobs, AI, and frontend code.

## Local Setup

```bash
uv sync --dev
cp .env.example .env
uv run uvicorn app.main:app --reload
```

## Docker Setup

```bash
cp .env.example .env
docker compose up --build
```

## Verification

```bash
uv run pytest
curl http://localhost:8000/
curl http://localhost:8000/health
```

Expected health response:

```json
{
  "status": "healthy",
  "service": "GridSense AI Backend",
  "version": "1.0.0"
}
```

## Alembic

```bash
uv run alembic revision --autogenerate -m "initial"
uv run alembic upgrade head
```

No database models are included in Sprint 1, so autogeneration should produce no schema changes until future sprints add models.

## Render Deployment

Create a Render Web Service using Docker.

- Root directory: `backend`
- Dockerfile path: `backend/Dockerfile` when deploying from the repository root, or `Dockerfile` when root directory is set to `backend`
- Health check path: `/health`
- Required environment variable: `DATABASE_URL`
- Recommended production variables:
  - `ENVIRONMENT=production`
  - `DEBUG=false`
  - `LOG_LEVEL=INFO`
  - `LOG_JSON=true`
  - `CORS_ALLOWED_ORIGINS=["https://your-frontend-domain.com"]`

Use Render PostgreSQL with PostGIS enabled for the managed database.
