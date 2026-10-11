import urllib.request
import re

url = 'https://fifaaddict.com/fo4db/pid228184484'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as r:
        html = r.read().decode('utf-8', errors='ignore')
    
    # search for traits
    matches = re.findall(r'<div class="trait_box".*?</div>', html, re.DOTALL)
    if matches:
        print("Matches found in trait_box:")
        for m in matches:
            print(m)
    else:
        # search for any trait
        print("Searching for trait images...")
        imgs = re.findall(r'<img[^>]+alt="([^"]+)"[^>]+title="([^"]+)"', html)
        for img in imgs:
            print(img)
        # print around 'Trait'
        pos = html.find('Trait')
        while pos != -1:
            print(html[pos:pos+300])
            pos = html.find('Trait', pos+1)
except Exception as e:
    print('Error:', e)
