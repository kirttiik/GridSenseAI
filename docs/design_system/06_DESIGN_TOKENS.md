# GridSense AI: Design Tokens Specification

This document defines the complete Design Tokens Specification for GridSense AI. Design tokens are the absolute source of truth for all visual attributes in the frontend. 

Hardcoded visual values (e.g., `#333333`, `16px`, `0.5s`) are strictly forbidden anywhere in the frontend codebase. Every component, chart, and map must consume these tokens.

---

## 1. Naming Convention

All tokens follow a strict semantic naming structure to ensure readability and predictability:
`[Category] - [Context] - [State/Variant]`

Examples:
- `color-primary-hover`
- `text-size-h1`
- `space-4`
- `z-index-modal`

---

## 2. Color Tokens

Colors are never hardcoded and must map to semantic intents.

| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `color-primary-base` | Main brand and action color. | Primary buttons, active tabs. | Inherits from theme definition. |
| `color-primary-hover` | Hover state for primary actions. | Button hovers. | Auto-generated via color manipulation functions. |
| `color-bg-base` | App shell background. | The lowest layer of the UI. | Adapts to dark/light mode automatically. |
| `color-bg-surface` | Card and panel backgrounds. | Any elevated surface. | Supports nested surfaces (`bg-surface-elevated`). |
| `color-success-base` | Positive state indicators. | Green arrows, "Online" status. | Accessible contrast ratios enforced. |
| `color-error-base` | Critical alerts, failures. | Frequency drops, form errors. | Always paired with an icon for color-blindness. |

---

## 3. Typography Tokens

Typography dictates readability and hierarchical structure.

| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `font-family-sans` | Standard UI text. | Labels, descriptions, buttons. | Points to a system stack if web fonts fail. |
| `font-family-mono` | Data and code. | Metrics, tables, AI queries. | Ensures tabular lining for real-time data flashing. |

### 4. Font Size Tokens
| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `text-size-xs` | Micro metadata. | Tooltips, axis labels. | Responsive scaling based on viewport. |
| `text-size-sm` | Secondary text. | Table headers, secondary descriptions. | Scales smoothly across devices. |
| `text-size-base` | Standard reading text. | Paragraphs, standard buttons. | Base rem size (usually 16px). |
| `text-size-lg` | Highlighted metrics. | Sub-headers, prominent values. | Expandable for ultra-wide displays. |
| `text-size-h1` | Page/Workspace headers. | Only one H1 per view. | Standardized across all workspaces. |

### 5. Font Weight Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `font-weight-regular` | Standard text. | Default weight for all body text. |
| `font-weight-medium` | Emphasis. | Table headers, active tabs, buttons. |
| `font-weight-semibold`| Strong emphasis. | Page headers, Metric card values. |

### 6. Line Height Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `line-height-tight` | Headings. | Keeps multi-line headers cohesive. |
| `line-height-normal` | Body text. | Ensures readable paragraphs. |
| `line-height-loose` | Spaced text. | Specialized data reading contexts. |

### 7. Letter Spacing Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `tracking-tight` | Large headers. | Reduces gaps in massive typography. |
| `tracking-normal` | Standard text. | Default letter spacing. |
| `tracking-wide` | Uppercase labels. | Increases legibility for `text-transform: uppercase`. |

---

## 8. Spacing Tokens

Spacing uses a rigid 4-point grid system.

| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `space-1` (4px) | Micro gaps. | Icon to text inside a button. | Scales proportionally if base grid changes. |
| `space-2` (8px) | Small padding. | Badge padding, small inputs. | Universal multiplier system. |
| `space-4` (16px)| Base padding. | Standard margins, card padding. | Responsive modifiers (`space-4-md`). |
| `space-6` (24px)| Widget gaps. | Dashboard grid spacing. | Standardized dashboard layouts. |
| `space-8` (32px)| Section gaps. | Vertical rhythm between page sections. | Ensures consistent white space. |

---

## 9. Border & Radius Tokens

### Border Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `border-width-1` | Standard lines. | Dividers, normal inputs, cards. |
| `border-width-2` | Emphasized lines. | Focused inputs, active state tabs. |
| `border-color-subtle`| Soft divisions. | Table row separators. |

### 10. Radius Tokens
| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `radius-none` | Sharp edges. | Full-bleed maps, dense data grids. | Modular theme rounding adjustments. |
| `radius-sm` | Subtle softening. | Checkboxes, tooltips, small inputs. | Ensures the UI never feels toy-like. |
| `radius-md` | Standard curves. | Cards, dropdown menus, buttons. | Easily globalized via a single variable. |
| `radius-full` | Circular elements. | Avatars, notification dots. | Independent of physical dimensions. |

