from typing import Optional, Union

# This should pass with Python 3.7
class TestClass:
    # Using Optional (correct for Python 3.7)
    attr1: Optional[str] = None
    
    # Using pipe operator (requires Python 3.10+)
    # attr2: str | None = None  # This would fail with Python 3.7
    
    def __init__(self):
        pass