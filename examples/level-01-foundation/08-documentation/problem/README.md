# Problem: Documentation Files That Help AI

This example demonstrates the **documentation files** you should create alongside your code to provide context that helps AI assistants produce better, more accurate code.

## The Documentation Strategy

When building with AI, you need documentation at multiple levels:

### 1. **Inline Documentation** (Embedded in Code)
- Docstrings in functions/classes
- Inline comments explaining "why"
- Type hints and interfaces
- This lives IN your code files

### 2. **Collocated Documentation** (Same Folder/Module)
- README.md for module-level context
- ARCHITECTURE.md for design decisions
- DOMAIN.md for business rules
- API.md for usage examples
- These files live **alongside your code** in the same directory or module

**When to Use Collocated Docs**:
- Module-specific context
- Design decisions for this component
- Business rules for this feature
- Usage patterns for this API
- Anything that's **scoped to this module**

### 3. **Centralized Documentation** (Shared Across Services)
- Enterprise-wide architecture docs
- Company policies and standards
- Domain knowledge shared across teams
- Integration patterns
- These files live in a **central docs folder** (e.g., `/docs/`, `/architecture/`)

**When to Use Centralized Docs**:
- Knowledge shared across multiple services
- Company-wide policies and standards
- Enterprise architecture decisions
- Domain knowledge used by multiple teams
- Integration patterns used everywhere

## What You'll Find Here

This `problem/` folder contains **example documentation files** that demonstrate:

1. **Collocated Documentation** (in this folder):
   - `README.md` - Module overview and usage
   - `ARCHITECTURE.md` - Design decisions for this module
   - `DOMAIN.md` - Business rules and domain knowledge
   - `API.md` - Usage examples and patterns

2. **Centralized Documentation** (referenced, typically in `/docs/` or `/architecture/`):
   - `docs/POLICIES.md` - Company-wide policies
   - `docs/DOMAIN_MODEL.md` - Shared domain knowledge
   - `docs/INTEGRATIONS.md` - Integration patterns

## How to Use These Docs

### For Development
1. **Reference collocated docs** when working on this module
2. **Reference centralized docs** when making decisions that affect multiple services
3. **Keep docs updated** as code evolves

### For AI Assistants
1. **Provide docs as context** when asking AI to modify code
2. **Point AI to relevant docs** ("See ARCHITECTURE.md for design decisions")
3. **Use docs to prevent AI guessing** at business rules and constraints

## The Goal

These documentation files provide **explicit context** that prevents AI from:
- Guessing at business rules
- Making incorrect assumptions about architecture
- Violating company policies
- Missing domain-specific constraints

Instead, AI can **reference these docs** to understand:
- What the code should do (business rules)
- How it should be structured (architecture)
- What constraints exist (policies)
- How to use it correctly (API patterns)
