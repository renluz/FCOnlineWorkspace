import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# search for fetch, $.ajax, $.post, $.get, axios
print("--- fetch calls ---")
fetches = re.findall(r'fetch\s*\([^)]+\)', content)
print("fetch:", fetches[:10])

print("--- ajax calls ---")
ajax = re.findall(r'\$\.(?:ajax|post|get)\([^)]+\)', content)
print("ajax:", ajax[:10])

print("--- axios create or other instances ---")
axios_instances = re.findall(r'[a-zA-Z0-9_$]+\.create\(\{[^}]+\}\)', content)
print("axios instances:", axios_instances)

# Look for all occurrences of "/api/" or "api/"
api_refs = re.findall(r'["\']([^"\']*/api/[^"\']*)["\']', content)
print("api references:", set(api_refs))

# Let's search for action dispatches or Redux / Zustand / React Query / mutation hooks
# Look for "spin", "vote", "predict", "nhận", "claim" in function definitions
print("\n--- Searching for 'spin' / 'quay' / 'vote' functions ---")
funcs = re.findall(r'(?:const|let|var|function)\s+([a-zA-Z0-9_$]+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>[^;]{10,200}', content)
for fn in funcs:
    if any(k in fn.lower() for k in ['spin', 'vote', 'claim', 'daily', 'point', 'share', 'reward']):
        print(fn)

