import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_chunk2.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("const Qo=")
if idx != -1:
    print(content[idx:idx+2500])
