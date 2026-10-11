# list_env_keys.py
import winreg

print("Iterating HKCU Environment:")
try:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
        i = 0
        while True:
            try:
                name, val, typ = winreg.EnumValue(key, i)
                print(f"  [{i}] {name} (len={len(str(val))})")
                i += 1
            except OSError:
                break
except Exception as e:
    print("Error:", e)

print("\nIterating HKLM Environment:")
try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment") as key:
        i = 0
        while True:
            try:
                name, val, typ = winreg.EnumValue(key, i)
                print(f"  [{i}] {name} (len={len(str(val))})")
                i += 1
            except OSError:
                break
except Exception as e:
    print("Error:", e)
