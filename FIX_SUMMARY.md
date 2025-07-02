# Union Syntax Fix Summary

## Issue Description
The CI workflow `.github/workflows/check_format.yml` was failing with the following errors:

### mypy Error
```
cloudinit/distros/__init__.py:154: error: X | Y syntax for unions requires Python 3.10
cloudinit/distros/__init__.py:158: error: X | Y syntax for unions requires Python 3.10
```

### pylint Error
```
cloudinit/distros/__init__.py:154: [E1131(unsupported-binary-operation), Distro] unsupported operand type(s) for |
cloudinit/distros/__init__.py:158: [E1131(unsupported-binary-operation), Distro] unsupported operand type(s) for |
```

## Root Cause
- The code was using Python 3.10+ union syntax (`str | None`) for type annotations
- The CI environment runs on ubuntu-20.04 which uses Python 3.8 by default
- Python 3.8 doesn't support the `X | Y` union syntax (introduced in Python 3.10)

## Solution
Replaced the Python 3.10+ union syntax with the backward-compatible `Optional[str]` syntax:

### Before (Lines 154 and 158)
```python
dhclient_lease_directory: str | None = None
dhclient_lease_file_regex: str | None = None
```

### After (Lines 154 and 158)
```python
dhclient_lease_directory: Optional[str] = None
dhclient_lease_file_regex: Optional[str] = None
```

## Changes Made
**File:** `cloudinit/distros/__init__.py`
- Line 154: Changed `str | None` to `Optional[str]`
- Line 158: Changed `str | None` to `Optional[str]`

**Note:** `Optional` was already imported from the `typing` module, so no import changes were needed.

## Verification
✅ **Syntax Check:** No more union syntax issues found in the codebase  
✅ **Compatibility:** Code now parses successfully on Python 3.8+  
✅ **Functionality:** All existing functionality preserved  
✅ **Type Checking:** pylint E1131 errors resolved  
✅ **Import Test:** Module imports successfully  
✅ **Attribute Test:** Class attributes work correctly with None and string values  

## Impact
- **Backward Compatibility:** Code now works with Python 3.8+ (CI requirement)
- **Forward Compatibility:** Code continues to work with Python 3.10+
- **No Functional Changes:** The semantic meaning is identical (`Optional[str]` ≡ `str | None`)
- **Minimal Changes:** Only 2 lines modified, no other files affected

## CI Status
This fix should resolve the failing mypy and pylint checks in the CI workflow, allowing the repository to pass the format checks on ubuntu-20.04.