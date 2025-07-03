#!/usr/bin/env python3

"""
Comprehensive test to verify the fix for the union syntax issue.
"""

import os
import re
import subprocess
import sys
import tempfile

# Create a temporary file with the original problematic code
with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
    original_code = """
from typing import Optional, Union

# This will cause an error in Python < 3.10
dhclient_lease_directory: str | None = None
dhclient_lease_file_regex: str | None = None
"""
    f.write(original_code.encode())
    original_file = f.name

# Create a temporary file with the fixed code
with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
    fixed_code = """
from typing import Optional, Union

# This should work in all Python versions
dhclient_lease_directory: Optional[str] = None
dhclient_lease_file_regex: Optional[str] = None
"""
    f.write(fixed_code.encode())
    fixed_file = f.name

# Create a temporary mypy config file
with tempfile.NamedTemporaryFile(suffix='.ini', delete=False) as f:
    mypy_config = """
[mypy]
python_version = 3.7
"""
    f.write(mypy_config.encode())
    mypy_config_file = f.name

# Test the original code with mypy
print("Testing original code with mypy...")
original_result = subprocess.run(
    ["python", "-m", "mypy", "--config-file", mypy_config_file, original_file],
    capture_output=True,
    text=True
)

# Test the fixed code with mypy
print("Testing fixed code with mypy...")
fixed_result = subprocess.run(
    ["python", "-m", "mypy", "--config-file", mypy_config_file, fixed_file],
    capture_output=True,
    text=True
)

# Clean up temporary files
os.unlink(original_file)
os.unlink(fixed_file)
os.unlink(mypy_config_file)

# Print results
print("\nOriginal code mypy result:")
print(original_result.stdout)
print(original_result.stderr)
print(f"Exit code: {original_result.returncode}")

print("\nFixed code mypy result:")
print(fixed_result.stdout)
print(fixed_result.stderr)
print(f"Exit code: {fixed_result.returncode}")

# Check if our fix works
if original_result.returncode != 0 and fixed_result.returncode == 0:
    print("\nSUCCESS: The fix works! Original code fails mypy check, fixed code passes.")
    sys.exit(0)
else:
    print("\nFAILURE: Unexpected results from mypy checks.")
    sys.exit(1)