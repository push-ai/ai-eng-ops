"""
Well-structured service integration example.

Demonstrates proper error handling, retry logic, circuit breakers,
timeouts, logging, and validation for AI-friendly service integration.
"""

import requests
import time
import logging
from typing import Optional, Dict, Any, Callable
from enum import Enum
from dataclasses import dataclass
from pydantic import BaseModel, ValidationError, EmailStr

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# Models and Types
# ============================================================================

class User(BaseModel):
    """User data model from external service."""
    id: int
    name: str
    email: EmailStr
    age: int


class NotificationRequest(BaseModel):
    """Notification request model."""
    user_id: int
    message: str


class PaymentStatus(BaseModel):
    """Payment status model."""
    payment_id: str
    status: str
    amount: float


class CircuitBreakerState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"  # Normal operation
    OPEN = "open"      # Failures exceeded threshold
    HALF_OPEN = "half_open"  # Testing if service recovered


@dataclass
class RetryConfig:
    """Retry configuration."""
    max_attempts: int = 3
    initial_delay: float = 1.0
    max_delay: float = 10.0
    exponential_base: float = 2.0


@dataclass
class CircuitBreakerConfig:
    """Circuit breaker configuration."""
    failure_threshold: int = 5
    success_threshold: int = 2
    timeout_seconds: float = 60.0


# ============================================================================
# Custom Exceptions
# ============================================================================

class ServiceError(Exception):
    """Base exception for service errors."""
    pass


class ServiceTimeoutError(ServiceError):
    """Service request timed out."""
    pass


class ServiceConnectionError(ServiceError):
    """Service connection failed."""
    pass


class ServiceValidationError(ServiceError):
    """Service response validation failed."""
    pass


class CircuitBreakerOpenError(ServiceError):
    """Circuit breaker is open."""
    pass


# ============================================================================
# Circuit Breaker
# ============================================================================

class CircuitBreaker:
    """
    Circuit breaker implementation.
    
    Prevents cascading failures by stopping calls to failing services.
    Opens after failure_threshold failures, closes after success_threshold successes.
    """
    
    def __init__(self, config: CircuitBreakerConfig):
        self.config = config
        self.state = CircuitBreakerState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: Optional[float] = None
    
    def call(self, func: Callable) -> Any:
        """
        Execute function with circuit breaker protection.
        
        Args:
            func: Function to execute
        
        Returns:
            Function result
        
        Raises:
            CircuitBreakerOpenError: If circuit breaker is open
        """
        # Check if circuit breaker should be reset
        if self.state == CircuitBreakerState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitBreakerState.HALF_OPEN
                self.success_count = 0
            else:
                raise CircuitBreakerOpenError(
                    f"Circuit breaker is OPEN. Last failure: {self.last_failure_time}"
                )
        
        try:
            result = func()
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise
    
    def _should_attempt_reset(self) -> bool:
        """Check if circuit breaker should attempt reset."""
        if self.last_failure_time is None:
            return False
        return time.time() - self.last_failure_time >= self.config.timeout_seconds
    
    def _on_success(self):
        """Handle successful call."""
        if self.state == CircuitBreakerState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.config.success_threshold:
                self.state = CircuitBreakerState.CLOSED
                self.failure_count = 0
                logger.info("Circuit breaker CLOSED - service recovered")
        else:
            self.failure_count = 0
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.config.failure_threshold:
            self.state = CircuitBreakerState.OPEN
            logger.warning(
                f"Circuit breaker OPENED - {self.failure_count} failures exceeded threshold"
            )


# ============================================================================
# Retry Decorator
# ============================================================================

