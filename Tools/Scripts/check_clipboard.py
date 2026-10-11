# check_clipboard.py
import winreg
import os

# Check if there's any file modified in the last 10 minutes in FCOnlineResearch or user home
import time
now = time.time()

print("Recent files in FCOnlineResearch:")
for root, dirs, files in os.walk(r"E:\FCOnlineWorkspace\Research"):
    if any(x in root for x in [".git", "node_modules", ".venv"]):
        continue
    for f in files:
        fp = os.path.join(root, f)
        try:
            mtime = os.path.getmtime(fp)
            if now - mtime < 1800:
                print(f"  {fp} ({int(now - mtime)}s ago)")
        except:
            pass

print("Recent files in C:\\Users\\PhucVu:")
for f in os.listdir(r"C:\Users\PhucVu"):
    fp = os.path.join(r"C:\Users\PhucVu", f)
    if os.path.isfile(fp):
        try:
            mtime = os.path.getmtime(fp)
            if now - mtime < 1800:
                print(f"  {fp} ({int(now - mtime)}s ago)")
        except:
            pass
