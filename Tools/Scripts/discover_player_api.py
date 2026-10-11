import urllib.request
import urllib.error

BASE_URL = "https://dc.fconline.garena.vn/api/app"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://dc.fconline.garena.vn/player"
}

endpoints = [
    "/meta/players",
    "/meta/player-rankings",
    "/meta/player-tiers",
    "/player",
    "/players",
    "/meta/player-usage",
    "/meta/players/tier",
    "/meta/tier",
    "/player/ranking",
    "/player/tier",
    "/player/meta"
]

for ep in endpoints:
    url = f"{BASE_URL}{ep}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"SUCCESS {ep}: {resp.status}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {ep}: {e.code}")
    except Exception as e:
        print(f"Error {ep}: {e}")
