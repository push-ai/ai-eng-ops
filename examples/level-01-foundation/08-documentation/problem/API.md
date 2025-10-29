# Subscription Calculator API

## Usage Examples

### Basic Price Calculation

```python
from subscription_calculator import SubscriptionCalculator

calc = SubscriptionCalculator()

# Basic plan, 1 month
price = calc.calculate_price("basic", 1)
# Returns: 10.0

# Premium plan, 12 months
price = calc.calculate_price("premium", 12)
# Returns: 192.0  # $20 × 12 × 0.8 annual discount
```

### Discount Combinations

```python
# Student discount
price = calc.calculate_price("basic", 6, is_student=True)
# Returns: 27.0  # $10 × 6 × 0.9 multi-month × 0.5 student

# Coupon discount
price = calc.calculate_price("enterprise", 3, has_coupon=True)
# Returns: 68.85  # $30 × 3 × 0.9 multi-month × 0.85 coupon

# All discounts stacked
price = calc.calculate_price(
    "enterprise", 
    12, 
    is_student=True, 
    has_coupon=True
)
# Returns: 122.4  # $30 × 12 × 0.8 annual × 0.5 student × 0.85 coupon
```

### Refund Calculations

```python
# Technical issue - full refund
refund = calc.calculate_refund(15, 30.0, "technical")
# Returns: 30.0  # Full refund regardless of days

# Billing issue - 50% refund
refund = calc.calculate_refund(20, 30.0, "billing")
# Returns: 15.0  # 50% refund regardless of days

# Other reason - pro-rated
refund = calc.calculate_refund(15, 30.0, "other")
# Returns: 15.0  # 15/30 × $30 = $15
```

## Error Handling

### Invalid Plan Type

```python
try:
    price = calc.calculate_price("invalid", 1)
except ValueError as e:
    print(f"Error: {e}")
    # Error: Invalid plan_type: invalid. Must be one of ('basic', 'premium', 'enterprise')
```

### Invalid Duration

```python
try:
    price = calc.calculate_price("basic", 0)
except ValueError as e:
    print(f"Error: {e}")
    # Error: Invalid months: 0. Must be between 1 and 24
```

### Invalid Refund Parameters

```python
try:
    refund = calc.calculate_refund(-1, 30.0, "other")
except ValueError as e:
    print(f"Error: {e}")
    # Error: remaining_days must be >= 0, got -1
```

## Integration Patterns

### Web Application Integration

```python
# Display price to user
def get_display_price(plan_type: str, months: int, user: User) -> float:
    calc = SubscriptionCalculator()
    return calc.calculate_price(
        plan_type,
        months,
        is_student=user.is_student,
        has_coupon=user.has_active_coupon
    )
```

### Billing System Integration

```python
# Calculate invoice amount
def calculate_invoice_amount(subscription: Subscription) -> float:
    calc = SubscriptionCalculator()
    return calc.calculate_price(
        subscription.plan_type,
        subscription.duration_months,
        is_student=subscription.user.is_student,
        has_coupon=subscription.coupon_code is not None
    )
```

### Customer Support Integration

```python
# Calculate refund for support request
def process_refund_request(request: RefundRequest) -> float:
    calc = SubscriptionCalculator()
    return calc.calculate_refund(
        request.remaining_days,
        request.original_price,
        request.cancellation_reason
    )
```

## Configuration

### Custom Pricing

```python
# Use custom base price for different markets
calc_us = SubscriptionCalculator(base_price=10.0)
calc_eu = SubscriptionCalculator(base_price=9.0)  # EUR equivalent

# Custom discount thresholds
calc_custom = SubscriptionCalculator(
    base_price=10.0,
    discount_threshold=6,  # 6+ months instead of 3+
    annual_multiplier=0.75  # 25% off instead of 20%
)
```

## Testing Examples

### Unit Testing

```python
import pytest
from subscription_calculator import SubscriptionCalculator

def test_basic_price():
    calc = SubscriptionCalculator()
    assert calc.calculate_price("basic", 1) == 10.0

def test_annual_discount():
    calc = SubscriptionCalculator()
    assert calc.calculate_price("premium", 12) == 192.0

def test_student_discount():
    calc = SubscriptionCalculator()
    assert calc.calculate_price("basic", 6, is_student=True) == 27.0
```

### Integration Testing

```python
def test_pricing_consistency():
    """Verify prices are consistent across multiple calls."""
    calc = SubscriptionCalculator()
    price1 = calc.calculate_price("premium", 12)
    price2 = calc.calculate_price("premium", 12)
    assert price1 == price2  # Stateless, always same result
```

## Performance Considerations

- **Speed**: O(1) - simple calculations, very fast
- **Memory**: Minimal - no caching or state
- **Concurrency**: Thread-safe - can run in parallel
- **Scalability**: Stateless design allows horizontal scaling

## Versioning

- **Current Version**: 1.0
- **Breaking Changes**: None planned
- **Backward Compatibility**: Maintained for all public APIs

