# Error Logs Principle: Clear Messages Enable Self-Correction

## The Principle

**Well-crafted error, warning, and validation messages enable AI self-correction and faster human diagnosis.** Good error messages don't just report failures—they provide context, guidance, and actionable information that helps both AI and humans understand what went wrong and how to fix it.

## Why This Matters for AI Engineering

### The Problem with Poor Error Messages

When code has vague error messages, AI struggles to:
- ✅ Identify what actually failed
- ❌ Understand the root cause
- ❌ Suggest appropriate fixes
- ❌ Self-correct when encountering errors
- ❌ Provide helpful debugging guidance

### How Good Error Messages Help AI

Clear error messages enable AI to:
1. **Understand Context**: Know what operation failed and why
2. **Identify Root Cause**: See input values, expected vs actual
3. **Suggest Fixes**: Understand what needs to change
4. **Self-Correct**: Modify code based on error information
5. **Provide Guidance**: Give users actionable next steps

### Characteristics of Effective Error Messages

- **Specific**: Tell exactly what went wrong
- **Contextual**: Include relevant values, file paths, line numbers
- **Actionable**: Suggest how to fix the issue
- **Hierarchical**: Different levels (ERROR, WARNING, INFO, DEBUG)
- **Structured**:的材料 Consistent format for parsing and filtering

## Copy-Paste Prompt

Use this prompt with your AI coding assistant:

```
Analyze the code in the `problem/` directory and improve all error messages, warnings, and validation messages to be clear, contextual, and actionable.

Requirements:
1. Replace generic errors (like "Error", "Invalid", "Unknown") with specific, descriptive messages
2. Include context in error messages:
   - File paths when file operations fail
   - Input values that caused the error
   - Expected vs actual values where applicable
   - Line numbers or operation names
3. Add appropriate error types (ValueError, FileNotFoundError, etc.) instead of generic Exception
4. Include actionable guidance: suggest how to fix the issue
5. Add warning messages for potentially problematic but non-fatal situations
6. Structure messages consistently for easy parsing

Focus on making errors that help AI understand what went wrong and how to fix it.
```

## Expected Outcomes

After using this prompt, you should see:

1. **Specific Errors**: Clear descriptions of what failed
2. **Contextual Information**: File paths, values, operation names
3. **Actionable Guidance**: Suggestions for fixing issues
4. **Proper Error Types**: Appropriate exception types
5. **Structured Format**: Consistent error message format

## Error Message Levels

### ERROR
- Something is broken and needs immediate attention
- Includes full context and fix suggestions
- Example: "FileNotFoundError: Cannot read '/path/to/file.json' - File does not exist. Check file path or create file first."

### WARNING
- Something might be problematic but doesn't prevent execution
- Provides context and potential impact
- Example: "Warning: File '/path/to/file.json' is empty. Processing will continue but may produce no results."

### INFO
- Informational messages about normal operations
- Useful for debugging and understanding flow
- Example: "Processing file '/path/to/file.json' (1024 bytes)"

### DEBUG
- Detailed information for debugging
- Usually only enabled in development
- Example: "Reading file '/path/to/file.json' with encoding 'utf-8'"

## Key Learning

**Error messages are a user interface—they should communicate clearly.** Good error messages:
- Tell you what happened
- Explain why it happened
- Suggest how to fix it
- Provide context for debugging

This is especially important for AI because clear errors enable:
- Better self-correction
- More accurate fix suggestions
- Faster iteration cycles
- Reduced debugging time

## Next Steps

1. Use the prompt above with your AI assistant
2. Compare.*solution
3. Test how the improved errors help debugging
4. Compare your approach with `solution/` to see example improvements

