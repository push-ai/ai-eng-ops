"""
System with comprehensive observability.

Demonstrates structured logging, metrics, distributed tracing, and error tracking
for complete system visibility.
"""

import time
import random
import logging
import uuid
from typing import Dict, Any, Optional
from contextvars import ContextVar
from dataclasses import dataclass
from datetime import datetime

# ============================================================================
# Observability Setup
# ============================================================================

# Structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(trace_id)s - %(span_id)s'
)
logger = logging.getLogger(__name__)

# Trace context
trace_id: ContextVar[Optional[str]] = ContextVar('trace_id', default=None)
span_id: ContextVar[Optional[str]] = ContextVar('span_id', default=None)


# ============================================================================
# Metrics
# ============================================================================

class Metrics:
    """Simple metrics collector (in production, use Prometheus, StatsD, etc.)."""
    
    def __init__(self):
        self.counters: Dict[str, int] = {}
        self.timers: Dict[str, list] = {}
    
    def counter(self, name: str) -> 'Counter':
        """Get or create a counter."""
        if name not in self.counters:
            self.counters[name] = 0
        return Counter(self, name)
    
    def timer(self, name: str) -> 'Timer':
        """Get or create a timer."""
        if name not in self.timers:
            self.timers[name] = []
        return Timer(self, name)
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get all metrics."""
        return {
            'counters': self.counters.copy(),
            'timers': {
                name: {
                    'count': len(times),
                    'sum': sum(times),
                    'avg': sum(times) / len(times) if times else 0,
                    'min': min(times) if times else 0,
                    'max': max(times) if times else 0
                }
                for name, times in self.timers.items()
            }
        }


class Counter:
    """Counter metric."""
    
    def __init__(self, metrics: Metrics, name: str):
        self.metrics = metrics
        self.name = name
    
    def inc(self, value: int = 1):
        """Increment counter."""
        self.metrics.counters[self.name] += value


class Timer:
    """Timer metric."""
    
    def __init__(self, metrics: Metrics, name: str):
        self.metrics = metrics
        self.name = name
    
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        duration = time.time() - self.start
        self.metrics.timers[self.name].append(duration)


# Global metrics instance
metrics = Metrics()


# ============================================================================
# Distributed Tracing
# ============================================================================

@dataclass
class Span:
    """Trace span."""
    trace_id: str
    span_id: str
    parent_span_id: Optional[str]
    operation: str
    start_time: float
    end_time: Optional[float] = None
    tags: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = {}


class Tracer:
    """Simple tracer (in production, use OpenTelemetry, Jaeger, etc.)."""
    
    def __init__(self):
        self.spans: list[Span] = []
    
    def start_span(self, operation: str, **tags) -> Span:
        """Start a new span."""
        current_trace_id = trace_id.get() or str(uuid.uuid4())
        current_span_id = span_id.get() or str(uuid.uuid4())
        parent_span_id = span_id.get()
        
        span = Span(
            trace_id=current_trace_id,
            span_id=current_span_id,
            parent_span_id=parent_span_id,
            operation=operation,
            start_time=time.time(),
            tags=tags
        )
        
        self.spans.append(span)
        trace_id.set(current_trace_id)
        span_id.set(current_span_id)
        
        return span
    
    def get_traces(self) -> list[Span]:
        """Get all spans."""
        return self.spans.copy()


# Global tracer instance
tracer = Tracer()


# ============================================================================
# Business Logic with Observability
# ============================================================================

def process_order(order_id: int, amount: float) -> Dict[str, Any]:
    """
    Process an order with full observability.
    
    Args:
        order_id: Order ID
        amount: Order amount
    
    Returns:
        Processing result
    """
    # Start span
    span = tracer.start_span(
        "process_order",
        order_id=order_id,
        amount=amount
    )
    
    try:
        # Log operation start
        logger.info(
            "Processing order",
            extra={
                "operation": "process_order",
                "order_id": order_id,
                "amount": amount,
                "trace_id": span.trace_id,
                "span_id": span.span_id
            }
        )
        
        # Increment counter
        metrics.counter("order.processing.total").inc()
        
        # Time the operation
        with metrics.timer("order.processing.duration"):
            # Simulate processing
            time.sleep(random.uniform(0.1, 0.5))
            
            # Validate
            if amount < 0:
                metrics.counter("order.processing.errors").inc()
                logger.error(
                    "Invalid order amount",
                    extra={
                        "order_id": order_id,
                        "amount": amount,
                        "error": "invalid_amount",
                        "trace_id": span.trace_id,
                        "span_id": span.span_id
                    }
                )
                return {'status': 'error', 'message': 'Invalid amount'}
            
            # Simulate random failures
            if random.random() < 0.1:  # 10% failure rate
                metrics.counter("order.processing.errors").inc()
                logger.error(
                    "Order processing failed",
                    extra={
                        "order_id": order_id,
                        "amount": amount,
                        "error": "processing_failed",
                        "trace_id": span.trace_id,
                        "span_id": span.span_id
                    }
                )
                return {'status': 'error', 'message': 'Processing failed'}
            
            # Success
            metrics.counter("order.processing.success").inc()
            logger.info(
                "Order processed successfully",
                extra={
                    "order_id": order_id,
                    "amount": amount,
                    "trace_id": span.trace_id,
                    "span_id": span.span_id
                }
            )
            
            return {'status': 'success', 'order_id': order_id}
    
    except Exception as e:
        metrics.counter("order.processing.exceptions").inc()
        logger.exception(
            "Exception processing order",
            extra={
                "order_id": order_id,
                "amount": amount,
                "error": str(e),
                "trace_id": span.trace_id,
                "span_id": span.span_id
            }
        )
        raise
    
    finally:
        # End span
        span.end_time = time.time()
        span.tags['duration'] = span.end_time - span.start_time


def handle_request(request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle incoming request with observability.
    
    Args:
        request_data: Request data
    
    Returns:
        Response data
    """
    # Start root span
    span = tracer.start_span(
        "handle_request",
        **request_data
    )
    
    try:
        order_id = request_data.get('order_id')
        amount = request_data.get('amount', 0)
        
        logger.info(
            "Handling request",
            extra={
                "operation": "handle_request",
                "order_id": order_id,
                "amount": amount,
                "trace_id": span.trace_id,
                "span_id": span.span_id
            }
        )
        
        metrics.counter("requests.total").inc()
        
        result = process_order(order_id, amount)
        
        metrics.counter("requests.success").inc()
        
        logger.info(
            "Request handled",
            extra={
                "order_id": order_id,
                "result": result,
                "trace_id": span.trace_id,
                "span_id": span.span_id
            }
        )
        
        return result
    
    except Exception as e:
        metrics.counter("requests.errors").inc()
        logger.exception(
            "Error handling request",
            extra={
                "request_data": request_data,
                "error": str(e),
                "trace_id": span.trace_id,
                "span_id": span.span_id
            }
        )
        raise
    
    finally:
        span.end_time = time.time()
        span.tags['duration'] = span.end_time - span.start_time


# ============================================================================
# Usage
# ============================================================================

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
    
    # Print observability data
    print("\n=== Metrics ===")
    print(metrics.get_metrics())
    
    print("\n=== Traces ===")
    for span in tracer.get_traces():
        print(f"{span.operation}: {span.duration if span.end_time else 'active'}s")

