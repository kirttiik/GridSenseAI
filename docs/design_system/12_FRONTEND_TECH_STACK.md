# GridSense AI: Frontend Technology Stack & Engineering Decisions

This document finalizes every technology choice for the GridSense AI frontend. It serves as the definitive engineering roadmap for Sprint 7 and beyond. Every selection has been rigorously evaluated against the strict requirements of a high-density, real-time, GIS-heavy enterprise energy intelligence platform.

---

## 1. Framework Decision

### Selected: React + Vite (SPA Architecture)
- **Why**: GridSense AI is a highly interactive, authenticated, behind-the-login enterprise dashboard. Traditional SEO and Server-Side Rendering (SSR) are entirely irrelevant. We require maximum client-side performance, seamless WebSocket integration, and raw WebGL rendering speed for GIS maps.
- **Alternatives Considered**: Next.js (App Router).
- **Disadvantages of Next.js for this use case**: The App Router’s Server Components add massive overhead and complexity for an app that fundamentally requires 95% Client Components (Charts, Maps, Real-time Grids, Zustand stores).
- **Advantages of Vite/React**: Blazing fast HMR, pure client-side routing (React Router), simplified deployment (static NGINX/S3), and zero server-side mental overhead when dealing with heavy `canvas` or WebGL libraries.

---

## 2. Programming Language

### Selected: TypeScript (Strict Mode)
- **Why**: Enterprise applications cannot survive at scale without static typing. TypeScript prevents runtime errors by guaranteeing the shape of the data received from the FastAPI backend.
- **Advantages**: Auto-completion in the IDE, explicit domain modeling (e.g., `PowerPlant`, `MarketBid`), and self-documenting code.
- **Enterprise Benefits**: Allows massive refactoring with confidence. Drastically reduces the cognitive load for onboarding new engineers.

---

## 3. Package Manager

### Selected: pnpm
- **Why**: `pnpm` uses a global content-addressable store and hard links, making it exceptionally fast and incredibly disk-space efficient. It enforces strict dependency resolution, preventing "phantom dependencies" where a package relies on a sub-dependency it didn't explicitly declare.
- **Alternatives**: `npm` (Too slow, bloated `node_modules`), `yarn` (Slightly slower, complex PnP setup).

---

## 4. UI Component Library

### Selected: shadcn/ui + Radix Primitives
- **Why**: `shadcn/ui` is not a traditional npm library. It provides raw, accessible React components that you copy directly into your codebase. This guarantees 100% customization over the styling. It leverages Radix UI for unstyled, WCAG-compliant accessibility primitives (keyboard navigation, focus traps).
- **Alternatives**: 
  - **MUI**: Too heavy, difficult to customize heavily without fighting the framework, poor runtime performance due to CSS-in-JS.
  - **Ant Design**: Heavily opinionated, bloated bundle size, looks like a generic admin panel.
- **Enterprise Suitability**: Supreme. We own the components, meaning future refactoring or design system changes (Sprint 6.9.6) are trivial.

---

## 5. Styling System

### Selected: Tailwind CSS + CSS Variables (Tokens)
- **Why**: Tailwind CSS provides a highly optimized utility-class system that generates near-zero CSS in production. By mapping our Design Tokens to Tailwind (e.g., `bg-surface` mapped to `var(--color-bg-surface)`), we achieve instant dark/light theme switching without JavaScript re-renders.
- **Alternatives**: CSS-in-JS (Emotion/Styled-components) adds runtime overhead which is fatal when rendering 1000-row tables. CSS Modules are too verbose for rapid prototyping.

---

## 6. Icons

### Selected: Lucide React
- **Why**: Clean, consistent 24x24 outline icons. SVG-based, easily styled via Tailwind (`text-primary`), extremely lightweight, and heavily supported by the community (default in `shadcn/ui`).
- **Alternatives**: Material Icons (looks dated), Heroicons (fewer energy-specific icons).

---

## 7. Motion Library

### Selected: Framer Motion
- **Why**: The gold standard for React animation. Supports complex spring physics, shared layout transitions (expanding cards), and effortlessly hooks into `prefers-reduced-motion` for accessibility.
- **Performance**: While heavy, it can be lazy-loaded. Its declarative syntax makes UI orchestration highly readable.

---

## 8. Charting Library

### Selected: Apache ECharts (via `echarts-for-react`)
- **Why**: GridSense AI processes massive datasets (e.g., year-long 15-minute interval market prices). ECharts is built on `ZRender` (Canvas/WebGL), allowing it to render 100,000+ data points smoothly. It supports complex multi-axis syncing, heatmaps, and massive customization.
- **Alternatives**:
  - **Recharts**: Built on SVG. Severe performance lag when rendering >5000 points.
  - **Chart.js**: Difficult to customize advanced tooltips.
  - **Highcharts**: Expensive commercial licensing.

---

## 9. GIS Library

### Selected: MapLibre GL JS (via `react-map-gl`)
- **Why**: MapLibre is an open-source fork of Mapbox GL. It provides phenomenal WebGL vector tile rendering, massive 3D capabilities, and heatmap generation without the exorbitant, restrictive commercial licensing of modern Mapbox.
- **Alternatives**: Leaflet/OpenLayers are CPU-based (Canvas/DOM) and cannot handle rendering thousands of real-time transmission lines smoothly.

---

## 10. Table Library

### Selected: TanStack Table (React Table v8)
- **Why**: A "headless" UI library. It provides intense data-grid logic (sorting, filtering, grouping, virtualization) while outputting zero markup, allowing us to style the table exactly per our Design System.
- **Alternatives**: AG Grid (Powerful, but commercial license required for enterprise features; extremely heavy). Material Table (Tied to MUI).

---

## 11. Data Fetching

