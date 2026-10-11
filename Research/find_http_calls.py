import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# find all references to already_shared or shared
for m in re.finditer(r'already_shared|not_played_in_day|not_enough_spins|claimMessage', content):
    idx = m.start()
    print(f"--- Ref to {m.group(0)} at {idx} ---")
    print(content[max(0, idx - 200):min(len(content), idx + 300)])

# find all occurrences of .post( or .get( or axios methods
print("\n--- All calls to HTTP methods ---")
all_http = re.finditer(r'\.(post|get|put|delete)\s*\(\s*[`\'"]([^`\'"]+)[`\'"]', content)
for h in all_http:
    print(f"{h.group(1).upper()} {h.group(2)}")
