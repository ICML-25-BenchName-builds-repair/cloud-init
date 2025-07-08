#!/usr/bin/env python3

"""
Test script to verify type annotation compatibility.
"""

import sys
from typing import Optional

# Python 3.10+ style
class TestPython310:
    value_310: str | None = None

# Python 3.7+ style
class TestPython37:
    value_37: Optional[str] = None

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print("Testing type annotations...")
    
    test_310 = TestPython310()
    test_37 = TestPython37()
    
    print("Python 3.10+ style:", test_310.value_310)
    print("Python 3.7+ style:", test_37.value_37)
    
    print("Test completed.")