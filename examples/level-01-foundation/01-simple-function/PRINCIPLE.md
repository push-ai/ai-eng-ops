# Simple Function Principle: Structure Enables Iteration

## The Principle

**A single, well-structured function with comprehensive tests enables AI to iterate safely and verify improvements.** Well-structured functions are the foundation of maintainable code—they're testable, documented, and easy for AI to understand and improve.

## Why This Matters for AI Engineering

### The Problem with Unstructured Functions

When functions lack structure, AI struggles to:
- ✅ Write code that works
- ❌ Verify correctness systematically
- ❌ Identify edge cases
- ❌ Refactor safely
- ❌ Understand expected behavior

### How Structure Helps AI

Well-structured functions enable AI to:
1. **Verify Correctness**: Tests confirm behavior works as expected
2. **Identify Edge Cases**: Tests reveal boundary conditions
3. **Refactor Safely**: Tests catch regressions immediately
4. **Understand Intent**: Documentation explains purpose and usage
5. **Iterate Quickly**: Fast feedback loop from tests

### Characteristics of Well-Structured Functions

- **Single Responsibility**: Does one thing well
- **Clear Documentation**: Docstring explains purpose, parameters, returns
- **Input Validation**: Handles invalid inputs gracefully
- **Comprehensive Tests**: Tests cover happy path, edge cases, errors
- **Descriptive Naming**: Function name clearly describes what it does

## Copy-Paste Prompt

Use this prompt with your AI coding assistant:

```
Analyze the function in the `problem/` directory and create a well-structured version with comprehensive tests.

Requirements:
1. Improve the function with:
   - Clear docstring documenting purpose, parameters, return value, and exceptions
   - Input validation with appropriate error messages
   - Edge case handling (boundary conditions, invalid inputs)
   - Descriptive function name if needed

2. Create comprehensive tests using pytest:
   - Happy path scenarios
   - Edge cases (boundary values, empty inputs, None values)
   - Error scenarios (invalid inputs should raise appropriate exceptions)
   - Use descriptive test names that explain what's being tested

3. Ensure the function is:
   - Single responsibility (does one thing)
   - Well-documented
   - Testable and tested
   - Handles edge cases gracefully

Focus on creating a function that AI can safely iterate on with confidence that tests will catch any regressions.
```

## Expected Outcomes

After using this prompt, you should see:

1. **Well-Documented Function**: Clear docstring with parameter and return documentation
2. **Input Validation**: Handles invalid inputs with clear errors
3. **Comprehensive Tests**: Tests covering all scenarios
4. **Safe Refactoring**: Tests enable confident code changes
5. **Clear Structure**: Function is easy to understand and modify

## Key Learning

**Structure enables iteration.** A well-structured function with tests is:
- Easy to understand (documentation)
- Safe to modify (tests catch regressions)
- Reliable (input validation)
- Maintainable (clear structure)

This foundation makes everything else easier—AI can confidently improve code knowing tests will catch problems.

## Next Steps

1. Use the prompt above with your AI assistant
2. Run the tests to see what passes and fails
3. Compare your approach with `solution/` to see example improvements

