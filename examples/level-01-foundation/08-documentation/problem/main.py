"""
Subscription pricing calculator.
This code works but lacks documentation that would help AI understand business logic.
"""


class SubscriptionCalculator:
    def __init__(self):
        self.base_price = 10.0
        self.discount_threshold = 3
        self.annual_multiplier = 0.8
    
    def calculate_price(self, plan_type, months, is_student=False, has_coupon=False):
        if plan_type == "basic":
            price = self.base_price
        elif plan_type == "premium":
            price = self.base_price * 2
        else:
            price = self.base_price * 3
        
        if months >= 12:
            price = price * self.annual_multiplier * months
        else:
            price = price * months
        
        if months >= self.discount_threshold:
            price = price * 0.9
        
        if is_student:
            price = price * 0.5
        
        if has_coupon:
            price = price * 0.85
        
        return round(price, 2)
    
    def calculate_refund(self, remaining_days, original_price, cancellation_reason):
        if cancellation_reason == "technical":
            refund = original_price
        elif cancellation_reason == "billing":
            refund = original_price * 0.5
        else:
            refund = original_price * (remaining_days / 30)
        
        return round(refund, 2)


if __name__ == "__main__":
    calc = SubscriptionCalculator()
    
    # Basic subscription
    price = calc.calculate_price("basic", 1)
    print(f"Basic 1 month: ${price}")
    
    # Premium annual
    price = calc.calculate_price("premium", 12)
    print(f"Premium 12 months: ${price}")
    
    # Student discount
    price = calc.calculate_price("basic", 6, is_student=True)
    print(f"Basic 6 months (student): ${price}")
    
    # Refund calculation
    refund = calc.calculate_refund(15, 30.0, "technical")
    print(f"Refund (technical, 15 days left): ${refund}")

