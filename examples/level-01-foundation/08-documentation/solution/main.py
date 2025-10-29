"""
Subscription Pricing Calculator

This module handles subscription pricing calculations with multiple discount types.
Used by the billing system to calculate customer subscription costs.

Business Rules:
- Annual subscriptions (12+ months) receive 20% discount
- Multi-month subscriptions (3+ months) receive 10% discount  
- Student discounts are 50% off and stack with other discounts
- Coupon discounts are 15% off and stack with other discounts
- Refunds vary by cancellation reason (technical issues = full refund)

Architecture:
- Designed as stateless calculator for easy testing and reuse
- Discounts are applied in specific order (annual → multi-month → student → coupon)
- All prices rounded to 2 decimal places for currency consistency
"""

from typing import Literal, Optional


PlanType = Literal["basic", "premium", "enterprise"]
CancellationReason = Literal["technical", "billing", "other"]


class SubscriptionCalculator:
    """
    Calculate subscription prices with multiple discount types.
    
    This calculator applies discounts in a specific order to ensure consistent
    pricing across the billing system. Designed to be stateless for thread-safety
    and easy testing.
    
    Attributes:
        base_price: Base monthly price for basic plan (default: $10.00)
        discount_threshold: Minimum months for multi-month discount (default: 3)
        annual_multiplier: Discount multiplier for annual subscriptions (default: 0.8 = 20% off)
    
    Example:
        >>> calc = SubscriptionCalculator()
        >>> calc.calculate_price("premium", 12, is_student=True)
        48.0  # Premium ($20) * 12 months * 0.8 annual * 0.5 student
    """
    
    def __init__(
        self,
        base_price: float = 10.0,
        discount_threshold: int = 3,
        annual_multiplier: float = 0.8
    ) -> None:
        """
        Initialize calculator with pricing configuration.
        
        Args:
            base_price: Base monthly price for basic plan
            discount_threshold: Minimum months to qualify for multi-month discount
            annual_multiplier: Discount multiplier for 12+ month subscriptions
                (0.8 = 20% discount, 1.0 = no discount)
        """
        self.base_price = base_price
        self.discount_threshold = discount_threshold
        self.annual_multiplier = annual_multiplier
    
    def calculate_price(
        self,
        plan_type: PlanType,
        months: int,
        is_student: bool = False,
        has_coupon: bool = False
    ) -> float:
        """
        Calculate subscription price with applicable discounts.
        
        Applies discounts in this order:
        1. Plan type multiplier (basic/premium/enterprise)
        2. Annual discount (20% off for 12+ months) - applied before monthly multiplication
        3. Multi-month discount (10% off for 3+ months) - only for non-annual subscriptions (< 12 months)
        4. Student discount (50% off) - stacks with all other discounts
        5. Coupon discount (15% off) - stacks with all other discounts
        
        Note: Annual subscriptions (12+ months) get the annual discount but NOT the multi-month discount.
        
        Args:
            plan_type: Subscription tier - must be "basic", "premium", or "enterprise"
            months: Subscription duration in months (must be 1-24)
            is_student: Whether user qualifies for student discount (50% off)
            has_coupon: Whether user has valid promotional coupon (15% off)
        
        Returns:
            Final price rounded to 2 decimal places (in dollars)
        
        Raises:
            ValueError: If plan_type is invalid or months is outside valid range
        
        Example:
            >>> calc = SubscriptionCalculator()
            >>> # Basic plan, 1 month
            >>> calc.calculate_price("basic", 1)
            10.0
            
            >>> # Premium plan, 12 months with student discount
            >>> calc.calculate_price("premium", 12, is_student=True)
            48.0  # $20 base * 12 months * 0.8 annual * 0.5 student
            
            >>> # Enterprise with coupon
            >>> calc.calculate_price("enterprise", 6, has_coupon=True)
            137.7  # $30 base * 6 months * 0.9 multi-month * 0.85 coupon
        """
        # Validate plan type
        valid_plans: tuple[PlanType, ...] = ("basic", "premium", "enterprise")
        if plan_type not in valid_plans:
            raise ValueError(
                f"Invalid plan_type: {plan_type}. Must be one of {valid_plans}"
            )
        
        # Validate months range
        if not (1 <= months <= 24):
            raise ValueError(
                f"Invalid months: {months}. Must be between 1 and 24"
            )
        
        # Step 1: Apply plan type multiplier
        # Basic = 1x, Premium = 2x, Enterprise = 3x base price
        if plan_type == "basic":
            price = self.base_price
        elif plan_type == "premium":
            price = self.base_price * 2
        else:  # enterprise
            price = self.base_price * 3
        
        # Step 2: Apply annual discount (20% off for 12+ months)
        # This discount is applied BEFORE multiplying by months
        # Per marketing strategy: incentivize longer commitments
        # Note: Annual subscriptions (12+ months) don't also get multi-month discount
        if months >= 12:
            price = price * self.annual_multiplier * months
        else:
            price = price * months
            
            # Step 3: Apply multi-month discount (10% off for 3+ months, but not for annual)
            # Applied after monthly multiplication for consistency
            # Business rule: reward customer loyalty with multi-month commitments
            # Only applies to non-annual subscriptions (less than 12 months)
            if months >= self.discount_threshold:
                price = price * 0.9
        
        # Step 4: Apply student discount (50% off)
        # Stackable with all other discounts per company policy
        # Policy: Make subscriptions accessible to students
        if is_student:
            price = price * 0.5
        
        # Step 5: Apply coupon discount (15% off)
        # Stackable with all other discounts
        # Used for promotional campaigns and retention
        if has_coupon:
            price = price * 0.85
        
        # Round to 2 decimal places for currency consistency
        return round(price, 2)
    
    def calculate_refund(
        self,
        remaining_days: int,
        original_price: float,
        cancellation_reason: CancellationReason
    ) -> float:
        """
        Calculate refund amount based on cancellation reason and remaining time.
        
        Refund policies:
        - Technical issues: Full refund regardless of remaining days
          (We take responsibility for technical problems)
        - Billing issues: 50% refund regardless of remaining days
          (Partial refund for billing problems)
        - Other reasons: Pro-rated refund based on remaining days
          (Fair refund based on unused service)
        
        Args:
            remaining_days: Number of days left in subscription period (must be >= 0)
            original_price: Original subscription price paid (must be > 0)
            cancellation_reason: Reason for cancellation - "technical", "billing", or "other"
        
        Returns:
            Refund amount rounded to 2 decimal places (in dollars)
        
        Raises:
            ValueError: If remaining_days < 0 or original_price <= 0
        
        Example:
            >>> calc = SubscriptionCalculator()
            >>> # Technical issue - full refund
            >>> calc.calculate_refund(15, 30.0, "technical")
            30.0
            
            >>> # Billing issue - 50% refund
            >>> calc.calculate_refund(20, 30.0, "billing")
            15.0
            
            >>> # Other reason - pro-rated
            >>> calc.calculate_refund(15, 30.0, "other")
            15.0  # 15 days / 30 days * $30
        """
        # Validate inputs
        if remaining_days < 0:
            raise ValueError(f"remaining_days must be >= 0, got {remaining_days}")
        if original_price <= 0:
            raise ValueError(f"original_price must be > 0, got {original_price}")
        
        # Technical issues: Full refund
        # Policy: We take responsibility for technical problems affecting service
        if cancellation_reason == "technical":
            refund = original_price
        
        # Billing issues: 50% refund
        # Policy: Partial refund for billing problems (acknowledges issue but covers costs)
        elif cancellation_reason == "billing":
            refund = original_price * 0.5
        
        # Other reasons: Pro-rated refund
        # Policy: Fair refund based on unused service (assumes 30-day billing period)
        else:
            # Calculate pro-rated refund based on remaining days
            # Assumes standard 30-day billing period
            refund = original_price * (remaining_days / 30)
        
        return round(refund, 2)


# Usage Examples
if __name__ == "__main__":
    calc = SubscriptionCalculator()
    
    print("=== Subscription Pricing Examples ===\n")
    
    # Basic subscription
    price = calc.calculate_price("basic", 1)
    print(f"Basic 1 month: ${price}")
    
    # Premium annual
    price = calc.calculate_price("premium", 12)
    print(f"Premium 12 months: ${price}")
    
    # Student discount
    price = calc.calculate_price("basic", 6, is_student=True)
    print(f"Basic 6 months (student): ${price}")
    
    # Enterprise with all discounts
    price = calc.calculate_price("enterprise", 12, is_student=True, has_coupon=True)
    print(f"Enterprise 12 months (student + coupon): ${price}")
    
    print("\n=== Refund Calculation Examples ===\n")
    
    # Technical issue - full refund
    refund = calc.calculate_refund(15, 30.0, "technical")
    print(f"Refund (technical, 15 days left): ${refund}")
    
    # Billing issue - 50% refund
    refund = calc.calculate_refund(20, 30.0, "billing")
    print(f"Refund (billing, 20 days left): ${refund}")
    
    # Other reason - pro-rated
    refund = calc.calculate_refund(15, 30.0, "other")
    print(f"Refund (other, 15 days left): ${refund}")

