import requests
import sys
import re
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

# Search FIFAAddict using their search API or page
# Let's inspect fo4db bookmark or query
for q in ['Zambrotta', 'Gullit', 'Del Piero', 'Rodri', 'Ramos']:
    url = f"https://fifaaddict.com/fo4db?keyword={q}"
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, 'html.parser')
    player_links = soup.find_all('a', href=re.compile(r'/fo4db/pid'))
    print(f"=== FIFAAddict search '{q}': {len(player_links)} results ===")
    for pl in player_links[:8]:
        print(" ", pl.get_text(' ', strip=True), "->", pl['href'])
