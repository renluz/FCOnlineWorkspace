import urllib.request
import re
import json

# search on fifaaddict search endpoint
url = "https://fifaaddict.com/fo4db?q=Ki+Sung+Yueng"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    # find links
    links = re.findall(r'href="(/fo4db/player/[^"]+)"', html)
    print("Player links:", set(links))
    # or find all pids
    pids = re.findall(r'data-pid="(\d+)"', html)
    print("PIDs:", set(pids))
except Exception as e:
    print(e)
