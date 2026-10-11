import requests
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

test_urls = [
    ('Del Piero HOT', 'https://fcoplayers.com/players/alessandro-del-piero-mua-hot'),
    ('Gullit HOT', 'https://fcoplayers.com/players/ruud-gullit-mua-hot'),
    ('Hennessey HOT', 'https://fcoplayers.com/players/wayne-hennessey-mua-hot'),
    ('Aubameyang LH', 'https://fcoplayers.com/players/pierre-emerick-aubameyang-mua-lh'),
    ('Inaki Williams HOT', 'https://fcoplayers.com/players/inaki-williams-mua-hot'),
    ('Williams HOT', 'https://fcoplayers.com/players/williams-mua-hot'),
    ('Ramos 19UCL', 'https://fcoplayers.com/players/sergio-ramos-mua-19ucl'),
    ('Ramos 19', 'https://fcoplayers.com/players/sergio-ramos-mua-19'),
    ('Rodri 19UCL', 'https://fcoplayers.com/players/rodrigo-hernandez-cascante-mua-19ucl'),
    ('Rodri 19', 'https://fcoplayers.com/players/rodrigo-hernandez-cascante-mua-19'),
    ('Rodri 19 short', 'https://fcoplayers.com/players/rodri-mua-19ucl'),
]

for name, url in test_urls:
    r = requests.get(url, headers=headers, timeout=10)
    print(f"{name:<20}: HTTP {r.status_code} -> {url}")