### Selected: TanStack Query (React Query)
- **Why**: Handles caching, background updates, stale-while-revalidate logic, retries, and deduplication automatically. Separates "Server State" entirely from "Client State."
- **Alternatives**: SWR (Excellent, but lacks some of the deep mutation/invalidation flexibility of React Query). Redux RTK Query (Too much boilerplate).

---

## 12. Forms & Validation

### Selected: React Hook Form + Zod
- **Why**: React Hook Form relies on uncontrolled components, preventing the entire form from re-rendering on every keystroke. Zod provides flawless, TypeScript-first schema validation.
- **Alternatives**: Formik (Causes excessive re-renders). Yup (Less robust TS inference than Zod).

---

## 13. State Management

### Selected: Zustand
- **Why**: A tiny, un-opinionated, flux-based state manager. Used strictly for "Client Global State" (e.g., Sidebar Open, Active Theme). 
- **Alternatives**: Redux Toolkit (Massive overkill when TanStack Query handles server state). Context API (Causes unnecessary re-renders across the entire provider tree).

---

## 14. Authentication Strategy

- **Strategy**: JWT via standard `Authorization: Bearer` header.
- **Tokens**: Access tokens stored in memory (Zustand) or `Secure/HttpOnly` cookies depending on exact deployment. 
- **Session Expiry**: Axios interceptor catches 401s, attempts a silent refresh via a `refresh_token`, or wipes the state and forces a login redirect.

---

## 15. API Client

### Selected: Axios
- **Why**: First-class support for interceptors (vital for JWT injection and global error handling). Easy request cancellation (crucial for "Search as you type").
- **Alternatives**: Native `fetch` (Requires too much boilerplate for JSON parsing and interceptor logic).

---

## 16. File Handling

- **CSV/Excel**: Use `Papaparse` for rapid client-side parsing of large datasets. Export via blob generation.
- **PDF**: For dashboard exports, use `html2canvas` + `jsPDF` to snapshot the DOM client-side, offloading server rendering costs.

---

## 17. Search Architecture

- **Command Palette (`cmdk`)**: A headless command menu wrapper that integrates beautifully with React.
- **Debouncing**: Search inputs are debounced locally using a custom `useDebounce` hook (e.g., 300ms) before triggering the TanStack Query API fetch.

---

## 18. Internationalization (i18n)

- **Selected**: `i18next` + `react-i18next`.
- **Numbers/Dates**: Standard `Intl.NumberFormat` and `date-fns` for robust, lightweight timezone and currency formatting.

---

## 19. Performance Strategy

- **Lazy Loading**: `React.lazy()` for route-level code splitting. 
- **Dynamic Imports**: MapLibre and ECharts are only downloaded when the user enters the GIS or Market workspaces.
- **Virtualization**: `@tanstack/react-virtual` used inside tables and long dropdowns to only render visible DOM nodes.

---

## 20. Testing Strategy

### Selected Stack: Vitest + React Testing Library + Playwright
- **Vitest**: Blazing fast, ESM-native unit testing runner that shares configuration with Vite.
- **React Testing Library**: For testing component interaction rather than implementation.
- **Playwright**: Supreme E2E testing for complex GIS and Dashboard user flows. Vastly superior to Cypress in handling multiple tabs and WebKit consistency.

---

## 21. Code Quality

- **ESLint + Prettier**: Standard syntax validation and automatic formatting.
- **Husky + lint-staged**: Pre-commit hooks to ensure no bad code is pushed.
- **Commitlint**: Enforces Conventional Commits (`feat:`, `fix:`) for automated changelog generation.

---

## 22. Monitoring

- **Error Tracking**: Sentry (Catches unhandled exceptions, provides stack traces mapped to source maps).
- **Analytics**: PostHog (Privacy-friendly, open-source capable product analytics).

---

## 23. Deployment

- **Frontend Hosting**: Vercel or AWS S3/CloudFront. (Static SPA distribution).
- **CI/CD**: GitHub Actions. On push to `main`: runs Vitest, builds Vite bundle, and syncs to CDN.
- **Preview Deployments**: PRs automatically generate ephemeral preview URLs for UX review.

---

## 24. Dependency Matrix

| Technology | Purpose | Depends On | Alternative |
|------------|---------|------------|-------------|
| **Vite** | Build Tool | Node.js | Webpack (Too slow) |
| **React 18** | UI Framework | None | Vue (Not preferred) |
| **shadcn/ui**| Components | Radix UI, Tailwind | MUI (Too heavy) |
| **TanStack Query**| Server State | Axios | SWR (Less features) |
| **Zustand** | Client State | React | Redux (Too verbose) |
| **ECharts** | Analytics | WebGL/Canvas | Recharts (Slow on large data) |
| **MapLibre** | GIS Maps | WebGL | Leaflet (CPU bound) |

---

## 25. Final Recommended Stack (GridSense AI)

| Domain | Selected Technology |
|--------|---------------------|
| **Framework** | React 18 (SPA) |
| **Build Tool** | Vite |
| **Language** | TypeScript |
| **UI Library** | shadcn/ui + Radix UI |
| **Styling** | Tailwind CSS + Native CSS Variables |
| **Icons** | Lucide React |
| **Charts** | Apache ECharts |
| **GIS Mapping** | MapLibre GL JS |
| **Tables** | TanStack Table v8 |
| **Forms** | React Hook Form |
| **Validation** | Zod |
| **State Mgt (Server)** | TanStack Query |
| **State Mgt (Client)** | Zustand |
| **Data Fetching** | Axios |
| **Animation** | Framer Motion |
| **Testing (Unit)** | Vitest + React Testing Library |
| **Testing (E2E)**| Playwright |
| **Package Manager**| pnpm |
| **Deployment** | Static CDN (Vercel / AWS) |
