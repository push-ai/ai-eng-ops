"""
A data processing pipeline with comprehensive structured logging.
This improved version demonstrates how good logging enables faster root cause identification.
"""

import time
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


class DataProcessor:
    """Processes data through multiple stages."""
    
    def __init__(self):
        self.data = []
        logger.info("DataProcessor initialized", extra={"component": "DataProcessor"})
    
    def fetch_data(self, source):
        """
        Fetch data from source.
        
        Args:
            source: Data source identifier
        
        Returns:
            List of data items
        """
        logger.info("Fetching data", extra={
            "function": "fetch_data",
            "source": source
        })
        
        start_time = time.time()
        
        try:
            # Simulate API call
            time.sleep(0.1)
            data = [random.randint(1, 100) for _ in range(10)]
            
            duration = (time.time() - start_time) * 1000
            logger.info("Data fetched successfully", extra={
                "function": "fetch_data",
                "source": source,
                "item_count": len(data),
                "duration_ms": round(duration, 2),
                "data_preview": str(data[:5])
            })
            
            return data
        
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            logger.error("Failed to fetch data", extra={
                "function": "fetch_data",
                "source": source,
                "error": str(e),
                "duration_ms": round(duration, 2)
            }, exc_info=True)
            raise
    
    def validate_data(self, data):
        """
        Validate data meets requirements.
        
        Args:
            data: Data to validate
        
        Returns:
            True if valid, False otherwise
        """
        logger.debug("Validating data", extra={
            "function": "validate_data",
            "data_size": len(data) if data else 0
        })
        
        if not data:
            logger.warning("Validation failed: data is empty", extra={
                "function": "validate_data",
                "reason": "empty_data"
            })
            return False
        
        if len(data) < 5:
            logger.warning("Validation failed: insufficient data", extra={
                "function": "validate_data",
                "data_size": len(data),
                "minimum_required": 5
            })
            return False
        
        logger.info("Data validation passed", extra={
            "function": "validate_data",
            "data_size": len(data)
        })
        return True
    
    def transform_data(self, data):
        """
        Transform data to target format.
        
        Args:
            data: Data to transform
        
        Returns:
            Transformed data
        """
        logger.info("Transforming data", extra={
            "function": "transform_data",
            "input_size": len(data)
        })
        
        start_time = time.time()
        transformed = []
        items_transformed = 0
        items_doubled = 0
        
        for item in data:
            if item > 50:
                transformed.append(item * 2)
                items_doubled += 1
            else:
                transformed.append(item)
            items_transformed += 1
        
        duration = (time.time() - start_time) * 1000
        logger.info("Data transformation completed", extra={
            "function": "transform_data",
            "input_size": len(data),
            "output_size": len(transformed),
            "items_doubled": items_doubled,
            "duration_ms": round(duration, 2)
        })
        
        return transformed
    
    def save_data(self, data, destination):
        """
        Save data to destination.
        
        Args:
            data: Data to save
            destination: Destination identifier
        
        Returns:
            Number of items saved
        """
        logger.info("Saving data", extra={
            "function": "save_data",
            "destination": destination,
            "item_count": len(data)
        })
        
        start_time = time.time()
        
        try:
            # Simulate save operation
            time.sleep(0.1)
            result = len(data)
            
            duration = (time.time() - start_time) * 1000
            logger.info("Data saved successfully", extra={
                "function": "save_data",
                "destination": destination,
                "items_saved": result,
                "duration_ms": round(duration, 2)
            })
            
            return result
        
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            logger.error("Failed to save data", extra={
                "function": "save_data",
                "destination": destination,
                "item_count": len(data),
                "error": str(e),
                "duration_ms": round(duration, 2)
            }, exc_info=True)
            raise
    
    def process(self, source, destination):
        """
        Process data from source to destination.
        
        Args:
            source: Data source identifier
            destination: Destination identifier
        
        Returns:
            True if successful, False otherwise
        """
        correlation_id = f"process_{int(time.time() * 1000)}"
        logger.info("Starting data processing", extra={
            "function": "process",
            "correlation_id": correlation_id,
            "source": source,
            "destination": destination
        })
        
        process_start = time.time()
        
        try:
            # Fetch data
            data = self.fetch_data(source)
            
            # Validate
            if not self.validate_data(data):
                logger.error("Processing failed: validation failed", extra={
                    "function": "process",
                    "correlation_id": correlation_id,
                    "stage": "validation",
                    "source": source
                })
                return False
            
            # Transform
            transformed = self.transform_data(data)
            
            # Save
            result = self.save_data(transformed, destination)
            
            if result <= 0:
                logger.error("Processing failed: save returned no items", extra={
                    "function": "process",
                    "correlation_id": correlation_id,
                    "stage": "save",
                    "items_saved": result
                })
                return False
            
            duration = (time.time() - process_start) * 1000
            logger.info("Data processing completed successfully", extra={
                "function": "process",
                "correlation_id": correlation_id,
                "source": source,
                "destination": destination,
                "items_processed": result,
                "total_duration_ms": round(duration, 2)
            })
            
            return True
        
        except Exception as e:
            duration = (time.time() - process_start) * 1000
            logger.error("Data processing failed", extra={
                "function": "process",
                "correlation_id": correlation_id,
                "source": source,
                "destination": destination,
                "error": str(e),
                "duration_ms": round(duration, 2)
            }, exc_info=True)
            return False


