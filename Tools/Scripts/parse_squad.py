import json, re, sys

with open(r'C:\Users\PhucVu\.gemini\antigravity\brain\bb318d08-30a5-4a17-b499-6d2d5f6b0de5\.system_generated\steps\10\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.SquadmakerBootstrap\s*=\s*(\{.*?\});\s*\}\)\(window\);', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    detail = data.get('shareDetail', {})
    print('Title:', detail.get('title'))
    print('Description:', detail.get('description'))
    print('Formation:', detail.get('formation'))
    print('Salary:', detail.get('salary'), 'OVR:', detail.get('avg_ovr'))
    print('Raw keys in shareDetail:', list(detail.keys()))
    # print entire shareDetail nicely
    with open('shareDetail_parsed.json', 'w', encoding='utf-8') as out:
        json.dump(detail, out, indent=2, ensure_ascii=False)
    print('Dumped shareDetail_parsed.json')
