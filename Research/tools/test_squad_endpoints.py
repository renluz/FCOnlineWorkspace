import requests
import json
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0', 'X-Requested-With': 'XMLHttpRequest'}

endpoints = [
    '/api/person/search',
    '/api/ajax/list-person',
    '/api/ajax/search',
    '/api/ajax/listThayCauThu'
]

for ep in endpoints:
    url = f"https://fcoplayers.com{ep}"
    print(f"\n--- Testing {url} ---")
    
    # Try GET
    try:
        r_get = requests.get(url, headers=headers, timeout=5)
        print(f"GET status: {r_get.status_code}, content-type: {r_get.headers.get('Content-Type')}, len: {len(r_get.text)}")
        if r_get.status_code == 200:
            print("  GET snippet:", r_get.text[:200])
    except Exception as e:
        print("GET error:", e)
        
    # Try POST with search query
    try:
        r_post = requests.post(url, data={'q': 'Boniface', 'search': 'Boniface'}, headers=headers, timeout=5)
        print(f"POST status: {r_post.status_code}, content-type: {r_post.headers.get('Content-Type')}, len: {len(r_post.text)}")
        if r_post.status_code == 200:
            print("  POST snippet:", r_post.text[:200])
            try:
                js = r_post.json()
                print("  POST JSON keys/sample:", list(js.keys()) if isinstance(js, dict) else f"List with {len(js)} items")
            except Exception:
                pass
    except Exception as e:
        print("POST error:", e)