class OrderProcessor:
    """Processes customer orders."""
    
    def __init__(self):
        self.inventory = {"item1": 10, "item2": 5, "item3": 0}
        self.orders = []
        logger.info("OrderProcessor initialized", extra={
            "component": "OrderProcessor",
            "initial_inventory": self.inventory.copy()
        })
    
    def check_inventory(self, item_id, quantity):
        """
        Check if item is available in inventory.
        
        Args:
            item_id: Item identifier
            quantity: Required quantity
        
        Returns:
            True if available, False otherwise
        """
        logger.debug("Checking inventory", extra={
            "function": "check_inventory",
            "item_id": item_id,
            "required_quantity": quantity
        })
        
        if item_id not in self.inventory:
            logger.warning("Item not found in inventory", extra={
                "function": "check_inventory",
                "item_id": item_id,
                "available_items": list(self.inventory.keys())
            })
            return False
        
        available = self.inventory[item_id]
        has_stock = available >= quantity
        
        if not has_stock:
            logger.warning("Insufficient inventory", extra={
                "function": "check_inventory",
                "item_id": item_id,
                "required": quantity,
                "available": available,
                "shortage": quantity - available
            })
        else:
            logger.debug("Inventory check passed", extra={
                "function": "check_inventory",
                "item_id": item_id,
                "available": available,
                "required": quantity
            })
        
        return has_stock
    
    def process_order(self, order_id, items):
        """
        Process a customer order.
        
        Args:
            order_id: Order identifier
            items: Dictionary of item_id -> quantity
        
        Returns:
            True if processed successfully, False otherwise
        """
        logger.info("Processing order", extra={
            "function": "process_order",
            "order_id": order_id,
            "items": items,
            "item_count": len(items)
        })
        
        order_start = time.time()
        
        # Check each item
        for item_id, quantity in items.items():
            if not self.check_inventory(item_id, quantity):
                logger.error("Order processing failed: insufficient inventory", extra={
                    "function": "process_order",
                    "order_id": order_id,
                    "failed_item": item_id,
                    "required_quantity": quantity,
                    "available_quantity": self.inventory.get(item_id, 0)
                })
                return False
        
        # Reserve inventory
        inventory_changes = {}
        for item_id, quantity in items.items():
            old_quantity = self.inventory[item_id]
            self.inventory[item_id] -= quantity
            inventory_changes[item_id] = {
                "old": old_quantity,
                "new": self.inventory[item_id],
                "reserved": quantity
            }
        
        logger.info("Inventory reserved", extra={
            "function": "process_order",
            "order_id": order_id,
            "inventory_changes": inventory_changes
        })
        
        # Record order
        order_record = {
            "order_id": order_id,
            "items": items,
            "status": "processed"
        }
        self.orders.append(order_record)
        
        duration = (time.time() - order_start) * 1000
        logger.info("Order processed successfully", extra={
            "function": "process_order",
            "order_id": order_id,
            "items_processed": len(items),
            "duration_ms": round(duration, 2)
        })
        
        return True


# Example usage demonstrating comprehensive logging
if __name__ == "__main__":
    processor = DataProcessor()
    
    # Process data - now we can see what's happening
    result = processor.process("api_source", "database")
    print(f"\nProcess result: {result}")
    print("Check the logs above to see detailed execution flow!\n")
    
    # Process order - same visibility
    order_processor = OrderProcessor()
    result = order_processor.process_order("order123", {"item1": 3, "item2": 2})
    print(f"Order processed: {result}")
    print("Check the logs to see inventory checks and state changes!\n")
    
    # Try to process order that will fail
    result = order_processor.process_order("order124", {"item3": 1})
    print(f"Order processed: {result}")
    print("Check the logs to see exactly why it failed (item3 out of stock)!")

