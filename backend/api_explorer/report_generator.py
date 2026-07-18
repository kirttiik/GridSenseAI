import os
import json
from endpoints import ENDPOINTS

RAW_DIR = os.path.join(os.path.dirname(__file__), "outputs", "raw")
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "outputs", "reports")

def generate_reports():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    inventory = []
    
    # 1. Gather stats and infer schemas
    for namespace, endpoints in ENDPOINTS.items():
        for name, path in endpoints.items():
            filepath = os.path.join(RAW_DIR, f"{name}.json")
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except:
                    continue
            
            # Identify array of records to build dictionary
            records = []
            if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
                records = data["data"]
            elif isinstance(data, list):
                records = data
            elif isinstance(data, dict):
                records = [data]
                
            record_count = len(records)
            latest_timestamp = "N/A"
            fields_dict = {}
            
            # Read execution metadata if it exists
            metadata_file = os.path.join(RAW_DIR, "execution_metadata.json")
            exec_metadata = {}
            if os.path.exists(metadata_file):
                try:
                    with open(metadata_file, "r", encoding="utf-8") as mf:
                        meta_list = json.load(mf)
                        for m in meta_list:
                            if m["endpoint_name"] == name:
                                exec_metadata = m
                                break
                except:
                    pass
            
            if records:
                # Get fields from first record
                first = records[0]
                if isinstance(first, dict):
                    for k, v in first.items():
                        fields_dict[k] = {
                            "type": type(v).__name__,
                            "nullable": v is None,
                            "sample": v
                        }
                    # Try to find a timestamp field
                    for k, v in first.items():
                        if "time" in k.lower() or "date" in k.lower():
                            latest_timestamp = str(v)
                            break
                            
            inventory.append({
                "namespace": namespace,
                "endpoint": name,
                "url": path,
                "records": record_count,
                "latest_timestamp": latest_timestamp,
                "fields": fields_dict,
                "cadence": "Unknown",
                "coverage": "National/State",
                "status": exec_metadata.get("status", "SUCCESS"),
                "status_code": exec_metadata.get("status_code", "Unknown"),
                "auth_method": exec_metadata.get("auth_method", "Unknown"),
                "duration_ms": exec_metadata.get("duration_ms", 0),
                "error": exec_metadata.get("error", None),
                "response_size": os.path.getsize(filepath)
            })

    # Save api_inventory.json
    with open(os.path.join(REPORTS_DIR, "api_inventory.json"), "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)

    # Generate API_INVENTORY.md
    with open(os.path.join(REPORTS_DIR, "API_INVENTORY.md"), "w", encoding="utf-8") as f:
        f.write("# API Inventory\n\n")
        f.write("| Namespace | Endpoint | URL | Auth Method | Status | HTTP Code | Records | Latest Timestamp | Response Size | Duration |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|\n")
        for item in inventory:
            err_text = f" ({item['error']})" if item['error'] else ""
            status_text = f"{item['status']}{err_text}"
            f.write(f"| {item['namespace']} | {item['endpoint']} | `{item['url']}` | {item['auth_method']} | {status_text} | {item['status_code']} | {item['records']} | {item['latest_timestamp']} | {item['response_size']} bytes | {item['duration_ms']} ms |\n")

    # Generate FIELD_DICTIONARY.md
    with open(os.path.join(REPORTS_DIR, "FIELD_DICTIONARY.md"), "w", encoding="utf-8") as f:
        f.write("# Field Dictionary\n\n")
        for item in inventory:
            f.write(f"## {item['endpoint']} ({item['namespace']})\n\n")
            if item["fields"]:
                f.write("| Field Name | Data Type | Nullable | Sample Value |\n")
                f.write("|---|---|---|---|\n")
                for k, v in item["fields"].items():
                    f.write(f"| {k} | {v['type']} | {v['nullable']} | {str(v['sample'])[:50]} |\n")
            else:
                f.write("No schema identified.\n")
            f.write("\n")
            
    print("Reports generated successfully in outputs/reports/")

if __name__ == "__main__":
    generate_reports()
