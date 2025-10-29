"""
A data processing pipeline without logging.
This example demonstrates how lack of logging makes root cause identification difficult.
"""

import time
import random


class DataProcessor:
    """Processes data through multiple stages."""
    
    def __init__(self):
        self.data = []
    
    def fetch_data(self, source):
        """Fetch data from source."""
        # Simulate API call
        time.sleep(0.1)
        data = [random.randint(1, 100) for _ in range(10)]
        return data
    
    def validate_data(self, data):
        """Validate data meets requirements."""
        if not data:
            return False
        if len(data) < 5:
            return False
        return True
    
    def transform_data(self, data):
        """Transform data to target format."""
        transformed = []
        for item in data:
            if item > 50:
                transformed.append(item * 2)
            else:
                transformed.append(item)
        return transformed
    
    def save_data(self, data, destination):
        """Save data to destination."""
        # Simulate save operation
        time.sleep(0.1)
        return len(data)
    
    def process(self, source, destination):
        """Process data from source to destination."""
        # Fetch data
        data = self.fetch_data(source)
        
        # Validate
        if not self.validate_data(data):
            return False
        
        # Transform
        transformed = self.transform_data(data)
        
        # Save
        result = self.save_data(transformed, destination)
        
        return result > 0


class OrderProcessor:
    """Processes customer orders."""
    
    def __init__(self):
        self.inventory = {"item1": 10, "item2": 5, "item3": 0}
        self.orders = []
    
    def check_inventory(self, item_id, quantity):
        """Check if item is available in inventory."""
        if item_id not in self.inventory:
            return False
        return self.inventory[item_id] >= quantity
    
    def process_order(self, order_id, items):
        """Process a customer order."""
        # Check each item
        for item_id, quantity in items.items():
            if not self.check_inventory(item_id, quantity):
                return False
        
        # Reserve inventory
        for item_id, quantity in items.items():
            self.inventory[item_id] -= quantity
        
        # Record order
        self.orders.append({
            "order_id": order_id,
            "items": items,
            "status": "processed"
        })
        
        return True


# Example usage demonstrating lack of visibility
if __name__ == "__main__":
    processor = DataProcessor()
    
    # Process data - but we can't see what's happening inside
    result = processor.process("api_source", "database")
    print(f"Process result: {result}")
    print("What happened? Hard to tell without logging!\n")
    
    # Process order - same issue
    order_processor = OrderProcessor()
    result = order_processor.process_order("order123", {"item1": 3, "item2": 2})
    print(f"Order processed: {result}")
    print("Why did it fail? Can't tell without logging!\n")
    
    # Try to process order that will fail
    result = order_processor.process_order("order124", {"item3": 1})
    print(f"Order processed: {result}")
    print("Which item was out of stock? No way to know!")

