# Subscription Domain Knowledge

## Business Rules

### Subscription Plans

#### Plan Types
- **Basic**: Base plan ($10/month)
- **Premium**: 2x base price ($20/month)
- **Enterprise**: 3x base price ($30/month)

#### Plan Selection
- Users select plan type at signup
- Can upgrade/downgrade (handled by billing system, not calculator)
- Plan type determines base monthly price

### Discount Rules

#### Annual Discount
- **Applies to**: Subscriptions of 12+ months
- **Discount**: 20% off
- **Rationale**: Incentivize longer commitments
- **Note**: Annual subscriptions do NOT also get multi-month discount
- **Example**: Premium 12 months = $20 × 12 × 0.8 = $192/year

#### Multi-Month Discount
- **Applies to**: Subscriptions of 3-11 months (non-annual)
- **Discount**: 10% off
- **Rationale**: Reward customer loyalty with multi-month commitments
- **Note**: Does NOT apply to annual subscriptions (they get annual discount instead)
- **Example**: Basic 6 months = $10 × 6 × 0.9 = $54

#### Student Discount
- **Applies to**: All plan types and durations
- **Discount**: 50% off
- **Rationale**: Company policy to make subscriptions accessible to students
- **Stacks with**: All other discounts
- **Verification**: Student status verified by separate system (not calculator concern)
- **Example**: Premium 12 months with student = $20 × 12 × 0.8 × 0.5 = $96/year

#### Coupon Discount
- **Applies to**: When user has valid promotional coupon
- **Discount**: 15% off
- **Rationale**: Used for promotional campaigns and customer retention
- **Stacks with**: All other discounts
- **Validation**: Coupon validity checked by separate system (not calculator concern)
- **Example**: Enterprise 6 months with coupon = $30 × 6 × 0.9 × 0.85 = $137.70

### Discount Stacking Rules

1. **Annual vs. Multi-Month**: Mutually exclusive (annual subscriptions don't get multi-month discount)
2. **Student and Coupon**: Both stack with all other discounts
3. **Application Order**: Plan type → Annual/Multi-month → Student → Coupon
4. **Result**: Always rounded to 2 decimal places (currency format)

### Refund Policies

#### Technical Issues
- **Refund**: 100% (full refund)
- **Rationale**: Company takes responsibility for technical problems affecting service
- **Applies**: Regardless of remaining days
- **Process**: Handled by customer support, calculator provides amount

#### Billing Issues
- **Refund**: 50% (partial refund)
- **Rationale**: Acknowledges billing problem but covers operational costs
- **Applies**: Regardless of remaining days
- **Process**: Handled by billing team, calculator provides amount

#### Other Reasons
- **Refund**: Pro-rated based on remaining days
- **Rationale**: Fair refund based on unused service
- **Calculation**: (remaining_days / 30) × original_price
- **Assumption**: Standard 30-day billing period
- **Process**: Standard cancellation, calculator provides amount

### Constraints

#### Subscription Duration
- **Minimum**: 1 month
- **Maximum**: 24 months
- **Validation**: Calculator enforces these limits

#### Pricing Constraints
- **Currency**: USD (US Dollars)
- **Precision**: Rounded to 2 decimal places
- **Negative Prices**: Not allowed (validated in calculator)

#### Refund Constraints
- **Remaining Days**: Must be >= 0
- **Original Price**: Must be > 0
- **Cancellation Reason**: Must be one of the documented reasons

## Domain Entities

### Subscription
- Plan type (basic/premium/enterprise)
- Duration (months)
- Student status (boolean)
- Coupon status (boolean)
- Start date
- End date

### Refund Request
- Subscription reference
- Cancellation reason
- Remaining days
- Original price paid
- Requested date

## Domain Events

### Pricing Events
- Price calculated (for display)
- Price updated (for changes)
- Discount applied (for tracking)

### Refund Events
- Refund calculated
- Refund processed
- Refund denied (if outside policy)

## Integration with Other Systems

### Billing System
- Receives calculated prices for invoices
- Handles payment processing
- Manages subscription lifecycle

### Customer Support
- Uses refund calculator for customer requests
- Applies refund policies based on reason
- Processes refunds through billing system

### Student Verification Service
- Verifies student status (separate from calculator)
- Provides student status to billing system
- Calculator trusts student flag passed in

### Coupon Management System
- Validates coupon codes (separate from calculator)
- Tracks coupon usage
- Calculator trusts coupon flag passed in

