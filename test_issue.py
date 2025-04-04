#!/usr/bin/env python3

import os
from unittest.mock import patch

# Simulate the test class
class TestNetworkManagerActivatorBringUp:
    # Fixed: properly defined as a static method
    @staticmethod
    def fake_isfile_no_nmconn(filename):
        return False if filename.endswith(".nmconnection") else True

# Simulate the conn_filename function
def conn_filename(devname):
    conn_file = f"/etc/NetworkManager/system-connections/cloud-init-{devname}.nmconnection"
    # If the network manager connection file is absent, also check for
    # presence of ifcfg files for the same interface
    if not os.path.isfile(conn_file):
        conn_file = f"/etc/sysconfig/network-scripts/ifcfg-{devname}"
    return conn_file if os.path.isfile(conn_file) else None

# Test the function with the mock
with patch.object(os.path, 'isfile', side_effect=TestNetworkManagerActivatorBringUp.fake_isfile_no_nmconn):
    result = conn_filename("eth0")
    print(f"Result: {result}")
    # Expected: /etc/sysconfig/network-scripts/ifcfg-eth0