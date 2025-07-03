#!/usr/bin/env python3

"""
Test script to verify the issue with Python 3.10+ union syntax.
"""

import sys
from typing import Optional, Union

# This will work in all Python versions
var1: Optional[str] = None
var2: Union[str, None] = None

# This will only work in Python 3.10+
var3: str | None = None

print(f"Python version: {sys.version}")
print("Using typing.Optional[str] and typing.Union[str, None] works in all Python versions")
print("Using 'str | None' only works in Python 3.10+")