# Logging Standards

## Overview

This document defines logging standards for all services, ensuring consistent, structured logs that enable effective debugging and monitoring.

## Log Format

### Structured Logging

- **Format**: JSON for machine parsing
- **Fields**: Consistent field names across services
- **Levels**: DEBUG, INFO, WARN, ERROR, CRITICAL
- **Timestamp**: ISO 8601 format (UTC)

### Log Structure

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "service": "user-service",
  "trace_id": "abc123",
  "span_id": "def456",
  "message": "User created successfully",
  "user_id": 123,
  "duration_ms": 45
}
```

## Log Levels

### DEBUG

- **Purpose**: Detailed debugging information
- **Usage**: Development, troubleshooting
- **Production**: Usually disabled
- **Example**: Function entry/exit, variable values

### INFO

- **Purpose**: Informational messages
- **Usage**: Normal operation events
- **Production**: Enabled
- **Example**: Request processed, user created, cache hit

### WARN

- **Purpose**: Warning conditions
- **Usage**: Recoverable errors, deprecations
- **Production**: Enabled
- **Example**: Retry required, deprecated API used

### ERROR

- **Purpose**: Error conditions
- **Usage**: Errors that are handled
- **Production**: Enabled
- **Example**: Validation error, API call failed

### CRITICAL

- **Purpose**: Critical errors
- **Usage**: System failures, data loss
- **Production**: Enabled, alerts triggered
- **Example**: Database unavailable, payment processing failed

## Required Fields

### Common Fields

- **timestamp**: ISO 8601 timestamp (UTC)
- **level**: Log level (DEBUG, INFO, WARN, ERROR, CRITICAL)
- **service**: Service name
- **message**: Human-readable message

### Context Fields

- **trace_id**: Distributed trace ID
- **span_id**: Current span ID
- **user_id**: User ID (if applicable)
- **request_id**: Request ID (if applicable)

### Error Fields

- **error**: Error type/code
- **error_message**: Error message
- **stack_trace**: Stack trace (for exceptions)
- **error_context**: Additional error context

## Logging Patterns

### Request Logging

```python
logger.info(
    "Request received",
    extra={
        "method": request.method,
        "path": request.path,
        "user_id": request.user.id,
        "trace_id": trace_id,
        "request_id": request_id
    }
)
```

### Error Logging

```python
try:
    process_order(order_id)
except OrderError as e:
    logger.error(
        "Order processing failed",
        extra={
            "order_id": order_id,
            "error": type(e).__name__,
            "error_message": str(e),
            "trace_id": trace_id,
            "stack_trace": traceback.format_exc()
        },
        exc_info=True
    )
```

### Performance Logging

```python
start_time = time.time()
result = process_payment(payment_id)
duration_ms = (time.time() - start_time) * 1000

logger.info(
    "Payment processed",
    extra={
        "payment_id": payment_id,
        "duration_ms": duration_ms,
        "success": result.success,
        "trace_id": trace_id
    }
)
```

## Log Aggregation

### Centralized Logging

- **Tool**: ELK Stack (Elasticsearch, Logstash, Kibana) or CloudWatch Logs
- **Collection**: All services send logs to central system
- **Retention**: 30 days for application logs, 90 days for audit logs
- **Indexing**: Indexed by service, level, timestamp

### Log Routing

- **By level**: Route ERROR/CRITICAL to alerting system
- **By service**: Separate indexes per service
- **By environment**: Separate indexes per environment

## Sensitive Data

### Never Log

- **Passwords**: Never log passwords
- **API keys**: Never log API keys
- **Tokens**: Never log authentication tokens
- **PII**: Don't log full credit card numbers, SSNs
- **Secrets**: Never log secrets or credentials

### Safe Alternatives

- **Hash values**: Log hashes instead of passwords
- **Partial data**: Log last 4 digits only
- **IDs**: Log IDs instead of full data
- **Redaction**: Redact sensitive fields

## Performance Considerations

### Log Volume

- **Limit verbosity**: Don't log excessively
- **Sample logs**: Sample high-volume logs
- **Async logging**: Use async logging for high throughput
- **Rate limiting**: Rate limit log output

### Cost Optimization

- **Retention policies**: Archive old logs
- **Filtering**: Filter unnecessary logs
- **Compression**: Compress log storage
- **Sampling**: Sample non-critical logs

## References

- Alert Definitions: `contexts/monitoring/alert-definitions.md`
- Observability: `contexts/monitoring/observability-requirements.md`

