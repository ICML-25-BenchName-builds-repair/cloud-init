#!/usr/bin/env python3

# This is a minimal test file to verify our fix

from typing import Union

# Original code (should fail with mypy --python-version 3.8)
dhclient_lease_directory: str | None = None
dhclient_lease_file_regex: str | None = None

# Fixed code (should work with mypy --python-version 3.8)
# dhclient_lease_directory: Union[str, None] = None
# dhclient_lease_file_regex: Union[str, None] = None

print("Test completed")