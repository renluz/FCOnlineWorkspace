import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('e:/FCOnlineWorkspace/Research/epl_index.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for "Bấm nhận điểm" or "nhận điểm" or "chia sẻ" or "QUAY" or "DỰ ĐOÁN"
keywords = ["nhận điểm", "Bấm nhận điểm", "quay", "chia sẻ", "LƯỢT QUAY", "ĐỔI QUÀ"]
for kw in keywords:
    matches = [m.start() for m in re.finditer(re.escape(kw), content, re.IGNORECASE)]
    print(f"Keyword '{kw}': {len(matches)} occurrences")
    for idx in matches[:5]:
        print(f"  Pos {idx}: {content[max(0, idx-50):min(len(content), idx+100)]}")
