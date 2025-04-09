#!/usr/bin/env python3

import os
from unittest.mock import patch

class TestClass:
    @staticmethod
    def fake_method(filename):
        return False if filename.endswith(".txt") else True

    @patch.object(os.path, "isfile", side_effect=fake_method)
    def test_method(self, m_isfile):
        print("Test method")

# Run pylint on this file
if __name__ == "__main__":
    import subprocess
    result = subprocess.run(["python", "-m", "pylint", __file__], capture_output=True, text=True)
    print(result.stdout)
    print(f"Exit code: {result.returncode}")