#!/usr/bin/env python3

"""
Simple test for pylint.
"""

from typing import Optional

class TestClass:
    """Test class with Optional type annotation."""
    value: Optional[str] = None

if __name__ == "__main__":
    test = TestClass()
    print(test.value)