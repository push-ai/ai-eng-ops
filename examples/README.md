# Development Examples

This directory contains practical, runnable examples that demonstrate how AI engineering agents can effectively work with common software development tasks. Each example focuses on areas where AI coding assistants often struggle, providing clear patterns and principles that help both AI and human engineers produce better code.

## Purpose

These examples serve as **teaching tools** and **prompt templates** that demonstrate:

1. **How to structure prompts** that guide AI to produce high-quality code
2. **Common pitfalls** in AI-generated code and how to avoid them
3. **Best practices** for iterating with AI to improve code quality
4. **Real-world scenarios** that engineers encounter daily

## Example Structure

Each example follows a consistent three-part structure:

```
examples/
└── level-01-foundation/
    ├── 01-simple-function/    # (Coming soon)
    ├── 02-utility-module/     # (Coming soon)
    ├── 03-data-structure/     # (Coming soon)
    ├── 04-testing/            # Effective tests for AI iteration
    ├── 05-bug-fix/            # TDD bug fixing workflow
    ├── 06-error-logs/         # Clear error messages for AI self-correction
    └── 07-logging/            # Structured logging for root cause identification
        ├── problem/           # Initial code that needs improvement
        │   ├── main.py        # Runnable example code
        │   ├── requirements.txt # Dependencies (if needed)
        │   └── README.md      # How to run the example
        ├── PRINCIPLE.md       # What we're teaching + copy-paste prompt
        └── solution/          # Example improvements with explanations
            ├── main.py        # Improved code
            ├── tests/         # Test files demonstrating the principle
            └── EXPLANATION.md # What changed and why
```

### Directory Breakdown

#### `problem/` Directory
- **Purpose**: Contains example code that demonstrates a problem or gap
- **Content**: Runnable Python code that showcases the issue
- **Usage**: Users run this code, identify issues, then use the prompt to guide AI improvements

#### `PRINCIPLE.md` File
- **Purpose**: Explains the principle being demonstrated and provides a ready-to-use prompt
- **Content**:
  - Clear explanation of the principle
  - Why this matters for AI engineering agents
  - A copy-paste prompt you can use with your AI assistant
  - Expected outcomes from using the prompt

#### `solution/` Directory
- **Purpose**: Shows example improvements that follow the principle
- **Content**:
  - Improved code demonstrating the principle
  - Tests that validate the improvements
  - `EXPLANATION.md` detailing what changed and why
  - Learning outcomes and takeaways

## Using These Examples

### Step 1: Explore the Example
1. Navigate to an example directory (e.g., `level-01-foundation/04-testing/`)
2. Read the `problem/README.md` to understand the example
3. Run the code in `problem/` to see the current state

### Step 2: Understand the Principle
1. Read `PRINCIPLE.md` to understand what we're teaching
2. Review why this principle matters for AI engineering

### Step 3: Use the Prompt
1. Copy the prompt from `PRINCIPLE.md`
2. Paste it into your AI coding assistant (Cursor, GitHub Copilot, etc.)
3. Point the AI to the `problem/` directory
4. Let the AI analyze and suggest improvements

### Step 4: Compare with Solution
1. Review the `solution/` directory to see example improvements
2. Read `solution/EXPLANATION.md` to understand what changed
3. Compare your AI's suggestions with the example solution
4. Learn from both the similarities and differences

## Example Categories

### Level 01: Foundation
Focuses on fundamental skills where AI often struggles:

- **01-simple-function** - Creating a single, well-tested function
- **02-utility-module** - Building a reusable utility module
- **03-data-structure** - Implementing a data structure/class with strong typing
- **04-testing** - Creating effective tests that help AI iterate through edge cases
- **05-bug-fix** - Reproducing bugs locally, fixing with TDD approach
- **06-error-logs** - Crafting error messages that help AI self-correct
- **07-logging** - Setting up logging for faster root cause identification
- **08-documentation** - Providing context through documentation to enable AI accuracy

