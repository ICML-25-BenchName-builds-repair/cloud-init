#!/usr/bin/env python3
"""
Simple script to verify the ruff linting issue in test_wsl.py
"""

import subprocess
import sys

def main():
    """Run ruff on the test_wsl.py file and check for F401 errors."""
    cmd = ["python", "-m", "ruff", "tests/unittests/sources/test_wsl.py"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print("Ruff output:")
    print(result.stdout)
    
    if "F401" in result.stdout and "Optional" in result.stdout:
        print("\nIssue confirmed: F401 error for unused import 'Optional'")
        return 1
    else:
        print("\nNo F401 error found for 'Optional'")
        return 0

if __name__ == "__main__":
    sys.exit(main())