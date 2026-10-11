import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all occurrences of "Nhiệm vụ" or similar
pos = 0
while True:
    idx = content.find("Nhiệm vụ", pos)
    if idx == -1:
        break
    start = max(0, idx - 200)
    end = min(len(content), idx + 400)
    print(f"--- MATCH AT {idx} ---")
    print(content[start:end])
    print("="*50)
    pos = idx + len("Nhiệm vụ")

print("\n=== SEARCH FOR ALL API CALLS IN THE APP ===")
# Look for request/api definitions
# Often axios.create({baseURL: '/api' ...}) or similar
api_methods = re.findall(r'([a-zA-Z0-9_$]+)\s*:\s*function\s*\([^)]*\)\s*\{\s*return\s+[^}]+\.(?:get|post)\([^}]+\)\s*\}', content)
print(f"API methods count: {len(api_methods)}")

# Let's print all URLs containing /api/
api_urls = re.findall(r'["\'](/api/[^"\']*)["\']', content)
print("API URLs:", sorted(set(api_urls)))

