#!/usr/bin/env python3

"""
Test script to verify the pylint issue with the Dhcpcd class.
"""

import os
import sys
import subprocess

def main():
    """Run pylint on the Dhcpcd class to verify the issue."""
    # Create a temporary file with the Dhcpcd class
    with open('temp_dhcpcd.py', 'w') as f:
        f.write('''
class DhcpClient:
    def __init__(self):
        pass

class Dhcpcd(DhcpClient):
    def __init__(self):
        super().__init__()
''')
    
    # Run pylint on the temporary file
    try:
        result = subprocess.run(
            ['pylint', 'temp_dhcpcd.py'],
            capture_output=True,
            text=True,
            check=False
        )
        print(result.stdout)
        print(result.stderr)
        
        # Check if the W0235 warning is present
        if 'W0235' in result.stdout:
            print("Pylint issue verified: W0235 (useless-super-delegation) warning found.")
        else:
            print("Pylint issue not verified: W0235 warning not found.")
    finally:
        # Clean up the temporary file
        if os.path.exists('temp_dhcpcd.py'):
            os.remove('temp_dhcpcd.py')

if __name__ == '__main__':
    main()