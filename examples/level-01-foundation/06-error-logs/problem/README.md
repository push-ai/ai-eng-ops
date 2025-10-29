# Error Logs Example - Before

This example demonstrates code with poor error messages that make debugging difficult for both AI and humans.

## Running the Example

```bash
python main.py
```

Observe how the error messages are vague and unhelpful:
- "Error" - What error?
- "Invalid" - What's invalid?
- "Unknown" - Unknown what?

## The Problem

Poor error messages cause:
- **AI confusion**: AI can't understand what went wrong to suggest fixes
- **Slow debugging**: Humans waste time figuring out the actual issue
- **Frustration**: Vague errors don't guide users to solutions
- **Poor user experience**: No actionable information

## What Makes Error Messages Poor

1. **Too generic**: "Error" doesn't tell you what
2. **No context**: Missing file paths, input values, expected vs actual
3. **No guidance**: Doesn't suggest how to fix the issue
4. **Technical jargon**: Uses internal terms users don't understand
5. **Missing details**: No line numbers, stack traces, or relevant state

## Next Steps

1. Read `../PRINCIPLE.md` to understand the error-logs principle
2. Use the provided prompt with your AI assistant
3. Compare improvements with `../solution/` to see better error messages

