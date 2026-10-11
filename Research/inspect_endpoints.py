import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_chunk2.js', 'r', encoding='utf-8') as f:
    content = f.read()

paths = [
    '/user/redeem-code',
    '/user/claim-free-points',
    '/user/update-daily',
    '/user/choose-support-team',
    '/user/spin',
    '/user/exchange',
    '/user/join-group'
]

for p in paths:
    idx = 0
    print(f"\n==================== {p} ====================")
    while True:
        idx = content.find(p, idx)
        if idx == -1:
            break
        start = max(0, idx - 250)
        end = min(len(content), idx + 350)
        print(f"--- Pos {idx} ---")
        print(content[start:end])
        idx += len(p)
