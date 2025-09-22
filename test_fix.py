#!/usr/bin/env python3

"""
Simple test script to verify the fix for the union operator syntax issue.
"""

import sys
from typing import Optional, Union

# Test with Optional[str]
var1: Optional[str] = None
print(f"var1: {var1}, type annotation: Optional[str]")

# For comparison, if Python version >= 3.10, also test with str | None
if sys.version_info >= (3, 10):
    var2: str | None = None
    print(f"var2: {var2}, type annotation: str | None")
else:
    print("Python version < 3.10, cannot use union operator syntax")

print(f"Python version: {sys.version}")