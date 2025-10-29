# Documentation Principle: Context Enables AI Accuracy

## The Principle

**Well-structured documentation provides context that enables AI to understand intent, constraints, and business logic—preventing incorrect assumptions and enabling accurate code generation.** Documentation acts as explicit context that guides AI to produce code that aligns with your actual requirements, not what it guesses.

## Why This Matters for AI Engineering

### The Problem: AI Guesses Without Context

When AI encounters code without documentation, it makes assumptions:

```python
# AI sees this code:
price = price * 0.5

# AI guesses:
# - Is this a 50% discount?
# - Is this a student discount?
# - Is this a special promotion?
# - Is this temporary or permanent?
# - What are the business rules?
```

Without documentation, AI will:
- **Guess at business logic** and make incorrect changes
- **Miss important constraints** when adding features
- **Violate domain rules** because it doesn't understand them
- **Produce inconsistent code** because it doesn't know the patterns

### The Solution: Documentation as Explicit Context

Documentation provides AI with the context it needs:

```python
# With documentation:
# Student discount: 50% off all plans (per company policy)
# Applies to all plan types and durations
price = price * 0.5
```

Now AI understands:
- **What** it is (student discount)
- **Why** it exists (company policy)
- **When** it applies (all plans)
- **Constraints** (universal application)

## Types of Documentation That Help AI

### 1. **Inline Comments: "Why" Not "What"**

**Purpose**: Explain the reasoning behind code, especially business logic and non-obvious decisions.

**When to Use Explicitly**:
- Business rules that aren't obvious from code
- Domain-specific logic
- Non-standard calculations or algorithms
- Workarounds or temporary solutions
- Historical context ("We do X because of Y requirement")

**When AI Can Find Implicitly**:
- Standard patterns (list comprehensions, common algorithms)
- Self-explanatory code with good naming
- Conventional code structures

**Example**:
```python
# Explicit (business logic needs explanation):
# Apply annual discount: 20% off for 12+ month commitments
# This incentivizes longer commitments per marketing strategy
if months >= 12:
    price = price * 0.8 * months

# Implicit is fine (standard pattern):
users = [u for u in all_users if u.is_active]
```

### 2. **Docstrings: API Contracts**

**Purpose**: Define function/class interfaces, expected inputs, outputs, and behavior.

**When to Use Explicitly**:
- Public APIs and interfaces
- Complex functions with multiple parameters
- Functions with side effects
- Functions with non-obvious return types
- Functions with important constraints or edge cases

**When AI Can Find Implicitly**:
- Very simple functions (if self-documenting)
- Private/internal functions (less critical, but still helpful)
- Standard library wrappers

**Example**:
```python
def calculate_price(
    plan_type: str,
    months: int,
    is_student: bool = False,
    has_coupon: bool = False
) -> float:
    """
    Calculate subscription price with applicable discounts.
    
    Applies discounts in this order:
    1. Annual discount (20% off for 12+ months)
    2. Multi-month discount (10% off for 3+ months)
    3. Student discount (50% off, stacks with others)
    4. Coupon discount (15% off, stacks with others)
    
    Args:
        plan_type: Subscription tier - "basic", "premium", or "enterprise"
        months: Subscription duration (1-24 months)
        is_student: Whether user qualifies for student discount
        has_coupon: Whether user has valid promotional coupon
    
    Returns:
        Final price rounded to 2 decimal places
    
    Raises:
        ValueError: If plan_type is invalid or months < 1
    
    Example:
        >>> calc.calculate_price("premium", 12, is_student=True)
        48.0  # Premium base ($20) * 12 months * 0.8 annual * 0.5 student
    """
```

### 3. **Collocated Documentation Files** (Same Folder/Module)

**Purpose**: Documentation files that live alongside your code in the same directory or module, providing module-specific context.

**Types of Collocated Docs**:
- **README.md**: Module overview, quick start, basic usage
- **ARCHITECTURE.md**: Design decisions specific to this module
- **DOMAIN.md**: Business rules and domain knowledge for this module
- **API.md**: Detailed API documentation and usage patterns

**When to Use Explicitly**:
- Module-specific architecture decisions
- Business rules that apply to this module
- API usage patterns for this module
- Design decisions and trade-offs
- Module-specific constraints

**When AI Can Find Implicitly**:
- Very simple modules with obvious structure
- Standard patterns that don't need explanation

**Example Structure**:
```
subscription_calculator/
├── main.py              # Code with inline docs
├── README.md            # Module overview
├── ARCHITECTURE.md      # Design decisions
├── DOMAIN.md            # Business rules
└── API.md               # Usage examples
```

### 4. **Centralized Documentation** (Shared Across Services)

**Purpose**: Documentation files in a central location (e.g., `/docs/`, `/architecture/`) that provide context shared across multiple services or the entire organization.

**Types of Centralized Docs**:
- **POLICIES.md**: Company-wide policies and standards
- **DOMAIN_MODEL.md**: Shared domain knowledge across services
- **INTEGRATIONS.md**: Integration patterns used by multiple services
- **ARCHITECTURE.md**: Enterprise-wide architecture decisions

**When to Use Explicitly**:
- Knowledge shared across multiple services
- Company-wide policies and standards
- Enterprise architecture decisions
- Domain knowledge used by multiple teams
- Integration patterns used everywhere

