# Logging Principle: Structured Logging Accelerates Root Cause Identification

## The Principle

**Well-structured logging enables faster root cause identification by providing visibility into system behavior, state changes, and execution flow.** Good logging isn't just about recording events—it's about creating a narrative that helps both AI and humans understand what happened, when it happened, and why.

## Why This Matters for AI Engineering

### The Problem Without Logging

When code lacks logging, AI struggles to:
- ✅ Know that something happened
- ❌ Understand what actually happened
- ❌ Identify where problems occurred
- ❌ See system state at failure points
- ❌ Trace execution flow

### How Good Logging Helps AI

Structured logging enables AI to:
1. **Trace Execution**: See step-by-step what happened
2. **Identify Failures**: Know exactly where and why things failed
3. **Understand State**: See data values and system state at each step
4. **Analyze Performance**: Identify bottlenecks and slow operations
5. **Debug Automatically**: Use logs to suggest fixes

### Characteristics of Effective Logging

- **Structured**: Consistent format (JSON, key-value pairs)
- **Hierarchical**: Different levels (DEBUG, INFO, WARNING, ERROR)
- **Contextual**: Include relevant data (user IDs, request IDs, timestamps)
- **Filterable**: Easy to filter by level, component, or context
- **Traceable**: Correlation IDs to trace requests across services

## Copy-Paste Prompt

Use this prompt with your AI coding assistant:

```
Analyze the code in the `problem/` directory and add comprehensive structured logging throughout.

Requirements:
1. Add logging at key points:
   - Entry/exit of major functions
   - State changes
   - Decision points
   - Error conditions
   - Performance-critical operations

2. Use appropriate log levels:
   - DEBUG: Detailed information for debugging
   - INFO: General informational messages about normal operation
   - WARNING: Potentially problematic situations
   - ERROR: Error events that might still allow the app to continue
   - CRITICAL: Serious errors that might cause the app to abort

3. Include contextual information:
   - Function names
   - Input parameters (sanitized if sensitive)
   - Return values or results
   - Execution time for operations
   - State changes

4. Use structured logging format (key-value pairs or JSON):
   - Consistent field names
   - Easy to parse and filter
   - Include correlation IDs for tracing

5. Add performance logging:
   - Time operations
   - Log slow operations
   - Track resource usage

Focus on logging that helps identify root causes quickly when things go wrong.
```

## Expected Outcomes

After using this prompt, you should see:

1. **Visibility**: Can see what happened at each step
2. **Context**: Logs include relevant data and state
3. **Performance**: Timing information for operations
4. **Traceability**: Can follow execution flow
5. **Debuggability**: Logs help identify problems quickly

## Logging Levels

### DEBUG
- Detailed information for diagnosing problems
- Usually only enabled in development
- Example: "Processing item 5 of 10: {'id': 123, 'value': 45}"

### INFO
- General informational messages
- Normal operation flow
- Example: "Order order123 processed successfully. Items: 3"

### WARNING
- Potentially problematic situations
- May not prevent operation but worth noting
- Example: "Inventory low for item3: 2 remaining"

### ERROR
- Error events that occurred
- May allow app to continue
- Example: "Failed to fetch data from api_source: Connection timeout"

### CRITICAL
- Serious errors requiring immediate attention
- May cause app to abort
- Example: "Database connection lost. Cannot process orders."

## Structured Logging Patterns

### Pattern 1: Entry/Exit Logging
```python
logger.info("Entering function", extra={"function": "process_order", "order_id": order_id})
# ... function logic ...
logger.info("Exiting function", extra={"function": "process_order", "result": "success"})
```

### Pattern 2: Performance Logging
```python
start_time = time.time()
# ... operation ...
duration = time.time() - start_time
logger.info("Operation completed", extra={"operation": "fetch_data", "duration_ms": duration * 1000})
```

### Pattern 3: State Change Logging
```python
logger.info("State changed", extra={
    "component": "inventory",
    "item_id": item_id,
    "old_value": old_quantity,
    "new_value": new_quantity
})
```

### Pattern 4: Error Logging with Context
```python
logger.error("Operation failed", extra={
    "operation": "validate_data",
    "error": str(e),
    "input_size": len(data),
    "input_preview": str(data[:5])
}, exc_info=True)
```

## Key Learning

**Logging is visibility—it shows you what's happening inside your code.** Good logging enables:
- Faster debugging (know where problems occurred)
- Better monitoring (see system health in real-time)
- Performance analysis (identify bottlenecks)
- Root cause analysis (trace execution flow)
- AI assistance (AI can analyze logs to suggest fixes)

This is especially powerful for AI because:
- AI can parse structured logs
- AI can trace execution flow
- AI can identify patterns in logs
- AI can suggest fixes based on log analysis

## Next Steps

1. Use the prompt above with your AI assistant
2. Run code and examine the logs
3. See how logs help identify issues
4. Compare your approach with `solution/` to see comprehensive logging examples

