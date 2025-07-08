#!/usr/bin/env python3

"""
Test script for pylint.
"""

class TestClass:
    """Test class with pipe operator type annotation."""
    value: str | None = None

if __name__ == "__main__":
    test = TestClass()
    print(test.value)