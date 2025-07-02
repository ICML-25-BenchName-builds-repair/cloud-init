#!/usr/bin/env python3
"""
Script to reproduce the pylint issue.
"""

import subprocess
import sys

def run_pylint():
    """Run pylint on the specific test file that's failing."""
    print("Running pylint on the test file that's failing...")
    
    cmd = [
        sys.executable, "-m", "pylint", 
        "tests/unittests/test_net_activators.py"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        print("STDOUT:")
        print(result.stdout)
        print("\nSTDERR:")
        print(result.stderr)
        print(f"\nReturn code: {result.returncode}")
        return result.returncode
    except Exception as e:
        print(f"Error running pylint: {e}")
        return 1

def check_syntax_warnings():
    """Check for syntax warnings in setup.py."""
    print("\nChecking for syntax warnings in setup.py...")
    
    cmd = [sys.executable, "-c", "import setup"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        print("STDOUT:")
        print(result.stdout)
        print("\nSTDERR:")
        print(result.stderr)
        print(f"\nReturn code: {result.returncode}")
        return result.returncode
    except Exception as e:
        print(f"Error checking syntax: {e}")
        return 1

if __name__ == "__main__":
    print("=== Reproducing pylint issue ===")
    
    # First check for syntax warnings
    check_syntax_warnings()
    
    # Then run pylint
    exit_code = run_pylint()
    
    if exit_code != 0:
        print("\n✗ Pylint failed as expected")
    else:
        print("\n✓ Pylint passed")
    
    sys.exit(exit_code)