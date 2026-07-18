# GridSense AI: Component Inventory

This document serves as the master inventory of all UI components required to build GridSense AI. It acts as the definitive punch-list for Frontend Engineering (Sprint 7), categorizing components by their functional domain and Atomic Design level.

---

## 1. Primitives (Atoms)
The foundational building blocks with zero business logic.

### 1.1 Button
- **Atomic Level**: Atom
- **Purpose**: Triggers user actions or navigational events.
- **Dependencies**: None.
- **Reusable**: Yes (Universal).
- **Props**: `variant` (primary/secondary/ghost), `size`, `isDisabled`, `isLoading`, `leftIcon`, `rightIcon`.
- **Events**: `onClick`, `onFocus`, `onBlur`.
- **Responsive Behaviour**: Adapts padding based on breakpoints; can optionally span 100% width on mobile.
- **Accessibility**: Requires `aria-label` if icon-only. Focus ring standard.
- **Future Extension**: Adding new brand variants.
- **Implementation Priority**: High (Sprint 7.3).
- **Used In**: Globally everywhere.
- **Backend Dependency**: None.
- **Estimated Complexity**: Low.

### 1.2 Badge
- **Atomic Level**: Atom
- **Purpose**: Displays status indicators or read-only tags.
- **Dependencies**: None.
- **Reusable**: Yes (Universal).
- **Props**: `intent` (success/warning/error/info), `label`, `isPulsing`.
- **Events**: None.
- **Responsive Behaviour**: Font size scales down slightly on mobile.
- **Accessibility**: Must have sufficient color contrast.
- **Future Extension**: New domain-specific intents (e.g., `intent="battery"`).
- **Implementation Priority**: High (Sprint 7.3).
- **Used In**: Metric Cards, Tables, Map Popups.
- **Backend Dependency**: None.
- **Estimated Complexity**: Low.

---

## 2. Navigation (Molecules & Organisms)
Components that dictate movement through the platform.

### 2.1 GlobalSidebar
- **Atomic Level**: Organism
- **Purpose**: Persistent workspace switching and user settings access.
- **Dependencies**: `Button`, `Icon`, Auth Context.
- **Reusable**: Yes (Shell level only).
- **Props**: `activeWorkspace`, `isCollapsed`.
- **Events**: `onNavigate`, `onToggleCollapse`.
- **Responsive Behaviour**: Hides completely behind a hamburger menu on mobile/tablet.
- **Accessibility**: Tab-navigable. Uses `nav` HTML5 tag.
- **Future Extension**: Dynamic injection of new Workspace routes via a registry.
- **Implementation Priority**: High (Sprint 7.2).
- **Used In**: App Shell.
- **Backend Dependency**: Depends on User Roles (Permissions).
- **Estimated Complexity**: Medium.

### 2.2 CommandPalette
- **Atomic Level**: Organism
- **Purpose**: Global fuzzy search and deep linking via keyboard.
- **Dependencies**: `Input`, API Client.
- **Reusable**: Yes (Shell level only).
- **Props**: `isOpen`.
- **Events**: `onClose`, `onResultSelect`.
- **Responsive Behaviour**: Becomes a full-screen modal on mobile.
- **Accessibility**: Esc key to dismiss, Arrow keys to navigate results.
- **Future Extension**: Integrating natural language LLM search.
- **Implementation Priority**: Medium.
- **Used In**: App Shell.
- **Backend Dependency**: `GET /api/v1/search/universal`.
- **Estimated Complexity**: High.

---

## 3. Composites (Molecules & Organisms)
Business-aware UI components.

### 3.1 MetricCard
- **Atomic Level**: Molecule
- **Purpose**: Displays a single, high-level KPI (e.g., Total Grid Load).
- **Dependencies**: `Badge`, `SparklineChart` (optional).
- **Reusable**: Yes.
- **Props**: `title`, `value`, `unit`, `trend` (+/-%), `trendDirection`.
- **Events**: `onClick` (optional drill-down).
- **Responsive Behaviour**: Stacks vertically on small screens.
- **Accessibility**: `aria-label` combines title, value, and trend for screen readers.
- **Future Extension**: Adding nested AI confidence intervals.
- **Implementation Priority**: High (Sprint 7.4).
- **Used In**: Executive Dashboard, Grid Operations.
- **Backend Dependency**: Assorted `/dashboard` endpoints.
- **Estimated Complexity**: Low.

---

## 4. Charts (Organisms)
Complex data visualizations.

