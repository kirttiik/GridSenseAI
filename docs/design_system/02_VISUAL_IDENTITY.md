# GridSense AI: Visual Identity

This document defines the foundational visual identity for GridSense AI. As an enterprise-grade platform for the energy industry, the visual language prioritizes clarity, performance, and trust, establishing a sophisticated environment for complex analysis and real-time operations.

---

## 1. Brand Personality

GridSense AI’s brand personality is the compass for all visual decisions. The platform must feel like an indispensable tool for national infrastructure, balancing technical rigor with modern elegance.

- **Authoritative & Trustworthy**: GridSense AI deals with national grid stability and high-stakes market trades. The UI must exude absolute reliability.
- **Intelligently Minimal**: The platform processes billions of data points, but the interface remains uncluttered. Complexity is handled under the hood; the surface is calm and focused.
- **Precision-Driven**: Analytics are sharp and exact. Visual elements avoid "fluff" in favor of crisp lines, high-legibility fonts, and mathematically precise spacing.
- **Modern & Premium**: Taking cues from high-end fintech and modern dev-tools, the platform feels expensive, responsive, and a generation ahead of legacy energy SCADA systems.

---

## 2. Brand Principles

Our visual execution is guided by the following principles:

1. **Information Before Aesthetics**: Visual flair must never compromise data legibility. A chart’s accuracy is more important than its gradient.
2. **Clarity Over Decoration**: Avoid unnecessary borders, backgrounds, and drop shadows. Use whitespace as the primary structural element.
3. **Purposeful Motion**: Animation is a functional tool used to explain state changes (e.g., expanding a row, loading a dataset), not for pure decoration.
4. **Absolute Consistency**: A button in the AI Studio must look, feel, and react identically to a button in the Grid Operations workspace.
5. **Universal Scalability**: The design tokens must scale from a 13-inch laptop screen to a 60-inch operations center monitor seamlessly.
6. **Accessible by Default**: Color contrast, font sizing, and focus states are not afterthoughts; they are baked into the core design tokens.

---

## 3. Logo Guidelines

The GridSense AI logo is the anchor of the brand.

- **Logo Philosophy**: The logo should be a minimalist abstraction representing convergence—data streams (lines/nodes) coming together to form intelligence (a spark/geometric core).
- **Logo Usage**: Used primarily in the top-left of the application shell, loading screens, and generated report headers.
- **Safe Spacing**: The logo must always have a safe area equal to 50% of its own height to ensure it breathes and remains distinct.
- **Minimum Size**: 24px height for digital screens; 16px height for favicons.
- **Dark Mode vs Light Mode**: The logo should have a pure white/light-gray variant for the dark theme and a deep slate/primary-color variant for the light theme.
- **Incorrect Usage**: Do not stretch, skew, or apply drop shadows to the logo. Do not place the dark-mode logo on a light background.
- **Future Scalability**: The logo mark should be identifiable even if the "GridSense AI" text is hidden (e.g., collapsed sidebars).

---

## 4. Color System

GridSense AI uses a tokenized, semantic color system. Colors are never hardcoded; they are mapped to purposeful design tokens.

### Core Palette
| Token | Purpose | Example Hex (Conceptual) |
|-------|---------|---------------------------|
| `primary` | Call to action, primary active states, branding. | Deep Cobalt Blue (`#0F52BA`) |
| `secondary` | Secondary actions, subtle highlights. | Muted Cyan (`#3E829A`) |
| `neutral` | Typography, standard borders, standard backgrounds. | Slate/Gray Scale (`#1A1D20` to `#F8F9FA`) |

### Background & Surface
| Token | Purpose | Dark Theme | Light Theme |
|-------|---------|------------|-------------|
| `bg-base` | The deepest background layer (app shell). | `#0A0A0B` | `#FAFAFA` |
| `bg-surface` | Cards, panels, and content containers. | `#141517` | `#FFFFFF` |
| `border-subtle` | Dividers, table borders. | `#2A2D31` | `#EAEAEA` |

