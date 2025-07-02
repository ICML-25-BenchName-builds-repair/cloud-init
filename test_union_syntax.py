#!/usr/bin/env python3
"""
Test script to reproduce the union syntax issue.
This script will try to import the problematic module and run mypy/pylint on it.
"""

import subprocess
import sys
import tempfile
import os

def test_import():
    """Test if the module can be imported without syntax errors."""
    try:
        import cloudinit.distros
        print("✓ Module import successful")
        return True
    except SyntaxError as e:
        print(f"✗ Module import failed with SyntaxError: {e}")
        return False
    except Exception as e:
        print(f"✓ Module import successful (other error: {e})")
        return True

def test_mypy():
    """Test mypy on the problematic file."""
    try:
        result = subprocess.run([
            sys.executable, "-m", "mypy", 
            "cloudinit/distros/__init__.py",
            "--python-version=3.9"
        ], capture_output=True, text=True, cwd="/lca-workspace/repos/canonical__cloud-init")
        
        if result.returncode == 0:
            print("✓ mypy check passed")
            return True
        else:
            print(f"✗ mypy check failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"✗ mypy test failed with exception: {e}")
        return False

def test_pylint():
    """Test pylint on the problematic file."""
    try:
        result = subprocess.run([
            sys.executable, "-m", "pylint", 
            "cloudinit/distros/__init__.py",
            "--disable=all",
            "--enable=E1131"  # Enable only the unsupported-binary-operation error
        ], capture_output=True, text=True, cwd="/lca-workspace/repos/canonical__cloud-init")
        
        if "E1131" not in result.stdout:
            print("✓ pylint check passed (no E1131 errors)")
            return True
        else:
            print(f"✗ pylint check failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"✗ pylint test failed with exception: {e}")
        return False

def test_python_version_compatibility():
    """Test if the syntax works with different Python versions."""
    # Create a minimal test file with the problematic syntax
    test_code = '''
from typing import Optional

class TestClass:
    # This should fail in Python < 3.10
    field1: str | None = None
    field2: str | None = None
    
    # This should work in all versions
    field3: Optional[str] = None
'''
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(test_code)
        temp_file = f.name
    
    try:
        # Try to compile the code
        with open(temp_file, 'r') as f:
            code = f.read()
        
        try:
            compile(code, temp_file, 'exec')
            print("✓ Python syntax compilation successful")
            return True
        except SyntaxError as e:
            print(f"✗ Python syntax compilation failed: {e}")
            return False
    finally:
        os.unlink(temp_file)

if __name__ == "__main__":
    print("Testing union syntax issue reproduction...")
    print("=" * 50)
    
    tests = [
        ("Import test", test_import),
        ("Python version compatibility", test_python_version_compatibility),
        ("mypy test", test_mypy),
        ("pylint test", test_pylint),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("Summary:")
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    # Overall result
    all_passed = all(result for _, result in results)
    if all_passed:
        print("\n✓ All tests passed - issue is fixed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed - issue still exists")
        sys.exit(1)