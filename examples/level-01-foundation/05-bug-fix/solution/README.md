# Bug Fix Example - After

This directory contains the bug fix implemented using test-driven development.

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_calculator.py -v

# Run with coverage
pytest tests/test_calculator.py --cov=main --cov-report=term-missing
```

## TDD Process Followed

1. **RED**: Wrote failing test reproducing the bug
2. **GREEN**: Fixed code to make test pass
3. **REFACTOR**: Added edge case tests and refined solution

## What Was Fixed

- Added input validation for discount percentages (0-100%)
- Added validation for negative prices
- Added clear error messages
- Ensured results are never negative
- Applied same principles to tax calculation

## Key Learning

The failing test proved the bug existed. The passing test proves the fix works. Tests prevent regressions and reveal edge cases.

See `EXPLANATION.md` for detailed analysis of the TDD process.

