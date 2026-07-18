# Database Indexing Strategy (GridSense AI)

**Version:** 1.0  
**Status:** Approved for Implementation  
**Author:** Data Architecture Team  

---

## 1. Introduction

This document defines the comprehensive indexing strategy for the GridSense AI PostgreSQL 18 database. Because the platform serves dual purposes—high-frequency ETL ingestion via the Energy Atlas SDK, and heavy analytical querying via FastAPI and Power BI—an optimized indexing strategy is essential to prevent write bottlenecks while guaranteeing rapid read performance.

---

## 2. Indexing Principles

- **Read vs. Write Trade-offs:** Every index accelerates read performance (`SELECT`) but degrades write performance (`INSERT/UPDATE`) because the index tree must be updated. For massive tables (like `grid_frequency`), we strictly limit the number of indexes.
- **Storage Overhead:** Indexes consume RAM. An over-indexed multi-million row table will push active data out of the PostgreSQL buffer cache, drastically slowing the system.
- **When NOT to index:** 
  - Low cardinality columns (e.g., a `boolean` like `is_active` where 99% of rows are `true`).
  - Small tables (< 1,000 rows, e.g., `reference.states`); sequential scans are faster in memory.
  - Opaque `JSONB` columns unless a specific search requirement exists.

---

## 3. Table-by-Table Analysis

| Schema | Table | Expected Vol. | Read Freq. | Write Freq. | Business Criticality |
|--------|-------|---------------|------------|-------------|----------------------|
| `reference` | `states`, `regions`, `fuel_types` | < 100 rows | Very High | Rare | High (Joins) |
| `assets` | `power_plants`, `transmission_lines`| ~20k rows | High | Daily | High (Filtering) |
| `energy` | `demand_timeseries` | Millions | High | Hourly | Critical (BI) |
| `energy` | `generation_timeseries` | Millions | High | Hourly | Critical (BI) |
| `grid` | `frequency_timeseries` | Tens of Millions| Medium | Every 15m | High (ML / APIs) |
| `market` | `iex_dam_pricing` | Hundreds of k | High | Daily | High (BI) |
| `ingestion` | `api_request_logs` | Millions | Low | Very High | Low (Audit only) |

---

## 4. Primary Key Indexes

Primary Keys (PKs) in PostgreSQL automatically generate a `UNIQUE B-Tree` index.

- **Dimensional Tables (UUID):** The PK index enables instant `O(log N)` lookups for FastAPI single-entity endpoints.
- **Fact Tables (Composite Natural Keys):** Our decision to use `(timestamp, dimension_id)` as the PK automatically clusters the B-Tree index by time first, then by entity. This perfectly optimizes the `ON CONFLICT DO UPDATE` UPSERT logic in our Ingestion Strategy and ensures chronological query filtering is naturally fast.

---

## 5. Foreign Key Indexes

Unlike PKs, PostgreSQL **does not** automatically index Foreign Keys (FKs). Unindexed FKs cause devastating full-table sequential scans when executing cascading deletes or joins.

**Strategy:** We will create explicit B-Tree indexes on FKs only for tables exceeding 1,000 rows.
- **`assets.power_plants(state_id)`**: Indexed (Enables "Show all plants in state X").
- **`assets.power_plants(fuel_type_id)`**: Indexed (Enables "Show all thermal plants").
- **`energy.demand_timeseries(state_id)`**: Covered by the Composite PK. No secondary index needed.

---

## 6. Composite Indexes & 7. Time-Series Optimization

Time-series fact tables are the largest structures in the database.

**B-Tree Descending Indexes:**
Because FastAPI and BI dashboards frequently ask for the *latest* data, a descending index on the composite key is highly recommended:
- `CREATE INDEX idx_demand_latest ON energy.demand_timeseries (timestamp DESC, state_id);`

**BRIN (Block Range Indexes):**
For historical aggregations (e.g., "Average generation over the last 3 years"), B-Tree indexes become too large to fit in memory. 
- **Recommendation:** Create a `BRIN` index on the `timestamp` column for all massive fact tables (`grid.frequency_timeseries`, `energy.demand_timeseries`). BRIN indexes are ~99% smaller than B-Trees and drastically accelerate large sequential range scans.

---

## 8. Power BI Optimization

Power BI relies heavily on the `time_dimension` table. 
- **Recommendation:** Index `time_dimensions(year, month)`.
- **Recommendation:** Create composite indexes mapping the primary slicing dimensions to the timestamp. Example: `(fuel_type_id, timestamp DESC)` in `energy.generation_timeseries`.

---

## 9. FastAPI Optimization & 10. ML Optimization

- **FastAPI:** Requires lightning-fast single-record retrieval. The existing PK indexes and `timestamp DESC` indexes fulfill this.
- **Machine Learning:** ML pipelines extract sliding windows of data (e.g., extracting 30 days of 15-minute frequency data). The `BRIN` index on `timestamp` perfectly supports these massive range extractions without polluting the RAM cache.

---

## 11. Ingestion Optimization

The ingestion pipeline designed in Sprint 3.4 relies heavily on idempotency (`ON CONFLICT DO UPDATE`).
- The existing unique B-Tree indexes automatically generated by our Composite Primary Keys in the Fact tables (`timestamp`, `dimension_id`) are the exact mechanism required to make this fast and safe. No additional indexes are required for ingestion.

---

## 12. Business Query → Index Mapping

| Business Query | Tables | Expected Frequency | Recommended Index | Priority |
|----------------|--------|--------------------|-------------------|----------|
| Latest grid frequency | `grid.frequency_timeseries` | Very High | `(timestamp DESC, region_id)` | Critical |
| Demand by state & date | `energy.demand_timeseries` | Very High | `(state_id, timestamp DESC)` | Critical |
| Generation by fuel | `energy.generation_timeseries` | High | `(fuel_type_id, timestamp DESC)` | High |
| Power plants by state | `assets.power_plants` | Medium | `(state_id)` | Medium |
| Latest DAM prices | `market.iex_dam_pricing` | High | `(timestamp DESC)` | High |
| 5-year historical average | `energy.generation_timeseries` | Low | `BRIN (timestamp)` | Low |

---

## 13. Index Maintenance

- **Index Bloat:** Frequent UPSERTs (from our Incremental refresh strategy) create dead tuples. `autovacuum` MUST be aggressively tuned for fact tables.
- **Reindexing:** B-Tree indexes on frequently updated asset tables (`power_plants`) should be concurrently reindexed (`REINDEX INDEX CONCURRENTLY`) monthly to recover space.
- **JSONB Strategy:** We will explicitly **avoid** GIN indexing the `metadata` column in `power_plants` to prevent write latency. It can be added later if text-search requirements emerge.

---

## 14. Validation Checklist

- [x] **No Duplicate Indexes:** Ensured FK indexes don't overlap with composite PK definitions.
- [x] **BRIN Applied:** Documented the use of BRIN indexes to solve historical scale.
- [x] **Read/Write Balance:** Excluded GIN indexing and low-cardinality indexing to keep ingestion fast.
- [x] **Query Mapping:** Included the mandatory Business Query matrix.
