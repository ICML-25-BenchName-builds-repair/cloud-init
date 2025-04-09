#!/usr/bin/env python3

import unittest
from unittest import mock

from cloudinit.net.dhcp import Dhcpcd, DhcpClient

class TestDhcpcd(unittest.TestCase):
    @mock.patch('cloudinit.subp.which', return_value='/usr/sbin/dhcpcd')
    def test_dhcpcd_init(self, m_which):
        """Test that Dhcpcd can be initialized."""
        dhcpcd = Dhcpcd()
        self.assertEqual(dhcpcd.client_name, 'dhcpcd')
        self.assertEqual(dhcpcd.dhcp_client_path, '/usr/sbin/dhcpcd')
        m_which.assert_called_once_with('dhcpcd')

if __name__ == '__main__':
    unittest.main()