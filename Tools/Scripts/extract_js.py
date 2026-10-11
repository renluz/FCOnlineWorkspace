import urllib.request
import re
url = "https://cdn.vn.garenanow.com/web/aov/static/fco-data-center/live/assets/index-CDqBgm-p.js"
js = urllib.request.urlopen(url).read().decode('utf-8')
print("Searching for objects with mode, rank, grade:")
for match in re.finditer(r'\{[^\}]*mode:[^\}]*\}', js):
    s = match.group(0)
    if 'rank' in s or 'players/tiers' in s:
        print(s[:200])

print("\nSearching for players/tiers requests:")
for match in re.finditer(r'url:\"/players/tiers\"[^\}]*\}', js):
    print(match.group(0)[:200])
