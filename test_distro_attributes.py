#!/usr/bin/env python3
"""
Test that the fixed attributes work correctly.
"""

def test_distro_attributes():
    """Test that the Distro class attributes work as expected."""
    
    try:
        from cloudinit.distros import Distro
        
        # Check that the class has the attributes
        if hasattr(Distro, 'dhclient_lease_directory'):
            print("✓ dhclient_lease_directory attribute exists")
            
            # Check the default value
            if Distro.dhclient_lease_directory is None:
                print("✓ dhclient_lease_directory default value is None")
            else:
                print(f"✗ dhclient_lease_directory default value is {Distro.dhclient_lease_directory}")
                return False
        else:
            print("✗ dhclient_lease_directory attribute missing")
            return False
        
        if hasattr(Distro, 'dhclient_lease_file_regex'):
            print("✓ dhclient_lease_file_regex attribute exists")
            
            # Check the default value
            if Distro.dhclient_lease_file_regex is None:
                print("✓ dhclient_lease_file_regex default value is None")
            else:
                print(f"✗ dhclient_lease_file_regex default value is {Distro.dhclient_lease_file_regex}")
                return False
        else:
            print("✗ dhclient_lease_file_regex attribute missing")
            return False
        
        # Test that we can set string values
        class TestDistro(Distro):
            dhclient_lease_directory = "/var/lib/dhcp"
            dhclient_lease_file_regex = r"dhclient.*\.lease"
        
        if TestDistro.dhclient_lease_directory == "/var/lib/dhcp":
            print("✓ Can set string value for dhclient_lease_directory")
        else:
            print("✗ Cannot set string value for dhclient_lease_directory")
            return False
        
        if TestDistro.dhclient_lease_file_regex == r"dhclient.*\.lease":
            print("✓ Can set string value for dhclient_lease_file_regex")
        else:
            print("✗ Cannot set string value for dhclient_lease_file_regex")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error testing distro attributes: {e}")
        return False

if __name__ == "__main__":
    print("Testing Distro class attributes...")
    print("=" * 40)
    
    if test_distro_attributes():
        print("\n✓ All attribute tests passed!")
    else:
        print("\n✗ Some attribute tests failed!")