**When AI Can Find Implicitly**:
- Organization-specific patterns that are obvious from code
- Standard industry practices

**Example Structure**:
```
project/
├── docs/
│   ├── POLICIES.md       # Company policies
│   ├── DOMAIN_MODEL.md   # Shared domain
│   └── INTEGRATIONS.md   # Integration patterns
├── service1/
│   └── main.py
└── service2/
    └── main.py
```

### 5. **Type Hints: Interface Contracts**

**Purpose**: Define expected data types and structure (see 03-data-structure for more detail).

**When to Use Explicitly**:
- **Always** for complex types and data structures
- Public APIs
- Functions with multiple parameters
- Return types that aren't obvious

**When AI Can Find Implicitly**:
- Simple, obvious types (`def add(a: int, b: int) -> int`)
- Python infers some types well

### 6. **Examples and Usage Patterns**

**Purpose**: Show how code should be used, demonstrate edge cases, and illustrate patterns.

**When to Use Explicitly**:
- Complex APIs that need demonstration
- Common usage patterns
- Edge cases and error handling
- Integration examples

**When AI Can Find Implicitly**:
- Self-explanatory APIs
- Standard library patterns

**Example**:
```python
"""
Usage Examples:

# Basic subscription
price = calc.calculate_price("basic", 1)  # $10.00

# Premium annual with student discount
price = calc.calculate_price("premium", 12, is_student=True)  # $48.00

# Edge case: Invalid plan type
try:
    price = calc.calculate_price("invalid", 1)
except ValueError as e:
    print(f"Error: {e}")
"""
```

## The Three Layers of Documentation

### Layer 1: Inline Documentation (In Code)
- **Docstrings**: Function/class documentation
- **Type Hints**: Type information
- **Inline Comments**: Explain "why" for business logic
- **Lives**: Embedded directly in code files

### Layer 2: Collocated Documentation (Same Folder)
- **README.md**: Module overview and quick start
- **ARCHITECTURE.md**: Module-specific design decisions
- **DOMAIN.md**: Module-specific business rules
- **API.md**: Detailed usage examples
- **Lives**: Same directory as code, scoped to this module

### Layer 3: Centralized Documentation (Shared)
- **POLICIES.md**: Company-wide policies
- **DOMAIN_MODEL.md**: Shared domain knowledge
- **INTEGRATIONS.md**: Integration patterns
- **Lives**: Central `/docs/` folder, shared across services

## When to Use Documentation Explicitly vs. Implicitly

### Use Explicit Documentation When:

1. **Business Logic**: Domain rules, policies, and business constraints
2. **Non-Obvious Decisions**: Why code works a certain way, not just what it does
3. **Constraints**: Valid inputs, expected outputs, side effects
4. **Architecture**: Design decisions and trade-offs
5. **Integration Points**: How code interacts with other systems
6. **Historical Context**: Why something was done a certain way
7. **Shared Knowledge**: Information used by multiple services (centralized docs)

### AI Can Find Implicitly When:

1. **Standard Patterns**: Common algorithms, list comprehensions, etc.
2. **Self-Explanatory Code**: Well-named functions that clearly express intent
3. **Conventional Structures**: Standard library usage, common frameworks
4. **Simple Code**: Trivial functions that are obvious from their implementation

## The Documentation Strategy

1. **Start with Inline Docs**: Docstrings, type hints, inline comments
2. **Add Collocated Docs**: README, ARCHITECTURE, DOMAIN, API files for each module
3. **Create Centralized Docs**: Policies, domain model, integrations for shared knowledge
4. **Reference Docs in Code**: Point AI to relevant documentation files
5. **Keep Docs Updated**: Documentation should evolve with code

## The Prompt

Copy this prompt and use it with your AI coding assistant:

```
I need you to help me create comprehensive documentation for this code module that will 
help AI assistants understand the code's purpose, business logic, and constraints.

Please help me create:

1. **Inline documentation** (in the code files):
   - Docstrings for all functions and classes
   - Inline comments explaining "why" for business logic
   - Type hints on all function signatures
   - Examples in docstrings

2. **Collocated documentation files** (in the same folder as the code):
   - README.md: Module overview, quick start, basic usage
   - ARCHITECTURE.md: Design decisions specific to this module
   - DOMAIN.md: Business rules and domain knowledge for this module
   - API.md: Detailed API documentation and usage patterns

3. **Reference centralized documentation** (in /docs/ folder):
   - Point to relevant POLICIES.md if company policies apply
   - Reference DOMAIN_MODEL.md for shared domain knowledge
   - Reference INTEGRATIONS.md for integration patterns

Focus especially on documenting:
- Business logic that isn't obvious from the code
- Domain knowledge that AI wouldn't know
- Constraints and validation rules
- Design decisions and their rationale
- How this module integrates with other systems

The goal is to give AI assistants enough context through documentation files to modify 
this code correctly without guessing at business rules or constraints. Documentation 
should be organized at three levels: inline (in code), collocated (same folder), and 
centralized (shared docs).
```

## Expected Outcome

After adding documentation, AI assistants will:

1. **Understand business logic** and apply it correctly when making changes
2. **Respect constraints** documented in docstrings and comments
3. **Make safe modifications** because they understand the design intent
4. **Add features correctly** because they know the patterns and rules
5. **Avoid breaking changes** because they understand the contracts

Documentation transforms code from "code that works" to "code that AI can reliably understand and modify."

