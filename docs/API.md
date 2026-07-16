# GridSense AI

## 1. Document Information
### API Specification
**Version:** 1.0  
**Author:** Kirtik Patidar  
**Last Updated:** July 2026

---

## 2. Purpose
This document defines the API architecture for GridSense AI.

It describes:
- External APIs consumed by the backend
- Internal REST APIs exposed by GridSense AI
- Authentication
- Request/Response standards
- Error handling
- API versioning

The frontend communicates only with GridSense AI APIs.  
The backend communicates with the India Energy Atlas API.

---

## 3. API Architecture
```text
                 India Energy Atlas API
                          │
                          ▼
                  FastAPI Backend
                          │
                   PostgreSQL
                          │
                          ▼
                   Internal APIs
                          │
                          ▼
                  Next.js Frontend
```

---

## 4. External API Provider
GridSense AI Version 1 uses only one external data provider.

**Provider:**  
India Energy Atlas Developer API

**Purpose:**  
Provides nationwide energy datasets including:
- Grid
- Demand
- Generation
- IEX
- Carbon
- Assets
- Investments

---

## 5. External API Endpoints
| Module | Energy Atlas Endpoint | Refresh |
| :--- | :--- | :--- |
| Grid Frequency | `/api/intelligence/grid-frequency` | 15 min |
| Demand | `/api/intelligence/demand-timeseries` | 15 min |
| DAM | `/developer/v1/market/iex/latest?market_type=DAM` | 15 min |
| RTM | `/developer/v1/market/iex/latest?market_type=RTM` | 15 min |
| GDAM | `/api/intelligence/iex-green-market` | Daily |
| Generation | `/api/intelligence/fuel-mix-timeseries` | Daily |
| Carbon | `/api/intelligence/carbon-intensity` | Hourly |
| Power Plants | `/api/intelligence/power-plants` | Daily |
| Transmission | `/api/edges` | Daily |
| Substations | `/api/nodes` | Daily |
| Investments | `/api/intelligence/energy-investments` | Daily |
| Power System Position | `/api/intelligence/posoco-psp` | Daily |

---

## 6. Internal APIs
- `GET /api/v1/dashboard`
- `GET /api/v1/states`
- `GET /api/v1/grid`
- `GET /api/v1/demand`
- `GET /api/v1/generation`
- `GET /api/v1/market`
- `GET /api/v1/carbon`
- `GET /api/v1/assets`
- `GET /api/v1/search`

---

## 7. API Versioning
**Current Version:** `v1`  
**Base URL:** `/api/v1/`

---

## 8. Authentication
- `POST /auth/login`
- `POST /auth/register`
- `POST /auth/logout`
- `POST /auth/refresh`

---

## 9. Response Format
Every API returns:
```json
{
  "success": true,
  "message": "Request successful",
  "data": {}
}
```

---

## 10. Error Format
```json
{
  "success": false,
  "error": {
    "code": 404,
    "message": "Resource not found"
  }
}
```

---

## 11. HTTP Status Codes
| Code | Meaning |
| :--- | :--- |
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 12. Data Flow
```text
Energy Atlas API
      ↓
   FastAPI
      ↓
  Validation
      ↓
  PostgreSQL
      ↓
 Internal API
      ↓
  Frontend
```

---

## 13. Rate Limits
**Energy Atlas Free Tier**
- 100 API Calls / Day
- 50,000 Rows / Request
- 500,000 Rows / Rolling 30 Days

*Note: These limits heavily influence how often the scheduler should fetch data (e.g., aggregating calls to stay under the 100 requests/day limit).*

---

## 14. Future Integrations
- Weather
- Satellite
- AI Models
- Notifications

*Currently marked as: **Not implemented**.*
