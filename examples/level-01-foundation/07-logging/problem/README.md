# Logging Example - Before

This example demonstrates code without logging, making it difficult to identify root causes when things go wrong.

## Running the Example

```bash
python main.py
```

Notice how you can see:
- ✅ That something happened (result: True/False)
- ❌ What actually happened inside
- ❌ Why it succeeded or failed
- ❌ Where problems occurred
- ❌ What data was processed

## The Problem

Without logging, debugging is like:
- Driving blindfolded - you know you moved but not where
- Flying without instruments - no visibility into system state
- Debugging in the dark - guessing what went wrong

## What You Can't See

1. **Operation Flow**: Which steps executed successfully?
2. **Data Values**: What data was processed at each step?
3. **Performance**: How long did each operation take?
4. **Errors**: What specific errors occurred and where?
5. **State Changes**: How did system state change over time?

## Next Steps

1. Read `../PRINCIPLE.md` to understand the logging principle
2. Use the provided prompt with your AI assistant
3. Compare improvements with `../solution/` to see comprehensive logging

