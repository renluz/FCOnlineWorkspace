import urllib.request
import re

url = "https://cdn.vn.garenanow.com/web/aov/static/fco-data-center/live/assets/index-CDqBgm-p.js"
js = urllib.request.urlopen(url).read().decode('utf-8')
matches = re.findall(r'[^\{]*(players/tiers)[^\}]*', js)
# Instead of regex, let's just find the index of "players/tiers" and print 100 chars around it
idx = js.find('players/tiers')
while idx != -1:
    print(js[max(0, idx-100):min(len(js), idx+100)])
    idx = js.find('players/tiers', idx+1)
