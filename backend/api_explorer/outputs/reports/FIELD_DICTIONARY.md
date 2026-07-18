# Field Dictionary

## grid_frequency (GRID)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'timestamp': '2026-07-15T12:58:00+00:00', 'frequ |
| count | int | False | 93 |

## grid_frequency_15min (GRID)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'timestamp': '2026-07-15T12:58:00+00:00', 'frequ |
| count | int | False | 93 |

## demand_timeseries (DEMAND)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'state': 'Gujarat', 'state_slug': 'gujarat', 'la |
| count | int | False | 6 |
| hours | int | False | 48 |
| state_slug | NoneType | True | None |
| mode | str | False | blended |
| resolution | str | False | raw |

## iex_dam (IEX)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| timestamp | str | False | 2026-07-16T18:15:00+00:00 |
| market_type | str | False | DAM |
| region | str | False | All India |
| purchase_bid_mw | str | False | 50831.000 |
| sell_bid_mw | str | False | 1807.500 |
| mcv_mw | str | False | 1800.700 |
| mcp_rs_mwh | str | False | 10000.000 |
| source | str | False | iex_dam_snapshot |
| collected_at | str | False | 2026-07-15T12:30:00.044151+00:00 |

## iex_rtm (IEX)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| timestamp | str | False | 2026-07-16T18:15:00+00:00 |
| market_type | str | False | DAM |
| region | str | False | All India |
| purchase_bid_mw | str | False | 50831.000 |
| sell_bid_mw | str | False | 1807.500 |
| mcv_mw | str | False | 1800.700 |
| mcp_rs_mwh | str | False | 10000.000 |
| source | str | False | iex_dam_snapshot |
| collected_at | str | False | 2026-07-15T12:30:00.044151+00:00 |

## iex_gdam (IEX)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| gdam | dict | False | {'items': [{'timestamp': '2026-06-16T13:00:00+00:0 |
| gtam | dict | False | {'items': [{'timestamp': '2026-06-16T13:00:00+00:0 |
| rec | dict | False | {'items': [{'session_date': '2026-07-08', 'rec_typ |
| green_premium | dict | False | {'gdam_avg_mcp': 6332.15, 'dam_avg_mcp': 5061.24,  |

## energy_investments (MARKET)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'company': 'Aditya Birla Sun Life Frontline Equi |
| count | int | False | 10 |

## generation (GENERATION)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'state': 'Andaman and Nicobar Islands', 'state_s |
| count | int | False | 36 |
| hours | int | False | 48 |
| state_slug | NoneType | True | None |
| view | str | False | production |
| sources | list | False | ['modeled_state_fuel_mix_v2', 'modeled_state_fuel_ |
| sanity | dict | False | {'buckets_seen': 1664, 'buckets_clamped': 250, 'st |

## carbon (CARBON)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'timestamp': '2026-07-14T13:00:00+00:00', 'state |
| count | int | False | 1906 |
| hours | int | False | 48 |
| state_slug | NoneType | True | None |
| states | list | False | ['andaman-and-nicobar-islands', 'andaman-nicobar', |
| unit | str | False | gCO2/kWh |
| granularity | str | False | hourly |
| emission_factors_basis | str | False | lifecycle |
| include_rooftop_solar | bool | False | False |
| tables | dict | False | {'fuel_mix': {'latest_measured_at': '2026-07-16T12 |
| latest_measured_at | str | False | 2026-07-16T12:00:00+00:00 |
| freshness_lag_hours | float | False | 0.89 |
| canonical_row_count | int | False | 7657899 |
| provenance | dict | False | {'data_source': 'modelled', 'model': 'modeled_stat |

## posoco_psp_daily (OPERATIONS)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'date': '2026-07-04', 'region': None, 'state': N |
| count | int | False | 1248 |
| days | int | False | 30 |
| scope | str | False | any |

## power_plants (ASSETS)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'id': 'b02ccb90-9db4-4c6a-a67b-a1be58c0e97e', 'p |
| count | int | False | 10 |
| total | int | False | 278 |
| limit | int | False | 10 |
| offset | int | False | 0 |

## transmission_lines (ASSETS)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'edge_id': 'osm-edge:1000383746', 'name': 'NaN', |
| count | int | False | 10 |
| total | int | False | 39400 |
| limit | int | False | 10 |
| offset | int | False | 0 |

## substations (ASSETS)

| Field Name | Data Type | Nullable | Sample Value |
|---|---|---|---|
| items | list | False | [{'node_id': 'vedas:vedas:substations.7160', 'name |
| count | int | False | 10 |
| total | int | False | 28744 |
| limit | int | False | 10 |
| offset | int | False | 0 |

