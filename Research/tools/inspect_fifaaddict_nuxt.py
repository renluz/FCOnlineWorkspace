import requests
import re

headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://fifaaddict.com/fo4db', headers=headers)
scripts = re.findall(r'src="([^"]+)"', r.text)
for script in scripts:
    if any(k in script for k in ['app', 'pages', 'fo4db']):
        full_url = 'https://fifaaddict.com' + script if script.startswith('/') else script
        try:
            js = requests.get(full_url, headers=headers).text
            # Look for api endpoints or search keywords
            matches = re.findall(r'https?://[^\s"\']+', js)
            api_matches = [m for m in matches if 'api' in m or 'search' in m or 'fifaaddict' in m]
            if api_matches:
                print(f"File {script}:")
                for m in set(api_matches):
                    print("  ", m)
            # Check url params
            params = re.findall(r'params:\{([^}]+)\}', js)
            if params:
                print("  Params:", params[:3])
        except Exception as e:
            print("Error:", e)
