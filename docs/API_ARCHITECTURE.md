# API Architecture Overview

The GridSense AI API is built using **FastAPI** and strictly adheres to RESTful design principles.

## Global Response Structure

All endpoints return a standardized JSON envelope to guarantee predictable parsing for front-end applications.

### Success Response (2xx)
```json
{
  "success": true,
  "data": { ... }
}
```

### Paginated Response (2xx)
```json
{
  "success": true,
  "data": [ ... ],
  "total": 100,
  "page": 1,
  "size": 25
}
```

### Error Response (4xx, 5xx)
```json
{
  "success": false,
  "error": "Human readable error message",
  "code": "INTERNAL_SERVER_ERROR"
}
```

## Security & Authentication

- **Authentication**: JWT (JSON Web Tokens). Obtain a token via `POST /api/v1/auth/login/access-token` by sending standard `application/x-www-form-urlencoded` credentials (`username`, `password`).
- **Authorization**: Endpoints are guarded using `Depends(get_current_active_user)`.
- **Role Based Access**: Can be enforced per-endpoint using `Depends(RequireRole(["Admin", "Operator"]))`.
- **API Keys**: External system integrations utilize `X-API-Key` headers evaluated by `verify_api_key`.

## Sub-Domains
1. **Analytics & Dashboard (`/api/v1/analytics`, `/api/v1/dashboard`)**: Heavily aggregated, cached endpoints outputting KPIs and chart series.
2. **Core Domain (`/api/v1/energy`, `/api/v1/grid`, `/api/v1/assets`)**: Raw standard entity operations.
3. **Reference Data (`/api/v1/reference`)**: Configuration tables, states, fuel types.

## Error Handling
Exceptions are managed globally in `app/exceptions/handlers.py`.
- **Domain Exceptions** (e.g. `ResourceNotFound`, `BusinessRuleViolation`) map to standard HTTP errors (404, 400).
- **Unhandled Exceptions** are caught, logged securely, and return a masked 500 error preventing internal stack leakages.
