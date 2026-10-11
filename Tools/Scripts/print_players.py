import json

with open(r'C:\Users\PhucVu\.gemini\antigravity\brain\bb318d08-30a5-4a17-b499-6d2d5f6b0de5\scratch\shareDetail_parsed.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

cards = d.get('squad_json', {}).get('cards', [])
print(f"Squad Title: {d.get('title')} by {d.get('creator_name')}")
print(f"Total FP: {d.get('total_fp')}, Avg OVR: {d.get('avg_ovr')}")
print("-" * 65)
for c in cards:
    p = c.get('playerData', {})
    role = c.get('role', '')
    name = p.get('name_short', '')
    year = p.get('year', '')
    ovr = p.get('ovr', 0)
    level = p.get('reinforceLevel', 0)
    salary = p.get('salary', 0)
    foot_p = p.get('foot_pref', '')
    foot_w = p.get('foot_weak', '')
    print(f"{role:5} | {name:20} | SeasonID:{year:4} | OVR:{ovr:3} | +{level} | FP:{salary:2} | Foot: {foot_p}(wf{foot_w})")
