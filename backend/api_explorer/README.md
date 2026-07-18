# Energy Atlas API Explorer

This standalone tool discovers, validates, and documents every endpoint available in the India Energy Atlas API.
It is explicitly built to be separated from the main production backend logic in GridSense AI, ensuring we can thoroughly understand the API schemas and behaviors without polluting our production architecture.

## Requirements
- `httpx`
- `python-dotenv`

## Usage
1. Configure your `.env` at the `backend/` root with:
   - `ENERGY_ATLAS_API_KEY`
   - `ENERGY_ATLAS_BASE_URL`
   - `ENERGY_ATLAS_TIMEOUT`

2. Run the explorer to fetch API data and save raw JSON responses:
   ```bash
   python explorer.py
   ```

3. Generate Markdown and JSON inventory reports based on the fetched data:
   ```bash
   python report_generator.py
   ```

## Outputs
- **Raw JSON Responses**: `outputs/raw/`
- **Markdown Inventory**: `outputs/reports/API_INVENTORY.md`
- **Field Dictionary**: `outputs/reports/FIELD_DICTIONARY.md`
- **JSON Inventory**: `outputs/reports/api_inventory.json`
