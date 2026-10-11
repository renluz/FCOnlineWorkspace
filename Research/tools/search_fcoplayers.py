import requests
import sys
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}
for q in ['Ruud Gullit', 'Gullit', 'Sergio Ramos', 'Ramos', 'Inaki Williams', 'Williams', 'Rodri', 'Rodrigo']:
    res = requests.post('https://fcoplayers.com/api/ajax/search-person', data={'q': q, 'page': 1}, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if '/players/' in a['href']]
    print(f"Query '{q}': {len(links)} links found: {links[:3]}")
