# check_specific_paths.py
import os

paths = [
    r"e:\Game\Garena\fifa\.env",
    r"e:\Game\Garena\.env",
    r"e:\Game\.env",
    r"C:\Users\PhucVu\.env",
    r"C:\Users\PhucVu\Documents\.env",
    r"E:\Game\Garena\FCOnline\.env",
    r"E:\FCOnlineWorkspace\Research\.env",
    r"E:\FCOnlineWorkspace\Research\repos\fconline-mcp\.env",
    r"E:\FCOnlineWorkspace\Research\repos\fconline-player-search\.env"
]

for p in paths:
    if os.path.exists(p):
        print(f"EXISTS: {p}")
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if "NEXON" in line:
                    print("  Contains NEXON key line!")
    else:
        print(f"NOT FOUND: {p}")
