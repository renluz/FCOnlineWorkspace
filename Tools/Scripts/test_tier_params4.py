import urllib.request
import urllib.parse
import urllib.error

url = "https://dc.fconline.garena.vn/api/app/players/tiers"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://dc.fconline.garena.vn/player"
}

modes = ["1vs1", "ranking", "pvp", "league", "friendly", "official_match", "manager_mode", "volta_live", "match", "rank", "competition"]
for m in modes:
    q = urllib.parse.urlencode({"mode": m, "rank": "pro_up", "grade": 8})
    req = urllib.request.Request(f"{url}?{q}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            print(f"SUCCESS {m}: {resp.status}")
            break
    except urllib.error.HTTPError as e:
        print(f"Failed {m}: {e.code}")
    except Exception:
        pass
