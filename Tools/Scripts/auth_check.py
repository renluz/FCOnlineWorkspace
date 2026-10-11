# auth_check.py
import os
import sys
import requests

DOTENV_PATH = r"E:\FCOnlineWorkspace\Research\.env"

def get_api_key():
    # Only read from environment variable or project .env
    key = os.environ.get("NEXON_OPEN_API_KEY")
    if not key and os.path.exists(DOTENV_PATH):
        try:
            with open(DOTENV_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("NEXON_OPEN_API_KEY="):
                        key = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break
        except Exception as e:
            pass
    return key

api_key = get_api_key()

if not api_key:
    print("API_AUTH=FAIL")
    print("Error: NEXON_OPEN_API_KEY is not found in process environment or E:\\FCOnlineWorkspace\\Research\\.env")
    sys.exit(0)

# Check endpoint specified in prompt:
# GET https://open.api.nexon.com/fconline/v1/match?matchtype=52&offset=0&limit=1&orderby=desc
url = "https://open.api.nexon.com/fconline/v1/match"
params = {
    "matchtype": 52,
    "offset": 0,
    "limit": 1,
    "orderby": "desc"
}
headers = {
    "x-nxopen-api-key": api_key,
    "User-Agent": "FCOnlineResearch-GLXH/2.0"
}

try:
    resp = requests.get(url, params=params, headers=headers, timeout=10)
    if resp.status_code == 200:
        print("API_AUTH=PASS")
        print(f"Status: {resp.status_code}")
        # Note: do not print body if it contains sensitive data, but match array is just match IDs
        print(f"Matches sample count: {len(resp.json()) if isinstance(resp.json(), list) else 'non-list'}")
    else:
        print("API_AUTH=FAIL")
        print(f"HTTP Status: {resp.status_code}")
        try:
            err = resp.json()
            err_name = err.get("error", {}).get("name", "UnknownError")
            err_msg = err.get("error", {}).get("message", resp.text)
            print(f"Error Name: {err_name}")
            print(f"Error Message: {err_msg}")
        except Exception:
            print(f"Response: {resp.text}")
except Exception as e:
    print("API_AUTH=FAIL")
    print(f"Request Exception: {str(e)}")
