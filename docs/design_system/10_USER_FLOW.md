# GridSense AI: User Flow Blueprint

This document defines the comprehensive user journeys for each primary persona in GridSense AI. By mapping exact behavioral workflows, we ensure the platform seamlessly accommodates vastly different user goals—from macro-economic executive briefings to real-time micro-level grid anomaly investigations.

---

## 1. The Executive Workflow (Strategic Overview)
**Persona**: CEO, Government Minister.
**Goal**: Rapid understanding of national energy security and macroeconomic trends in under 5 minutes.

```mermaid
graph TD
    A[Authentication: SSO / Biometric] -->|Role: Executive| B(Default: Executive Workspace)
    B --> C{Dashboard Check}
    C -->|Normal Operations| D[View KPI Summaries]
    C -->|Alert Banner Active| E[View Critical Notification]
    E --> F[Click 'Explain with AI']
    F --> G[Read AI Executive Summary]
    G --> H[Export PDF Briefing]
    D --> I[Global Search: 'Solar Capacity']
    I --> J[Navigate to Renewable Overview]
    J --> H
    H --> K[Logout / Background Session]
```
**Permissions Note**: Executives possess sweeping read permissions across all workspaces but generally lack write/configuration permissions to prevent accidental system changes.

---

## 2. The Grid Operator Workflow (Real-Time Tactical)
**Persona**: Load Dispatch Center Operator.
**Goal**: Ensuring grid stability, monitoring telemetry, and managing sudden outages.

```mermaid
graph TD
    A[Authentication: 2FA] -->|Role: Operator| B(Default: Grid Operations)
    B --> C[Monitor Live Telemetry]
    C -->|Frequency Drop < 49.9Hz| D[System Alert Banner]
    D --> E[Click Map Notification]
    E --> F[Map Auto-Pans to Substation]
    F --> G[Expand GIS Vector Layers]
    G --> H[Select 'Analyze Local Weather']
    H --> I[AI Overlays Storm Path on Map]
    I --> J[Operator Acknowledges Alert]
    J --> K[System Logs Acknowledgment]
```
**Permissions Note**: Operators have exclusive write access to operational acknowledgment flags and override capabilities in the GIS/Grid workspaces.

---

## 3. The Analyst Workflow (Deep Investigation)
**Persona**: Energy Trader, Market Analyst.
**Goal**: Investigating historical data to build trading strategies and forecast load.

```mermaid
graph TD
    A[Authentication: Password] -->|Role: Analyst| B(Default: Market Intelligence)
    B --> C[Configure Date Range Filter]
    C --> D[View DAM vs RTM Prices]
    D --> E[Observe Price Spike]
    E --> F[Navigate to Forecast Workspace]
    F --> G[Run ML Load Forecast Model]
    G -->|Processing... Toast| H[Review Confidence Intervals]
    H --> I[Open AI SHAP Explanation]
    I --> J[Understand Weather caused Spike]
    J --> K[Export Timeseries to CSV]
    K --> L[Save Dashboard Layout to Settings]
```
**Permissions Note**: Analysts possess execution permissions for heavy ML generation jobs and massive data export limits.

---

## 4. The Researcher Workflow (Data Exploration)
**Persona**: Data Scientist, Academic.
**Goal**: Exploring raw datasets and correlating long-term climate data with generation efficiency.

```mermaid
graph TD
    A[Authentication] -->|Role: Researcher| B(Default: Reports & Analytics)
    B --> C[Open Command Palette]
    C -->|Search: 'Wind CUF 2024'| D[Navigate to Asset Analytics]
    D --> E[Toggle GIS Satellite Layer]
    E --> F[Overlay Historical Weather Raster]
    F --> G[Compare with Live Generation]
    G --> H[Select 100+ Assets via Map Tool]
    H --> I[Generate Custom Batch Report]
    I --> J[API Rate Limit Checked]
    J --> K[Download JSON Dataset]
```
**Permissions Note**: Researchers are tightly constrained by API rate limits and cannot access real-time critical operational telemetry to prevent server load.

---

## 5. The Student / Public Viewer Workflow (Educational)
**Persona**: University Student, General Public.
**Goal**: General learning about the energy transition.

```mermaid
graph TD
    A[Authentication: OAuth / Public] -->|Role: Viewer| B(Default: Energy Dashboard)
    B --> C[View National Energy Mix]
    C --> D[Click 'How does this work?']
    D --> E[AI Copilot answers basic query]
    E --> F[Navigate to India GIS Map]
    F --> G[View Solar Parks]
    G --> H[Export limitations hit]
    H --> I[Upgrade Prompt / End Session]
```
**Permissions Note**: Viewers have strict Read-Only access. ML Forecasting and heavy ETL exports are entirely disabled.

---

## 6. The Administrator Workflow (System Configuration)
**Persona**: Platform DevOps, IT Admin.
**Goal**: Managing system health, resolving user permission issues, and monitoring ETL pipelines.

```mermaid
graph TD
    A[Authentication: YubiKey / MFA] -->|Role: Admin| B(Default: Administration)
    B --> C[View Global Settings]
    C --> D[Check System Health Dashboard]
    D --> E[Notification: ETL Job Failed]
    E --> F[Navigate to Data Pipelines]
    F --> G[Review API Logs & Exceptions]
    G --> H[Manually trigger ETL Retry]
    H --> I[Modify User Role Permissions]
    I --> J[Clear Global Cache]
    J --> K[Confirm System Stable]
```
**Permissions Note**: Administrators bypass all RBAC restrictions, possessing universal Write/Delete/Configure permissions across the entire platform architecture.
