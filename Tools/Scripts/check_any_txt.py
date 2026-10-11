# check_any_txt.py
import os
import time

now = time.time()
found = []
for root, dirs, files in os.walk(r"E:\FCOnlineWorkspace\Research"):
    if any(x in root for x in [".git", "node_modules", ".venv"]):
        continue
    for f in files:
        if f.endswith(('.txt', '.json', '.csv', '.py', '.md')):
            p = os.path.join(root, f)
            try:
                mtime = os.path.getmtime(p)
                if now - mtime < 7200:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                        for line in fl:
                            if 'live_' in line or 'test_' in line:
                                found.append((p, line.strip()[:10]))
            except:
                pass

print("Matches for live_ or test_ key patterns:")
for p, snippet in found:
    print(f"  {p}: {snippet}")
