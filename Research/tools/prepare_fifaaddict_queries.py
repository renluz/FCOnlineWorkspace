import requests
import re
import sys
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Search web for fifaaddict URLs of the remaining players
queries = [
    ("Boniface WS", "site:fifaaddict.com Victor Boniface WS"),
    ("Gvardiol 25DP", "site:fifaaddict.com Josko Gvardiol 25DP"),
    ("Rosicky WG", "site:fifaaddict.com Tomas Rosicky WG"),
    ("Park Ji Sung NO7", "site:fifaaddict.com Ji Sung Park NO7 OR NO.7"),
    ("Schar 25DP", "site:fifaaddict.com Fabian Schar 25DP"),
    ("Rodri 19UCL", "site:fifaaddict.com Rodri 19UCL"),
    ("Ramos 19UCL", "site:fifaaddict.com Sergio Ramos 19UCL"),
    ("Hennessey HOT", "site:fifaaddict.com Wayne Hennessey HOT"),
    ("Williams HOT", "site:fifaaddict.com Inaki Williams HOT"),
    ("Aubameyang LH", "site:fifaaddict.com Pierre-Emerick Aubameyang LH")
]

print("Ready to search.")
