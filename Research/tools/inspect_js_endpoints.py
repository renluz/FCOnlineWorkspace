import requests
import re
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://fcoplayers.com', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

scripts = [s.get('src') for s in soup.find_all('script') if s.get('src')]
print("Scripts on fcoplayers.com:")
for s in scripts:
    print(" ", s)
    if s.startswith('/') or 'fcoplayers' in s:
        full_url = s if s.startswith('http') else f"https://fcoplayers.com{s}"
        try:
            js_res = requests.get(full_url, headers=headers, timeout=5)
            # Search for api endpoints in js
            endpoints = re.findall(r'[\'"`](/api/[^\'"`]+)[\'"`]', js_res.text)
            print(f"    Endpoints in {s}:", set(endpoints))
            keywords = [w for w in ['price', 'market', 'sell', 'buy', 'gia_bp', 'ttcn'] if w in js_res.text.lower()]
            print(f"    Keywords in {s}:", keywords)
        except Exception as e:
            print("    Error fetching script:", e)
