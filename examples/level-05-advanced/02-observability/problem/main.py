"""
System without observability.

This demonstrates a system that works but provides no visibility into
its behavior, making debugging and AI assistance difficult.
"""

import time
import random

def process_order(order_id, amount):
    """Process an order - no logging or observability."""
    # Simulate processing
    time.sleep(random.uniform(0.1, 0.5))
    
    if amount < 0:
        return {'status': 'error', 'message': 'Invalid amount'}
    
    if random.random() < 0.1:  # 10% failure rate
        return {'status': 'error', 'message': 'Processing failed'}
    
    return {'status': 'success', 'order_id': order_id}

def handle_request(request_data):
    """Handle incoming request - no observability."""
    order_id = request_data.get('order_id')
    amount = request_data.get('amount', 0)
    
    result = process_order(order_id, amount)
    return result

if __name__ == '__main__':
    # Simulate requests
    requests = [
        {'order_id': 1, 'amount': 100},
        {'order_id': 2, 'amount': -50},
        {'order_id': 3, 'amount': 200},
    ]
    
    for req in requests:
        result = handle_request(req)
        print(result)

