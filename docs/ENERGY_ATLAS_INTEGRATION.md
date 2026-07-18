# ENERGY_ATLAS_INTEGRATION.md

Version: 1.0

Status: Active Development

---

# 1. Purpose

This document defines how GridSense AI integrates with the India Energy Atlas API.

It serves as the technical reference for:

- API authentication
- Endpoint usage
- Refresh strategy
- Rate limiting
- Data caching
- Error handling
- Backend integration

This document should always reflect the actual implementation.

---

# 2. API Provider

Provider

India Energy Atlas

Platform

https://energymap.in

License

CC BY 4.0

Student Tier

---

# 3. API Limits

## Daily Limits

Maximum API Calls

100 Requests / Day

Maximum Requests

20 Requests / Minute

Maximum Rows

50,000 Rows / Request

Monthly Limit

500,000 Rows (Rolling)

---

# 4. Development Principles

GridSense AI **never exposes the Energy Atlas API directly to the frontend.**

Architecture

Frontend

↓

FastAPI Backend

↓

PostgreSQL Cache

↓

Energy Atlas API

The frontend always consumes backend APIs.

---

# 5. Authentication

Credentials are stored only inside:

backend/.env

Example

```env
ENERGY_ATLAS_API_KEY=xxxxxxxxxxxxxxxx
ENERGY_ATLAS_BASE_URL=https://api.energymap.in
ENERGY_ATLAS_TIMEOUT=30
```

API keys must never be:

- committed to Git
- returned to frontend
- logged

## Authentication Strategy

The Energy Atlas platform exposes multiple API namespaces that use different authentication headers.

### Intelligence API

Header:

`Authorization: Bearer <API_KEY>`

Examples:

- `/api/intelligence/grid-frequency`
- `/api/intelligence/demand-timeseries`
- `/api/intelligence/fuel-mix-timeseries`

### Developer API

Header:

`X-API-Key: <API_KEY>`

Examples:

- `/Developer/v1/grid/frequency`
- `/developer/v1/market/iex/latest`

---

# 6. SDK Architecture

The backend communicates with Energy Atlas through a reusable SDK.

```text
app/

ingestion/

energy_atlas/

client.py

config.py

constants.py

exceptions.py

validators.py

models.py
```

Only the SDK communicates with the external API.

---

# 7. Modules Used

Version 1 will integrate the following modules.

| Module | Purpose | Status |
|----------|---------|--------|
| Grid | National Grid Analytics | Planned |
| Demand | Demand Dashboard | Planned |
| Generation | Generation Dashboard | Planned |
| Carbon | Carbon Analytics | Planned |
| IEX | Market Analytics | Planned |
| Power Plants | Interactive Map | Planned |
| Transmission | Interactive Map | Planned |
| Substations | Interactive Map | Planned |

---

# 8. Endpoint Strategy

Each API endpoint should have its own dedicated method.

Example

```python
get_grid()

get_demand()

get_generation()

get_carbon()

get_power_plants()

get_transmission()

get_substations()

get_iex()
```

Avoid creating large generic methods containing business logic.

---

# 9. Request Strategy

Every request should include:

- Authentication
- Timeout
- Retry Logic
- Validation
- Logging

The SDK should use:

- httpx
- Typed responses
- Custom exceptions

---

# 10. Error Handling

Handle the following cases gracefully.

Authentication Error

- Invalid API Key

Rate Limit

- Too Many Requests

Connection Error

- Timeout
- Network Failure

Response Error

- Invalid JSON
- Empty Response

Server Error

- 500
- 502
- 503

Unknown Error

- Unexpected Response

---

# 11. Retry Strategy

Retry only transient failures.

Recommended

- Maximum Retries: 3
- Exponential Backoff

Never retry:

- Invalid API Key
- 404
- Validation Errors

---

# 12. Logging

Every request should log:

- Endpoint
- Timestamp
- Response Time
- Status Code
- Retry Count

Never log:

- API Keys
- Sensitive Headers

---

# 13. Data Refresh Strategy

The frontend never requests Energy Atlas directly.

Instead:

Energy Atlas

↓

Backend

↓

PostgreSQL Cache

↓

Frontend

---

## Refresh Policy

| Module | Refresh Interval |
|----------|------------------|
| Grid Frequency | 15 Minutes |
| Demand | 30 Minutes |
| IEX | 30 Minutes |
| Carbon | Every 4 Hours |
| Generation | Daily |
| Power Plants | Weekly |
| Transmission | Weekly |
| Substations | Weekly |

Refresh intervals may be adjusted based on API limits.

---

# 14. API Quota Management

The backend should monitor:

- Requests Used Today
- Remaining Daily Requests
- Last Refresh Time
- Failed Requests

If the daily quota is close to exhaustion:

- Skip non-critical refreshes
- Continue serving cached data

---

# 15. Database Policy

Version 1 stores only the latest required data.

Historical data should be stored only where required by the dashboard.

The database acts as a cache layer between the frontend and Energy Atlas.

---

# 16. Frontend Policy

The frontend must never:

- Know the API Key
- Call Energy Atlas directly
- Store authentication credentials

All requests must go through FastAPI.

---

# 17. Future Enhancements

Version 2 may include:

- Multiple Data Providers
- Grid India Integration
- IEX Live APIs
- Weather APIs
- Forecast Models
- AI Recommendations
- Automatic Scheduler

---

# 18. Definition of Done

The Energy Atlas integration is considered complete when:

- SDK implemented
- Authentication working
- Endpoint wrappers implemented
- Retry logic implemented
- Logging implemented
- Response validation completed
- API limits respected
- Database cache connected
- Frontend consumes backend APIs only

---

# 19. Notes

This document should evolve as new Energy Atlas endpoints are integrated.

It is the authoritative technical reference for all Energy Atlas-related development in GridSense AI.
