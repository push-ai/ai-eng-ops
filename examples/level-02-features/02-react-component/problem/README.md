# Problem: React Component Without Structure

This example demonstrates React component code that works but lacks the structure needed for AI to reliably understand and modify it.

## The Problem

Without proper structure, AI struggles with React components because:

1. **No TypeScript types**: Props and state aren't typed
2. **No prop validation**: No way to verify prop types
3. **No error boundaries**: Errors crash the component
4. **No loading states**: User experience issues
5. **No tests**: No way to verify component behavior

## Setup

```bash
# Install dependencies
npm install

# Run development server (if you have a React app setup)
npm start
```

## Issues to Notice

- No TypeScript interfaces for props
- No type safety for state
- No error handling boundaries
- Inconsistent error states
- No prop validation
- No component tests

When AI tries to modify this component, it will guess at:
- What props are expected
- What data structures are used
- What error handling exists
- What the component contract is

