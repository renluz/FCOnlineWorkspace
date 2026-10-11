import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/Traits/hidden_traits_vi.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== GOLD TRAITS (Chỉ số ẩn Vàng) ===")
for t in data['traits']:
    if t.get('type') == 'gold_hidden_trait' or 'gold' in t.get('type', ''):
        print(f"ID: {t['id']} | Tên: {t.get('name_vi')} | Vị trí: {t.get('positions')} | Mô tả: {t.get('description_vi')}")
