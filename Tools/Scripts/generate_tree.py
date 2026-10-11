# generate_tree.py
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"E:\FCOnlineWorkspace\Research"
ignore_dirs = {".git", ".venv", "node_modules", "__pycache__"}

def print_tree(dir_path, prefix=""):
    try:
        entries = sorted(os.listdir(dir_path))
    except Exception as e:
        return
    
    # Filter entries
    filtered = [e for e in entries if e not in ignore_dirs]
    
    for i, entry in enumerate(filtered):
        is_last = (i == len(filtered) - 1)
        connector = "└── " if is_last else "├── "
        full_path = os.path.join(dir_path, entry)
        
        print(f"{prefix}{connector}{entry}")
        
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(full_path, new_prefix)

print("E:\\FCOnlineWorkspace\\Research")
print_tree(root_dir)
