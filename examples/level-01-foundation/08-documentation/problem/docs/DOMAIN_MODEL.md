# Shared Domain Model

## Subscription Domain

### Core Concepts

#### Subscription Plan
- **Basic**: Entry-level plan ($10/month base)
- **Premium**: Mid-tier plan ($20/month base)
- **Enterprise**: High-tier plan ($30/month base)

#### Subscription Duration
- Measured in months (1-24)
- Minimum commitment: 1 month
- Maximum commitment: 24 months
- Standard billing cycle: 30 days

#### Discount Types
- **Annual**: 20% off for 12+ month commitments
- **Multi-Month**: 10% off for 3-11 month commitments
- **Student**: 50% off (company policy)
- **Coupon**: 15% off (promotional)

### Entities

#### Subscription
```
- id: string
- plan_type: enum (basic|premium|enterprise)
- duration_months: int (1-24)
- start_date: date
- end_date: date
- user_id: string
- student: boolean
- coupon_code: string | null
- status: enum (active|cancelled|expired)
```

#### Refund
```
- id: string
- subscription_id: string
- cancellation_reason: enum (technical|billing|other)
- remaining_days: int
- original_price: float
- refund_amount: float
- processed_date: date
- status: enum (pending|approved|denied|processed)
```

### Business Rules

#### Discount Rules
1. Annual and multi-month discounts are mutually exclusive
2. Student discount applies to all plans and durations
3. Coupon discount applies to all plans and durations
4. Student and coupon discounts stack with other discounts
5. Discounts applied in specific order (see ARCHITECTURE.md)

#### Refund Rules
1. Technical issues: Full refund
2. Billing issues: 50% refund
3. Other reasons: Pro-rated refund
4. Refunds calculated based on original price paid

### Shared Knowledge

This domain model is used across:
- Subscription Calculator (this module)
- Billing System
- Web Application
- Mobile Application
- Customer Support System
- Subscription API

