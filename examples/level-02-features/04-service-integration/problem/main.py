"""
Basic service integration without proper structure.
This demonstrates common issues with AI-generated integration code.
"""

import requests

def get_user_data(user_id):
    """Get user data from external API."""
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

def send_notification(user_id, message):
    """Send notification to user."""
    response = requests.post(
        'https://api.example.com/notifications',
        json={'user_id': user_id, 'message': message}
    )
    return response.json()

def get_payment_status(payment_id):
    """Get payment status from payment service."""
    response = requests.get(f'https://payments.example.com/status/{payment_id}')
    return response.json()

if __name__ == '__main__':
    # Example usage
    user_data = get_user_data(123)
    print(user_data)
    
    send_notification(123, 'Hello!')
    
    status = get_payment_status('pay_123')
    print(status)

