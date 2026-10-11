# find_api_key.py
import os
import winreg

print("Searching for NEXON_OPEN_API_KEY...")

# 1. Process environment
k1 = os.environ.get("NEXON_OPEN_API_KEY")
print("Process env:", "FOUND" if k1 else "NOT FOUND")

# 2. HKCU Environment
try:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
        k2, _ = winreg.QueryValueEx(key, "NEXON_OPEN_API_KEY")
        print("HKCU Environment:", "FOUND" if k2 else "NOT FOUND")
except Exception as e:
    print("HKCU Environment error:", e)

# 3. HKLM Environment
try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment") as key:
        k3, _ = winreg.QueryValueEx(key, "NEXON_OPEN_API_KEY")
        print("HKLM Environment:", "FOUND" if k3 else "NOT FOUND")
except Exception as e:
    print("HKLM Environment error:", e)

# 4. Check for .env in current workspace or home
paths_to_check = [
    r"E:\FCOnlineWorkspace\Research\.env",
    r"E:\FCOnlineWorkspace\Research\repos\fconline-mcp\.env",
    os.path.expanduser("~/.env"),
]
for p in paths_to_check:
    if os.path.exists(p):
        print(f"File exists: {p}")
        try:
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    if "NEXON_OPEN_API_KEY" in line:
                        print(f"  -> Contains NEXON_OPEN_API_KEY in {p}")
        except Exception as e:
            print("  Error reading:", e)
