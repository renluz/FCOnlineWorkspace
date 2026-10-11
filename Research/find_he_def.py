import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Search for definition of He
for fn in ['e:/FCOnlineWorkspace/Research/epl_index.js', 'e:/FCOnlineWorkspace/Research/epl_chunk2.js']:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = [m.start() for m in re.finditer(r'(?:const|let|var|function)\s+He\b', content)]
    print(f"File {fn}: {len(matches)} matches")
    for idx in matches:
        print(content[max(0, idx - 50):min(len(content), idx + 250)])
