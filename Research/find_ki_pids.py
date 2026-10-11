import urllib.request
import re
import json

url = 'https://fifaaddict.com/fo4db?keyword=Ki+Sung+Yueng'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as r:
        html = r.read().decode('utf-8', errors='ignore')
    # search for fo4db/pid
    pids = set(re.findall(r'fo4db/pid\d+', html))
    print('PIDs:', pids)
    # search for FA
    for m in re.finditer(r'Ki Sung Yueng', html):
        idx = m.start()
        print(html[max(0, idx-50):min(len(html), idx+150)])
except Exception as e:
    print('Error:', e)
