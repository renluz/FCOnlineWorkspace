import urllib.request
import urllib.parse
import urllib.error
import json

url = "https://dc.fconline.garena.vn/api/app/players/tiers"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://dc.fconline.garena.vn/player"
}

params_list = [
    {"mode": "1v1", "rank": "pro_up", "grade": 8, "position": "all", "window": "30d"},
    {"mode": "official", "rank": "pro_up", "grade": 8, "position": "all"},
    {"mode": 50, "rank": "pro_up", "grade": 8},
    {"mode": "50", "rank": "pro_up", "grade": 8},
    {"mode": "rank", "rank": "pro_up", "grade": 8}
]

for p in params_list:
    q = urllib.parse.urlencode(p)
    req = urllib.request.Request(f"{url}?{q}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            print(f"SUCCESS {q}: {resp.status}")
            data = resp.read().decode('utf-8')
            print(data[:100])
            break
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {q}: {e.code} - {e.read().decode('utf-8')}")
