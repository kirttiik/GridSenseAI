# Endpoint definitions mapped by namespace

ENDPOINTS = {
    "GRID": {
        "grid_frequency": "/api/intelligence/grid-frequency",
        "grid_frequency_15min": "/api/intelligence/grid-frequency?resolution=15m", 
    },
    "DEMAND": {
        "demand_timeseries": "/api/intelligence/demand-timeseries"
    },
    "IEX": {
        "iex_dam": "/developer/v1/market/iex/latest?market_type=DAM",
        "iex_rtm": "/developer/v1/market/iex/latest?market_type=RTM",
        "iex_gdam": "/api/intelligence/iex-green-market"
    },
    "MARKET": {
        "energy_investments": "/api/intelligence/energy-investments"
    },
    "GENERATION": {
        "generation": "/api/intelligence/fuel-mix-timeseries"
    },
    "CARBON": {
        "carbon": "/api/intelligence/carbon-intensity"
    },
    "OPERATIONS": {
        "posoco_psp_daily": "/api/intelligence/posoco-psp",
        "cea_monthly_psp": "/api/intelligence/cea-psp"
    },
    "ASSETS": {
        "power_plants": "/api/intelligence/power-plants",
        "transmission_lines": "/api/edges",
        "substations": "/api/nodes"
    }
}
