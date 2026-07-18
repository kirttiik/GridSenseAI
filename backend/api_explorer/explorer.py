import asyncio
import json
import os
import time
from datetime import datetime
import httpx

from config import ENERGY_ATLAS_API_KEY, ENERGY_ATLAS_BASE_URL, ENERGY_ATLAS_TIMEOUT
from logger import logger
from endpoints import ENDPOINTS

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs", "raw")

class Explorer:
    def __init__(self):
        self.base_url = ENERGY_ATLAS_BASE_URL
        self.timeout = ENERGY_ATLAS_TIMEOUT
        self.results = []
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    async def fetch_endpoint(self, client: httpx.AsyncClient, namespace: str, name: str, path: str):
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        
        start_time = time.time()
        start_dt = datetime.now().isoformat()
        
        result = {
            "namespace": namespace,
            "endpoint_name": name,
            "url": url,
            "auth_method": None,
            "start_time": start_dt,
            "status": "FAILED",
            "status_code": None,
            "duration_ms": 0,
            "record_count": 0,
            "response_size_bytes": 0,
            "error": None
        }
        
        logger.info(f"[{namespace}] Fetching {name}...")
        try:
            # Determine correct authentication header
            req_headers = {"Accept": "application/json"}
            if "/developer/v1/" in path:
                req_headers["X-API-Key"] = ENERGY_ATLAS_API_KEY
                result["auth_method"] = "X-API-Key"
            else:
                req_headers["Authorization"] = f"Bearer {ENERGY_ATLAS_API_KEY}"
                result["auth_method"] = "Bearer"
                
            params = {"limit": 10}
            
            response = await client.get(url, headers=req_headers, params=params)
            result["status_code"] = response.status_code
            result["duration_ms"] = int((time.time() - start_time) * 1000)
            result["response_size_bytes"] = len(response.content)
            
            response.raise_for_status()
            
            data = response.json()
            
            filename = f"{name}.json"
            filepath = os.path.join(OUTPUT_DIR, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                
            result["status"] = "SUCCESS"
            
            if isinstance(data, dict):
                if "data" in data and isinstance(data["data"], list):
                    result["record_count"] = len(data["data"])
                else:
                    result["record_count"] = 1
            elif isinstance(data, list):
                result["record_count"] = len(data)
                
            logger.info(f"[{namespace}] {name} SUCCESS - {result['status_code']} - {result['record_count']} records - {result['duration_ms']}ms")
            
        except httpx.HTTPStatusError as e:
            result["error"] = f"HTTP Error {e.response.status_code}"
            logger.error(f"[{namespace}] {name} FAILED - HTTP {e.response.status_code}")
        except httpx.RequestError as e:
            result["error"] = f"Request Error: {str(e)}"
            logger.error(f"[{namespace}] {name} FAILED - Request Error: {str(e)}")
        except Exception as e:
            result["error"] = f"Unexpected Error: {str(e)}"
            logger.error(f"[{namespace}] {name} FAILED - Unexpected Error: {str(e)}")
            
        result["end_time"] = datetime.now().isoformat()
        self.results.append(result)
        return result

    async def run(self):
        logger.info("Starting API Exploration...")
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            tasks = []
            for namespace, endpoints in ENDPOINTS.items():
                for name, path in endpoints.items():
                    tasks.append(self.fetch_endpoint(client, namespace, name, path))
            
            await asyncio.gather(*tasks)
        
        logger.info("Exploration finished. Run report_generator.py to build reports.")
        self.print_summary()

    def print_summary(self):
        print("\n" + "="*50)
        print("EXECUTION SUMMARY")
        print("="*50)
        for r in self.results:
            print(f"\n{r['endpoint_name']} [{r['auth_method']}]")
            print(r["status"])
            if r["status"] == "SUCCESS":
                print(f"Records : {r['record_count']} | Duration: {r['duration_ms']}ms")
            else:
                print(f"Error: {r['error']}")
            print("="*50)
            
        with open(os.path.join(OUTPUT_DIR, "execution_metadata.json"), "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2)

if __name__ == "__main__":
    explorer = Explorer()
    asyncio.run(explorer.run())
