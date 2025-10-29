# Data Structure Example - Solution

This directory contains a strongly typed data structure that prevents AI spiral through explicit type annotations, TypedDict models, and comprehensive tests.

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_shopping_cart.py -v

# Run with coverage
pytest tests/test_shopping_cart.py --cov=main --cov-report=term-missing

# Optional: Run type checker (mypy) to verify type annotations
# pip install mypy
# mypy main.py
```

## What Was Improved

1. **CRITICAL: Strong Type Annotations**: Every method has explicit type hints
2. **Typed Data Models**: CartItem TypedDict defines exact structure
3. **Type-Guided Validation**: Validation matches type expectations
4. **Clear Invariants**: Documented rules about valid state
5. **Invariant Enforcement**: Methods validate and maintain invariants
6. **Encapsulation**: Protected internal state prevents violations
7. **Comprehensive Tests**: Tests verify types, invariants, and behavior

## Key Learning

**Strong typing prevents AI spiral.** A strongly typed data structure:
- Shows exact types (AI knows what to pass)
- Defines structure (TypedDict shows data shape)
- Prevents type confusion (no guessing required)
- Enables accurate code generation (types guide AI)
- Stops AI spiral (clear types = correct code)

Without strong typing: AI guesses → mistakes → corrections → **spiral**  
With strong typing: AI knows → correct code → **no spiral**

See `EXPLANATION.md` for detailed analysis of the improvements.

