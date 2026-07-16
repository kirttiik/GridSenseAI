# System Architecture Document (SAD)
**Project:** GridSense-AI (AI Energy Intelligence Platform)

This document outlines the system architecture for GridSense-AI, detailing how the frontend, backend, database, APIs, and external services interact to provide a centralized, scalable, and AI-powered energy intelligence platform.

## 1. Overall System Architecture
GridSense-AI follows a modern, decoupled client-server architecture:
- **Client Tier:** A Next.js (React) frontend serving as the interactive user interface.
- **Application Tier:** A FastAPI backend handling business logic, AI model inferences, data processing, and serving RESTful APIs.
- **Data Tier:** A PostgreSQL database with PostGIS extensions for handling spatial and relational data.
- **Ingestion Layer:** Background tasks managed by APScheduler to ingest data from external APIs (Energy Atlas, NASA POWER) and handle ETL workflows.

**Communication Flow:**
1. The Next.js frontend communicates with the FastAPI backend over HTTP/REST (and WebSocket for real-time updates if needed).
2. The FastAPI backend queries the PostgreSQL database using SQLAlchemy ORM.
3. The Data Ingestion Layer runs asynchronously on the backend, fetching data from external APIs, transforming it, and loading it into the database.

## 2. Frontend Architecture
The frontend is built with Next.js, React, TypeScript, and Tailwind CSS.

- **Next.js App Structure:** Uses the Next.js `App Router` for a modular, component-driven directory layout.
- **Routing:** 
  - File-system based routing via the `app/` directory.
  - Protected routes for authenticated dashboards and user workspaces.
- **State Management:**
  - React Context API / Zustand for global UI state.
  - React Query (TanStack Query) for server-state management, caching, and data synchronization.
- **Components:**
  - Reusable UI elements utilizing `shadcn/ui` and Tailwind CSS.
  - Complex interactive maps using React Leaflet.
  - Interactive data visualizations using Apache ECharts.
- **Services:**
  - API client layer (using Axios or Fetch API) abstracted into a `services/` directory to handle all requests to the FastAPI backend, including interceptors for JWT injection.

## 3. Backend Architecture
The backend is built with Python and FastAPI for high-performance, asynchronous API serving.

- **FastAPI Folder Structure:**
  - `/api` - Route definitions (controllers) separated by version.
  - `/core` - Configuration, security, and global dependencies.
  - `/models` - SQLAlchemy database models.
  - `/schemas` - Pydantic models for request validation and response serialization.
  - `/services` - Business logic and AI/ML processing (Scikit-learn, XGBoost).
  - `/repositories` - Database interaction logic.
- **API Versioning:** All endpoints are versioned (e.g., `/api/v1/...`) to maintain backward compatibility for future integrations.
- **Services:** Decoupled service layer to ensure routes remain thin and testable. Includes an AI service layer for running predictive models.
- **Repository Pattern:** Abstracts database queries using SQLAlchemy. Routes interact with services, and services interact with repositories.
- **Scheduler:** `APScheduler` runs in the background to handle periodic data ingestion, materialized view refreshes, and cache invalidation.
- **Authentication:** OAuth2 with JWT (JSON Web Tokens) for secure, stateless user authentication and authorization.

## 4. Database Architecture
The primary data store is PostgreSQL, optimized for analytical workloads and geospatial queries.

- **PostgreSQL:** Handles user data, historical energy metrics, system logs, and market data.
- **PostGIS:** Extends PostgreSQL to support geographic objects, enabling geospatial queries for the India Energy Map (e.g., finding power plants within a specific state or bounding box).
- **Table Relationships:**
  - Normalized schemas for structured entities (Users, States, Power Plants).
  - Time-series optimized tables for high-frequency data (Grid Frequency, Market Prices, Generation).
- **Indexing Strategy:**
  - B-Tree indexes on primary keys and frequently filtered foreign keys.
  - BRIN (Block Range INdexes) for large time-series tables (e.g., hourly generation data).
  - GiST indexes on PostGIS geometry columns for rapid spatial querying.

## 5. Data Source Strategy
GridSense AI Version 1 follows a single-source architecture.

All operational, market, asset, and intelligence datasets are ingested exclusively from the India Energy Atlas Developer API.

The backend is responsible for:
- Fetching data from the external API.
- Validating responses.
- Transforming data into the internal schema.
- Storing historical records in PostgreSQL.
- Exposing stable internal REST APIs to the frontend.

The frontend never communicates directly with external APIs.

Additional data providers (weather APIs, satellite data, and other public sources) may be integrated in future versions without affecting the frontend or public API contracts.

## 6. Data Ingestion Layer
An automated ETL (Extract, Transform, Load) pipeline is crucial for keeping GridSense-AI up to date.

- **Energy Atlas API:** Fetches master data for power plants, installed capacity, and geospatial coordinates.
- **Weather APIs:** Uses NASA POWER API and other weather sources to fetch temperature, solar radiation, and wind speed data necessary for AI forecasting models (planned for future versions).
- **Future Scrapers:** Extensible architecture using tools like BeautifulSoup or Playwright for public web scraping (where APIs are absent and terms permit).
- **ETL Workflow:**
  1. **Extract:** Scheduled jobs fetch JSON/CSV payloads from external sources.
  2. **Transform:** Data is cleaned, normalized, missing values handled, and mapped to internal schemas using Pandas.
  3. **Load:** Transformed data is upserted into PostgreSQL.

## 7. Deployment
The platform is designed for cloud-native deployment.

- **Render Frontend:** Next.js application deployed as a Web Service or Static Site on Render.
- **Render Backend:** FastAPI application deployed as a Dockerized Web Service on Render, configured for auto-scaling and continuous deployment from GitHub.
- **Render PostgreSQL:** Managed PostgreSQL database with automated backups, point-in-time recovery, and PostGIS extensions enabled.

## 8. Security
- **JWT (JSON Web Tokens):** Stateless, secure token-based authentication with short expiration times and refresh token rotation.
- **Environment Variables:** All secrets (database URLs, API keys, JWT secrets) are injected at runtime via environment variables and never committed to source control.
- **API Rate Limiting:** Implemented via middleware (e.g., Slowapi) to prevent abuse, DDoS attacks, and control scraper traffic.
- **Input Validation:** Strict payload validation using FastAPI and Pydantic to prevent SQL injection and cross-site scripting (XSS). CORS policies restrict access to trusted origins.

## 9. Logging & Monitoring
- **Logging:** Structured JSON logging on the backend capturing request latency, errors, and system events.
- **Monitoring:** Application performance monitoring (APM) and uptime checks. Render's built-in metrics track CPU, memory, and database I/O.
- **Error Tracking:** Integration with tools (e.g., Sentry) to capture unhandled exceptions in both frontend and backend.

## 10. Scalability
- **Stateless Backend:** FastAPI application is entirely stateless, allowing horizontal scaling by adding more instances behind a load balancer.
- **Database Scalability:** Read replicas can be added in the future for heavy analytical dashboard queries, keeping the primary database responsive for ingestion and writes.
- **Caching:** Future implementation of Redis to cache expensive AI forecasts, API responses, and static dashboard metrics.
