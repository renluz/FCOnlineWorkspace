# find_recent.py
import os
import time

now = time.time()
check_dirs = [
    r"C:\Users\PhucVu\Desktop",
    r"C:\Users\PhucVu\Downloads",
    r"C:\Users\PhucVu\Documents",
    r"E:\Game\Garena\FCOnline",
    r"C:\Users\PhucVu\.gemini"
]

print("Checking recent files (last 30m):")
for d in check_dirs:
    if not os.path.exists(d):
        continue
    for root, dirs, files in os.walk(d):
        if any(x in root for x in [".git", "node_modules", ".venv", "Cache", "logs"]):
            continue
        for f in files:
            p = os.path.join(root, f)
            try:
                mtime = os.path.getmtime(p)
                if now - mtime < 1800:
                    print(f"  {p}")
            except:
                pass
