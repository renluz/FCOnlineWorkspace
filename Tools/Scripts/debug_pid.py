# debug_pid.py
import ctypes
from ctypes import wintypes
import sys

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

kernel32 = ctypes.WinDLL('kernel32.dll')

for pid in [23172, 21784]:
    h = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    err = kernel32.GetLastError()
    print(f"PID {pid}: handle={h}, err={err}")
    if h:
        kernel32.CloseHandle(h)
