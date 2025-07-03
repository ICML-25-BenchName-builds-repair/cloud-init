#!/usr/bin/env python3

"""
Verify that the fix for the union syntax issue works.
"""

import re
import sys

# Read the file
with open('cloudinit/distros/__init__.py', 'r') as f:
    content = f.read()

# Check for pipe operator in type annotations
pipe_operator_pattern = r':\s*str\s*\|\s*None'
matches = re.findall(pipe_operator_pattern, content)

if matches:
    print(f"ERROR: Found {len(matches)} instances of 'str | None' syntax in the file.")
    sys.exit(1)
else:
    print("SUCCESS: No instances of 'str | None' syntax found in the file.")
    
# Check for Optional[str] syntax
optional_pattern = r':\s*Optional\[str\]'
matches = re.findall(optional_pattern, content)

if matches:
    print(f"SUCCESS: Found {len(matches)} instances of 'Optional[str]' syntax in the file.")
else:
    print("ERROR: No instances of 'Optional[str]' syntax found in the file.")
    sys.exit(1)

print("Verification completed successfully!")