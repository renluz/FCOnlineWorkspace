import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("baseURL")
while idx != -1:
    print(f"=== baseURL at {idx} ===")
    print(content[max(0, idx - 100):min(len(content), idx + 1000)])
    idx = content.find("baseURL", idx + 1)
