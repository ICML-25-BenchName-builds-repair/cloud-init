#!/usr/bin/env python3

"""
Verification script for the fix to the union syntax issue in cloudinit/distros/__init__.py.
"""

import sys
import inspect
from typing import Optional, Union

# Import the Distro class
from cloudinit.distros import Distro

def check_type_annotations():
    """Check if the type annotations in Distro class are using Optional[str] instead of str | None."""
    # Get the class annotations
    annotations = getattr(Distro, '__annotations__', {})
    
    # Check the specific attributes
    lease_dir_type = annotations.get('dhclient_lease_directory', None)
    lease_regex_type = annotations.get('dhclient_lease_file_regex', None)
    
    print(f"dhclient_lease_directory type: {lease_dir_type}")
    print(f"dhclient_lease_file_regex type: {lease_regex_type}")
    
    # Check if they're using Optional[str]
    if str(lease_dir_type) == "typing.Optional[str]" and str(lease_regex_type) == "typing.Optional[str]":
        print("SUCCESS: Both attributes are using Optional[str] type annotation")
        return True
    else:
        print("FAILURE: One or both attributes are not using Optional[str] type annotation")
        return False

if __name__ == "__main__":
    print("Verifying fix for union syntax issue in cloudinit/distros/__init__.py")
    
    # Check if Distro class can be imported
    print(f"Successfully imported Distro class: {Distro.__name__}")
    
    # Check type annotations
    result = check_type_annotations()
    
    sys.exit(0 if result else 1)