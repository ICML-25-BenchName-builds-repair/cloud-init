#!/usr/bin/env python3

# This script tests the mypy issue with the union operator syntax

from typing import Union

# This is the old style that should work with mypy 0.950
var1: Union[str, None] = None

# This is the new style that requires Python 3.10+ and newer mypy
# This should fail with mypy 0.950
var2: str | None = None

# Class attribute with the same issue
class TestClass:
    attr1: Union[str, None] = None  # This should work
    attr2: str | None = None  # This should fail with mypy 0.950

print("Test completed")