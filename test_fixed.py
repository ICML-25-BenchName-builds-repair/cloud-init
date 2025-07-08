#!/usr/bin/env python3

"""
Fixed version using Optional from typing.
"""

from typing import Optional

class TestClass:
    """Test class with Optional type annotation."""
    dhclient_lease_directory: Optional[str] = None
    dhclient_lease_file_regex: Optional[str] = None