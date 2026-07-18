# GridSense AI: Frontend Architecture

This document defines the rigorous structural architecture for the GridSense AI frontend. To manage the immense complexity of an enterprise Energy Intelligence Platform, the codebase strictly enforces a **Feature-Sliced Design** methodology. This prevents domain coupling, ensures infinite scalability, and allows independent teams to build new vertical modules without breaking core platform stability.

---

## 1. Folder Structure

The repository is divided into isolated, hierarchical layers. A lower layer can never import from a higher layer.

```text
src/
├── app/             # Application shell, global providers, routing logic
├── pages/           # Compositional route components
├── widgets/         # Complex, standalone UI blocks (e.g., Header, Dashboard)
├── features/        # User interactions and business workflows (e.g., ExportReport)
├── entities/        # Business entities (e.g., PowerPlant, User, MarketBid)
└── shared/          # Reusable primitives, tokens, and infrastructural code
```

---

## 2. Feature-Based Architecture (The Layers)

### 3. Shared Layer
**Rule**: Absolutely no business logic.
Contains pure UI primitives (Buttons, Inputs), design tokens, global utility functions (date formatters), and generic infrastructural wrappers (API client).

### 4. Entity Layer
**Rule**: Represents domain knowledge, but possesses no interactive workflows.
Contains the structural definition of business objects (e.g., a `PowerPlantCard` UI component, `useMarketPrices` data hook). It knows what a "Power Plant" looks like, but doesn't know how to export it or edit it.

### 5. Feature Layer
**Rule**: User actions that mutate state or trigger business workflows.
Contains the interactive slice of a domain. For example, `EditPowerPlantForm`, `AcknowledgeGridAlert`, or `ExportMarketData`. A feature consumes entities.

### 6. Widget Layer
**Rule**: Standalone layout blocks combining features and entities.
Examples include `GlobalSidebar`, `MarketPricingDashboard`, or `OutageMap`. Widgets are highly decoupled and can be dropped onto any page.

### 7. Page Layer
**Rule**: Zero UI logic. Only composition.
A page simply imports Widgets and Layouts and maps them to a specific route URL.

### 8. Layout Layer
**Rule**: Structural wireframes.
Defines responsive structural grids (e.g., `MasterDetailLayout`, `SplitScreenLayout`) where Widgets are injected as children.

### 9. App Layer
**Rule**: Global initialization.
Contains the root routing provider, theme provider, authentication wrapper, and global error boundaries.

---

## 10. Routing Architecture

Routing is declarative and nested.
- **Root**: `/*` (Wrapped in Auth Check).
- **Workspaces**: `/:workspaceId/*` (e.g., `/market/prices`).
- **Context Preservation**: Navigating within a workspace changes the child content but preserves the parent layout (Sidebar, Header, Map state).
- **Deep Linking**: Every modal, drawer, or specific asset state must be reflected in the URL (e.g., `/grid/outages?assetId=123&panel=history`) so views can be bookmarked and shared.

---

## 11. State Management Strategy

State is strictly divided into three domains to prevent UI lag and synchronization bugs:

1. **Server State (Async)**: Managed via a dedicated fetching/caching library. Data fetched from the REST API (e.g., Market Prices) is cached globally, automatically deduplicated, and background-refreshed.
2. **Client Global State (Sync)**: Minimal footprint. Managed via atomic stores. Contains only UI states that cross widget boundaries (e.g., `isSidebarCollapsed`, `activeTheme`).
3. **Local Component State**: Managed within the specific component. Transient states like an open dropdown menu or a typed search query.

---

## 12. API Layer

The frontend communicates with the backend exclusively through a centralized API Client wrapper.
- **Interceptors**: Automatically attach the JWT `Authorization` header to every outgoing request.
- **Response Parsing**: Translates snake_case backend JSON to camelCase frontend objects.
- **Centralized Definition**: Endpoints are defined in a single registry, grouped by Entity, ensuring URLs are not hardcoded randomly across components.

---

## 13. Authentication Layer

