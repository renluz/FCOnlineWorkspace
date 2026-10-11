import urllib.request
import re

url = "https://cdn.vn.garenanow.com/web/aov/static/fco-data-center/live/assets/index-CDqBgm-p.js"
js = urllib.request.urlopen(url).read().decode('utf-8')
strings = set(re.findall(r'\"(/[^\"]+)\"', js))
for s in strings:
    if 'player' in s:
        print(s)
