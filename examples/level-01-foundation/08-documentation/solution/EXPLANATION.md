# Documentation: Context Enables AI Accuracy

## What Changed

The solution demonstrates the **three layers of documentation** needed to help AI assistants understand and modify code correctly:

1. **Inline Documentation** (embedded in code)
2. **Collocated Documentation** (same folder as code)
3. **Centralized Documentation** (shared across services)

This multi-layered approach provides context at different levels of granularity, from code-level details to enterprise-wide policies.

## The Transformation

### Before: Code Without Context

The original code worked but provided no context:
- No explanation of business rules
- No documentation of discount application order
- No clarity on why certain calculations exist
- No constraints documented
- No examples or usage patterns

**Result**: AI would guess at business logic and potentially make incorrect modifications.

### After: Code With Comprehensive Documentation

The solution adds multiple layers of documentation:

#### 1. **Module-Level Documentation**
```python
"""
Subscription Pricing Calculator

Business Rules:
- Annual subscriptions (12+ months) receive 20% discount
- Multi-month subscriptions (3+ months) receive 10% discount
...
"""
```
**Why**: Provides high-level context that AI can read at the top of the file.

#### 2. **Inline Comments Explaining "Why"**
```python
# Annual discount: 20% off for 12+ months
# Per marketing strategy: incentivize longer commitments
if months >= 12:
    price = price * self.annual_multiplier * months
```
**Why**: Explains the business rationale, not just what the code does.

#### 3. **Comprehensive Docstrings**
```python
def calculate_price(...) -> float:
    """
    Calculate subscription price with applicable discounts.
    
    Applies discounts in this order:
    1. Plan type multiplier
    2. Annual discount (20% off for 12+ months)
    ...
    
    Args:
        plan_type: Subscription tier - must be "basic", "premium", or "enterprise"
        ...
    
    Returns:
        Final price rounded to 2 decimal places
    
    Raises:
        ValueError: If plan_type is invalid or months is outside valid range
    
    Example:
        >>> calc.calculate_price("premium", 12, is_student=True)
        48.0
    """
```
**Why**: Defines the complete contract - inputs, outputs, behavior, examples.

#### 4. **Type Hints**
```python
PlanType = Literal["basic", "premium", "enterprise"]

def calculate_price(
    plan_type: PlanType,
    months: int,
    is_student: bool = False,
    has_coupon: bool = False
) -> float:
```
**Why**: Explicitly defines allowed values and types, preventing AI from guessing.

#### 5. **Usage Examples**
```python
if __name__ == "__main__":
    # Multiple examples showing different patterns
    price = calc.calculate_price("premium", 12)
    ...
```
**Why**: Shows AI how the code should be used in practice.

## The Three Layers of Documentation

### Layer 1: Inline Documentation (In Code)

**Location**: Embedded directly in code files (`main.py`)

**Includes**:
- **Docstrings**: Function/class documentation with parameters, returns, examples
- **Type Hints**: Explicit types including `Literal` types for constrained values
- **Inline Comments**: Explain "why" for business logic, not just "what"

**Example**:
```python
# Student discount: 50% off all plans
# Policy: Make subscriptions accessible to students
if is_student:
    price = price * 0.5
```

**Why This Layer**: Provides immediate context when reading or modifying code.

### Layer 2: Collocated Documentation (Same Folder)

**Location**: Same directory as code (alongside `main.py`)

**Files**:
- **README.md**: Module overview, quick start, basic usage
- **ARCHITECTURE.md**: Design decisions specific to this module
- **DOMAIN.md**: Business rules and domain knowledge for this module
- **API.md**: Detailed API documentation and usage patterns

**When to Use**:
- Module-specific context
- Design decisions for this component
- Business rules for this feature
- Usage patterns for this API

**Why This Layer**: Provides module-level context that's too extensive for inline docs but specific to this module.

### Layer 3: Centralized Documentation (Shared)

**Location**: Central `/docs/` folder (or `/architecture/`), shared across services

**Files**:
- **POLICIES.md**: Company-wide policies and standards
- **DOMAIN_MODEL.md**: Shared domain knowledge across services
- **INTEGRATIONS.md**: Integration patterns used by multiple services

**When to Use**:
- Knowledge shared across multiple services
- Company-wide policies and standards
- Enterprise architecture decisions
- Domain knowledge used by multiple teams

**Why This Layer**: Provides enterprise-wide context that applies to multiple modules or services.

## How AI Uses These Layers

### Reading Code
1. **Inline docs** provide immediate context in the code
2. **Collocated docs** provide module-level context
3. **Centralized docs** provide enterprise-wide context

### Modifying Code
1. AI references **inline docs** to understand function contracts
2. AI references **collocated docs** to understand module design
3. AI references **centralized docs** to understand policies and domain rules

### Adding Features
1. AI uses **inline docs** to maintain existing patterns
2. AI uses **collocated docs** to align with module architecture
3. AI uses **centralized docs** to respect company policies

## When to Use Documentation Explicitly vs. Implicitly

### Use Explicit Documentation When:

1. **Business Logic** ⭐ Critical
   - Domain rules that aren't obvious
   - Policies and constraints
   - Why code works a certain way

2. **Constraints**
   - Valid inputs and ranges
   - Expected outputs
   - Error conditions

3. **Architecture**
   - Design decisions
   - Trade-offs
   - Integration points

4. **Domain Knowledge**
   - Information AI wouldn't know
   - Industry-specific rules
   - Company policies

### AI Can Find Implicitly When:

1. **Standard Patterns**
   - Common algorithms
   - List comprehensions
   - Standard library usage

2. **Self-Explanatory Code**
   - Well-named functions
   - Obvious implementations
   - Conventional structures

## The Impact

### Before Documentation:
- AI guesses at business logic
- AI doesn't know discount order matters
- AI might add features that violate policies
- AI doesn't understand constraints

### After Documentation:
- AI understands business rules
- AI respects discount application order
- AI adds features that align with policies
- AI knows all constraints and validates correctly

## Key Takeaway

**Documentation provides context that prevents AI from making incorrect assumptions.** Without it, AI guesses. With it, AI knows.

The most critical documentation to add explicitly:
1. Business logic and domain rules
2. Constraints and validation rules
3. Architecture decisions
4. Non-obvious design choices

Everything else can often be inferred from well-written code, but these require explicit documentation.

