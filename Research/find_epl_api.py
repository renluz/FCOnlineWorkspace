import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "chia sẻ" or "share" or "nhận điểm" or related handlers
matches = re.finditer(r'(chia sẻ|nhận điểm|claim|share|spin|vote|predict)', content, re.IGNORECASE)
found_snippets = []
for m in matches:
    start = max(0, m.start() - 150)
    end = min(len(content), m.end() + 250)
    snippet = content[start:end]
    # filter out common words if too many
    found_snippets.append((m.start(), snippet))

print(f"Total matches: {len(found_snippets)}")

# Let's inspect unique areas around POST / GET or fetch / axios
# In Vite/Webpack bundles, axios base URL or axios calls:
endpoints = re.findall(r'(https?://[a-zA-Z0-9_\-\.:]+)?/(?:api|user|event|v1|ajax)/[a-zA-Z0-9_\-\./\?=&]+', content)
print("Endpoints found:", set(endpoints))

# Let's search for functions that call backend
# Look for baseURL
base_urls = re.findall(r'baseURL\s*:\s*["\']([^"\']+)["\']', content)
print("BaseURLs:", base_urls)

# Look for post requests
post_calls = re.findall(r'\.post\(\s*[`\'"]([^`\'"]+)[`\'"]', content)
print("POST endpoints:", set(post_calls))

# Look for get requests
get_calls = re.findall(r'\.get\(\s*[`\'"]([^`\'"]+)[`\'"]', content)
print("GET endpoints:", set(get_calls))
