import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_chunk2.js', 'r', encoding='utf-8') as f:
    content = f.read()

# search for bt
matches = [m.start() for m in re.finditer(r'\bbt\b', content)]
print(f"Occurrences of bt: {len(matches)}")
for idx in matches:
    print(content[max(0, idx - 150):min(len(content), idx + 200)])
    print("="*40)
