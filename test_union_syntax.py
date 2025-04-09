#!/usr/bin/env python3

"""
Simple script to verify that the union syntax in cloudinit/distros/__init__.py
is compatible with older Python versions.
"""

import sys
import re

def check_file(file_path):
    """Check if the file contains Python 3.10 union syntax."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Look for patterns like "var_name: type1 | type2"
    union_syntax_pattern = r'\w+\s*:\s*\w+\s*\|\s*\w+'
    matches = re.findall(union_syntax_pattern, content)
    
    if matches:
        print(f"Found Python 3.10 union syntax in {file_path}:")
        for match in matches:
            print(f"  - {match}")
        return False
    else:
        print(f"No Python 3.10 union syntax found in {file_path}")
        return True

if __name__ == "__main__":
    file_path = "cloudinit/distros/__init__.py"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    result = check_file(file_path)
    sys.exit(0 if result else 1)