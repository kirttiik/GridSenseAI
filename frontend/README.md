# GridSense AI - Frontend

This is the official frontend for the GridSense AI platform, built with Next.js 15 App Router.

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

3. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Architecture

This frontend adheres to the Feature-Sliced Design methodology as defined in `07_FRONTEND_ARCHITECTURE.md`.
- **Framework**: Next.js 15
- **Styling**: Tailwind CSS v4 + Shadcn UI
- **State Management**: Zustand
- **Theme**: `next-themes` (Dark/Light mode support)

## Design Tokens

All colors, typography, spacing, and animations are strictly controlled via CSS design tokens documented in `06_DESIGN_TOKENS.md`. Do not use hardcoded values in components.
