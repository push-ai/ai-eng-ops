# Company Policies

## Student Discount Policy

### Eligibility
- **Qualification**: Current enrollment in accredited educational institution
- **Verification**: Required annually via student verification service
- **Application**: 50% discount on all subscription plans
- **Stacking**: Student discount stacks with all other discounts

### Rationale
Company policy to make subscriptions accessible to students and support education.

### Implementation
- Student status verified by separate verification service
- Calculator receives boolean flag `is_student`
- No verification logic in calculator (separation of concerns)

## Refund Policy

### Technical Issues
- **Policy**: Full refund regardless of remaining subscription time
- **Rationale**: Company takes responsibility for technical problems affecting service
- **Process**: Customer support verifies technical issue, calculator provides refund amount

### Billing Issues
- **Policy**: 50% refund regardless of remaining subscription time
- **Rationale**: Acknowledges billing problem but covers operational costs
- **Process**: Billing team verifies issue, calculator provides refund amount

### Other Cancellations
- **Policy**: Pro-rated refund based on remaining days
- **Rationale**: Fair refund based on unused service
- **Calculation**: (remaining_days / 30) × original_price
- **Process**: Standard cancellation process

## Pricing Policies

### Discount Application
- Discounts applied in documented order (see ARCHITECTURE.md)
- Annual and multi-month discounts are mutually exclusive
- Student and coupon discounts stack with all other discounts

### Currency
- All prices in USD (US Dollars)
- Rounded to 2 decimal places
- No support for other currencies (handled by separate service)

### Price Changes
- Price changes require notification to billing system
- Historical prices maintained for active subscriptions
- Calculator uses current pricing for new subscriptions

