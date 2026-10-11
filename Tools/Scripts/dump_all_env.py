# dump_all_env.py
import os

print("All env var keys in current process:")
for k in sorted(os.environ.keys()):
    if any(term in k.lower() for term in ["nexon", "api", "key", "fc", "token", "auth"]):
        print(f"  {k} (len={len(os.environ[k])})")

print("\nTotal env vars:", len(os.environ))
