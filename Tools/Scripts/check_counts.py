# -*- coding: utf-8 -*-
import os

path = r"E:\Game\Garena\FCOnline"
counts = {}

for item in os.listdir(path):
    fp = os.path.join(path, item)
    if os.path.isdir(fp):
        cnt = 0
        sz = 0
        for r, _, fnames in os.walk(fp):
            for f in fnames:
                cnt += 1
                try:
                    sz += os.path.getsize(os.path.join(r, f))
                except Exception:
                    pass
        counts[item] = (cnt, sz)
    else:
        counts[item] = (1, os.path.getsize(fp))

for name, (c, s) in sorted(counts.items(), key=lambda x: x[1][0], reverse=True):
    safe_name = name.encode("ascii", "replace").decode()
    print(f"{c:>6} files | {s/1024/1024:>10.2f} MB | {safe_name}")
