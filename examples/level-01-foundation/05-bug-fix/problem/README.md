# Bug Fix Example - Before

This example demonstrates code with a bug that needs to be identified, reproduced, and fixed using test-driven development.

## The Bug Report

**Issue**: `calculate_discount()` returns incorrect results for edge cases:
- Negative discount percentages result in prices higher than original
- Discounts over 100% result in negative prices
- The function doesn't validate input ranges

## Running the Example

```bash
python main.py
```

Observe the output - notice how negative discounts give unexpected results.

## The Problem

Without a failing test that reproduces the bug:
- We can't verify the bug exists locally
- We can't confirm our fix actually works
- We might introduce regressions
- We can't ensure edge cases are handled

## The TDD Approach

1. **Reproduce**: Write a test that fails due to the bug
2. **Fix**: Make minimal changes to make the test pass
3. **Verify**: Ensure fix doesn't break existing functionality
4. **Refine**: Add tests for edge cases to prevent future bugs

## Next Steps

1. Read `../PRINCIPLE.md` to understand the bug-fix principle
2. Use the provided prompt with your AI assistant
3. Compare your approach with `../solution/` to see the TDD solution

