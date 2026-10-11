import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_chunk2.js', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} characters")

# find all occurrences of .post or .get or /api/
http_calls = re.findall(r'\.(post|get|put|delete)\s*\(\s*[`\'"]([^`\'"]+)[`\'"]', content)
print("HTTP calls in chunk 2:")
for method, path in sorted(set(http_calls)):
    print(f"{method.upper()}: {path}")

# find all strings containing /user/ or /api/
api_strings = re.findall(r'["\'](/user/[^"\']+)["\']', content)
print("\nUser API paths:")
for p in sorted(set(api_strings)):
    print(p)

# check if other chunks are imported
js_files = re.findall(r'["\']([^"\']+\.js)["\']', content)
print("\nJS files mentioned in chunk 2:", set(js_files))
