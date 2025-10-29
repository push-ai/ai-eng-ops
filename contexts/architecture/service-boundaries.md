# Service Boundaries and Responsibilities

## Overview

This document defines service boundaries, responsibilities, and communication patterns for our microservices architecture.

## Service Responsibilities

### User Service

**Owns**: User data, authentication, user profiles

**Boundaries**:
- Manages user accounts and authentication
- Stores user profile data
- Handles user preferences
- Does NOT handle payments or orders

**APIs**:
- `POST /users` - Create user
- `GET /users/{id}` - Get user
- `POST /auth/login` - Authenticate
- `POST /auth/logout` - Logout

### Order Service

**Owns**: Orders, order processing, order status

**Boundaries**:
- Manages order lifecycle
- Tracks order status
- Coordinates with Payment Service for payments
- Does NOT handle user authentication

**APIs**:
- `POST /orders` - Create order
- `GET /orders/{id}` - Get order
- `PUT /orders/{id}/status` - Update status

### Payment Service

**Owns**: Payment processing, transactions, refunds

**Boundaries**:
- Processes payments
- Handles refunds
- Manages payment methods
- Does NOT handle user data or orders

**APIs**:
- `POST /payments` - Process payment
- `POST /payments/{id}/refund` - Process refund

## Service Communication

### Synchronous Communication

- **HTTP/REST**: For request/response patterns
- **API Gateway**: All external requests through gateway
- **Service mesh**: For service-to-service communication
- **Circuit breakers**: Prevent cascading failures

### Asynchronous Communication

- **Event bus**: For event-driven communication
- **Message queue**: For async processing
- **Event sourcing**: For audit and replay
- **Pub/Sub**: For fan-out patterns

## Data Ownership

### Rule: One Service Owns Each Data Entity

- **User Service**: Owns user data
- **Order Service**: Owns order data
- **Payment Service**: Owns payment data
- **No shared databases**: Each service has its own database

### Cross-Service Data Access

- **APIs only**: Access other services' data via APIs
- **Caching**: Cache frequently accessed data
- **Event replication**: Replicate needed data via events
- **Never direct DB access**: Services cannot access each other's databases

## Service Boundaries Enforcement

### API Contracts

- **OpenAPI specs**: Document all service APIs
- **Contract testing**: Verify contracts between services
- **Versioning**: Version APIs for evolution
- **Breaking changes**: Coordinate breaking changes

### Database Isolation

- **Separate databases**: Each service has own database
- **No cross-database queries**: Services cannot query other services' databases
- **Data replication**: Use events to replicate needed data
- **Eventual consistency**: Accept eventual consistency for cross-service data

## Anti-Patterns to Avoid

### ❌ Shared Database

```python
# Bad: Services sharing database
# User Service and Order Service both access same database
```

### ❌ Direct Database Queries

```python
# Bad: Order Service querying User Service database directly
user = db.query("SELECT * FROM users WHERE id = ?", user_id)
```

### ❌ God Service

```python
# Bad: One service handling everything
class MegaService:
    def handle_users(self): pass
    def handle_orders(self): pass
    def handle_payments(self): pass
```

## References

- API Design: `contexts/architecture/api-design.md`
- Integration Patterns: `contexts/architecture/integration-patterns.md`

