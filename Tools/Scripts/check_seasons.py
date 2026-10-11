import re, json

with open(r'C:\Users\PhucVu\.gemini\antigravity\brain\bb318d08-30a5-4a17-b499-6d2d5f6b0de5\.system_generated\steps\10\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for classes dictionary
m = re.search(r'\"classes\"\s*:\s*(\{.*?\})', text)
if m:
    try:
        classes = json.loads(m.group(1))
        target_ids = ['867', '856', '826', '825', '866', '855', '863', '283', '274']
        for tid in target_ids:
            print(f"Season {tid}: {classes.get(tid)}")
    except Exception as e:
        print("Error parsing classes:", e)
else:
    print("No 'classes' key directly found")