### Semantic Palette
| Token | Purpose | Usage |
|-------|---------|-------|
| `success` | Positive trends, operational stability. | Emerald Green |
| `warning` | Anomalies, approaching thresholds, maintenance. | Amber/Orange |
| `error` | Grid frequency drops, critical failures, outages. | Crimson Red |
| `info` | System notifications, tooltips. | Bright Blue |

### Domain Accents
Specific domain workspaces use distinct accents to subtly orient the user.
| Domain | Accent Color | Purpose |
|--------|--------------|---------|
| **AI Accent** | Amethyst Purple | Highlighting AI-generated insights or predictions. |
| **Market Accent** | Mint Green | Financial data, day-ahead pricing, trading views. |
| **Renewable Accent** | Sunburst Yellow/Teal | Solar and Wind generation metrics. |
| **Grid Accent** | Electric Blue | Transmission lines, substations, grid frequency. |
| **Carbon Accent** | Forest Green | Emissions data and carbon intensity tracking. |
| **Weather Accent** | Soft Cyan | Temperature, irradiance, and meteorological overlays. |

---

## 5. Theme System

The platform operates on a strict theme token system.

1. **Dark Theme (Primary)**: The default experience. Energy data is complex and operators stare at screens for 8-12 hours a day. Dark mode reduces eye strain and makes bright semantic alerts (like red frequency drops) highly visible.
2. **Light Theme (Secondary)**: Available for users who prefer it, optimized for daylight environments or when generating printable reports.
3. **High Contrast**: A specialized theme strictly adhering to WCAG AAA contrast ratios for visually impaired users.
4. **Theme Switching**: Managed via a context provider at the root level. All UI components read from CSS variables (e.g., `var(--color-bg-surface)`), ensuring zero hardcoded colors.

---

## 6. Typography

Typography in GridSense AI must balance dense data legibility with modern aesthetic appeal.

- **Primary Font (Sans-Serif)**: *Inter* or *Geist Sans*. Used for all UI elements, headings, and standard body text. It is clean, highly legible, and optimized for screen reading.
- **Monospace Font**: *JetBrains Mono* or *Geist Mono*. Used strictly for tabular data, code snippets, AI query outputs, and raw numerical values where vertical alignment (tabular lining) is critical.

### Hierarchy Tokens
| Token | Size | Weight | Usage |
|-------|------|--------|-------|
| `text-h1` | 32px | Semi-Bold | Workspace titles, major report headers. |
| `text-h2` | 24px | Medium | Panel titles, section headers. |
| `text-h3` | 18px | Medium | Card titles, widget headers. |
| `text-body` | 14px | Regular | Standard UI text, descriptions. |
| `text-sm` | 12px | Regular | Metadata, axis labels, tooltips. |
| `text-mono` | 13px | Regular | Tables, KPI values, market tickers. |

### Layout & Legibility
- **Line Heights**: `1.5` for body text to ensure readability; `1.2` for headings to maintain tight groupings.
- **Tabular Figures**: All numbers in tables and dashboards must use `font-variant-numeric: tabular-nums` to prevent horizontal shifting when live data updates.

---

## 7. Iconography

Icons must be strictly functional. They provide instant visual recognition for complex energy concepts.

- **Icon Philosophy**: Minimal, geometric, and consistent. No multi-colored or overly detailed illustrative icons in the core UI.
- **Stroke Thickness**: Standardized to `1.5px` (or `2px` for micro-icons). 
- **Style**: Outline style for default states; Filled style for active/selected states (e.g., active sidebar tabs).
- **Sizes**: `16x16` (inline/metadata), `20x20` (buttons/inputs), `24x24` (navigation).

### Category Standards
- **Grid/Assets**: Transmission towers, substations, transformers.
- **Market**: Candlesticks, currency symbols, trend arrows.
- **Weather**: Clouds, sun, wind vectors.
- **AI**: Sparkles, nodes, neural network abstractions.
- **System**: Cogwheels (Settings), Bells (Notifications), Magnifying Glass (Search).

---

## 8. Spacing System

GridSense AI uses a strict **4px baseline grid**. This ensures mathematical harmony across all components.

