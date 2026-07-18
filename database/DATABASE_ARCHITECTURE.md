# Database Architecture Design (GridSense AI)

**Version:** 1.1  
**Status:** Architecture Approved  
**Author:** Data Architecture Team  

---

## 1. Executive Summary

GridSense AI leverages **PostgreSQL 18** as its core analytical data warehouse. Rather than functioning as a simplistic 1:1 cache of the Energy Atlas API responses, the architecture is designed as a fully normalized, dimensional, time-series optimized repository. 

This architecture supports:
- High-volume time-series analytics.
- Extensive historical data retention.
- Direct connectivity with Power BI (via dimensional modeling).
- Machine Learning (ML) forecasting workloads via dedicated schemas.
- Rapid querying via FastAPI.

---

## 2. Architectural Decisions

### Why PostgreSQL 18?
PostgreSQL 18 offers advanced declarative partitioning, robust window functions, and `JSONB` support. It perfectly bridges the gap between relational integrity and high-throughput time-series storage without requiring a dedicated NoSQL engine. 

### Why Relational / Normalized Design?
A normalized, star-schema-inspired design prevents data duplication, enforces referential integrity, and drastically reduces the footprint of massive time-series tables (by storing integer or UUID references instead of repeating string dimensions like state names or fuel types).

### Historical & Time-Series Strategy
- **Historical Storage:** Time-series tables are append-only. Reference data uses Slowly Changing Dimensions (SCD Type 2) or simple UPSERTs depending on the volatility of the asset.
- **Time-Series Strategy:** We rely on native PostgreSQL Range Partitioning rather than introducing third-party extensions like TimescaleDB. This reduces operational complexity while still providing excellent query and retention performance.
- **Source Tracking:** Every fact table includes a `source_system` column (e.g., 'EnergyAtlas', 'POSOCO') to seamlessly support multi-source integration in the future without schema redesigns.

---

## 3. Logical Schema Design

To enforce boundary contexts and maintain organization, the database is divided into logical schemas:

1. **`ingestion`**: Staging tables for raw API payloads, centralized dataset registries (`dataset_registry`), and distinct request/response API logs.
2. **`reference`**: Static master data (e.g., states, regions, entities, fuel types, market types, operators, owners, voltage levels).
3. **`assets`**: Physical infrastructure data (Power plants, substations, transmission lines).
4. **`grid`**: Core grid telemetry (Frequency, voltage).
5. **`energy`**: Power supply, demand, generation mix, and carbon intensity metrics.
6. **`market`**: Financial and market volume metrics (IEX DAM, RTM, GDAM).
7. **`operations`**: Administrative and operational metrics (POSOCO/CEA PSP, energy investments).
8. **`ml`**: Machine learning model tracking (`model_registry`) and predictions (`predictions`).

---

## 4. Data Domains

Based on the Energy Atlas API inspection and best practices, the datasets map to our logical schemas as follows:

### Grid Schema
- `grid_frequency` (Real-time and historical frequency metrics)
- `grid_frequency_15min` (Aggregated 15-minute blocks)

### Energy Schema
- `demand_timeseries` (State/Regional load metrics)
- `generation` (Fuel-mix time-series)
- `carbon` (Carbon intensity telemetry)

### Market Schema
- `iex_dam` (Day-Ahead Market pricing and volume)
- `iex_rtm` (Real-Time Market pricing and volume)
- `iex_gdam` (Green Day-Ahead Market)

### Assets Schema
- `power_plants` (Generation unit metadata and capacities)
- `transmission_lines` (Edges/Grid connectivity)
- `substations` (Nodes/Transformers)

### Operations Schema
- `posoco_psp_daily` (Daily Power Supply Position)
- `cea_monthly_psp` (Monthly Power Supply Position)
- `energy_investments` (Financial outlays)

### Reference Schema
- `states`, `regions`, `fuel_types`, `market_types`, `operators`, `owners`, `voltage_levels`

### ML Schema
- `model_registry` (Tracks ML models and versions)
- `predictions` (Stores forecasted values vs actuals)

---

## 5. Database Design Principles

### Keys
- **Reference & Asset Tables:** Use `UUID` (v7 or v4) for primary keys to prevent ID collisions and simplify distributed ingestion.
- **Time-Series Tables:** Use composite natural keys (e.g., `(timestamp, region_id)`) to optimize index clustering and partition pruning. Surrogate keys on massive time-series tables create unnecessary overhead.
- **Time Dimension:** Uses a Kimball-style integer `date_key` (e.g., `20260717`) to simplify BI joins and fiscal calendar mappings.

### Timestamp Strategy
- **Timezones:** All timestamps are stored as `TIMESTAMP WITH TIME ZONE` (`timestamptz`). 

### Audit & Metadata Columns
All tables (excluding raw ingestion) must include:
- `created_at` (timestamptz, default `now()`)
- `updated_at` (timestamptz, updated via trigger or ORM)
- `deleted_at` (timestamptz, nullable - explicitly used for soft-deleting records while preserving the exact time of deletion).

---

## 6. Time Series Strategy

### Granularity
Time-series data is stored at the lowest available API granularity (typically 15-minute or 5-minute intervals).

### Partitioning
- **Mechanism:** Native PostgreSQL Declarative Range Partitioning.
- **Partition Key:** The `timestamp` column.
- **Interval:** Monthly partitions (`_yyyy_mm`) for high-volume tables (e.g., `energy.demand_timeseries`, `grid.frequency`).

---

## 7. Data Flow Architecture

The end-to-end data pipeline is structured as follows:

**1. Energy Atlas API:** The external source of truth.  
**2. Energy Atlas SDK:** Manages HTTP resilience, authentication, and structured error handling.  
**3. Refresh Service (Python):** Orchestrates API polling based on dynamic intervals. Stores execution metadata in `ingestion.dataset_registry` and splits API traces into `api_request_logs` and `api_response_logs`.  
**4. Transformation:** Normalizes the data, resolving references and upserting records into the domain schemas. Injects the `source_system` string.  
**5. PostgreSQL (Domain Schemas):** The structured, partitioned data warehouse.  
**6. FastAPI / ML Pipelines:** Serves data to the frontend or feeds training jobs (logging output to `ml.predictions`).  
**7. React Dashboard / Power BI:** Consumes the APIs and direct dimensional models for end-user visualization.

---

## 8. Naming Conventions

Strict naming conventions ensure maintainability and predictability:

- **Schemas:** `snake_case` (e.g., `market`)
- **Tables:** `snake_case`, strictly plural (e.g., `power_plants`, `fuel_types`)
- **Columns:** `snake_case` (e.g., `installed_capacity_mw`)
- **Primary Keys:** `id` for UUIDs, `date_key` for Time Dimension, or `pk_<table_name>` for constraint names.
- **Foreign Keys:** `<singular_table>_id` (e.g., `region_id`). Constraint names: `fk_<table_name>_<ref_table>`.
- **Indexes:** `idx_<table_name>_<column_name>`.

---
