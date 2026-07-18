# API Inventory

| Namespace | Endpoint | URL | Auth Method | Status | HTTP Code | Records | Latest Timestamp | Response Size | Duration |
|---|---|---|---|---|---|---|---|---|---|
| GRID | grid_frequency | `/api/intelligence/grid-frequency` | Bearer | SUCCESS | 200 | 1 | N/A | 12473 bytes | 853 ms |
| GRID | grid_frequency_15min | `/api/intelligence/grid-frequency?resolution=15m` | Bearer | SUCCESS | 200 | 1 | N/A | 12473 bytes | 956 ms |
| DEMAND | demand_timeseries | `/api/intelligence/demand-timeseries` | Bearer | SUCCESS | 200 | 1 | N/A | 17372122 bytes | 2498 ms |
| IEX | iex_dam | `/developer/v1/market/iex/latest?market_type=DAM` | X-API-Key | SUCCESS | 200 | 10 | 2026-07-16T18:15:00+00:00 | 4169 bytes | 1717 ms |
| IEX | iex_rtm | `/developer/v1/market/iex/latest?market_type=RTM` | X-API-Key | SUCCESS | 200 | 10 | 2026-07-16T18:15:00+00:00 | 4169 bytes | 1712 ms |
| IEX | iex_gdam | `/api/intelligence/iex-green-market` | Bearer | SUCCESS | 200 | 1 | N/A | 6241 bytes | 1549 ms |
| MARKET | energy_investments | `/api/intelligence/energy-investments` | Bearer | SUCCESS | 200 | 1 | N/A | 5234 bytes | 1632 ms |
| GENERATION | generation | `/api/intelligence/fuel-mix-timeseries` | Bearer | SUCCESS | 200 | 1 | N/A | 3939564 bytes | 4423 ms |
| CARBON | carbon | `/api/intelligence/carbon-intensity` | Bearer | SUCCESS | 200 | 1 | N/A | 933740 bytes | 6472 ms |
| OPERATIONS | posoco_psp_daily | `/api/intelligence/posoco-psp` | Bearer | SUCCESS | 200 | 1 | N/A | 571638 bytes | 1144 ms |
| ASSETS | power_plants | `/api/intelligence/power-plants` | Bearer | SUCCESS | 200 | 1 | N/A | 4449 bytes | 781 ms |
| ASSETS | transmission_lines | `/api/edges` | Bearer | SUCCESS | 200 | 1 | N/A | 19471 bytes | 1177 ms |
| ASSETS | substations | `/api/nodes` | Bearer | SUCCESS | 200 | 1 | N/A | 6419 bytes | 1616 ms |
