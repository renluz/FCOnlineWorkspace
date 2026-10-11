# test_nexon_no_key.py
import requests

url = "https://open.api.nexon.com/fconline/v1/ranker-stats"
try:
    r = requests.get(url, params={"matchtype": 52}, timeout=10)
    print(f"Status Code: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Exception: {e}")