def retry_with_backoff(
    config: RetryConfig,
    retryable_exceptions: tuple = (ServiceError,)
):
    """
    Decorator for retrying function calls with exponential backoff.
    
    Args:
        config: Retry configuration
        retryable_exceptions: Exceptions that should trigger retry
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            delay = config.initial_delay
            
            for attempt in range(config.max_attempts):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as e:
                    if attempt == config.max_attempts - 1:
                        logger.error(
                            f"Max retries ({config.max_attempts}) exceeded for {func.__name__}"
                        )
                        raise
                    
                    logger.warning(
                        f"Attempt {attempt + 1}/{config.max_attempts} failed for {func.__name__}: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)
                    delay = min(delay * config.exponential_base, config.max_delay)
            
            raise ServiceError(f"Failed after {config.max_attempts} attempts")
        
        return wrapper
    return decorator


# ============================================================================
# Service Clients
# ============================================================================

class UserServiceClient:
    """
    Client for User Service API.
    
    Handles all interactions with the user service including error handling,
    retries, circuit breaking, and validation.
    """
    
    def __init__(
        self,
        base_url: str = "https://api.example.com",
        timeout: tuple = (5, 30),
        retry_config: Optional[RetryConfig] = None,
        circuit_breaker_config: Optional[CircuitBreakerConfig] = None
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.retry_config = retry_config or RetryConfig()
        self.circuit_breaker = CircuitBreaker(
            circuit_breaker_config or CircuitBreakerConfig()
        )
    
    @retry_with_backoff(
        config=RetryConfig(),
        retryable_exceptions=(ServiceTimeoutError, ServiceConnectionError)
    )
    def get_user(self, user_id: int) -> User:
        """
        Get user by ID.
        
        Args:
            user_id: User ID to retrieve
        
        Returns:
            User object
        
        Raises:
            ServiceError: If request fails
            ServiceValidationError: If response validation fails
            CircuitBreakerOpenError: If circuit breaker is open
        """
        logger.info("Getting user", extra={"user_id": user_id, "service": "user_service"})
        
        def _make_request():
            try:
                response = requests.get(
                    f"{self.base_url}/users/{user_id}",
                    timeout=self.timeout
                )
                response.raise_for_status()
                
                # Validate response
                try:
                    user_data = response.json()
                    return User(**user_data)
                except ValidationError as e:
                    raise ServiceValidationError(f"Invalid user data: {e}")
            
            except requests.Timeout:
                raise ServiceTimeoutError(f"Request to user service timed out after {self.timeout[1]}s")
            except requests.ConnectionError as e:
                raise ServiceConnectionError(f"Failed to connect to user service: {e}")
            except requests.HTTPError as e:
                if e.response.status_code == 404:
                    raise ServiceError(f"User {user_id} not found")
                raise ServiceError(f"HTTP error: {e}")
        
        return self.circuit_breaker.call(_make_request)


class NotificationServiceClient:
    """
    Client for Notification Service API.
    
    Handles sending notifications with proper error handling and retries.
    """
    
    def __init__(
        self,
        base_url: str = "https://api.example.com",
        timeout: tuple = (5, 30),
        retry_config: Optional[RetryConfig] = None
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.retry_config = retry_config or RetryConfig()
    
    @retry_with_backoff(
        config=RetryConfig(),
        retryable_exceptions=(ServiceTimeoutError, ServiceConnectionError)
    )
    def send_notification(self, user_id: int, message: str) -> Dict[str, Any]:
        """
        Send notification to user.
        
        Args:
            user_id: User ID to notify
            message: Notification message
        
        Returns:
            Response data
        
        Raises:
            ServiceError: If request fails
        """
        logger.info(
            "Sending notification",
            extra={"user_id": user_id, "service": "notification_service"}
        )
        
        # Validate request
        try:
            request_data = NotificationRequest(user_id=user_id, message=message)
        except ValidationError as e:
            raise ServiceValidationError(f"Invalid notification request: {e}")
        
        try:
            response = requests.post(
                f"{self.base_url}/notifications",
                json=request_data.dict(),
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        except requests.Timeout:
            raise ServiceTimeoutError(f"Request to notification service timed out")
        except requests.ConnectionError as e:
            raise ServiceConnectionError(f"Failed to connect to notification service: {e}")
        except requests.HTTPError as e:
            raise ServiceError(f"HTTP error: {e}")


class PaymentServiceClient:
    """
    Client for Payment Service API.
    
    Handles payment status checks with proper error handling.
    """
    
    def __init__(
        self,
        base_url: str = "https://payments.example.com",
        timeout: tuple = (5, 30),
        retry_config: Optional[RetryConfig] = None,
        circuit_breaker_config: Optional[CircuitBreakerConfig] = None
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.retry_config = retry_config or RetryConfig()
        self.circuit_breaker = CircuitBreaker(
            circuit_breaker_config or CircuitBreakerConfig()
        )
    
    @retry_with_backoff(
        config=RetryConfig(),
        retryable_exceptions=(ServiceTimeoutError, ServiceConnectionError)
    )
    def get_payment_status(self, payment_id: str) -> PaymentStatus:
        """
        Get payment status.
        
        Args:
            payment_id: Payment ID to check
        
        Returns:
            PaymentStatus object
        
        Raises:
            ServiceError: If request fails
            ServiceValidationError: If response validation fails
        """
        logger.info(
            "Getting payment status",
            extra={"payment_id": payment_id, "service": "payment_service"}
        )
        
        def _make_request():
            try:
                response = requests.get(
                    f"{self.base_url}/status/{payment_id}",
                    timeout=self.timeout
                )
                response.raise_for_status()
                
                # Validate response
                try:
                    status_data = response.json()
                    return PaymentStatus(**status_data)
                except ValidationError as e:
                    raise ServiceValidationError(f"Invalid payment status data: {e}")
            
            except requests.Timeout:
                raise ServiceTimeoutError(f"Request to payment service timed out")
            except requests.ConnectionError as e:
                raise ServiceConnectionError(f"Failed to connect to payment service: {e}")
            except requests.HTTPError as e:
                if e.response.status_code == 404:
                    raise ServiceError(f"Payment {payment_id} not found")
                raise ServiceError(f"HTTP error: {e}")
        
        return self.circuit_breaker.call(_make_request)


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    # Initialize clients
    user_client = UserServiceClient()
    notification_client = NotificationServiceClient()
    payment_client = PaymentServiceClient()
    
    try:
        # Get user
        user = user_client.get_user(123)
        print(f"User: {user.name} ({user.email})")
        
        # Send notification
        notification_client.send_notification(123, 'Hello!')
        print("Notification sent")
        
        # Get payment status
        status = payment_client.get_payment_status('pay_123')
        print(f"Payment status: {status.status}")
    
    except ServiceError as e:
        logger.error(f"Service error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

