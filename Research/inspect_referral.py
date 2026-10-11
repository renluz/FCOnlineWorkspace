import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_chunk2.js', 'r', encoding='utf-8') as f:
    content = f.read()

for m in re.finditer(r'referral_code|referral_prizes|referred', content):
    idx = m.start()
    print(f"--- Ref to {m.group(0)} at {idx} ---")
    print(content[max(0, idx - 150):min(len(content), idx + 250)])
