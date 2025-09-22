#!/usr/bin/env python3

"""
This script verifies the pylint issue in the test_net_activators.py file.
"""

import os
import sys
import subprocess

def run_pylint_on_file(file_path):
    """Run pylint on a specific file and return the output."""
    result = subprocess.run(
        ["pylint", file_path],
        capture_output=True,
        text=True,
    )
    return result.stdout, result.returncode

def main():
    """Main function to test the pylint issue."""
    file_path = "tests/unittests/test_net_activators.py"
    
    print(f"Running pylint on {file_path}...")
    output, return_code = run_pylint_on_file(file_path)
    
    print("Pylint output:")
    print(output)
    
    if "E0213(no-self-argument)" in output and "E1101(no-member)" in output:
        print("\nIssue confirmed: The method 'fake_isfile_no_nmconn' needs to be fixed.")
        print("It should be decorated with @staticmethod since it doesn't use 'self'.")
    
    return return_code

if __name__ == "__main__":
    sys.exit(main())