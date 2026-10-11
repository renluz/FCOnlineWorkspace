# test_match_http_error.py
import requests

url = "https://open.api.nexon.com/fconline/v1/match"
params = {
    "matchtype": 52,
    "offset": 0,
    "limit": 1,
    "orderby": "desc"
}

# 1. No key
r1 = requests.get(url, params=params, timeout=10)
print(f"No key: HTTP {r1.status_code} - {r1.text}")

# 2. Invalid dummy key
r2 = requests.get(url, params=params, headers={"x-nxopen-api-key": "invalid_test_key_dummy"}, timeout=10)
print(f"Invalid key: HTTP {r2.status_code} - {r2.text}")
