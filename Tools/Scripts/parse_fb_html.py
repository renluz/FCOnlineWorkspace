import os, re
from bs4 import BeautifulSoup

html_path = r'e:\Game\Garena\fifa\CỘNG ĐỒNG GIẢ LẬP XẾP HẠNG FC ONLINE _ Facebook.html'
print(f"File exists: {os.path.exists(html_path)}")
print(f"File size: {os.path.getsize(html_path) / 1024 / 1024:.2f} MB")

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Parse using BeautifulSoup if available or regex
try:
    soup = BeautifulSoup(html, 'html.parser')
    # Find all divs with dir="auto"
    divs = soup.find_all('div', attrs={'dir': 'auto'})
    print(f"Found {len(divs)} divs with dir='auto'")
    
    unique_texts = []
    seen = set()
    for d in divs:
        txt = d.get_text(strip=True)
        if len(txt) > 20 and txt not in seen:
            # Filter out generic Facebook UI text
            if not any(skip in txt for skip in ["Thích", "Bình luận", "Chia sẻ", "Viết bình luận", "Tất cả bình luận"]):
                unique_texts.append(txt)
                seen.add(txt)
                
    print(f"Filtered to {len(unique_texts)} interesting text blocks:")
    with open(r'e:\Game\Garena\fifa\extracted_posts.txt', 'w', encoding='utf-8') as out:
        for idx, t in enumerate(unique_texts):
            out.write(f"--- POST/COMMENT #{idx+1} ---\n{t}\n\n")
    print("Wrote extracted_posts.txt successfully")

except Exception as e:
    print("BeautifulSoup error, trying regex:", e)
