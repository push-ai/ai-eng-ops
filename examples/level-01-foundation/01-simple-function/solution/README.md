# Simple Function Example - Solution

This directory contains a well-structured simple function with comprehensive tests.

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_calculate_discount.py -v

# Run with coverage
pytest tests/test_calculate_discount.py --cov=main --cov-report=term-missing
```

## What Was Improved

1. **Comprehensive Documentation**: Clear docstring with parameters, returns, exceptions, examples
2. **Input Validation**: Type checking and range validation with clear errors
3. **Edge Case Handling**: Explicit handling of boundaries and special cases
4. **Comprehensive Tests**: Tests covering all scenarios and edge cases
5. **Clear Structure**: Single responsibility, well-organized code

## Key Learning

Proper structure enables:
- Safe refactoring (tests catch regressions)
- Clear understanding (documentation explains purpose)
- Reliable behavior (validation prevents bugs)
- Rapid iteration (tests provide fast feedback)

See `EXPLANATION.md` for detailed analysis of the improvements.

