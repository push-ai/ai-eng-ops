# Level 02: Features

> ⚠️ **WARNING: THIS CONTENT HAS NOT BEEN REVIEWED YET, PROCEED WITH CAUTION**
> 
> This level contains examples that are still under development and review. The patterns and principles demonstrated may change based on feedback and real-world testing. Use with caution and verify best practices for your specific use case.

## What This Level Focuses On

**Level 02: Features** builds on the foundation principles and demonstrates how to build **complete, production-ready features** with AI assistance. These examples show how to combine multiple components, follow architectural patterns, and integrate with external systems while maintaining code quality and AI reliability.

Each example demonstrates building a feature end-to-end, from API endpoints to database models to frontend components, showing how AI can effectively work across the full stack when given proper structure and context.

## What You'll Learn

By working through these feature examples, you'll understand:

1. **How to structure complete features** that AI can understand and modify
2. **How to integrate multiple components** (APIs, databases, frontend) coherently
3. **How to maintain consistency** across different parts of a feature
4. **How to enable AI to work across the stack** with proper context
5. **How to build production-ready features** that follow best practices

These examples bridge the gap between foundation principles and real-world feature development, showing how to apply Level 01 principles to complete features.

## The Core Principles

Each example demonstrates building a complete feature while applying foundation principles:

- **01-api-endpoint**: Building RESTful API endpoints with proper structure, validation, and error handling
- **02-react-component**: Creating React components with proper state management, props validation, and testing
- **03-database-model**: Designing database models with relationships, constraints, and migrations
- **04-service-integration**: Integrating with external services (APIs, third-party services) with proper error handling and retries

## How to Use These Examples

### Workflow for Each Example

1. **Explore the Problem**: Review the incomplete or poorly structured feature
2. **Understand the Architecture**: Read the documentation to understand the feature requirements
3. **Practice with AI**: Use the prompts from `PRINCIPLE.md` to guide AI through building/improving the feature
4. **Review the Solution**: See a complete, production-ready implementation
5. **Run and Test**: Execute the feature and verify it works correctly

### Prerequisites

- **Python 3.7+** (for backend examples)
- **Node.js 16+** (for React examples)
- **PostgreSQL** (for database examples) - or Docker for containerized setup
- **Git** (for version control)
- An **AI coding assistant** (Cursor, GitHub Copilot, etc.)
- Understanding of **Level 01 principles** (strong typing, testing, documentation, etc.)

## Example Modules

### 01-api-endpoint: Building RESTful API Endpoints

**Principle**: Well-structured API endpoints with proper validation, error handling, and documentation enable AI to build and modify APIs reliably.

**What You'll Learn**:
- How to structure API endpoints with clear request/response types
- How to implement proper validation and error handling
- How to document APIs so AI understands the contract
- How to write tests that verify API behavior
- How to maintain consistency across multiple endpoints

**Terminal Commands**:
```bash
cd 01-api-endpoint

# Explore the problem (incomplete API)
cd problem
python main.py
# Start the development server
python -m uvicorn main:app --reload

# Review the solution (complete API)
cd ../solution
pip install -r requirements.txt
python -m uvicorn main:app --reload

# Run comprehensive tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=main --cov-report=term-missing

# Test API endpoints
curl http://localhost:8000/api/users
curl http://localhost:8000/api/users/1
```

**Files**:
- `problem/main.py` - Incomplete API endpoint
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/main.py` - Complete API with FastAPI/Flask
- `solution/tests/test_api.py` - API tests
- `solution/requirements.txt` - Dependencies

**Key Concepts**:
- Request/response models with Pydantic
- Route handlers with proper typing
- Error handling and status codes
- API documentation with OpenAPI/Swagger
- Testing API endpoints

---

### 02-react-component: Building React Components

**Principle**: Well-structured React components with proper TypeScript types, props validation, and state management enable AI to build UI components reliably.

**What You'll Learn**:
- How to structure React components with TypeScript
- How to define props interfaces and component state
- How to manage component lifecycle and side effects
- How to write component tests with React Testing Library
- How to maintain consistency across component hierarchies

**Terminal Commands**:
```bash
cd 02-react-component

# Explore the problem (incomplete component)
cd problem
npm install
npm start
# Open http://localhost:3000

# Review the solution (complete component)
cd ../solution
npm install
npm start
# Open http://localhost:3000

# Run component tests
npm test

# Run with coverage
npm test -- --coverage

# Type check
npm run type-check
```

**Files**:
- `problem/src/Component.tsx` - Incomplete React component
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/src/Component.tsx` - Complete component with TypeScript
- `solution/src/__tests__/Component.test.tsx` - Component tests
- `solution/package.json` - Dependencies

