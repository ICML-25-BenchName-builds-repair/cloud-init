import os

def test_function():
    return os.path.exists("/tmp")

if __name__ == "__main__":
    print(test_function())