# rename_and_tag_schema_sample.py
import os
import json

old_file = r"E:\FCOnlineWorkspace\Research\data\ranker_stats_52_raw_sample.json"
new_file = r"E:\FCOnlineWorkspace\Research\data\ranker_stats_52_schema_example.json"

data = {}
if os.path.exists(old_file):
    with open(old_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    os.remove(old_file)
    print(f"Removed {old_file}")

# Add required metadata
data["source"] = "NEXON_API_SPEC"
data["is_live_api_response"] = False
data["notice"] = "This is a schema structure example from fconline-mcp tests & Nexon documentation, NOT a live HTTP 200 response."

with open(new_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Created {new_file} with source=NEXON_API_SPEC, is_live_api_response=False")
