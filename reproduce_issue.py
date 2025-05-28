#!/usr/bin/env python3
"""
Script to reproduce the pylint issue in test_net_activators.py
"""

import subprocess
import sys

def run_pylint_on_file():
    """Run pylint on the specific file to reproduce the issue"""
    cmd = [
        sys.executable, "-m", "pylint", 
        "tests/unittests/test_net_activators.py",
        "--disable=import-error"  # Disable import errors to focus on the main issue
    ]
    
    print("Running pylint on test_net_activators.py...")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 50)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print(f"\nReturn code: {result.returncode}")
    
    # Check for the specific errors we're looking for
    expected_errors = [
        "E0213(no-self-argument)",
        "E1101(no-member), TestNetworkManagerActivatorBringUp.fake_isfile_no_nmconn"
    ]
    
    found_errors = []
    for error in expected_errors:
        if error in result.stdout:
            found_errors.append(error)
    
    print(f"\nFound expected errors: {found_errors}")
    
    # Check specifically for the original issue errors
    original_issue_errors = [
        "TestNetworkManagerActivatorBringUp.fake_isfile_no_nmconn] Method should have \"self\" as first argument",
        "TestNetworkManagerActivatorBringUp.fake_isfile_no_nmconn] Instance of 'TestNetworkManagerActivatorBringUp' has no 'endswith' member"
    ]
    
    original_found = []
    for error in original_issue_errors:
        if error in result.stdout:
            original_found.append(error)
    
    print(f"Original issue errors found: {original_found}")
    
    return result.returncode != 0, found_errors, original_found

if __name__ == "__main__":
    has_errors, found_errors, original_found = run_pylint_on_file()
    
    if len(original_found) == 0:
        print("\n✅ SUCCESS: Original issue errors are FIXED!")
        print("The specific errors mentioned in the issue description are no longer present.")
        if has_errors:
            print("Note: There are still some other pylint errors, but they were not part of the original issue.")
    elif len(original_found) > 0:
        print("\n❌ ISSUE STILL EXISTS:")
        print("Found the original issue errors:")
        for error in original_found:
            print(f"  - {error}")
    else:
        print("\n✗ Could not determine issue status")
        print(f"Expected 2 errors, found {len(found_errors)}")
    
    # Exit with 0 if the original issue is fixed, regardless of other errors
    sys.exit(0 if len(original_found) == 0 else 1)