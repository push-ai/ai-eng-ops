# What Changed and Why: Data Structure Invariants

## Overview

This example demonstrates how proper structure transforms a basic class into a reliable data structure that maintains invariants and provides safe operations.

## The Problem with Unstructured Data Structures

### Before: Basic Class
- ✅ Works for simple cases
- ❌ No invariant enforcement
- ❌ State can become invalid
- ❌ No validation
- ❌ No tests
- ❌ Purpose unclear

Without structure, AI struggles to:
- Maintain valid state
- Understand constraints
- Safely modify behavior
- Test systematically

## Improvements Made

### 1. Clear Invariants

**Before**: No documented rules about valid state

**After**: Documented invariants:
- All items have non-negative prices
- No duplicate items
- Total is always sum of item prices

**Why**: Invariants define:
- What makes state valid
- Rules that must always be true
- Constraints on operations

### 2. Invariant Enforcement

**Before**: No enforcement, state could become invalid

**After**: Methods enforce invariants:
- `add_item()` validates price >= 0
- `add_item()` prevents duplicates
- `update_item_price()` validates new price
- Total is always calculated from items

**Why**: Enforcement ensures:
- State never becomes invalid
- Operations maintain invariants
- Predictable behavior

### 3. Input Validation

**Before**: No validation, undefined behavior

**After**: Comprehensive validation:
- Type checking (string names, numeric prices)
- Range validation (non-negative prices)
- Format validation (non-empty names)
- Duplicate prevention

**Why**: Validation ensures:
- Invalid state cannot be created
- Clear errors when rules violated
- Predictable behavior

### 4. Encapsulation

**Before**: Direct access to `items` list

**After**: Protected internal state:
- `_items` is private (convention)
- `items` property returns read-only tuple
- Methods control all state changes

**Why**: Encapsulation ensures:
- Invariants can't be violated externally
- State changes go through validation
- Internal representation can change

### 5. Additional Methods

**Before**: Basic operations only

**After**: Complete interface:
- `update_item_price()` - Update existing items
- `get_item_count()` - Query state
- `is_empty()` - Query state
- `clear()` - Reset state
- `__repr__()` - String representation

**Why**: Complete interface:
- Easier to use
- More functionality
- Better usability

### 6. Comprehensive Tests

**Before**: No tests

**After**: Organized test suite:
- Invariant tests (verify rules maintained)
- Method tests (test each operation)
- State transition tests (test workflows)
- Error scenario tests (test validation)

**Why**: Tests verify:
- Invariants are maintained
- Methods work correctly
- State transitions are valid
- Errors are handled properly

## Invariant Maintenance

### Invariant 1: Non-Negative Prices
- Enforced by: `add_item()` and `update_item_price()` validation
- Verified by: Tests that negative prices raise errors
- Maintained by: Always validating before adding/updating

### Invariant 2: No Duplicates
- Enforced by: `add_item()` checking existing items
- Verified by: Tests that duplicates raise errors
- Maintained by: Checking before adding

### Invariant 3: Total Equals Sum
- Enforced by: `get_total()` always calculates from items
- Verified by: Tests that verify total equals sum
- Maintained by: No direct total storage, always calculated

## Learning Outcomes

### For AI Engineering Agents

1. **Invariant Awareness**: Understand rules that must be maintained
2. **State Safety**: Ensure operations maintain valid state
3. **Validation**: Validate inputs to prevent invalid state
4. **Testing**: Test invariants are maintained

### For Human Engineers

1. **Clear Contracts**: Invariants define what's valid
2. **Safe Operations**: Validation prevents errors
3. **Maintainable Code**: Structure makes code easier to maintain
4. **Reliable Behavior**: Invariants ensure predictable behavior

## Key Takeaway

**Invariants enable safety.** A well-structured data structure:
- Documents invariants (rules about valid state)
- Enforces invariants (validation in methods)
- Tests invariants (verify rules are maintained)
- Protects invariants (encapsulation prevents violations)

This foundation ensures the data structure can be safely used and modified—state remains valid, operations are predictable, and tests verify correctness.

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_shopping_cart.py -v

# Run with coverage
pytest tests/test_shopping_cart.py --cov=main --cov-report=html
```

## Data Structure Usage Example

```python
cart = ShoppingCart()

# Add items (invariants enforced)
cart.add_item("Apple", 1.50)
cart.add_item("Banana", 0.75)

# Query state
total = cart.get_total()
is_empty = cart.is_empty()

# Update state (invariants maintained)
cart.update_item_price("Apple", 2.00)

# Remove items
cart.remove_item("Banana")

# Clear state
cart.clear()
```

The data structure now maintains its invariants and provides safe, predictable operations.

