# Data Ingestion Strategy (GridSense AI)

**Version:** 1.1  
**Status:** Approved for Implementation  
**Author:** Data Architecture Team  

---

## 1. Introduction

This document details the production-grade data ingestion pipeline architecture for GridSense AI. It defines the rules by which data flows from the external Energy Atlas API, undergoes validation and transformation, and is securely persisted in the PostgreSQL data warehouse. This strategy incorporates advanced data lineage tracking and decoupling of heavy payloads to preserve performance.

---

## 2. High-Level Data Flow

The ingestion pipeline executes sequentially through the following layers:

`Energy Atlas API` 
↓ 
`Energy Atlas SDK` *(Handles HTTP retries, rate limits, correlation IDs)*
↓ 
`Data Validation Layer` *(Type checking, null-enforcement)*
↓ 
`Transformation Layer` *(FK resolution, source_system injection)*
↓ 
`Deduplication (Idempotency)` *(Conflict resolution via UPSERT)*
↓ 
`PostgreSQL` *(Domain schemas: energy, market, grid, etc.)*
↓ 
`Ingestion Logs` *(Records to dataset_registry, api_request_logs, and api_response_logs)*
↓ 
`FastAPI / React Dashboard` *(Downstream consumption)*

---

## 3. Dataset Classification

To apply appropriate refresh rules, datasets are categorized:
- **Data Lineage:** `ingestion.dataset_registry` holds the master list of all SDK methods and their required refresh behavior.
- **Static Reference Data:** Almost never changes (e.g., `States`, `Operators`).
- **Slowly Changing Data:** Changes infrequently; requires historical preservation via soft-deletes (`deleted_at` timestamp).
- **High Frequency Time-Series:** Appends rapidly; immense volume.
- **Operational Metadata:** System logs separated by lightweight traces (`api_request_logs`) and heavy payloads (`api_response_logs`).

---

## 4. Refresh Strategy

- **Static:** One-time manual insert (e.g., `reference.states`).
- **Full Refresh:** Erase (set `deleted_at = now()`) and reload the entire dataset. Used for low-volume entity tables where state tracking is complex (e.g., `assets.power_plants`).
- **Incremental (Append + Merge):** Pull only recent data (e.g., last 24 hours). If a record exists for that timestamp, update it; otherwise, insert.

---

## 5. Dataset Ingestion Matrix (Driven by Dataset Registry)

| Dataset | Source SDK Method | Destination Table | Refresh Type | Frequency | Load Strategy |
|---------|-------------------|-------------------|--------------|-----------|---------------|
| States/Regions | Static Reference | `reference.states` | Static | Once | Insert Only |
| Power Plants | `atlas.assets.get_power_plants()` | `assets.power_plants` | Full Refresh | Daily | Soft-Delete + Replace |
| Grid Frequency | `atlas.grid.get_frequency()` | `grid.frequency_timeseries` | Incremental | 15 min | Append + Merge |
| Demand | `atlas.demand.get_timeseries()` | `energy.demand_timeseries` | Incremental | Hourly | Append + Merge |
| Generation | `atlas.generation.get_generation()` | `energy.generation_timeseries` | Incremental | Hourly | Append + Merge |

---

## 6. Transformation & Idempotency Strategy

- **Source System Injection:** During transformation, a hardcoded `source_system` string (e.g., `'EnergyAtlas'`, `'POSOCO'`) is injected into every row being loaded into a fact table. This enables safe, conflict-free integration of multiple third-party data vendors later.
- **Date Key Generation:** A transformation hook translates raw datetime objects into the Kimball-style `date_key` integers (e.g., `20260717`) for BI-ready joins.
- **Idempotency Guarantee:** 
  - Time-Series rely on PostgreSQL's `INSERT ... ON CONFLICT (timestamp, dimension_id) DO UPDATE`.
  - Reference tables use UPSERT logic, strictly preserving `created_at` but modifying `updated_at`. If a record disappears from the source, `deleted_at` is populated.

---

## 7. Error Handling & Monitoring

- **API Failures:** Handled natively by the SDK.
- **Database Rollbacks:** All transformations and DB inserts for a single endpoint run inside a single PostgreSQL Transaction (`BEGIN ... COMMIT`).
- **Decoupled API Logging:** To prevent massive JSON payloads from clogging operational metrics, basic request statuses (200, 429) go to `api_request_logs` while the full JSON body is shunted to a 1:1 `api_response_logs` table. This allows fast aggregated queries on the request logs without sequential scanning through gigabytes of JSON.

---

## 8. Future Enhancements

- **Machine Learning Integration:** Later phases will introduce the `ml` schema to pull training data directly from the verified domain schemas, tracking model versions in `model_registry` and appending output to `predictions` seamlessly alongside actual ingestion facts.
