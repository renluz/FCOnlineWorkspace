import os, sys
sys.stdout.reconfigure(encoding='utf-8')

repo_dir = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search'

for fn in os.listdir(repo_dir):
    if fn.endswith('.py'):
        full_path = os.path.join(repo_dir, fn)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            if 'subprocess' in line or 'os.system' in line:
                print(f"{fn}:{idx+1}: {line.strip()}")
