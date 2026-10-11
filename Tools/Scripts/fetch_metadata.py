import urllib.request, json, os, sys

data_dir = r'E:\FCOnlineWorkspace\Research\data'
os.makedirs(data_dir, exist_ok=True)

meta_kinds = ['matchtype', 'spposition', 'division', 'division-volta', 'seasonid']
for kind in meta_kinds:
    url = f'https://open.api.nexon.com/static/fconline/meta/{kind}.json'
    dest = os.path.join(data_dir, f'{kind}.json')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            with open(dest, 'wb') as f:
                f.write(content)
            data = json.loads(content.decode('utf-8'))
            print(f"Downloaded {kind}.json: {len(data)} items")
            if kind == 'matchtype':
                print("--- MATCH TYPES ---")
                for item in data:
                    print(f"Code: {item.get('matchtype')} | Desc: {item.get('desc')}")
    except Exception as e:
        print(f"Error fetching {kind}: {e}")
