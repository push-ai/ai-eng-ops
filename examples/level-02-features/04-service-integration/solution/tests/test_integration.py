"""
Comprehensive tests for service integration clients.

These tests verify that service clients correctly handle:
- Successful requests
- Error handling
- Retry logic
- Circuit breaker
- Timeout handling
- Request/response validation
"""

import pytest
import responses
import requests
from unittest.mock import patch, MagicMock
from main import (
    UserServiceClient,
    NotificationServiceClient,
    PaymentServiceClient,
    ServiceError,
    ServiceTimeoutError,
    ServiceConnectionError,
    ServiceValidationError,
    CircuitBreakerOpenError,
    User,
    PaymentStatus,
    RetryConfig,
    CircuitBreakerConfig
)


class TestUserServiceClient:
    """Test UserServiceClient."""
    
    @responses.activate
    def test_get_user_success(self):
        """Test successful user retrieval."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            json={'id': 123, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
            status=200
        )
        
        client = UserServiceClient()
        user = client.get_user(123)
        
        assert isinstance(user, User)
        assert user.id == 123
        assert user.name == 'Alice'
        assert user.email == 'alice@example.com'
        assert user.age == 25
    
    @responses.activate
    def test_get_user_not_found(self):
        """Test error when user not found."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/999',
            status=404
        )
        
        client = UserServiceClient()
        with pytest.raises(ServiceError, match="not found"):
            client.get_user(999)
    
    @responses.activate
    def test_get_user_timeout(self):
        """Test timeout handling."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            body=requests.Timeout("Request timed out")
        )
        
        client = UserServiceClient(timeout=(1, 1))
        with pytest.raises(ServiceTimeoutError):
            client.get_user(123)
    
    @responses.activate
    def test_get_user_invalid_response(self):
        """Test validation error on invalid response."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            json={'id': 'invalid', 'name': 'Alice'},  # Missing required fields
            status=200
        )
        
        client = UserServiceClient()
        with pytest.raises(ServiceValidationError):
            client.get_user(123)
    
    @responses.activate
    def test_get_user_retry_on_timeout(self):
        """Test retry on timeout."""
        # First two calls timeout, third succeeds
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            body=requests.Timeout("Timeout 1")
        )
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            body=requests.Timeout("Timeout 2")
        )
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            json={'id': 123, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
            status=200
        )
        
        client = UserServiceClient(retry_config=RetryConfig(max_attempts=3, initial_delay=0.1))
        user = client.get_user(123)
        
        assert user.id == 123
        assert len(responses.calls) == 3  # Two retries + one success
    
    @responses.activate
    def test_circuit_breaker_opens_after_threshold(self):
        """Test circuit breaker opens after failure threshold."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            status=500  # Server error
        )
        
        config = CircuitBreakerConfig(failure_threshold=3)
        client = UserServiceClient(circuit_breaker_config=config)
        
        # Fail multiple times to open circuit breaker
        for _ in range(3):
            with pytest.raises(ServiceError):
                client.get_user(123)
        
        # Next call should raise CircuitBreakerOpenError
        with pytest.raises(CircuitBreakerOpenError):
            client.get_user(123)


class TestNotificationServiceClient:
    """Test NotificationServiceClient."""
    
    @responses.activate
    def test_send_notification_success(self):
        """Test successful notification sending."""
        responses.add(
            responses.POST,
            'https://api.example.com/notifications',
            json={'status': 'sent', 'notification_id': 'notif_123'},
            status=200
        )
        
        client = NotificationServiceClient()
        result = client.send_notification(123, 'Hello!')
        
        assert result['status'] == 'sent'
    
    @responses.activate
    def test_send_notification_invalid_request(self):
        """Test validation error on invalid request."""
        client = NotificationServiceClient()
        
        # Invalid user_id (should be int)
        with pytest.raises(ServiceValidationError):
            client.send_notification("invalid", "message")
        
        # Invalid message (should be non-empty)
        with pytest.raises(ServiceValidationError):
            client.send_notification(123, "")  # Empty message


class TestPaymentServiceClient:
    """Test PaymentServiceClient."""
    
    @responses.activate
    def test_get_payment_status_success(self):
        """Test successful payment status retrieval."""
        responses.add(
            responses.GET,
            'https://payments.example.com/status/pay_123',
            json={'payment_id': 'pay_123', 'status': 'completed', 'amount': 100.0},
            status=200
        )
        
        client = PaymentServiceClient()
        status = client.get_payment_status('pay_123')
        
        assert isinstance(status, PaymentStatus)
        assert status.payment_id == 'pay_123'
        assert status.status == 'completed'
        assert status.amount == 100.0
    
    @responses.activate
    def test_get_payment_status_not_found(self):
        """Test error when payment not found."""
        responses.add(
            responses.GET,
            'https://payments.example.com/status/invalid',
            status=404
        )
        
        client = PaymentServiceClient()
        with pytest.raises(ServiceError, match="not found"):
            client.get_payment_status('invalid')


class TestErrorHandling:
    """Test error handling across all clients."""
    
    @responses.activate
    def test_connection_error_handling(self):
        """Test connection error handling."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            body=requests.ConnectionError("Connection failed")
        )
        
        client = UserServiceClient()
        with pytest.raises(ServiceConnectionError):
            client.get_user(123)
    
    @responses.activate
    def test_http_error_handling(self):
        """Test HTTP error handling."""
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            status=500
        )
        
        client = UserServiceClient()
        with pytest.raises(ServiceError):
            client.get_user(123)


class TestCircuitBreaker:
    """Test circuit breaker functionality."""
    
    @responses.activate
    def test_circuit_breaker_resets_on_success(self):
        """Test circuit breaker resets after successful calls."""
        # First: failures to open circuit breaker
        for _ in range(5):
            responses.add(
                responses.GET,
                'https://api.example.com/users/123',
                status=500
            )
        
        # Then: success to reset
        responses.add(
            responses.GET,
            'https://api.example.com/users/123',
            json={'id': 123, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
            status=200
        )
        
        config = CircuitBreakerConfig(failure_threshold=5, success_threshold=1)
        client = UserServiceClient(circuit_breaker_config=config)
        
        # Fail to open circuit breaker
        for _ in range(5):
            with pytest.raises(ServiceError):
                client.get_user(123)
        
        # Wait for timeout (mock time)
        with patch('time.time', return_value=time.time() + 100):
            # Success should reset circuit breaker
            user = client.get_user(123)
            assert user.id == 123