### 4.1 TimeseriesChart
- **Atomic Level**: Organism
- **Purpose**: Plotting historical or forecasted data against time.
- **Dependencies**: Third-party charting library (e.g., Recharts/ECharts), `ChartTooltip`.
- **Reusable**: Yes.
- **Props**: `data` (Array), `xKey`, `yKeys` (Array), `colors`, `showConfidenceInterval`.
- **Events**: `onHover`, `onZoom`.
- **Responsive Behaviour**: Scales width 100%; rotates X-axis labels if cramped.
- **Accessibility**: Includes a visually hidden HTML table mirroring the chart data for screen readers.
- **Future Extension**: Adding draggable prediction nodes.
- **Implementation Priority**: High (Sprint 7.4).
- **Used In**: Market Intelligence, Forecasting.
- **Backend Dependency**: Any Timeseries API.
- **Estimated Complexity**: High.

---

## 5. Maps (Organisms)
GIS and Spatial components.

### 5.1 BaseGISMap
- **Atomic Level**: Organism
- **Purpose**: The interactive national grid map.
- **Dependencies**: Third-party map engine (e.g., Mapbox/Leaflet).
- **Reusable**: Yes.
- **Props**: `centerCoordinates`, `zoomLevel`, `activeLayers`.
- **Events**: `onPan`, `onZoom`, `onFeatureClick`.
- **Responsive Behaviour**: Takes 100% of parent container. Touch-friendly pan/zoom on mobile.
- **Accessibility**: Keyboard panning controls; `aria-labels` on controls.
- **Future Extension**: 3D Digital Twin rendering.
- **Implementation Priority**: High (Sprint 7.5).
- **Used In**: Grid Operations, Renewable Intelligence.
- **Backend Dependency**: Map tile server, GeoJSON API endpoints.
- **Estimated Complexity**: Very High.

---

## 6. AI (Organisms)
Intelligent platform integrations.

### 6.1 AIInsightPanel
- **Atomic Level**: Molecule
- **Purpose**: Explains anomalies or chart peaks in plain text.
- **Dependencies**: `Icon`, `Button`.
- **Reusable**: Yes.
- **Props**: `context` (String), `isGenerating` (Boolean), `confidenceScore`.
- **Events**: `onThumbsUp`, `onThumbsDown` (Feedback loop).
- **Responsive Behaviour**: Shrinks text slightly on mobile.
- **Accessibility**: Auto-announces when generation completes via `aria-live`.
- **Future Extension**: Transition into a fully interactive voice copilot.
- **Implementation Priority**: Medium (Sprint 7.6).
- **Used In**: Executive Workspace, Market Intelligence.
- **Backend Dependency**: OpenAI / internal LLM API wrapper.
- **Estimated Complexity**: Medium.

---

## 7. Tables (Organisms)
High-density data grids.

### 7.1 VirtualizedDataTable
- **Atomic Level**: Organism
- **Purpose**: Rendering thousands of rows (e.g., Power Plant lists) without lag.
- **Dependencies**: Table primitives, Virtualization library.
- **Reusable**: Yes.
- **Props**: `columns`, `data`, `isLoading`, `totalRows`, `paginationState`.
- **Events**: `onSort`, `onRowClick`, `onPageChange`.
- **Responsive Behaviour**: Enables horizontal scroll; pins the first column.
- **Accessibility**: Standard `table`, `th`, `tr`, `td` semantic tags despite virtualization.
- **Future Extension**: Inline cell editing for Admin data entry.
- **Implementation Priority**: High (Sprint 7.7).
- **Used In**: All workspaces.
- **Backend Dependency**: Any paginated API endpoint.
- **Estimated Complexity**: High.

---

## 8. Forms (Molecules & Organisms)
Data entry and configuration.

### 8.1 DateRangePicker
- **Atomic Level**: Molecule
- **Purpose**: Selecting historical timeframes for analytics.
- **Dependencies**: `Input`, Calendar library.
- **Reusable**: Yes.
- **Props**: `startDate`, `endDate`, `minDate`, `maxDate`.
- **Events**: `onChange`.
- **Responsive Behaviour**: Calendar popover switches to a full-screen modal on mobile.
- **Accessibility**: Keyboard navigability for calendar days.
- **Future Extension**: NLP input (e.g., typing "Last Tuesday").
- **Implementation Priority**: High.
- **Used In**: Market Intelligence, Forecasting, Analytics.
- **Backend Dependency**: None.
- **Estimated Complexity**: Medium.

---

## 9. Layouts (Templates)
Structural wireframes defining page composition.

### 9.1 DashboardLayout
- **Atomic Level**: Template
- **Purpose**: Standard grid for KPI metrics and charts.
- **Dependencies**: None.
- **Reusable**: Yes.
- **Props**: `children` (React Nodes).
- **Events**: None.
- **Responsive Behaviour**: Reflows from 4-columns (Desktop) to 1-column (Mobile).
- **Accessibility**: Maintains logical source order.
- **Future Extension**: Drag-and-drop customization.
- **Implementation Priority**: High (Sprint 7.2).
- **Used In**: Executive, Grid, Market workspaces.
- **Backend Dependency**: None.
- **Estimated Complexity**: Low.
