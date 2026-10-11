import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all base URLs / APIs
print("=== All Axios or Fetch calls ===")
calls = re.findall(r'(?:get|post|put|delete)\s*\(\s*[`\'"]([^`\'"]+)[`\'"]', content)
for c in sorted(set(calls)):
    print(c)

print("\n=== Functions related to mission / task / share / giftcode ===")
# Search for axios instances or API wrappers
api_matches = re.findall(r'(\w+)\s*=\s*\{\s*[^}]*(?:mission|task|share|daily|history|claim|point)[^}]*\}', content, re.IGNORECASE)
print(f"Object matches: {len(api_matches)}")

# Search for exact Vietnamese strings related to missions
vi_matches = re.findall(r'["\']([^"\']*(?:nhiệm vụ|nhiem vu|chia sẻ|lượt|mã|nhập|code|quà|nhận)[^"\']*)["\']', content, flags=re.IGNORECASE)
print(f"\nVietnamese strings count: {len(vi_matches)}")
for s in sorted(set(vi_matches))[:50]:
    if len(s) < 100:
        print("-", s)
