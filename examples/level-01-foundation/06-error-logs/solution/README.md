# Error Logs Example - After

This directory contains improved code with clear, contextual error messages.

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/test_file_processor.py -v

# Run with coverage
pytest tests/test_file_processor.py --cov=main --cov-report=term-missing
```

## What Was Improved

1. **Specific Error Messages**: Replaced generic "Error" with descriptive messages
2. **Appropriate Exception Types**: Used FileNotFoundError, InvalidFileError, etc.
3. **Contextual Information**: Added file paths, values, expected vs actual
4. **Actionable Guidance**: Suggested how to fix each error
5. **Structured Format**: Consistent error message patterns

## Key Learning

Clear error messages enable AI to:
- Understand what went wrong
- Identify root causes
- Suggest appropriate fixes
- Self-correct automatically

See `EXPLANATION.md` for detailed analysis of error message improvements.

