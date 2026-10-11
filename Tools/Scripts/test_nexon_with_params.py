# test_nexon_with_params.py
import requests
import json

url = "https://open.api.nexon.com/fconline/v1/ranker-stats"
params = {
    "matchtype": 52,
    "players": json.dumps([{"id": 100000051, "po": 25}])
}

# 1. Without header
r1 = requests.get(url, params=params, timeout=10)
print(f"Without header -> HTTP {r1.status_code}: {r1.text}")

# 2. With dummy header
r2 = requests.get(url, params=params, headers={"x-nxopen-api-key": "dummy_key_12345"}, timeout=10)
print(f"With dummy header -> HTTP {r2.status_code}: {r2.text}")
