import requests
import sys
import re
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

urls = [
    ('G. Zambrotta WG', 'https://fcoplayers.com/players/gianluca-zambrotta-mua-wg'),
    ('A. Del Piero HOT', 'https://fcoplayers.com/players/alessandro-del-piero-mua-hot'),
    ('R. Gullit HOT', 'https://fcoplayers.com/players/ruud-gullit-mua-hot'),
    ('Rodri 19', 'https://fcoplayers.com/players/rodri-mua-19ucl'),
    ('Sergio Ramos 19', 'https://fcoplayers.com/players/sergio-ramos-mua-19ucl'),
    ('Inaki Williams HOT', 'https://fcoplayers.com/players/williams-mua-hot'),
    ('W. Hennessey HOT', 'https://fcoplayers.com/players/wayne-hennessey-mua-hot'),
    ('P. Aubameyang LH', 'https://fcoplayers.com/players/pierre-emerick-aubameyang-mua-lh'),
    ('T. Rosicky WG', 'https://fcoplayers.com/players/toma-rosicky-mua-wg'),
    ('Park Ji Sung NO.7', 'https://fcoplayers.com/players/ji-sung-park-mua-no7'),
    ('V. Boniface WS', 'https://fcoplayers.com/players/victor-boniface-mua-ws'),
    ('J. Gvardiol 25DP', 'https://fcoplayers.com/players/josko-gvardiol-mua-25dp'),
    ('F. Schar 25DP', 'https://fcoplayers.com/players/fabian-schr-mua-25dp')
]

for label, url in urls:
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Check card header
    hdr = soup.find('div', class_='fo4-card-header')
    hdr_txt = hdr.get_text(' | ', strip=True) if hdr else ''
    
    # Check position boxes or badges
    # Look for fo4-pos-box or position tags
    pos_boxes = [p.get_text(strip=True) for p in soup.find_all(class_='fo4-pos-box')]
    
    # Look at all positions in OVR table
    ovr_cells = soup.find_all('div', class_='fo4-position-cell')
    
    print(f"=== {label} ===")
    print(f"  Header: {hdr_txt}")
    print(f"  Pos boxes: {pos_boxes}")
