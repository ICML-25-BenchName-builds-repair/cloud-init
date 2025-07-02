#!/usr/bin/env python3
"""
Simple test to demonstrate the union syntax issue.
This simulates the CI environment which runs on Python 3.8 (ubuntu-20.04).
"""

import ast
import sys

def test_union_syntax():
    """Test if the union syntax is valid in different Python versions."""
    
    # Code with Python 3.10+ union syntax (problematic)
    code_with_new_syntax = '''
class TestClass:
    field1: str | None = None
    field2: str | None = None
'''
    
    # Code with older union syntax (compatible)
    code_with_old_syntax = '''
from typing import Optional

class TestClass:
    field1: Optional[str] = None
    field2: Optional[str] = None
'''
    
    print(f"Testing on Python {sys.version}")
    print("=" * 50)
    
    # Test new syntax with different Python versions
    print("Testing new syntax (str | None):")
    try:
        # Try to compile with Python 3.8 compatibility
        compile(code_with_new_syntax, '<string>', 'exec')
        if sys.version_info >= (3, 10):
            print("✓ New syntax works (Python 3.10+)")
        else:
            print("✓ New syntax works (unexpected for Python < 3.10)")
    except SyntaxError as e:
        print(f"✗ New syntax failed: {e}")
        print("  This is expected for Python < 3.10")
    
    # Test old syntax
    print("\nTesting old syntax (Optional[str]):")
    try:
        compile(code_with_old_syntax, '<string>', 'exec')
        print("✓ Old syntax works (compatible with all Python versions)")
    except SyntaxError as e:
        print(f"✗ Old syntax failed: {e}")
    
    # Test the actual problematic lines from the file
    print("\nTesting actual problematic lines from cloudinit/distros/__init__.py:")
    problematic_code = '''
class Distro:
    dhclient_lease_directory: str | None = None
    dhclient_lease_file_regex: str | None = None
'''
    
    try:
        compile(problematic_code, '<string>', 'exec')
        if sys.version_info >= (3, 10):
            print("✓ Problematic code works (Python 3.10+)")
            print("  But will fail on CI (ubuntu-20.04 uses Python 3.8)")
        else:
            print("✓ Problematic code works (unexpected)")
    except SyntaxError as e:
        print(f"✗ Problematic code failed: {e}")
        print("  This is the error that occurs on CI")
    
    # Show the fix
    print("\nTesting the fix (using Optional[str]):")
    fixed_code = '''
from typing import Optional

class Distro:
    dhclient_lease_directory: Optional[str] = None
    dhclient_lease_file_regex: Optional[str] = None
'''
    
    try:
        compile(fixed_code, '<string>', 'exec')
        print("✓ Fixed code works (compatible with all Python versions)")
    except SyntaxError as e:
        print(f"✗ Fixed code failed: {e}")

def simulate_python38_check():
    """Simulate what happens on Python 3.8 (CI environment)."""
    print("\n" + "=" * 60)
    print("SIMULATING CI ENVIRONMENT (Python 3.8 on ubuntu-20.04)")
    print("=" * 60)
    
    # This is what the CI sees
    problematic_lines = [
        "    dhclient_lease_directory: str | None = None",
        "    dhclient_lease_file_regex: str | None = None"
    ]
    
    print("Problematic lines that cause CI to fail:")
    for i, line in enumerate(problematic_lines, 154):
        print(f"Line {i}: {line}")
    
    print("\nExpected CI errors:")
    print("mypy: X | Y syntax for unions requires Python 3.10")
    print("pylint: unsupported operand type(s) for |")
    
    print("\nProposed fix:")
    fixed_lines = [
        "    dhclient_lease_directory: Optional[str] = None",
        "    dhclient_lease_file_regex: Optional[str] = None"
    ]
    
    for i, line in enumerate(fixed_lines, 154):
        print(f"Line {i}: {line}")

if __name__ == "__main__":
    test_union_syntax()
    simulate_python38_check()