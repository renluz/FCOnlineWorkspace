import requests
import re
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

r = requests.get('https://fcoplayers.com/squad-builder', headers={'User-Agent': 'Mozilla/5.0'})
print("Squad builder status:", r.status_code)
endpoints = re.findall(r'[\'"`](/api/[^\'"`]+)[\'"`]', r.text)
print("Endpoints in squad builder:", set(endpoints))

ajax_calls = re.findall(r'url:\s*[\'"`]([^\'"`]+)[\'"`]', r.text)
print("AJAX calls in squad builder:", set(ajax_calls))

keywords = re.findall(r'.{0,30}(?:market|price|ttcn|giá|bp).{0,30}', r.text, re.I)
print(f"Occurrences of market/price/bp: {len(keywords)}")
for k in keywords[:5]:
    print("  ", k.strip().replace('\n', ' '))
