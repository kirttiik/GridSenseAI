# UI/UX Design Document (UI_UX.md)
**Project:** GridSense-AI

## 1. Design Philosophy
GridSense-AI follows these core design principles:
- **Modern SaaS Interface:** Clean, professional, and visually engaging.
- **Data-First Experience:** The data, charts, and maps are the heroes of the page.
- **Minimal Visual Clutter:** Strategic use of whitespace and contrast to avoid overwhelming the user.
- **Responsive Layout:** Fluid designs adapting to different screen sizes.
- **Dark Mode by Default:** Reduces eye strain for analysts looking at glowing screens and enhances the visual pop of data charts.
- **Desktop-First, Mobile-Friendly:** Optimized for large analytical displays, but accessible on smaller devices.

## 2. Color Palette
Our color system is built around a sleek dark mode aesthetic with vibrant data accents.

| Role | Color | Hex Code |
| :--- | :--- | :--- |
| **Primary** | Electric Blue | `#2563EB` |
| **Success** | Emerald | `#16A34A` |
| **Warning** | Amber | `#F59E0B` |
| **Danger** | Rose | `#DC2626` |
| **Background** | Slate 900 | `#0F172A` |
| **Surface** | Slate 800 | `#1E293B` |
| **Text (Primary)** | Slate 50 | `#F8FAFC` |
| **Text (Muted)** | Slate 400 | `#94A3B8` |

## 3. Typography
- **Font Family:** `Inter` (Sans-serif) for all UI text, enabling excellent readability at small sizes and data-dense tables.
- **Heading Sizes:**
  - `H1`: 32px / 40px line-height (bold)
  - `H2`: 24px / 32px line-height (semibold)
  - `H3`: 20px / 28px line-height (semibold)
- **Body Text:** 14px / 20px line-height (regular)
- **Button Text:** 14px (medium)

## 4. Navigation
**Sidebar Structure:**
- GridSense AI (Brand/Home)
  - Dashboard
  - India Map
  - States
  - Power Plants
  - Transmission
  - Demand
  - Generation
  - Grid Intelligence
  - Market
  - Carbon
  - Investments
  - Reports
  - Settings

## 5. Page Hierarchy
The platform enables users to drill down from a macro view to micro details:
```text
Dashboard (National Overview)
        ↓
    India Map
        ↓
 State Profile (e.g., Gujarat)
        ↓
  Power Plant Profile
```

## 6. Dashboard Layout
The primary view when a user logs in.
```text
Header (Search, User Profile, Global Filters)
        ↓
KPI Cards (Total Cap, Current Demand, Carbon Intensity, Grid Freq)
        ↓
India Map (Interactive Geospatial View - Top half)
        ↓
Demand vs Generation (Dual Line Chart - Bottom left)
        ↓
Market Overview (DAM/RTM Prices - Bottom center)
        ↓
Carbon & Renewables Share (Donut Chart - Bottom right)
        ↓
Latest Updates / Audit Feed (Ticker)
```

## 7. Every Page

### Dashboard
- **Purpose:** Provide an at-a-glance summary of India's current energy status.
- **Components:** KPI Grid, Map Preview, Chart Containers.
- **Charts:** Line (Demand), Donut (Fuel Mix).
- **Tables:** Market Summary snippet.
- **Filters:** Date Range, Time Resolution.

### India Map
- **Purpose:** Interactive GIS explorer for national energy assets.
- **Map Layers:** Transmission Lines, Power Plants (clustered), Substations, District Boundaries.
- **Filters:** By Fuel Type (Solar/Wind), Status (Operational/Planned).
- **Search:** Autocomplete search for specific assets.

### States
- **Purpose:** Detailed profile for each Indian State.
- **Charts:** State Demand Curve, Emissions Trend.
- **Tables:** Top 10 Power Plants by capacity in the state.
- **Filters:** State Selector dropdown, Year selector.

### Power Plants
- **Purpose:** Explore utility-scale generation assets.
- **Table:** Paginated, sortable list of all plants.
- **Map:** Mini-map showing the specific plant location on row click.
- **Filters:** Fuel Type, Capacity Range, State.
- **Details Panel:** Slide-out drawer showing plant capacity, owner, and generation history.

### Market
- **Purpose:** Analyze IEX power prices.
- **Charts:** Candlestick or Line charts for MCP (Market Clearing Price).
- **Tables:** Order book summary (Bid vs Offer volumes).
- **Filters:** DAM vs RTM vs GDAM, Region selector.

### Carbon
- **Purpose:** Track grid emissions.
- **Charts:** Area chart of gCO2/kWh over time.
- **Map:** Heat map layer of emissions by state.
- **Filters:** Date range.

## 8. Reusable Components
A unified design system using Tailwind CSS and `shadcn/ui`.
- **Navbar:** Top bar with breadcrumbs and user menu.
- **Sidebar:** Collapsible left navigation.
- **Footer:** Links and version info.
- **Card:** Container for charts and grouped data.
- **Table:** Sortable, filterable, paginated data grids.
- **Chart:** Wrapper for Apache ECharts.
- **Filter Panel:** Global filters (Date, Region).
- **Search Box:** Autocomplete enabled.
- **Pagination:** For large tables.
- **Modal:** For detailed forms or alerts.
- **Toast:** Non-blocking notifications (e.g., "Data exported").
- **Loader:** Skeleton loaders for components waiting on API calls.
- **Map Legend:** Overlays for the Leaflet map.

## 9. Charts
Visualizations built using Apache ECharts:
- **Line Chart:** Demand, Frequency, Prices.
- **Bar Chart:** Installed Capacity by State.
- **Area Chart:** Generation Mix over time.
- **Heat Map:** Market prices across hours/days.
- **Pie / Donut Chart:** Current Renewable vs Conventional share.
- **Treemap:** State-wise energy consumption proportions.
- **Timeline:** Future investment/commissioning schedules.
- **Map:** State boundaries with Choropleth coloring.
- **Gauge:** Real-time grid frequency dial.
- **KPI Card:** Large numeric displays with trend arrows (↑/↓).

## 10. Responsive Behaviour
- **Desktop (1024px+):** Sidebar expanded, complex tables show all columns, dashboard shows 3-column layout.
- **Tablet (768px - 1023px):** Sidebar collapses to icons, 2-column dashboard layout, some table columns hidden behind a "Details" button.
- **Mobile (<768px):** Sidebar becomes a hamburger menu, 1-column layout, maps require explicit touch interaction to scroll over, tables convert to stacked card views.
