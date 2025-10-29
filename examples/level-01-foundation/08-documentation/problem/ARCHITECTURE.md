# Subscription Calculator Architecture

## Overview

The subscription calculator is designed as a **stateless service** that can be used across multiple systems (billing, web app, mobile app, API).

## Design Decisions

### Stateless Design
- **Decision**: Calculator has no internal state
- **Rationale**: Enables thread-safety, easy testing, and horizontal scaling
- **Trade-off**: All configuration must be passed in or initialized each time
- **Benefit**: Multiple instances can run concurrently without coordination

### Discount Application Order
- **Decision**: Discounts are applied in a specific, documented order
- **Rationale**: Ensures consistent pricing across all systems
- **Order**:
  1. Plan type multiplier
  2. Annual discount (for 12+ months)
  3. Multi-month discount (for 3-11 months, not annual)
  4. Student discount (stacks with all)
  5. Coupon discount (stacks with all)
- **Impact**: Changing order would affect pricing calculations

### Configuration vs. Hard-coded Values
- **Decision**: Base prices and multipliers are configurable via constructor
- **Rationale**: Allows different pricing tiers or A/B testing
- **Default Values**: Sensible defaults provided for simple usage
- **Override**: Production systems can pass in config values

## Integration Points

### Used By
- Billing system (for invoice generation)
- Web application (for price display)
- Mobile app (for subscription UI)
- Subscription API (for real-time pricing)

### Dependencies
- None (pure Python, no external dependencies)
- Can be imported as a module or used as a service

## Thread Safety

- **Safe**: Multiple threads can use the same instance
- **Reason**: No shared mutable state
- **Testing**: Unit tests can run in parallel

## Performance Considerations

- **Complexity**: O(1) - simple calculations
- **Memory**: Minimal - no caching or state storage
- **Scalability**: Stateless design allows horizontal scaling

## Future Considerations

- **Caching**: Could add result caching for repeated calculations
- **Currency**: Currently assumes USD (could be parameterized)
- **Tax**: Tax calculation not included (handled by billing system)
- **Trial Periods**: Free trial logic not included (separate concern)

