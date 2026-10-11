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

# Try combinations
params_list = [
    {"rank": "pro_up", "grade": 8, "position": "all", "window": "30d"},
    {"rank": "professional_up", "grade": 8, "position": "all"},
    {"rank": "pro", "grade": 8},
    {"grade": 8, "position": "all", "dimension": "player"},
    {"dimension": "tier", "rank": "legend_up"},
    {"rank": "pro_up", "grade": 8, "position": "all", "window": "7d"},
    {"rank": "pro_up", "grade": 8, "position": "all"},
    {"position": "all", "grade": 8},
    {"rank": "legend_up", "grade": 8, "position": "all"},
    {"rank": "legend_up", "grade": "8", "position": "LAM"},
    {"rank": "pro_up", "grade": "8", "position": "LAM"}
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
    except Exception as e:
        pass
