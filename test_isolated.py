#!/usr/bin/env python3

"""
Isolated test for the problematic lines.
"""

class TestClass:
    """Test class with pipe operator type annotation."""
    dhclient_lease_directory: str | None = None
    dhclient_lease_file_regex: str | None = None