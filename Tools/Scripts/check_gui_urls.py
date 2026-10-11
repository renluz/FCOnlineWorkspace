import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

repo_dir = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search'

for fn in os.listdir(repo_dir):
    if fn.endswith('.py') and fn != 'FCDataMaker_v1.py':
        full_path = os.path.join(repo_dir, fn)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        print(f"=== File: {fn} (Lines: {len(content.splitlines())}, Size: {len(content)} bytes) ===")
        urls = re.findall(r'https?://[^\s"\'<>]+', content)
        print("URLs accessed:", list(set(urls))[:15])
