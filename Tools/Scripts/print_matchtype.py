import json, sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'E:\FCOnlineWorkspace\Research\data\matchtype.json', 'r', encoding='utf-8') as f:
    items = json.load(f)
for item in items:
    print(f"Code: {item.get('matchtype')} -> {item.get('desc')}")
