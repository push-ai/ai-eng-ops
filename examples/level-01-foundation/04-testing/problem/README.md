# Testing Example - Before

This example demonstrates a user authentication module that lacks comprehensive testing.

## Running the Example

```bash
python main.py
```

## What to Observe

Run the code and notice:
- The code works for basic cases
- But what edge cases might break it?
- What happens with empty strings?
- What about special characters in usernames?
- How do we know if deactivation works correctly?

## The Problem

This code "works" but lacks tests. Without tests:
- AI can't verify edge cases
- It's hard to refactor safely
- Bugs can be introduced unknowingly
- Edge cases are overlooked

## Next Steps

1. Read `../PRINCIPLE.md` to understand the testing principle
2. Use the provided prompt with your AI assistant
3. Compare your results with `../solution/` to see example improvements

