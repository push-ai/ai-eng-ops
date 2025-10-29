# Data Structure Example - Problem

This example demonstrates a data structure (class) that works but lacks proper structure for testing and extension.

## Running the Example

```bash
python main.py
```

## What to Observe

Notice how the class:
- ✅ Works for basic cases
- ❌ **NO TYPE ANNOTATIONS** - AI has to guess types
- ❌ **NO TYPED DATA MODELS** - Structure is ambiguous
- ❌ Has no input validation
- ❌ No clear invariants
- ❌ No tests to verify behavior
- ❌ Edge cases not handled
- ❌ No documentation of class purpose

## The Critical Problem: AI Spiral

**Without strong typing**:
- AI doesn't know if `item` should be str, dict, or object
- AI doesn't know if `price` should be int, float, or Decimal
- AI makes incorrect assumptions → generates wrong code
- AI gets corrected → makes new incorrect assumptions → **spirals**
- Can't verify correctness
- Edge cases undefined
- State can become invalid
- Refactoring is risky

## Next Steps

1. Read `../PRINCIPLE.md` to understand the data structure principle
2. Use the provided prompt with your AI assistant
3. Compare improvements with `../solution/` to see proper class structure

