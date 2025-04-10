#!/usr/bin/env python3

"""
This script verifies the ruff linting issue in the test_wsl.py file.
"""

import subprocess

def run_ruff_on_file(file_path):
    """Run ruff on a specific file and return the output."""
    try:
        result = subprocess.run(
            ["ruff", file_path],
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout, result.returncode
    except Exception as e:
        return str(e), 1

if __name__ == "__main__":
    # Install ruff if not already installed
    subprocess.run(["pip", "install", "ruff===0.0.285"], check=True)
    
    # Run ruff on the test_wsl.py file
    file_path = "tests/unittests/sources/test_wsl.py"
    output, exit_code = run_ruff_on_file(file_path)
    
    print(f"Ruff output for {file_path}:")
    print(output)
    print(f"Exit code: {exit_code}")
    
    # Check if the issue is related to unused imports
    if "F401" in output and "typing.Optional" in output:
        print("\nIssue confirmed: 'typing.Optional' is imported but unused in the file.")
        print("This needs to be fixed in the DataSourceWSL.py file.")
    else:
        print("\nThe expected issue was not found.")