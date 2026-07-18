# GridSense AI: Frontend Engineering Standards

This document is the definitive engineering handbook for the GridSense AI frontend codebase. Adherence to these standards is strictly mandatory. Consistency across the codebase ensures that the platform remains endlessly scalable and deeply maintainable as new engineering teams onboard and new energy verticals are launched.

---

## 1. Naming Conventions

### Folder Naming
- Use `kebab-case` for all directories.
- Example: `market-intelligence/`, `shared-components/`, `api-client/`.

### File Naming
- **React Components**: `PascalCase.tsx` (e.g., `MetricCard.tsx`).
- **Hooks**: `camelCase.ts` (e.g., `useMarketData.ts`).
- **Utilities/Helpers**: `camelCase.ts` (e.g., `formatDate.ts`).
- **Constants**: `SCREAMING_SNAKE_CASE.ts` (e.g., `API_ENDPOINTS.ts`).
- **Types/Interfaces**: `PascalCase.types.ts` (e.g., `PowerPlant.types.ts`).

### Component Naming
- Components must be named with a noun representing their domain.
- Use `PascalCase`.
- Example: `<AssetDashboard />`, `<FrequencyGauge />`.

### Hook Naming
- Always prefix with `use`.
- Example: `useAuthSession()`, `useGISMapLayers()`.

### Context Naming
- Suffix with `Context`.
- Example: `ThemeContext`, `WorkspaceContext`.
- Provider components must suffix with `Provider` (e.g., `<ThemeProvider>`).

### Store Naming
- If using atomic state (Zustand/Jotai), prefix with `use` and suffix with `Store`.
- Example: `useSidebarStore()`.

### API Naming
- API request functions must use action verbs (`fetch`, `create`, `update`, `delete`).
- Example: `fetchMarketPrices()`, `createExportJob()`.

---

## 2. Import & Export Rules

### Import Rules
- **Absolute Imports**: Always use absolute paths configured via `tsconfig.json` (e.g., `import { Button } from '@shared/ui/Button'`).
- **Order**: 
  1. External libraries (`react`, `axios`).
  2. Internal absolute imports (`@features/...`).
  3. Relative imports (`./types`).
- Never import from a higher architectural layer (e.g., `shared/` cannot import from `features/`).

### Export Rules
- **Named Exports**: Prefer named exports over default exports to guarantee refactoring consistency. 
  - *Good*: `export const MetricCard = () => {}`
  - *Bad*: `export default MetricCard`
- Default exports are only permitted for dynamically lazy-loaded route pages (e.g., `React.lazy`).

---

## 3. State Management

- **Server State**: Managed exclusively by a data-fetching library (e.g., React Query/SWR). Do NOT store API responses in Redux or `useState`.
- **Client Global State**: Managed via atomic stores (Zustand/Jotai). Keep to an absolute minimum (e.g., Sidebar state, Theme).
- **Local State**: Managed via `useState`/`useReducer`. Prop drilling is permitted for maximum 3 levels deep before switching to Context.

---

## 4. Styling & Animation Rules

- **Styling Rules**:
  - CSS/Tailwind classes must NEVER use hardcoded colors or pixel values.
  - *Good*: `bg-surface text-primary p-4` (mapped to design tokens).
  - *Bad*: `bg-[#1A1D20] text-blue-500 p-[16px]`.
- **Animation Rules**:
  - Prefer CSS transitions for simple hover states.
  - Complex mounting/unmounting animations must use a physics-based animation library respecting the `prefers-reduced-motion` OS media query.

---

## 5. Error Handling & Logging

- **Error Boundaries**: Every independent widget must be wrapped in an Error Boundary to prevent localized crashes from breaking the global dashboard.
- **API Errors**: Caught at the interceptor level. Translate technical errors into user-friendly localized messages.
- **Logging**: Do not use `console.log()` in production. Use a dedicated logger utility (e.g., `Logger.warn()`) that pipes to an external observability platform.

---

## 6. Testing

- **Unit Tests**: Business logic and formatting utilities must have 100% test coverage.
- **Component Tests**: Use React Testing Library. Test user behavior (e.g., clicking a button), not implementation details.
- **E2E Tests**: Critical workflows (Authentication, Report Export) must be covered by Cypress/Playwright.

---

## 7. Accessibility (a11y) & Internationalization (i18n)

- **Accessibility**: 
  - All interactive elements must be keyboard navigable (`Tab`).
  - Strict adherence to WCAG 2.1 AA color contrast.
  - `aria-labels` must be provided for icon-only buttons.
- **Internationalization**: 
  - No hardcoded English strings in JSX.
  - Use an `i18n` translation hook: `<p>{t('dashboard.title')}</p>`.
  - Date and currency formatting must be locale-aware.

---

## 8. Performance & SEO

- **Performance**:
  - Virtualize any list/table exceeding 100 DOM nodes.
  - Use `React.memo` only when profiling dictates a heavy re-render penalty.
  - Heavy chart and map libraries must be aggressively code-split.
- **SEO**:
  - GridSense AI is a private enterprise platform; traditional SEO is not a priority. However, dynamic `<title>` tags must be updated per route (e.g., `Grid Operations | GridSense AI`) for browser tab legibility and bookmarking.

---

## 9. Source Control Strategy

### Branch Strategy
- `main`: The production-ready source of truth.
- `staging`: The pre-production environment.
- `feat/feature-name`: For new features.
- `fix/bug-name`: For bug fixes.
- `chore/task-name`: For dependency updates or configuration changes.

### Git Commit Convention (Conventional Commits)
- `feat: add AI forecast panel`
- `fix: resolve mapping loop in market charts`
- `docs: update visual identity markdown`
- `refactor: extract date logic to shared utility`

---

## 10. Code Review Checklist

Before approving a PR, reviewers must verify:
- [ ] No hardcoded tokens/colors/strings.
- [ ] Feature-Sliced Architecture boundaries are respected (no circular imports).
- [ ] Complex components are wrapped in Error Boundaries.
- [ ] A11y standards (keyboard navigation, `aria-labels`) are met.
- [ ] Unit tests are written for new utilities.
- [ ] Production build succeeds without TypeScript/Linter errors.

---

## 11. Definition of Done (DoD)

A task is officially "Done" when:
1. Code meets all standards outlined in this document.
2. PR is approved by at least one Senior Engineer.
3. Automated CI/CD pipelines (Lint, Test, Build) pass.
4. The feature is verified in the Staging environment.
5. All relevant Design System markdown documentation is updated if a new primitive was created.

---

## 12. Documentation & Refactoring Rules

- **Documentation Standards**: Complex algorithms and API mappings must include JSDoc comments. Standard UI components should be self-documenting through clean typing.
- **Refactoring Rules**: The "Boy Scout Rule" applies—leave the codebase cleaner than you found it. If you touch a file with legacy technical debt, refactor it to meet current standards.

---

## 13. Future Module Rules

When initializing a new module (e.g., *Green Hydrogen*):
1. **Never mutate core shared files**: Drop the new module directly into the `/features` or `/widgets` directory.
2. **Dynamic Registration**: The module must register itself to the navigation shell via the plugin registry, rather than hardcoding its route into the global `App.tsx`.
3. **Decoupled Deployment**: Future modules must be built in a way that supports Micro-Frontend architecture if the platform scales beyond a single monolithic repository.
