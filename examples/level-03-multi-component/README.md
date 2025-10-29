# Level 03: Multi-Component

> ⚠️ **WARNING: THIS CONTENT HAS NOT BEEN REVIEWED YET, PROCEED WITH CAUTION**
> 
> This level contains examples that are still under development and review. The patterns and principles demonstrated may change based on feedback and real-world testing. Use with caution and verify best practices for your specific use case.

## What This Level Focuses On

**Level 03: Multi-Component** demonstrates how to coordinate multiple components, services, and systems to build complex features. These examples show how to structure interactions between components, manage state across boundaries, handle async operations, and maintain consistency when AI needs to work across multiple files and systems.

Each example demonstrates coordinating multiple components—from feature modules that span frontend and backend, to authentication flows that cross service boundaries, to data pipelines that process through multiple stages.

## What You'll Learn

By working through these multi-component examples, you'll understand:

1. **How to structure multi-component features** that AI can understand and modify
2. **How to coordinate components** across service boundaries
3. **How to manage state** across multiple components
4. **How to handle async operations** across components
5. **How to maintain consistency** when changes span multiple files

These examples bridge the gap between single features and complete systems, showing how to apply Level 01 and Level 02 principles across component boundaries.

## The Core Principles

Each example demonstrates coordinating multiple components:

- **01-feature-module**: Building features that span frontend and backend with shared types
- **02-auth-flow**: Implementing authentication flows across multiple services
- **03-data-pipeline**: Creating data pipelines with multiple processing stages
- **04-api-client**: Building API clients that coordinate with multiple endpoints

## How to Use These Examples

### Workflow for Each Example

1. **Explore the Problem**: Review the disconnected or poorly coordinated components
2. **Understand the Architecture**: Read documentation to understand component interactions
3. **Practice with AI**: Use prompts from `PRINCIPLE.md` to guide AI through coordination
4. **Review the Solution**: See well-coordinated components working together
5. **Run and Test**: Execute the multi-component system and verify integration

### Prerequisites

- **Python 3.7+** (for backend examples)
- **Node.js 16+** (for frontend examples)
- **Understanding of Level 01** principles (typing, testing, documentation)
- **Understanding of Level 02** principles (APIs, components, models, integrations)
- An **AI coding assistant** (Cursor, GitHub Copilot, etc.)

## Example Modules

### 01-feature-module: Coordinating Frontend and Backend

**Principle**: Shared type definitions and clear component boundaries enable AI to coordinate frontend and backend components reliably.

**What You'll Learn**:
- How to share types between frontend and backend
- How to structure feature modules across the stack
- How to maintain consistency across components
- How to test multi-component features

**Terminal Commands**:
```bash
cd 01-feature-module

# Explore the problem (disconnected components)
cd problem
# Review frontend and backend separately

# Review the solution (coordinated components)
cd ../solution
# Run backend
cd backend && pip install -r requirements.txt && python main.py
# Run frontend (in another terminal)
cd frontend && npm install && npm start

# Run tests
pytest backend/tests/ -v
npm test --prefix frontend
```

**Files**:
- `problem/backend/` - Backend without shared types
- `problem/frontend/` - Frontend without shared types
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/shared/` - Shared type definitions
- `solution/backend/` - Backend using shared types
- `solution/frontend/` - Frontend using shared types

---

### 02-auth-flow: Authentication Across Services

**Principle**: Clear authentication patterns and token management enable AI to implement secure auth flows across multiple services.

**What You'll Learn**:
- How to structure authentication flows
- How to manage tokens across services
- How to handle auth errors consistently
- How to test authentication flows

**Terminal Commands**:
```bash
cd 02-auth-flow

# Explore the problem (fragmented auth)
cd problem
python main.py

# Review the solution (coordinated auth)
cd ../solution
pip install -r requirements.txt
python main.py

# Run tests
pytest tests/ -v
```

**Files**:
- `problem/` - Fragmented authentication logic
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/` - Coordinated authentication flow
- `solution/tests/` - Auth flow tests

---

### 03-data-pipeline: Multi-Stage Data Processing

**Principle**: Well-defined pipeline stages with clear interfaces enable AI to build and modify data pipelines reliably.

**What You'll Learn**:
- How to structure pipeline stages
- How to handle errors in pipelines
- How to test pipeline stages independently
- How to coordinate multiple processing stages

**Terminal Commands**:
```bash
cd 03-data-pipeline

# Explore the problem (monolithic pipeline)
cd problem
python main.py

# Review the solution (structured pipeline)
cd ../solution
pip install -r requirements.txt
python main.py

# Run tests
pytest tests/ -v
```

**Files**:
- `problem/` - Monolithic pipeline
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/` - Structured pipeline with stages
- `solution/tests/` - Pipeline tests

---

### 04-api-client: Coordinating Multiple Endpoints

**Principle**: Well-structured API clients with consistent patterns enable AI to coordinate multiple API endpoints reliably.

**What You'll Learn**:
- How to structure API clients
- How to coordinate multiple endpoints
- How to handle errors across endpoints
- How to test API client coordination

**Terminal Commands**:
```bash
cd 04-api-client

# Explore the problem (disconnected API calls)
cd problem
python main.py

# Review the solution (coordinated client)
cd ../solution
pip install -r requirements.txt
python main.py

# Run tests
pytest tests/ -v
```

**Files**:
- `problem/` - Disconnected API calls
- `PRINCIPLE.md` - Explanation and copy-paste prompt
- `solution/` - Coordinated API client
- `solution/tests/` - Client tests

---

## Running All Examples

To run all examples and see multi-component coordination:

```bash
# From level-03-multi-component directory

# 01-feature-module
cd 01-feature-module/solution && pytest backend/tests/ -v && cd ../..

# 02-auth-flow
cd 02-auth-flow/solution && pytest tests/ -v && cd ../..

# 03-data-pipeline
cd 03-data-pipeline/solution && pytest tests/ -v && cd ../..

# 04-api-client
cd 04-api-client/solution && pytest tests/ -v && cd ../..
```

## Recommended Learning Path

### Start Here: Feature Coordination

1. **01-feature-module** - Learn to coordinate frontend and backend
2. **04-api-client** - Learn to coordinate multiple API endpoints

### Then: Flows and Pipelines

3. **02-auth-flow** - Learn to coordinate authentication across services
4. **03-data-pipeline** - Learn to coordinate data processing stages

## Key Takeaways

After completing Level 03, you'll understand:

1. **Component coordination** - How to coordinate multiple components
2. **Shared types** - How to share types across components
3. **State management** - How to manage state across boundaries
4. **Error handling** - How to handle errors across components
5. **Testing** - How to test multi-component systems
6. **AI coordination** - How to guide AI across multiple files

## Relationship to Previous Levels

Level 03 applies Level 01 and Level 02 principles across component boundaries:

- **Strong typing** → Shared types across components
- **Effective tests** → Multi-component test suites
- **Clear errors** → Consistent error handling across components
- **Structured logging** → Cross-component logging
- **Documentation** → Component interaction documentation

Master Levels 01 and 02 first, then apply them to Level 03 coordination.

## Next Steps

After mastering Level 03, you'll be ready for:
- **Level 04: System-Level** - Architecture and system design
- **Level 05: Advanced** - Distributed systems and optimization

---

**Remember**: These multi-component examples demonstrate how to apply foundation principles when coordinating multiple components. Always start with strong typing, comprehensive tests, clear errors, structured logging, and proper documentation across all components.

