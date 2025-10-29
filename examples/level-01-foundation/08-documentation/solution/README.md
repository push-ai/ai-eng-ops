# Documentation Example - Solution

This directory contains well-documented code that provides context for AI coding assistants.

## What Changed

The solution adds comprehensive documentation that enables AI to understand:

1. **Business logic** - Why discounts are applied and in what order
2. **Constraints** - Valid inputs, expected outputs, error conditions
3. **Domain knowledge** - Policies, rules, and business context
4. **Design decisions** - Architecture choices and their rationale

## Running the Code

```bash
# Run the main example
python main.py

# Run tests
pip install -r requirements.txt
pytest tests/ -v
```

## The Three Layers of Documentation

This solution demonstrates all three layers of documentation:

### Layer 1: Inline Documentation (In Code)
- **Docstrings**: Complete function/class documentation
- **Type Hints**: Explicit types including `Literal` types
- **Inline Comments**: Explain "why" for business logic

### Layer 2: Collocated Documentation (Same Folder)
These files live alongside `main.py`:
- **README.md**: Module overview and quick start
- **ARCHITECTURE.md**: Design decisions for this module
- **DOMAIN.md**: Business rules specific to this module
- **API.md**: Detailed usage examples

### Layer 3: Centralized Documentation (Shared)
These files would live in `/docs/` (referenced, not included):
- **POLICIES.md**: Company-wide policies
- **DOMAIN_MODEL.md**: Shared domain knowledge
- **INTEGRATIONS.md**: Integration patterns

## How This Helps AI

### AI Can Reference:
1. **Inline docs** when reading/modifying code
2. **Collocated docs** when understanding module design
3. **Centralized docs** when respecting company policies

### AI Can:
1. Understand business rules from DOMAIN.md
2. Respect design decisions from ARCHITECTURE.md
3. Follow integration patterns from INTEGRATIONS.md
4. Apply company policies from POLICIES.md
5. Use correct API patterns from API.md

## Key Documentation Patterns

- **Business rules**: Documented in DOMAIN.md and inline comments
- **Discount order**: Explicitly documented in ARCHITECTURE.md and docstrings
- **Policy rationale**: Explained in POLICIES.md and inline comments
- **Validation**: Documented constraints in docstrings and DOMAIN.md
- **Examples**: Show common usage patterns in API.md

## Benefits for AI

With this three-layer documentation approach, AI assistants can:

1. **Understand context** at multiple levels (code → module → enterprise)
2. **Respect business rules** documented in DOMAIN.md
3. **Follow architecture** documented in ARCHITECTURE.md
4. **Apply policies** documented in POLICIES.md
5. **Use correct patterns** documented in API.md
6. **Generate correct code** without guessing at constraints
7. **Make safe modifications** knowing the full context

The key is providing documentation at the right level of granularity for the right audience (code-level, module-level, enterprise-level).

