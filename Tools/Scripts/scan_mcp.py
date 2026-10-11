import os

repo_path = r'E:\FCOnlineWorkspace\Research\repos\fconline-mcp'
findings = []
for root, dirs, files in os.walk(repo_path):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        full_path = os.path.join(root, f)
        rel = os.path.relpath(full_path, repo_path)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
            for bad in ['child_process', 'registry', 'reg.exe', 'cmd.exe', 'cookie', 'rmSync', 'unlink', 'eval(', 'Function(']:
                if bad in content:
                    findings.append((rel, bad))

print("Total findings:", len(findings))
for rel, bad in findings:
    print(f"File: {rel} - Suspicious keyword: {bad}")
