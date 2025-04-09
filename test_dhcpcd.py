#!/usr/bin/env python3

from cloudinit.net.dhcp import Dhcpcd, DhcpClient
import traceback

# Create an instance of Dhcpcd
try:
    # This will fail because we don't have dhcpcd installed, but it will
    # at least verify that the class initialization works
    dhcpcd = Dhcpcd()
    print("Dhcpcd instance created successfully")
except Exception as e:
    if "No such file or directory" in str(e):
        print("Dhcpcd initialization attempted successfully (expected error because dhcpcd is not installed)")
    else:
        print(f"Unexpected error: {e}")
        traceback.print_exc()

print("Test completed")