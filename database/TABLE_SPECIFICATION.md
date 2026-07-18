# Table Specification Design (GridSense AI)

**Version:** 1.1  
**Status:** Approved for Implementation  
**Author:** Data Architecture Team  

---

## 1. Introduction

This document provides the definitive data dictionary and table specification for the GridSense AI database. Strict naming conventions, audit standardizations, and precise PostgreSQL data typing are enforced throughout.

---

## 2. Naming Conventions & Standards

### Primary & Foreign Key Strategy
- **Dimensions:** Use `UUID` generated via `gen_random_uuid()`.
- **Time Dimension:** Uses `date_key INTEGER` (e.g., 20260717).
- **Facts (Time-Series):** Use Composite Natural Keys `(timestamp, dimension_id)`.
- **Foreign Keys:** Enforce `ON DELETE RESTRICT`.

### Audit Column Standards
- **Dimensional Tables** require:
  - `created_at` (`TIMESTAMPTZ`, default `now()`)
  - `updated_at` (`TIMESTAMPTZ`, default `now()`)
  - `deleted_at` (`TIMESTAMPTZ`, nullable, tracks exact soft-deletion time)
- **Fact Tables** require:
  - `created_at` (`TIMESTAMPTZ`, default `now()`)
  - `source_system` (`VARCHAR(50)`, tracks multi-vendor data origination)

---

## 3. Schema Overview

| Schema | Purpose |
|--------|---------|
| `reference` | Static dimensions (States, Regions, Operators, Calendar). |
| `assets` | Physical grid infrastructure. |
| `grid` | Grid frequency and physical telemetry. |
| `energy` | Power supply, demand, generation mix, and carbon metrics. |
| `market` | Financial pricing and volume metrics. |
| `operations` | Administrative reports (POSOCO/CEA PSP). |
| `ingestion` | Data lineage (`dataset_registry`) and API logs. |
| `ml` | Model versioning and historical predictions. |

---

## 4. Detailed Table Specifications

### A. Reference Schema

#### 1. `reference.time_dimensions`
**Business Purpose:** Contiguous calendar table enabling advanced Power BI time-intelligence.  
**Refresh Strategy:** Generated Annually.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `date_key` | Primary Key | `INTEGER` | No | `PK` (e.g., 20260717) |
| `date` | Actual Date | `DATE` | No | `UNIQUE` |
| `year` | Calendar Year | `SMALLINT` | No | |

*(Note: `regions`, `states`, `fuel_types`, `market_types`, `operators`, `owners`, and `voltage_levels` follow the standard UUID pattern with `deleted_at`).*

---

### B. Energy Schema (Fact Example)

#### 1. `energy.demand_timeseries`
**Business Purpose:** State-level power load requirements.  
**Source API Endpoint:** `/api/intelligence/demand-timeseries`  
**Refresh Strategy:** Incremental Append.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `timestamp` | Reading Time | `TIMESTAMPTZ` | No | `PK` (Composite part 1) |
| `state_id` | Target State | `UUID` | No | `PK` (Part 2), `FK` |
| `source_system`| Data Origin | `VARCHAR(50)` | No | e.g. 'EnergyAtlas' |
| `demand_mw` | Met Demand | `NUMERIC(12,2)`| No | |
| `created_at` | Audit timestamp | `TIMESTAMPTZ` | No | `now()` |

*(Note: `source_system` is applied to all tables in `energy`, `grid`, `market`, and `operations` schemas).*

---

### C. ML Schema

#### 1. `ml.model_registry`
**Business Purpose:** Tracks deployed machine learning models.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `model_id` | Primary Key | `UUID` | No | `PK`, `gen_random_uuid()` |
| `model_name` | Name of model | `VARCHAR(100)`| No | |
| `version` | Model version | `VARCHAR(50)` | No | |
| `created_at` | Audit timestamp | `TIMESTAMPTZ` | No | `now()` |
| `deleted_at` | Soft delete | `TIMESTAMPTZ` | Yes | |

#### 2. `ml.predictions`
**Business Purpose:** Stores generated forecasts against actuals for MAE tracking.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `prediction_id`| Primary Key | `UUID` | No | `PK`, `gen_random_uuid()` |
| `model_id` | Foreign Key | `UUID` | No | `FK` to `model_registry(model_id)`|
| `timestamp` | Target Time | `TIMESTAMPTZ` | No | |
| `prediction` | Forecast Value | `NUMERIC(12,2)`| No | |
| `actual` | True Value | `NUMERIC(12,2)`| Yes | Populated later |
| `mae` | Error Metric | `NUMERIC(12,4)`| Yes | |

---

### D. Ingestion Schema

#### 1. `ingestion.dataset_registry`
**Business Purpose:** Centralized data lineage tracking.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `dataset` | Name (e.g. demand) | `VARCHAR(100)`| No | `PK` |
| `sdk_method` | SDK Invocation | `VARCHAR(150)`| No | e.g. `atlas.demand.get_timeseries()`|
| `refresh_type`| Strategy | `VARCHAR(50)` | No | e.g. `Incremental` |

#### 2. `ingestion.api_request_logs`
**Business Purpose:** Tracks lightweight API execution latency and statuses.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `request_id` | Trace ID | `UUID` | No | `PK` |
| `endpoint` | API Path | `VARCHAR(255)` | No | |
| `http_status` | Response code | `SMALLINT` | No | |

#### 3. `ingestion.api_response_logs`
**Business Purpose:** Isolates heavy payload auditing from operational metrics.  

| Column Name | Business Meaning | Data Type | Nullable | Constraints / Default |
|-------------|------------------|-----------|----------|-----------------------|
| `request_id` | Trace ID | `UUID` | No | `PK`, `FK` to `request_logs` |
| `payload` | Raw Response | `JSONB` | No | |

---
