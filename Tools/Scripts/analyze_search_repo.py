import os, re

repo_dir = r'E:\FCOnlineWorkspace\Research\repos\fconline-player-search'

for fn in os.listdir(repo_dir):
    if fn.endswith('.py'):
        full_path = os.path.join(repo_dir, fn)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        print(f"=== File: {fn} (Lines: {len(content.splitlines())}, Size: {len(content)} bytes) ===")
        # Check imports
        imports = re.findall(r'^(?:from\s+[\w\.]+\s+import\s+[\w\.,\s]+|import\s+[\w\.,\s]+)', content, re.MULTILINE)
        print("Imports:", imports[:15])
        
        # Check URLs accessed
        urls = re.findall(r'https?://[^\s"\'<>]+', content)
        print("URLs accessed:", list(set(urls))[:15])
        
        # Check security
        for bad in ['os.system', 'subprocess', 'shutil.rmtree', 'registry', 'socket', 'exec(', 'eval(']:
            if bad in content:
                print(f"Warning keyword found: {bad}")
