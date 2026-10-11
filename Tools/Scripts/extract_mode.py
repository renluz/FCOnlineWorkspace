import urllib.request
import re
url = "https://cdn.vn.garenanow.com/web/aov/static/fco-data-center/live/assets/index-CDqBgm-p.js"
js = urllib.request.urlopen(url).read().decode('utf-8')
print(set(re.findall(r'mode\:\"([^\"]+)\"', js)))
print(set(re.findall(r'mode:\"([^\"]+)\"', js)))
