# check_all_users.py
import winreg

with winreg.OpenKey(winreg.HKEY_USERS, "") as root:
    i = 0
    while True:
        try:
            sub = winreg.EnumKey(root, i)
            i += 1
            if sub.endswith("_Classes"):
                continue
            print("User SID:", sub)
            try:
                with winreg.OpenKey(winreg.HKEY_USERS, f"{sub}\\Environment") as env_k:
                    j = 0
                    while True:
                        try:
                            name, val, _ = winreg.EnumValue(env_k, j)
                            print(f"   -> {name}")
                            j += 1
                        except OSError:
                            break
            except Exception as e:
                pass
        except OSError:
            break
