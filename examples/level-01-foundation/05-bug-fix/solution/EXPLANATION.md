# What Changed and Why: TDD Bug Fixing

## Overview

This example demonstrates fixing a bug using test-driven development (TDD). The bug was first reproduced with a failing test, then fixed, and finally expanded with edge case tests.

## The Bug

**Original Issue**: `calculate_discount()` didn't validate input ranges:
- Negative discount percentages resulted in prices higher than original
- Discounts over 100% resulted in negative prices
- No validation of price constraints

## TDD Bug Fix Process

### Step 1: RED - Write Failing Test

First, we wrote a test that reproduced the bug:

```python
def test_negative_discount_raises_error(self):
    """Test that negative discount raises ValueError."""
    with pytest.raises(ValueError, match="cannot be negative"):
        self.calc.calculate_discount(100, -10)
```

**This test failed** with the original code, proving the bug exists.

### Step 2: GREEN - Fix the Code

Made minimal changes to make the test pass:

```python
if discount_percent < 0:
    raise ValueError("Discount percentage cannot be negative")
```

**The test now passes**, confirming the fix works.

### Step 3: REFACTOR - Expand Coverage

Added more tests for edge cases and refined the fix:

- Added validation for discount > 100%
- Added validation for negative prices
- Added edge case tests (0%, 100%, boundaries)
- Ensured result is never negative

## Key Changes

### 1. Input Validation Added

**Before**: No validation of discount_percent or price ranges.

**After**: Comprehensive validation:
- `discount_percent` must be between 0 and 100
- `price` cannot be negative
- Clear error messages for each violation

**Why**: Tests revealed that invalid inputs produced incorrect results.

### 2. Error Messages

**Before**: No errors, just incorrect calculations.

**After**: Specific ValueError exceptions:
- "Discount percentage cannot be negative"
- "Discount percentage cannot exceed 100%"
- "Price cannot be negative"

**Why**: Clear errors help AI and humans understand what went wrong.

### 3. Result Validation

**Before**: Could return negative prices.

**After**: Ensures result is never negative using `max(0, result)`.

**Why**: Edge cases (like floating point precision) could produce negative results.

### 4. Expanded to Tax Calculation

**Before**: Only discount had bugs.

**After**: Applied same validation principles to `calculate_total_with_tax()`.

**Why**: Tests revealed similar issues in related methods.

## Test Coverage

The test suite includes:

1. **Bug Reproduction Tests**: Tests that fail with original code
2. **Fix Verification Tests**: Tests that pass after fix
3. **Edge Case Tests**: Boundaries (0%, 100%), decimal values
4. **Regression Tests**: Ensure existing functionality still works
5. **Error Scenario Tests**: Invalid inputs raise appropriate errors

## Learning Outcomes

### For AI Engineering Agents

1. **Reproduce First**: Always write a failing test that reproduces the bug
2. **Fix Minimally**: Make smallest change to make test pass
3. **Expand Safely**: Add edge case tests while keeping everything green
4. **Prevent Regressions**: Tests ensure bug doesn't return

### For Human Engineers

1. **TDD Cycle**: Red → Green → Refactor is powerful for bug fixes
2. **Tests as Documentation**: Tests show what the bug was and how it's fixed
3. **Confidence**: Comprehensive tests allow safe refactoring
4. **Edge Cases**: Tests reveal related issues that might not be obvious

## TDD Bug Fix Workflow

```
1. Read bug report
2. Write failing test (RED) ← Proves bug exists
3. Run test to confirm it fails
4. Fix code minimally (GREEN) ← Confirms fix works
5. Run test to confirm it passes
6. Add edge case tests
7. Refactor while keeping tests green
```

## Key Takeaway

**A failing test is proof the bug exists. A passing test is proof the fix works.** The TDD cycle ensures:
- Bugs are reproduced locally
- Fixes are verified immediately
- Regressions are prevented
- Edge cases are discovered

This approach is especially powerful with AI because:
- AI can write the failing test first
- AI can see the test fail
- AI can fix the code to make it pass
- AI can expand tests systematically

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_calculator.py -v

# Run with coverage
pytest tests/test_calculator.py --cov=main --cov-report=html
```

The tests demonstrate the complete TDD bug fix cycle from reproduction to verification.

