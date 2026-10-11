# test_api_auth.py
import os
import sys
import requests

# Check environment variable
api_key = os.environ.get("NEXON_OPEN_API_KEY")

# If not in process env, check Windows user environment
if not api_key:
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment")
        api_key, _ = winreg.QueryValueEx(key, "NEXON_OPEN_API_KEY")
        # propagate to current process
        os.environ["NEXON_OPEN_API_KEY"] = api_key
        print("Loaded NEXON_OPEN_API_KEY from User Environment registry.")
    except Exception as e:
        pass

if not api_key:
    print("API_AUTH = FAIL")
    print("Error: NEXON_OPEN_API_KEY environment variable is missing.")
    sys.exit(1)

# Masked check
masked = api_key[:4] + "..." + api_key[-4:] if len(api_key) > 8 else "***"
print(f"API key detected: {masked} (length: {len(api_key)})")

url = "https://open.api.nexon.com/fconline/v1/ranker-stats"
headers = {
    "x-nxopen-api-key": api_key
}
params = {
    "matchtype": 52
}

try:
    response = requests.get(url, headers=headers, params=params, timeout=10)
    print(f"HTTP Status Code: {response.status_code}")
    if response.status_code == 200:
        print("API_AUTH = PASS")
    else:
        print("API_AUTH = FAIL")
        print(f"HTTP Error: {response.status_code} - {response.text}")
except Exception as e:
    print("API_AUTH = FAIL")
    print(f"Request Exception: {str(e)}")
