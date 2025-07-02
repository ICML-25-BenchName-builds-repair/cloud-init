#!/usr/bin/env python3
"""
Test script to verify that the union syntax fix has been applied correctly.
"""

import ast
import sys

def test_fixed_file():
    """Test that the actual file no longer contains problematic union syntax."""
    
    print("Verifying the fix in cloudinit/distros/__init__.py")
    print("=" * 60)
    
    # Read the actual file
    with open('cloudinit/distros/__init__.py', 'r') as f:
        content = f.read()
    
    # Check for problematic patterns
    problematic_patterns = [
        'str | None',
        ': str|None',
        ':str | None',
        ':str|None'
    ]
    
    found_issues = []
    for pattern in problematic_patterns:
        if pattern in content:
            found_issues.append(pattern)
    
    if found_issues:
        print(f"✗ Found problematic union syntax: {found_issues}")
        return False
    else:
        print("✓ No problematic union syntax found")
    
    # Check that Optional is used instead
    if 'Optional[str]' in content:
        print("✓ Found Optional[str] usage (correct)")
    else:
        print("✗ No Optional[str] usage found")
        return False
    
    # Check specific lines
    lines = content.split('\n')
    
    # Check line 154 (0-indexed: 153)
    if len(lines) > 153:
        line_154 = lines[153].strip()
        if 'dhclient_lease_directory: Optional[str] = None' in line_154:
            print("✓ Line 154 correctly uses Optional[str]")
        else:
            print(f"✗ Line 154 issue: {line_154}")
            return False
    
    # Check line 158 (0-indexed: 157)
    if len(lines) > 157:
        line_158 = lines[157].strip()
        if 'dhclient_lease_file_regex: Optional[str] = None' in line_158:
            print("✓ Line 158 correctly uses Optional[str]")
        else:
            print(f"✗ Line 158 issue: {line_158}")
            return False
    
    # Try to parse the file
    try:
        ast.parse(content)
        print("✓ File parses successfully")
    except SyntaxError as e:
        print(f"✗ File has syntax error: {e}")
        return False
    
    # Try to import the module
    try:
        import cloudinit.distros
        print("✓ Module imports successfully")
    except Exception as e:
        print(f"✗ Module import failed: {e}")
        return False
    
    return True

def test_compatibility():
    """Test that the fix maintains compatibility."""
    
    print("\nTesting compatibility...")
    print("=" * 30)
    
    # Test that Optional[str] works the same as str | None
    from typing import Optional
    
    # These should be equivalent
    def func_optional(param: Optional[str] = None) -> Optional[str]:
        return param
    
    # Test with None
    result1 = func_optional(None)
    if result1 is None:
        print("✓ Optional[str] works with None")
    else:
        print("✗ Optional[str] failed with None")
        return False
    
    # Test with string
    result2 = func_optional("test")
    if result2 == "test":
        print("✓ Optional[str] works with string")
    else:
        print("✗ Optional[str] failed with string")
        return False
    
    return True

if __name__ == "__main__":
    print("Verifying union syntax fix...")
    print("=" * 60)
    
    success1 = test_fixed_file()
    success2 = test_compatibility()
    
    print("\n" + "=" * 60)
    if success1 and success2:
        print("✓ All verification tests passed! Fix is successful.")
        sys.exit(0)
    else:
        print("✗ Some verification tests failed.")
        sys.exit(1)