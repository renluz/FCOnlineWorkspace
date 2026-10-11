# check_proc_env.py
import ctypes
import ctypes.wintypes as wintypes
import os

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

# Check running processes with cmd.exe or powershell
import subprocess
out = subprocess.check_output("tasklist /FI \"USERNAME eq desktop-6c7ds1q\\phucvu\" /FO CSV", shell=True).decode('cp1252', errors='ignore')
print("Running processes for phucvu:")
for line in out.strip().split('\n'):
    if any(k in line.lower() for k in ['cmd', 'powershell', 'pwsh', 'terminal', 'code', 'antigravity']):
        print(line.strip())