| Token | Value | Example Usage |
|-------|-------|---------------|
| `space-1` | 4px | Gap between an icon and text inside a button. |
| `space-2` | 8px | Standard padding inside small inputs/badges. |
| `space-3` | 12px | Spacing between items in a list. |
| `space-4` | 16px | Standard card padding; standard margin. |
| `space-6` | 24px | Spacing between widgets on a dashboard. |
| `space-8` | 32px | Section spacing within a workspace. |
| `space-12` | 48px | Major layout separations (e.g., between the header and content). |

---

## 9. Border Radius

Rounding is used sparingly to soften the UI without making it feel toy-like.

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 4px | Inputs, checkboxes, standard buttons, tooltips. |
| `radius-md` | 8px | Standard cards, charts, dropdown menus. |
| `radius-lg` | 12px | Large dialogs, primary modals, floating command palettes. |
| `radius-full` | 999px | Avatars, notification dots, specific pill badges. |

*Note: Maps and massive data grids often look best with `0px` or `radius-sm` to maximize screen real estate.*

---

## 10. Elevation & Shadows

In a dark-theme primary environment, standard drop shadows often look muddy. Elevation is primarily communicated through background lightness and subtle borders.

- **Level 0 (Flat)**: `bg-base`. The main app background. No shadow.
- **Level 1 (Surface)**: `bg-surface` + 1px subtle border. Used for standard cards, widgets, and charts.
- **Level 2 (Floating)**: `bg-surface-elevated` + subtle border + soft ambient shadow. Used for dropdown menus and popovers.
- **Level 3 (Overlay)**: `bg-surface-elevated` + distinct border + large diffuse shadow. Used for Modals, Dialogs, and the Command Palette.
- **Hover States**: Subtle vertical translation (`transform: translateY(-1px)`) combined with a slight glow or shadow enhancement, providing tactile feedback.

---

## 11. Glassmorphism Usage

Glassmorphism (background blur) is a powerful but easily abused tool. In GridSense AI, it is strictly reserved for ephemeral overlays to maintain spatial context.

**Allowed Usage:**
- **Command Palette**: Blurring the main dashboard ensures the user focuses entirely on search while subconsciously knowing they haven't left the page.
- **Sticky Headers/Navbars**: A subtle backdrop blur on scrolling panels allows data to pass underneath without breaking legibility.
- **Critical AI Alerts**: A floating AI insight panel may use glassmorphism to signify its ephemeral, overlay nature.

**Forbidden Usage:**
- Standard dashboard cards, data tables, or primary buttons.

---

## 12. Visual Language Context

The UI actively communicates the domain it represents:
- **Live Systems (Grid Operations)**: Uses high contrast, stark borders, and pulsing animations for real-time telemetry. The visual language here says "Mission Critical."
- **Enterprise Intelligence (Market/Analytics)**: Uses softer neutral backgrounds, dense typography, and clean data grids. The visual language here says "Analytical Precision."
- **AI (Predictive Overlays)**: Uses subtle gradients and the Amethyst Purple accent to clearly delineate machine-generated predictions from ground-truth historical data.

---

## 13. Accessibility

GridSense AI is an enterprise tool; it must be usable by everyone.

- **Contrast Ratios**: All text and critical UI boundaries must meet WCAG 2.1 AA standards (minimum 4.5:1 for normal text, 3:1 for large text).
- **Color Blindness**: Never use color alone to convey meaning. A red "Error" state must always be accompanied by an error icon or explicit text.
- **Keyboard Navigation**: The entire platform must be navigable via the `Tab` key. Focus rings must be highly visible (e.g., a 2px solid primary-color outline offset by 2px).
- **Responsive Scaling**: Typography must use `rem` units so it scales fluidly if a user increases their browser's default font size.

---

## 14. Future Scalability

The visual identity is designed as a modular token system to support the platform's 5-year vision without redesigns.

When new modules are introduced (e.g., *Green Hydrogen* or *Nuclear*):
1. **No Layout Changes**: The standard card/widget grid system will inherently support new data types.
2. **New Accent Tokens**: We simply introduce a new semantic color token (e.g., `accent-nuclear: #FF00FF`) and map it to the charting libraries.
3. **Iconography Expansion**: Add new 24x24 icons for the new domains using the established `1.5px` stroke guidelines.

The design system is a living platform—built not just for what the Indian Power Sector is today, but for what it will become.
