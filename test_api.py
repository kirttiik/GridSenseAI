import urllib.request
import json
import time

endpoints = [
    "/api/v1/health",
    "/api/v1/dashboard/overview",
    "/api/v1/energy/current",
    "/api/v1/grid/current",
    "/api/v1/market/current",
    "/api/v1/weather/current",
    "/api/v1/insights/current"
]

base_url = "http://127.0.0.1:8000"

print("Part 6: REST API Validation")
for ep in endpoints:
    url = f"{base_url}{ep}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            status = response.status
            print(f"[{status}] {ep} -> Success (Type: {type(data)})")
            
            if ep == "/api/v1/health":
                print("   Health Data:", data.get("data", data))
    except Exception as e:
        print(f"[ERROR] {ep} -> {e}")

print("\nPart 3: Data Sync Validation")
try:
    req = urllib.request.Request(f"{base_url}/api/v1/sync", method="POST")
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(f"[{response.status}] /api/v1/sync -> Success")
        print("   Sync Response:", data)
except Exception as e:
    print(f"[ERROR] /api/v1/sync -> {e}")
