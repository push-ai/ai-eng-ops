# Data Structure Example - Solution

This directory contains a well-structured data structure with clear invariants and comprehensive tests.

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_shopping_cart.py -v

# Run with coverage
pytest tests/test_shopping_cart.py --cov=main --cov-report=term-missing
```

## What Was Improved

1. **Clear Invariants**: Documented rules about valid state
2. **Invariant Enforcement**: Methods validate and maintain invariants
3. **Input Validation**: Comprehensive validation prevents invalid state
4. **Encapsulation**: Protected internal state prevents violations
5. **Complete Interface**: Additional methods for usability
6. **Comprehensive Tests**: Tests verify invariants and behavior

## Key Learning

Data structure invariants enable:
- Safe state management (state always valid)
- Predictable behavior (invariants maintained)
- Reliable operations (validation prevents errors)
- Maintainable code (clear contracts)

See `EXPLANATION.md` for detailed analysis of the improvements.

