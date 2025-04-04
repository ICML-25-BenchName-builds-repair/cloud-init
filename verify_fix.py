#!/usr/bin/env python3

"""
Simple script to verify that the fix for the pipe operator issue works.
"""

import sys
import re

def check_file_for_pipe_operator(file_path):
    """Check if a file contains the pipe operator for type unions."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Look specifically for the lines that were causing issues
    for i, line in enumerate(lines, 1):
        if "dhclient_lease_directory:" in line and "str | None" in line:
            print(f"Line {i}: Found pipe operator in type annotation: {line.strip()}")
            return False
        if "dhclient_lease_file_regex:" in line and "str | None" in line:
            print(f"Line {i}: Found pipe operator in type annotation: {line.strip()}")
            return False
    
    print("No pipe operator found in the problematic type annotations.")
    return True

if __name__ == "__main__":
    file_path = "cloudinit/distros/__init__.py"
    if check_file_for_pipe_operator(file_path):
        print("Fix verified: No pipe operator found in the problematic type annotations.")
        sys.exit(0)
    else:
        print("Fix failed: Pipe operator still found in type annotations.")
        sys.exit(1)