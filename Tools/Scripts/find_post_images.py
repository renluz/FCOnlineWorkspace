import os, sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

html_path = r'e:\Game\Garena\fifa\CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

imgs = soup.find_all('img')
print(f"Total img tags: {len(imgs)}")
for img in imgs:
    src = img.get('src', '')
    alt = img.get('alt', '')
    if any(ext in src for ext in ['.jpg', '.png', '.webp']):
        parent_post = img.find_parent('div', attrs={'role': 'article'})
        parent_text = ""
        if parent_post:
            parent_text = parent_post.get_text(separator=" | ", strip=True)[:150]
        print(f"SRC: {src[:60]}... | ALT: {alt} | Context: {parent_text}")
