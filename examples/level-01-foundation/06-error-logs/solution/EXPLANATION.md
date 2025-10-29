# What Changed and Why: Clear Error Messages

## Overview

This example demonstrates how transforming vague error messages into clear, contextual ones enables both AI self-correction and faster human debugging.

## The Problem with Original Errors

### Before: Vague Errors
- `"Error"` - What error?
- `"Invalid"` - What's invalid?
- `"Unknown"` - Unknown what?

These messages provide **no actionable information** and force both AI and humans to guess what went wrong.

## Improvements Made

### 1. Specific Error Messages

**Before**:
```python
raise Exception("Error")
```

**After**:
```python
raise FileNotFoundError(
    f"Cannot read file '{filepath}': File does not exist. "
    f"Check that the file path is correct and the file has been created."
)
```

**Why**: The specific message tells you:
- What operation failed (reading file)
- Which file (the filepath)
- What the problem is (doesn't exist)
- How to fix it (check path or create file)

### 2. Appropriate Exception Types

**Before**: Generic `Exception` for everything

**After**: Specific exception types:
- `FileNotFoundError` - File doesn't exist
- `InvalidFileError` - File format is invalid
- `InvalidOperationError` - Operation not supported
- `PermissionError` - Access denied

**Why**: Exception types allow:
- Better error handling (catch specific types)
- Clearer intent (what kind of error occurred)
- Better IDE support (autocomplete, type checking)

### 3. Contextual Information

**Before**: Just "Error"

**After**: Includes:
- File paths
- Input values
- Expected vs actual values
- Operation names
- Line numbers (for JSON parsing)
- Current working directory

**Why**: Context helps AI and humans understand:
- Where the error occurred
- What inputs caused it
- What was expected

### 4. Actionable Guidance

**Before**: No guidance

**After**: Suggests fixes:
- "Check that the file path is correct"
- "Create the directory first"
- "Ensure you have read access"
- "Validate the JSON syntax"

**Why**: Guidance enables:
- Faster problem resolution
- AI to suggest fixes automatically
- Better user experience

### 5. Structured Error Hierarchy

**Before**: All errors are same level

**After**: Different error types for different severities:
- **ERROR**: Something is broken (FileNotFoundError)
- **WARNING**: Potential issue (could add for empty files)
- **INFO**: Normal operation info (could add for successful operations)
- **DEBUG**: Detailed debugging info (could add for tracing)

**Why**: Hierarchy allows:
- Filtering by severity
- Different handling strategies
- Better logging configuration

## Error Message Patterns

### Pattern 1: Operation + Context + Problem + Solution
```
Cannot [operation] [context]: [problem]. [solution]
```

Example:
```
Cannot read file '/path/to/file.json': File does not exist. 
Check that the file path is correct and the file has been created.
```

### Pattern 2: Expected vs Actual
```
Expected [expected], but got [actual]. [guidance]
```

Example:
```
Expected data to be a list, but got dict. 
Data value: {'key': 'value'}
```

### Pattern 3: Invalid Value + Valid Options
```
Invalid [thing] '[value]'. [valid options]. Received: '[value]'
```

Example:
```
Invalid operation 'invalid_op'. 
Supported operations are: sum, count, average. 
Received: 'invalid_op'
```

## Learning Outcomes

### For AI Engineering Agents

1. **Self-Correction**: Clear errors help AI understand what to fix
2. **Better Suggestions**: Context enables more accurate fix suggestions
3. **Faster Iteration**: Less time guessing what went wrong
4. **Automated Fixes**: AI can automatically address common issues

### For Human Engineers

1. **Faster Debugging**: Know immediately what went wrong
2. **Less Context Switching**: Don't need to dig through code
3. **Better User Experience**: Users understand how to fix issues
4. **Easier Logging**: Structured errors are easier to parse and filter

## Key Takeaway

**Error messages are user interfaces—they should communicate clearly.** Good error messages:
- Tell you **what** happened (operation + context)
- Explain **why** it happened (problem description)
- Suggest **how** to fix it (actionable guidance)
- Provide **context** for debugging (values, paths, expected vs actual)

This is especially powerful for AI because:
- AI can parse structured errors
- AI can understand context from error messages
- AI can suggest fixes based on error content
- AI can self-correct when encountering errors

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_file_processor.py -v

# Run with coverage
pytest tests/test_file_processor.py --cov=main --cov-report=html
```

The tests verify that error messages contain the expected contextual information and actionable guidance.

