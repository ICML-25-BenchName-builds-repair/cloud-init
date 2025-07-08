#!/usr/bin/env python3

import subprocess
import sys

def run_ruff_check():
    """Run ruff linter on the codebase and check for F401 error in test_wsl.py."""
    cmd = ["python3", "-m", "ruff", "tests/unittests/sources/test_wsl.py"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    print("STDOUT:")
    print(result.stdout)
    print("STDERR:")
    print(result.stderr)
    
    # Check if the specific error is present
    if "F401 [*] `typing.Optional` imported but unused" in result.stdout:
        print("\nFound the specific error: F401 [*] `typing.Optional` imported but unused")
        return True
    else:
        print("\nDid not find the specific error")
        return False

if __name__ == "__main__":
    print("Running ruff check to reproduce the issue...")
    issue_found = run_ruff_check()
    
    if issue_found:
        print("Successfully reproduced the issue!")
        sys.exit(1)
    else:
        print("Issue not reproduced or already fixed.")
        sys.exit(0)