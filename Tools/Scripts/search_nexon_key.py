# search_nexon_key.py
import os

print("Searching for any files containing NEXON_OPEN_API_KEY in config dirs...")
search_dirs = [
    r"C:\Users\PhucVu\.gemini",
    r"C:\Users\PhucVu\AppData\Roaming\Code",
    r"C:\Users\PhucVu\AppData\Roaming\npm",
    r"e:\Game\Garena\fifa",
    r"E:\Game\Garena\FCOnline"
]

found = []
for d in search_dirs:
    if not os.path.exists(d):
        continue
    for root, dirs, files in os.walk(d):
        if any(x in root for x in [".git", "node_modules", ".venv", "Cache", "CachedData", "logs", "transcripts"]):
            continue
        for f in files:
            if f.endswith(('.json', '.env', '.txt', '.yaml', '.yml', '.ini', '.cfg')):
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                        content = fl.read()
                        if 'NEXON_OPEN_API_KEY' in content and 'export NEXON' not in content and 'SetEnvironmentVariable' not in content:
                            found.append(p)
                except:
                    pass

print("Found files:")
for f in found:
    print(" ", f)
