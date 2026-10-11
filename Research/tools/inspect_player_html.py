import re
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('data/vn_market_raw_samples/player_boniface_ws_raw.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Page title:", soup.title.text if soup.title else "")

# Check all classes and ids
print("\nDiv classes matching player/info/market:")
for d in soup.find_all('div'):
    c = " ".join(d.get('class', []))
    if any(k in c.lower() for k in ['market', 'price', 'stats', 'rating', 'badge', 'card']):
        print(" ", c)

print("\nSearching text for price / BP occurrences:")
for word in ['market', 'price', 'thị trường', 'chuyển nhượng', 'ttcn', 'giá']:
    matches = re.findall(rf'.{{0,30}}{word}.{{0,30}}', html, re.I)
    print(f"Keyword '{word}': {len(matches)} occurrences")
    for m in matches[:3]:
        print("   ...", m.strip().replace('\n', ' '), "...")