---

## 11. Elevation, Shadow & Opacity Tokens

### Elevation Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `elevation-flat` | Base layer. | The app background. |
| `elevation-surface` | Default cards. | Standard content blocks. |
| `elevation-floating` | Popovers. | Dropdowns, tooltips. |
| `elevation-modal` | Dialogs. | Large overlays requiring focus. |

### 12. Shadow Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `shadow-none` | Flat design. | Default for most elements in dark mode. |
| `shadow-sm` | Subtle depth. | Hover states on cards. |
| `shadow-lg` | High floating. | Modals, command palette. |

### 13. Opacity Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `opacity-disabled` | Inactive states. | Disabled buttons, unavailable map layers. |
| `opacity-hover` | Subtle interactions. | Hovering over table rows. |
| `opacity-backdrop` | Modal backgrounds. | Dimming the main app behind a dialog. |

### 14. Blur Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `blur-sm` | Sticky headers. | Let data pass under headers fluidly. |
| `blur-md` | Modals. | Blurs the app background for the command palette. |

---

## 15. Icon, Motion & Layout Tokens

### 16. Icon Size Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `icon-sm` | Inline data. | Icons next to text in tables. |
| `icon-md` | Standard actions. | Button icons, sidebar collapsed icons. |
| `icon-lg` | Empty states. | Illustrative icons in "No Data" screens. |

### 17. Animation Duration Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `duration-fast` | Micro-interactions. | Button hovers, checkbox ticks (e.g., 150ms). |
| `duration-normal`| Layout shifts. | Expanding accordions, sliding drawers (e.g., 300ms). |

### 18. Easing Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `ease-in-out` | Standard motion. | Symmetrical entering and exiting. |
| `ease-spring` | Natural movement. | Bouncy, physics-based modal openings. |

### 19. Z-index Tokens
| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `z-base` | Standard content. | The default stacking context. | Prevents `z-index: 9999` wars. |
| `z-sticky` | Fixed headers. | Table headers, sticky navbars. | Organized via semantic names. |
| `z-dropdown` | Context menus. | Appears above sticky headers. | Predictable stacking hierarchy. |
| `z-modal` | Dialog overlays. | Appears above everything except toasts. | Ensures critical actions are visible. |
| `z-toast` | Notifications. | The absolute highest layer. | Guarantees alerts are never occluded. |

### 20. Breakpoint Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `bp-sm` | Mobile devices. | Stacks widgets, collapses sidebars. |
| `bp-md` | Tablets. | Fluid grids, touch-friendly adjustments. |
| `bp-lg` | Laptops. | Standard dashboard layouts. |
| `bp-xl` | Control rooms. | Expands data density, ultra-wide charts. |

---

## 21. Domain Specific Tokens

To ensure GridSense AI maintains its unique identity, domain-specific semantic tokens are required.

### 22. Chart Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `chart-line-width` | Standardizes stroke thickness. | All line charts use this token. |
| `chart-axis-color` | Standardizes grid lines. | Subtle background grid colors. |
| `chart-tooltip-bg` | Chart hover overlays. | Consistent floating tooltip backgrounds. |

### 23. GIS Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `gis-layer-transmission` | Grid lines. | Maps directly to electrical transmission visualizations. |
| `gis-layer-weather` | Irradiance/Wind heatmaps. | Controls opacity and blend modes for weather rasters. |
| `gis-cluster-bg` | Clustered points. | Background color for grouped power plants at high zoom. |

### 24. AI Tokens
| Token | Purpose | Usage Rules | Future Scalability |
|-------|---------|-------------|--------------------|
| `ai-accent-color` | Amethyst purple semantic color. | Distinguishes ML predictions from ground truth data. | New AI features instantly inherit branding. |
| `ai-shimmer-speed`| "Thinking" state. | Standardizes the pulse speed of AI generation loaders. | Reusable across Copilot and Inline Insights. |

### 25. Notification Tokens
| Token | Purpose | Usage Rules |
|-------|---------|-------------|
| `notify-bg-toast` | Ephemeral alerts. | Standard toast background color. |
| `notify-bg-critical`| High severity banners. | Unignorable red background for grid failures. |
| `notify-duration` | Auto-dismiss timer. | Standardizes how long a toast stays on screen. |

---

## Conclusion

By strictly adhering to this Design Token Specification, GridSense AI guarantees that the frontend will remain maintainable, scalable, and visually coherent regardless of how many new pages, developers, or energy verticals are added over the next decade. If a rebrand or theme change is required, modifying the root token values will instantly and flawlessly propagate across the entire application.