- **Token Lifecycle**: The frontend stores JWTs securely.
- **Refresh Strategy**: The API Client interceptor catches `401 Unauthorized` errors, automatically pauses pending requests, calls the `/refresh` endpoint, and replays the original requests without disrupting the user experience.
- **Session Termination**: Forced logouts instantly wipe the Global Client State and Server State cache to prevent data leaks.

---

## 14. Permission Layer

Permissions dictate UI presence (Attribute-Based Access Control).
- **Guarded Components**: A wrapper component (`<RequirePermission action="export" resource="market">`) surrounds sensitive UI elements (like export buttons). If the user lacks permission, the element is excluded from the DOM.
- **Route Guards**: Users navigating to unauthorized URLs are intercepted and redirected to a `403 Forbidden` standard view.

---

## 15. Theme Layer

- **CSS Variables**: Themes are purely driven by CSS variables bound to the `:root` pseudo-class.
- **Context Provider**: A global ThemeProvider listens to OS preferences (`prefers-color-scheme`) but allows manual override (Light/Dark/High Contrast).
- **Switching Mechanism**: Toggling the theme instantly rewrites the CSS variables, causing the entire UI (and SVG-based charts) to repaint without a page reload.

---

## 16. Localization & Configuration Layers

- **Localization Layer**: All static text is routed through an `i18n` localization dictionary. Dates, times, and currencies are processed through standardized utility formatters to respect the user's Locale and Timezone.
- **Configuration Layer**: Environment variables (`API_BASE_URL`, `FEATURE_FLAGS`) are validated at app startup. Invalid configurations halt the boot process and display a fatal system error.

---

## 17. Plugin Architecture

GridSense AI supports dynamic, isolated modules.
- **Registry Pattern**: Workspaces are not hardcoded into the Sidebar. They register themselves into a central `WorkspaceRegistry` on boot.
- **Future Expansion**: When a "Battery" module is added, the development team drops it into the `features/` directory and adds it to the registry. The Sidebar loop dynamically renders it.

---

## 18. Error Handling & Logging

- **Error Boundaries**: Every Widget is wrapped in a React-agnostic conceptual Error Boundary. If the `MarketChartWidget` crashes, it displays a fallback UI ("Failed to load chart"), but the surrounding Dashboard remains fully operational.
- **Global Catch**: Unhandled promise rejections and fatal rendering errors trigger a full-screen "System Crash" overlay.
- **Logging**: Client-side errors, along with the user's browser details and last 5 navigation events, are batched and sent securely to a frontend logging endpoint.

---

## 19. Analytics

- **Privacy-First**: No intrusive third-party trackers.
- **Event Bus**: User interactions (e.g., "Exported Report", "Changed Map Layer") emit standard JSON objects to an internal Event Bus. This bus aggregates the events and flushes them to the backend API asynchronously.

---

## 20. Performance, Caching & Loading Strategy

- **Virtualization**: Tables and lists with >100 items render only what is visible in the viewport DOM.
- **Caching**: API responses are cached in memory. Navigating away and returning to the "Grid Outages" page pulls instantly from the cache while a background fetch checks for new data.
- **Lazy Loading Strategy**: Entire workspaces are lazy-loaded. When a user first logs in, they download only the Application Shell and their default workspace. The `GIS Map Engine` is only downloaded over the network if they navigate to a map view.
- **Code Splitting**: The bundler is configured to split heavy third-party dependencies (like charting or mapping libraries) into separate chunks.

---

## 21. Asset Management

- **Vector First**: All icons and logos are rendered as inline SVGs, inheriting their fill/stroke colors from the Theme Layer.
- **Static Assets**: Large images or domain illustrations are compressed in modern formats (WebP) and served via a global CDN.

---

## 22. Environment & Deployment Structure

- **Environment Configuration**: The build process consumes `.env` files mapping to `development`, `staging`, and `production`. No secrets are bundled.
- **Deployment Structure**: The frontend compiles to static HTML/JS/CSS assets. It is deployed behind an Edge CDN (Content Delivery Network). The origin server enforces strict security headers (CSP, HSTS) and routes all paths to `index.html` to support client-side routing.