**Key Concepts**:
- TypeScript interfaces for props
- Functional components with hooks
- State management patterns
- Component composition
- Testing React components

---

### 03-database-model: Designing Database Models

**Principle**: Well-structured database models with clear relationships, constraints, and migrations enable AI to design and modify database schemas reliably.

**What You'll Learn**:
- How to define database models with SQLAlchemy/Django ORM
- How to establish relationships between models
- How to define constraints and validations
- How to write migrations that are reversible
- How to write tests that verify model behavior

**Terminal Commands**:
```bash
cd 03-database-model

# Explore the problem (incomplete models)
cd problem
python manage.py makemigrations
python manage.py migrate
python manage.py shell
# Test models in shell

# Review the solution (complete models)
cd ../solution
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py shell
# Test models in shell

# Run model tests
pytest tests/test_models.py -v

# Run with coverage
pytest tests/test_models.py --cov=models --cov-report=term-missing

# Check migrations
python manage.py showmigrations
```

**Files**:
- `problem/models.py` - Incomplete database models
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/models.py` - Complete models with relationships
- `solution/migrations/` - Database migrations
- `solution/tests/test_models.py` - Model tests

**Key Concepts**:
- Model definition with ORM
- Foreign keys and relationships
- Model constraints and validations
- Database migrations
- Testing database models

---

### 04-service-integration: Integrating External Services

**Principle**: Well-structured service integrations with proper error handling, retries, and configuration enable AI to integrate with external APIs reliably.

**What You'll Learn**:
- How to structure service clients with proper error handling
- How to implement retry logic and circuit breakers
- How to handle authentication and rate limiting
- How to write integration tests with mocks
- How to document integration patterns

**Terminal Commands**:
```bash
cd 04-service-integration

# Explore the problem (basic integration)
cd problem
python main.py
# Test integration manually

# Review the solution (robust integration)
cd ../solution
pip install -r requirements.txt
python main.py

# Run integration tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=main --cov-report=term-missing

# Test with mocked external service
pytest tests/test_integration.py::test_service_call_with_retry -v
```

**Files**:
- `problem/main.py` - Basic service integration
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/main.py` - Robust integration with retries
- `solution/tests/test_integration.py` - Integration tests
- `solution/requirements.txt` - Dependencies

**Key Concepts**:
- Service client abstraction
- Error handling and retries
- Circuit breaker pattern
- Mocking external services for tests
- Configuration management

---

## Running All Examples

To run all examples and see the complete feature development patterns:

```bash
# From level-02-features directory

# 01-api-endpoint
cd 01-api-endpoint/solution && pip install -r requirements.txt && pytest tests/ -v && cd ../..

# 02-react-component
cd 02-react-component/solution && npm install && npm test && cd ../..

# 03-database-model
cd 03-database-model/solution && pip install -r requirements.txt && pytest tests/ -v && cd ../..

# 04-service-integration
cd 04-service-integration/solution && pip install -r requirements.txt && pytest tests/ -v && cd ../..
```

## Recommended Learning Path

### Start Here: Backend Features

1. **01-api-endpoint** - Learn to build RESTful APIs
2. **03-database-model** - Learn to design database schemas

### Then: Frontend Features

3. **02-react-component** - Learn to build React components

### Finally: Integration

4. **04-service-integration** - Learn to integrate with external services

### Alternative Paths

**Full-Stack Path**: 01 → 02 → 03 → 04 (complete feature stack)
**Backend-First Path**: 01 → 03 → 04 (API + database + integrations)
**Frontend-First Path**: 02 → 01 → 04 (component + API + integrations)

## Key Takeaways

After completing Level 02, you'll understand:

1. **Feature structure** - How to organize complete features
2. **Component integration** - How components work together
3. **API design** - How to build consistent APIs
4. **Database design** - How to model data relationships
5. **Service integration** - How to integrate with external services
6. **Testing strategies** - How to test complete features
7. **AI collaboration** - How to guide AI through feature development

## Relationship to Level 01

Level 02 applies Level 01 principles to complete features:

- **Strong typing** → Type-safe APIs and components
- **Effective tests** → Feature-level test suites
- **Clear errors** → API error responses and component error states
- **Structured logging** → Feature-level logging
- **Documentation** → API docs, component docs, integration docs

Master Level 01 principles first, then apply them to Level 02 features.

## Next Steps

After mastering Level 02, you'll be ready for:
- **Level 03: Multi-Component** - Coordinating multiple features and components
- **Level 04: System-Level** - Architecture and system design
- **Level 05: Advanced** - Distributed systems and optimization

---

**Remember**: These feature examples demonstrate how to apply foundation principles to real-world feature development. Always start with strong typing, comprehensive tests, clear errors, structured logging, and proper documentation.

