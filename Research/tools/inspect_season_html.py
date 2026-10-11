import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('data/vn_market_raw_samples/season_25dp_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Title:", soup.title.string if soup.title else "No title")
links = soup.find_all('a')
print("Total links:", len(links))
for a in links[:25]:
    print(" ", a.get('href'), "->", a.get_text(strip=True)[:40])

scripts = soup.find_all('script')
print("\nScripts on season page:")
for s in scripts:
    src = s.get('src')
    if src:
        print("  src:", src)
    else:
        txt = s.get_text()[:100].replace('\n', ' ')
        print("  inline:", txt)
