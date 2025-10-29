# Feature Module Principle: Shared Types Enable Cross-Stack Coordination

## The Principle

**Shared type definitions and clear component boundaries enable AI to coordinate frontend and backend components reliably.** When types are defined once and shared across the stack, AI can verify consistency and make changes confidently across multiple files.

## Why This Matters for AI Engineering

### The Problem: Type Mismatches Across Components

When frontend and backend define types separately:

```typescript
// Frontend defines:
interface User {
  age?: number;  // Optional
}

// Backend defines:
class User:
    age: int  # Required

# AI sees mismatch but can't easily fix both
```

Without shared types, AI will:
- **Miss type mismatches** between frontend and backend
- **Create inconsistencies** when modifying one side
- **Break contracts** unknowingly
- **Require manual coordination** for every change

### The Solution: Shared Type Definitions

Shared types provide a single source of truth:

```python
# shared/types.py
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int = Field(ge=0, le=150)
```

```typescript
// shared/types.ts (generated from Python)
export interface User {
  id: number;
  name: string;
  email: string;
  age: number;  // Always matches backend
}
```

Now AI can:
- **Verify consistency** automatically
- **Make changes** that propagate correctly
- **Catch mismatches** before they cause bugs
- **Coordinate changes** across components

## The Prompt

Copy this prompt and use it with your AI coding assistant:

```
I need you to refactor this feature module to use shared type definitions across frontend and backend.

Please:

1. **Create Shared Types**:
   - Define types in a shared location (shared/types.py or shared/types.ts)
   - Use Pydantic for Python/backend types
   - Generate TypeScript types from Python types (or vice versa)
   - Ensure types match exactly

2. **Update Backend**:
   - Import shared types
   - Use shared types for request/response models
   - Remove duplicate type definitions
   - Ensure validation matches type definitions

3. **Update Frontend**:
   - Import shared types
   - Use shared types for component props and state
   - Remove duplicate type definitions
   - Ensure forms match type definitions

4. **Type Generation**:
   - Set up type generation from single source of truth
   - Automate type generation in build process
   - Document type generation process

Focus especially on:
- Making types the single source of truth
- Ensuring frontend and backend types always match
- Making it easy for AI to verify type consistency
- Enabling AI to make changes across components confidently

The goal is to create a feature module where frontend and backend share types, enabling AI to coordinate changes across the entire stack reliably.
```

## Expected Outcome

After implementing shared types, AI assistants will:

1. **Verify type consistency** automatically
2. **Make changes** that propagate correctly
3. **Catch mismatches** before deployment
4. **Coordinate changes** across frontend and backend
5. **Generate correct code** without manual coordination

Structured feature modules transform development from "manual coordination" to "automatic consistency."

