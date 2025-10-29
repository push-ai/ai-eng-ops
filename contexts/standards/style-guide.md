# Code Style Guide

## Overview

This style guide defines formatting, naming, and organization conventions for our codebase. Consistent style improves readability and makes code easier for AI assistants to understand and modify.

## General Principles

1. **Readability over brevity** - Code should be clear, not clever
2. **Consistency** - Follow established patterns
3. **Self-documenting** - Good naming reduces need for comments
4. **Type safety** - Use type hints/interfaces everywhere

## Formatting

### Python

- **Line length**: Maximum 100 characters (black default)
- **Indentation**: 4 spaces (never tabs)
- **Quotes**: Single quotes for strings, double for docstrings
- **Imports**: Sorted, grouped (stdlib, third-party, local)
- **Formatting**: Black formatter, isort for imports

```python
# Good
from typing import List, Optional
from pydantic import BaseModel

from app.models import User
from app.services import auth_service

# Bad
from app.models import User
from typing import List, Optional
from pydantic import BaseModel
```

### TypeScript/JavaScript

- **Line length**: Maximum 100 characters
- **Indentation**: 2 spaces
- **Quotes**: Single quotes for strings
- **Semicolons**: Always use semicolons
- **Formatting**: Prettier configured

```typescript
// Good
import { User } from './types';
import { authService } from './services';

// Bad
import {User} from "./types"
import {authService} from "./services"
```

## Naming Conventions

### Variables and Functions

- **Snake_case** for Python (functions, variables)
- **camelCase** for TypeScript/JavaScript (functions, variables)
- **Descriptive names**: `calculate_total_price` not `calc` or `tot`
- **Boolean prefixes**: `is_`, `has_`, `should_`, `can_`

```python
# Good
def calculate_total_price(items: List[Item]) -> float:
    is_valid = validate_items(items)
    if is_valid:
        return sum(item.price for item in items)
    return 0.0

# Bad
def calc(items):
    v = check(items)
    if v:
        return sum(i.p for i in items)
    return 0
```

### Classes

- **PascalCase** for both Python and TypeScript
- **Descriptive names**: `UserAuthenticator` not `Auth` or `UA`

```python
# Good
class UserAuthenticator:
    pass

class PaymentProcessor:
    pass

# Bad
class Auth:
    pass

class PP:
    pass
```

### Constants

- **UPPER_SNAKE_CASE** for constants
- **Module-level**: Defined at module level

```python
# Good
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30

# Bad
maxRetries = 3
timeout = 30
```

## File Organization

### Python

```
module/
├── __init__.py
├── models.py          # Data models
├── services.py        # Business logic
├── utils.py           # Utility functions
└── tests/
    ├── __init__.py
    ├── test_models.py
    └── test_services.py
```

### TypeScript

```
module/
├── index.ts           # Public exports
├── types.ts           # Type definitions
├── services.ts        # Business logic
├── utils.ts           # Utility functions
└── __tests__/
    ├── services.test.ts
    └── utils.test.ts
```

## Comments and Documentation

### Docstrings

- **All public functions/classes**: Required docstrings
- **Google style** for Python, JSDoc for TypeScript
- **Include**: Parameters, returns, raises/exceptions, examples

```python
def process_payment(
    amount: float,
    currency: str,
    payment_method: str
) -> PaymentResult:
    """
    Process a payment transaction.
    
    Args:
        amount: Payment amount (must be > 0)
        currency: Currency code (ISO 4217, e.g., 'USD')
        payment_method: Payment method ('credit_card', 'paypal', etc.)
    
    Returns:
        PaymentResult with transaction_id and status
    
    Raises:
        ValueError: If amount <= 0 or invalid currency
        PaymentError: If payment processing fails
    
    Example:
        >>> result = process_payment(100.0, 'USD', 'credit_card')
        >>> result.status
        'success'
    """
    pass
```

### Inline Comments

- **Explain "why"** not "what"
- **Rare** - Code should be self-documenting
- **Complex logic**: Explain non-obvious algorithms

```python
# Good: Explains why
# Apply 10% discount for orders over $1000 (company policy)
if order_total > 1000:
    discount = order_total * 0.1

# Bad: Explains what (obvious)
# Calculate discount by multiplying order_total by 0.1
discount = order_total * 0.1
```

## Type Hints and Interfaces

### Python

- **Always use type hints** for function parameters and returns
- **Use TypedDict** for dictionary structures
- **Use Literal** for constrained string values

```python
from typing import TypedDict, Literal

PlanType = Literal["basic", "premium", "enterprise"]

class User(TypedDict):
    id: int
    name: str
    email: str

def get_user(user_id: int) -> Optional[User]:
    pass
```

### TypeScript

- **Always use interfaces** for object types
- **Use types** for unions and intersections
- **Use enums** for fixed sets of values

```typescript
type PlanType = "basic" | "premium" | "enterprise";

interface User {
  id: number;
  name: string;
  email: string;
}

function getUser(userId: number): User | null {
  // ...
}
```

## Error Handling

### Error Types

- **Custom exceptions** for domain errors
- **Standard exceptions** for common errors (ValueError, TypeError)
- **Clear error messages** with context

```python
# Good
class PaymentError(Exception):
    """Raised when payment processing fails."""
    pass

def process_payment(amount: float) -> PaymentResult:
    if amount <= 0:
        raise ValueError(f"Invalid amount: {amount}. Amount must be > 0")
    try:
        return _charge_card(amount)
    except CardError as e:
        raise PaymentError(f"Card charge failed: {e}") from e
```

## Testing Style

### Test Naming

- **Descriptive names**: `test_calculate_discount_with_valid_input`
- **Test organization**: Group related tests in classes
- **Arrange-Act-Assert**: Clear test structure

```python
class TestCalculateDiscount:
    def test_valid_discount_returns_correct_price(self):
        # Arrange
        price = 100.0
        discount = 10.0
        
        # Act
        result = calculate_discount(price, discount)
        
        # Assert
        assert result == 90.0
    
    def test_invalid_price_raises_error(self):
        # Arrange
        price = -10.0
        discount = 10.0
        
        # Act & Assert
        with pytest.raises(ValueError):
            calculate_discount(price, discount)
```

## Language-Specific Guidelines

### Python

- **Type hints**: Always use (see above)
- **Docstrings**: Google style
- **Imports**: Grouped and sorted
- **Virtual environments**: Use for all projects
- **Dependencies**: Pin versions in requirements.txt

### TypeScript

- **Strict mode**: Always enabled
- **No `any`**: Avoid `any` type
- **Interfaces over types**: Prefer interfaces for objects
- **ESLint**: Configured with strict rules
- **Prettier**: Auto-format on save

## Tools Configuration

### Python

- **Black**: Code formatter (line length: 100)
- **isort**: Import sorter
- **mypy**: Type checker (strict mode)
- **pylint**: Linter

### TypeScript

- **Prettier**: Code formatter
- **ESLint**: Linter with strict rules
- **TypeScript**: Strict compiler options

## References

- Code Quality Standards: `contexts/standards/code-quality.md`
- Architecture Patterns: `contexts/architecture/patterns.md`

