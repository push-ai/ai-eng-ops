# Integration Patterns

## Subscription Calculator Integration

### Overview
The subscription calculator is a **stateless service** that can be integrated into multiple systems.

### Integration Points

#### 1. Price Calculation
**Used By**: Web app, Mobile app, Subscription API

**Pattern**:
```python
from subscription_calculator import SubscriptionCalculator

calc = SubscriptionCalculator()
price = calc.calculate_price(
    plan_type="premium",
    months=12,
    is_student=user.is_student,
    has_coupon=user.has_active_coupon
)
```

**Context Provided**:
- User student status (from user service)
- Active coupon (from coupon service)
- Plan selection (from user input)

#### 2. Invoice Generation
**Used By**: Billing System

**Pattern**:
```python
# Billing system calculates invoice amount
calc = SubscriptionCalculator()
invoice_amount = calc.calculate_price(
    subscription.plan_type,
    subscription.duration_months,
    is_student=subscription.user.is_student,
    has_coupon=subscription.coupon_code is not None
)
```

**Context Provided**:
- Subscription details (from subscription service)
- User information (from user service)
- Coupon information (from coupon service)

#### 3. Refund Processing
**Used By**: Customer Support, Billing System

**Pattern**:
```python
# Calculate refund amount
calc = SubscriptionCalculator()
refund_amount = calc.calculate_refund(
    remaining_days=subscription.remaining_days,
    original_price=subscription.original_price,
    cancellation_reason=request.reason
)
```

**Context Provided**:
- Subscription status (from subscription service)
- Cancellation reason (from support request)
- Original price (from billing records)

## Service Dependencies

### Calculator Dependencies
- **None**: Pure Python, no external dependencies
- **Status**: Fully self-contained

### Services That Depend on Calculator
- **Billing System**: Uses for invoice calculations
- **Web Application**: Uses for price display
- **Mobile Application**: Uses for subscription UI
- **Subscription API**: Uses for real-time pricing
- **Customer Support**: Uses for refund calculations

## Data Flow

### Price Calculation Flow
```
User → Web App → Subscription Calculator → Price Display
                     ↑
                (student status, coupon from other services)
```

### Refund Calculation Flow
```
Support Request → Billing System → Subscription Calculator → Refund Amount
                                        ↑
                              (subscription details from subscription service)
```

## Error Handling

### Calculator Errors
- Invalid plan type → ValueError
- Invalid duration → ValueError
- Invalid refund parameters → ValueError

### Integration Error Handling
```python
try:
    price = calc.calculate_price(plan_type, months, is_student, has_coupon)
except ValueError as e:
    # Log error, return error response to user
    logger.error(f"Price calculation failed: {e}")
    return {"error": "Invalid subscription parameters"}
```

## Testing Integration

### Mock Calculator for Testing
```python
from unittest.mock import Mock

# Mock calculator for integration tests
mock_calc = Mock(spec=SubscriptionCalculator)
mock_calc.calculate_price.return_value = 100.0
```

### Integration Test Example
```python
def test_billing_integration():
    """Test billing system integrates correctly with calculator."""
    calc = SubscriptionCalculator()
    subscription = create_test_subscription()
    
    amount = billing_system.calculate_invoice(subscription, calc)
    
    assert amount > 0
    assert isinstance(amount, float)
```

## Performance Considerations

- **Stateless**: No state to manage, scales horizontally
- **Fast**: O(1) calculations, minimal overhead
- **Thread-Safe**: Can handle concurrent requests
- **Caching**: Consider caching results if called frequently with same inputs

## Deployment

### Standalone Module
- Import as Python module
- No additional deployment needed
- Works in any Python environment

### Microservice (Future)
- Could be deployed as separate service
- REST API wrapper around calculator
- Allows independent scaling

