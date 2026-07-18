# GridSense AI - Backend Coding Standards

## 1. Architecture Philosophy
We strictly follow **Clean Architecture** principles. Dependencies flow inwards.

### The Flow of Data
`Router (API)` -> `Service (Business Logic)` -> `Repository (Database)` -> `PostgreSQL`

- **Routers (`api/v1/`):** Should ONLY handle HTTP requests, path parameters, query parsing, and return Pydantic schemas. NO database logic here.
- **Services (`services/`):** Contains all business rules, orchestration, validation across multiple domains, and error throwing.
- **Repositories (`repositories/`):** ONLY contains SQLAlchemy queries (`select`, `insert`, `update`). Services call Repositories. Repositories NEVER call Services.

## 2. Naming Conventions
- **Classes/Models/Schemas:** `PascalCase` (e.g. `DemandTimeseries`, `DemandCreate`)
- **Functions/Variables:** `snake_case` (e.g. `get_demand_by_state`, `installed_capacity_mw`)
- **Files/Modules:** `snake_case.py` (e.g. `power_plants.py`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g. `MAX_RETRIES`)

## 3. Type Hinting
- Every function, method, and variable should use explicit Python 3.10+ type hinting.
- Use `|` instead of `Union`.
- Use `dict[str, Any]` instead of `Dict`.

## 4. Asynchronous Code
- The entire backend is asynchronous.
- Database queries must use `AsyncSession` and `await session.execute(...)`.
- AVOID `sync` code in the request lifecycle to prevent blocking the event loop.

## 5. Dependency Injection
Use FastAPI's `Depends()` for:
- Database sessions (`get_db`)
- Authentication context (`get_current_user`)
- Injecting Repositories into Services.

## 6. Exception Handling
- DO NOT return HTTP 500 or 400 responses directly from a Service.
- Services should `raise BusinessRuleError("msg")` or `raise RepositoryError("msg")`.
- The global Exception Handler in `middleware/exception_handler.py` will catch these and format them into standard JSON HTTP responses.
