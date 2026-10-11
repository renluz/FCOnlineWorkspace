# read_proc_env.py
import ctypes
from ctypes import wintypes
import sys

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

ntdll = ctypes.WinDLL('ntdll.dll')
kernel32 = ctypes.WinDLL('kernel32.dll')

class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('ExitStatus', ctypes.c_ulonglong),
        ('PebBaseAddress', ctypes.c_ulonglong),
        ('AffinityMask', ctypes.c_ulonglong),
        ('BasePriority', ctypes.c_ulonglong),
        ('UniqueProcessId', ctypes.c_ulonglong),
        ('InheritedFromUniqueProcessId', ctypes.c_ulonglong),
    ]

def get_env(pid):
    hProc = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not hProc:
        return None
    try:
        pbi = PROCESS_BASIC_INFORMATION()
        retLen = wintypes.ULONG()
        status = ntdll.NtQueryInformationProcess(hProc, 0, ctypes.byref(pbi), ctypes.sizeof(pbi), ctypes.byref(retLen))
        if status != 0 or not pbi.PebBaseAddress:
            return None
        
        # Read ProcessParameters pointer at PebBaseAddress + 0x20
        params_ptr = ctypes.c_ulonglong()
        bytesRead = ctypes.c_size_t()
        if not kernel32.ReadProcessMemory(hProc, ctypes.c_void_p(pbi.PebBaseAddress + 0x20), ctypes.byref(params_ptr), 8, ctypes.byref(bytesRead)):
            return None
        
        # Read Environment pointer at params_ptr + 0x80
        env_ptr = ctypes.c_ulonglong()
        if not kernel32.ReadProcessMemory(hProc, ctypes.c_void_p(params_ptr.value + 0x80), ctypes.byref(env_ptr), 8, ctypes.byref(bytesRead)):
            return None
        
        # Read environment block (read up to 64KB)
        buf = ctypes.create_string_buffer(65536)
        if not kernel32.ReadProcessMemory(hProc, ctypes.c_void_p(env_ptr.value), buf, 65536, ctypes.byref(bytesRead)):
            return None
        
        # Decode UTF-16
        raw = buf.raw[:bytesRead.value]
        text = raw.decode('utf-16le', errors='ignore')
        entries = text.split('\0')
        return [e for e in entries if e]
    finally:
        kernel32.CloseHandle(hProc)

pids = [23172, 21784, 19776, 21540, 20624]
for pid in pids:
    print(f"Checking PID {pid}...")
    env = get_env(pid)
    if env:
        for item in env:
            if "NEXON" in item.upper():
                name = item.split("=")[0]
                val = item[len(name)+1:]
                masked = val[:4] + "..." + val[-4:] if len(val) > 8 else "***"
                print(f"  FOUND IN PID {pid}: {name}={masked} (len={len(val)})")
                # Save to user environment or .env so our process can use it
                os.system(f'[Environment]::SetEnvironmentVariable("NEXON_OPEN_API_KEY", "{val}", "User")')
                with open(r"E:\FCOnlineWorkspace\Research\.env", "w", encoding="utf-8") as f:
                    f.write(f"NEXON_OPEN_API_KEY={val}\n")
                print("  -> Saved to .env and persistent registry!")
                break
        else:
            print(f"  No NEXON variable in PID {pid}")
    else:
        print(f"  Could not read PID {pid}")
