# Bug Fix Principle: Reproduce Locally, Fix with TDD

## The Principle

**Reproducing bugs locally in code with a failing test enables test-driven bug fixing.** A failing test that reproduces the bug is the first step—it verifies the bug exists, confirms the fix works, and prevents regressions.

## Why This Matters for AI Engineering

### The Problem Without Test-Driven Bug Fixes

When fixing bugs without tests, AI often:
- ✅ Fixes the reported issue
- ❌ Breaks other functionality (regressions)
- ❌ Doesn't verify the fix actually works
- ❌ Misses related edge cases
- ❌ Creates code that's hard to verify

### How TDD Helps Bug Fixing

Test-driven bug fixing enables:
1. **Reproduction**: Failing test proves the bug exists
2. **Verification**: Passing test confirms the fix works
3. **Regression Prevention**: Tests catch if bug returns
4. **Edge Case Discovery**: Tests reveal related issues
5. **Confidence**: Safe refactoring knowing tests will catch problems

### The TDD Bug Fix Cycle

1. **RED**: Write a failing test that reproduces the bug
2. **GREEN**: Make minimal changes to make the test pass
3. **REFACTOR**: Improve code while keeping tests green
4. **EXPAND**: Add tests for edge cases to prevent future bugs

## Copy-Paste Prompt

Use this prompt with your AI coding assistant:

```
Analyze the bug report and code in the `problem/` directory. Use test-driven development to fix the bug.

Process:
1. First, write a failing test that reproduces the bug described in the README
2. Run the test to confirm it fails (this verifies the bug exists)
3. Fix the code with minimal changes to make the test pass
4. Add additional tests for edge cases (negative values, boundary conditions, invalid inputs)
5. Refine the fix to handle all edge cases
6. Ensure existing functionality still works

The bug: calculate_discount() doesn't validate discount_percent ranges, allowing negative values and values over 100% which produce incorrect results.

Create a comprehensive test suite using pytest that:
- Reproduces the reported bug with a failing test
- Tests edge cases (0%, 100%, negative, >100%)
- Validates input constraints
- Ensures the fix doesn't break existing behavior
```

## Expected Outcomes

After using this prompt, you should see:

1. **Failing Test**: A test that fails, proving the bug exists
2. **Minimal Fix**: Code changes that just fix the bug
3. **Passing Tests**: Tests that pass, confirming the fix works
4. **Edge Case Coverage**: Tests for related scenarios
5. **Confidence**: Ability to refactor safely knowing tests catch regressions

## Key Learning

**A failing test is your first checkpoint—it proves the bug exists and confirms your fix works.** The TDD cycle (Red → Green → Refactor) ensures:
- Bugs are reproduced locally
- Fixes are verified with tests
- Regressions are prevented
- Edge cases are considered

## Bug Fix Workflow

```
1. Read bug report / identify issue
2. Write failing test (RED) ← Start here!
3. Run test to confirm it fails
4. Fix the code (GREEN)
5. Run test to confirm it passes
6. Add edge case tests
7. Refactor while keeping tests green
```

## Next Steps

1. Use the prompt above with your AI assistant
2. Watch the test fail first (RED)
3. Have AI fix the code to make tests pass (GREEN)
4. Compare your approach with `solution/` to see the TDD solution