### Level 02: Features ⚠️
> **WARNING: THIS CONTENT HAS NOT BEEN REVIEWED YET, PROCEED WITH CAUTION**

Focuses on building complete, production-ready features:
- **01-api-endpoint** - Building RESTful API endpoints with proper structure
- **02-react-component** - Creating React components with TypeScript
- **03-database-model** - Designing database models with relationships
- **04-service-integration** - Integrating with external services

See [level-02-features/README.md](level-02-features/README.md) for detailed documentation.

### Level 03: Multi-Component ⚠️
> **WARNING: THIS CONTENT HAS NOT BEEN REVIEWED YET, PROCEED WITH CAUTION**

Focuses on coordinating multiple components:
- **01-feature-module** - Coordinating frontend and backend with shared types
- **02-auth-flow** - Implementing authentication flows across services
- **03-data-pipeline** - Creating data pipelines with multiple stages
- **04-api-client** - Building API clients that coordinate multiple endpoints

See [level-03-multi-component/README.md](level-03-multi-component/README.md) for detailed documentation.

### Level 04: System-Level ⚠️
> **WARNING: THIS CONTENT HAS NOT BEEN REVIEWED YET, PROCEED WITH CAUTION**

Focuses on system-level architecture and design:
- **01-microservices** - Designing microservices with clear boundaries
- **02-full-stack** - Building full-stack applications
- **03-legacy-refactor** - Refactoring legacy systems safely
- **04-performance** - Optimizing system performance

See [level-04-system-level/README.md](level-04-system-level/README.md) for detailed documentation.

### Level 05: Advanced ⚠️
> **WARNING: THIS CONTENT HAS NOT BEEN REVIEWED YET, PROCEED WITH CAUTION**

Focuses on advanced patterns for complex systems:
- **01-distributed-systems** - Designing distributed systems
- **02-observability** - Implementing comprehensive observability
- **03-security** - Hardening systems with security best practices
- **04-optimization** - Advanced optimization techniques

See [level-05-advanced/README.md](level-05-advanced/README.md) for detailed documentation.

## Principles Demonstrated

### Testing Example
**Principle**: Effective tests enable AI agents to quickly identify edge cases and iterate through failures.

**Why It Matters**: AI often writes code that "works" but misses edge cases. Good tests force AI to consider boundary conditions and error scenarios, leading to more robust code.

### Bug Fix Example
**Principle**: Reproducing bugs locally with tests enables test-driven bug fixing.

**Why It Matters**: AI needs concrete, reproducible test cases to fix bugs effectively. Without a failing test, AI can't verify the fix works.

### Error Logs Example
**Principle**: Well-crafted error messages enable AI self-correction and faster human diagnosis.

**Why It Matters**: Vague errors confuse both AI and humans. Clear, contextual error messages help AI understand what went wrong and suggest fixes.

### Logging Example
**Principle**: Structured logging accelerates root cause identification.

**Why It Matters**: When debugging issues, good logs provide the context AI needs to understand system state and identify problems quickly.

## Contributing Examples

When adding new examples:

1. **Follow the structure**: Use `problem/`, `PRINCIPLE.md`, and `solution/` pattern
2. **Make it runnable**: All code should execute successfully
3. **Focus on AI gaps**: Target areas where AI commonly struggles
4. **Provide clear prompts**: Include copy-paste ready prompts
5. **Explain principles**: Help users understand why it matters
6. **Show problem/solution**: Clear contrast helps learning
7. **Use numbered naming**: Follow sequential numbering (01-, 02-, etc.)

## Language Choice

Examples use **Python** because:
- Universally understood syntax
- Easy to run locally (no complex setup)
- Represents common patterns used across languages
- Great for teaching fundamental concepts

You can adapt these patterns to your preferred language and framework.

---

**Next Steps**: Start with `level-01-foundation/04-testing/` to see how effective tests help AI iterate through edge cases.

