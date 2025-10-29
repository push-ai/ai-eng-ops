# Engineering Context Documentation

> **Purpose**: Provide reference documentation that reinforces engineering best practices and guides AI engineering agents to produce code that aligns with your team's specific patterns, standards, and requirements.

## What This Directory Contains

This `contexts/` directory contains **organizational knowledge** in the form of documentation files that define:

- **Engineering standards** - Code quality, patterns, and conventions
- **Architecture decisions** - System design principles and patterns
- **CI/CD processes** - Build, test, and deployment workflows
- **DevOps practices** - Infrastructure and operations patterns
- **Engineering workflows** - Development processes and best practices
- **Infrastructure standards** - Cloud, networking, and infrastructure patterns
- **Monitoring practices** - Observability, logging, and alerting standards
- **Security fundamentals** - Security policies, practices, and requirements

## Why Context Documentation Matters for AI Engineering

### The Problem: AI Lacks Organizational Context

When AI coding assistants don't have access to your team's specific context, they:

- **Guess at patterns** instead of following your established conventions
- **Miss critical requirements** that aren't obvious from code alone
- **Violate standards** because they don't know your team's rules
- **Create inconsistent code** because they can't see your patterns
- **Break compliance** because they don't understand your security/regulatory needs

### The Solution: Explicit Context Documentation

Context documentation provides AI with the organizational knowledge it needs:

- **Standards** define what "good code" means for your team
- **Architecture** explains system design decisions and constraints
- **CI/CD** documents deployment processes and requirements
- **DevOps** defines infrastructure patterns and operations procedures
- **Engineering** captures development workflows and best practices
- **Infrastructure** documents cloud/infrastructure standards
- **Monitoring** defines observability requirements and patterns
- **Security** captures security policies and implementation requirements

## How Context Documentation Works

### 1. **Reference Documentation**

Context files serve as **reference documentation** that:

- Define **team-specific patterns** and conventions
- Capture **organizational knowledge** that isn't in code
- Document **historical decisions** and their rationale
- Specify **requirements** that aren't obvious from code
- Establish **standards** that guide AI decision-making

### 2. **AI Assistant Guidance**

When AI assistants reference context documentation, they:

- **Follow established patterns** instead of guessing
- **Respect constraints** documented in architecture docs
- **Apply standards** from your standards documentation
- **Follow processes** defined in workflow docs
- **Meet requirements** specified in compliance docs

### 3. **Team Customization**

Each team can customize context documentation to:

- **Reflect their patterns** - Document actual patterns used in codebase
- **Capture requirements** - Include domain-specific, regulatory, or business requirements
- **Define standards** - Set code quality, security, and operational standards
- **Document processes** - Explain workflows, review processes, deployment procedures
- **Guide AI behavior** - Provide explicit instructions for AI assistants

## Structure and Organization

Each context folder contains:

- **README.md** - Explains the purpose of that context category and how to use it
- **Example documentation files** - Demonstrates the type of documentation to create
- **Templates** (where applicable) - Starting points for creating your own documentation

### Example Context Files

Context files are typically:
- **Markdown files** (`.md`) for easy reading and version control
- **Living documents** that evolve with your team's practices
- **Referenced in code** via comments pointing to context files
- **Version controlled** alongside your codebase

## How to Use Context Documentation

### For Engineering Teams

1. **Review existing examples** in each context folder
2. **Customize examples** to match your team's patterns
3. **Add new documentation** as your team establishes new patterns
4. **Keep documentation updated** as practices evolve
5. **Reference in code** via comments linking to context docs

### For AI Assistants

1. **Read context documentation** when working on code
2. **Apply patterns** from standards and architecture docs
3. **Follow processes** defined in workflow documentation
4. **Respect constraints** documented in context files
5. **Reference context** when making decisions

### For Code Reviews

1. **Check against standards** documented in context files
2. **Verify patterns** match architecture documentation
3. **Ensure compliance** with security and regulatory requirements
4. **Validate processes** follow workflow documentation

## Best Practices for Context Documentation

### 1. **Keep It Current**

- Update documentation when patterns change
- Remove outdated information
- Document new patterns as they emerge
- Review periodically for accuracy

### 2. **Make It Specific**

- Include concrete examples from your codebase
- Reference actual code patterns used
- Document real requirements and constraints
- Provide specific, actionable guidance

### 3. **Link to Code**

- Reference context docs in code comments
- Link from code to relevant context documentation
- Keep documentation close to code
- Make connections explicit

### 4. **Include Examples**

- Show both good and bad examples
- Demonstrate patterns in practice
- Provide copy-paste examples where applicable
- Include real-world scenarios

### 5. **Make It Accessible**

- Use clear, concise language
- Organize logically
- Include tables of contents for long documents
- Make it easy to find information

## Integration with AI Engineering

### Providing Context to AI

When working with AI assistants:

1. **Reference context files** explicitly: "See `contexts/standards/code-quality.md`"
2. **Quote specific requirements**: "Per `contexts/security/policies.md`, all APIs must..."
3. **Point to patterns**: "Follow the pattern in `contexts/architecture/api-design.md`"
4. **Link to processes**: "Use the deployment process in `contexts/ci-cd/deployment.md`"

### AI Using Context

AI assistants should:

1. **Read context files** when mentioned or when relevant
2. **Apply documented patterns** without deviation
3. **Respect documented constraints** strictly
4. **Follow documented processes** completely
5. **Reference context** in code comments

## Context Categories

### `/standards/` - Code Quality and Conventions
Defines coding standards, style guides, and quality metrics that ensure consistency and maintainability.

### `/architecture/` - System Design Principles
Documents architectural decisions, design patterns, and system constraints that guide system design.

### `/ci-cd/` - Build and Deployment Processes
Defines continuous integration and deployment workflows, build processes, and release procedures.

### `/devops/` - Infrastructure and Operations
Documents infrastructure patterns, operational procedures, and DevOps best practices.

### `/engineering/` - Development Workflows
Captures development processes, code review practices, and engineering best practices.

### `/infrastructure/` - Cloud and Infrastructure Standards
Defines infrastructure standards, cloud patterns, and infrastructure-as-code conventions.

### `/monitoring/` - Observability and Monitoring
Documents monitoring requirements, logging standards, alerting rules, and observability patterns.

### `/security/` - Security Policies and Practices
Defines security requirements, secure coding practices, and compliance requirements.

## Getting Started

1. **Review** the README in each context folder
2. **Examine** the example documentation files
3. **Customize** examples to match your team's patterns
4. **Create** new documentation as needed
5. **Reference** context docs in your code and workflows

## Maintenance

- **Review quarterly** - Ensure documentation stays current
- **Update on changes** - Modify docs when patterns change
- **Remove outdated** - Delete obsolete documentation
- **Gather feedback** - Ask team what context they need
- **Measure usage** - Track which context docs are referenced most

---

**Remember**: Context documentation is your team's organizational memory. It captures knowledge that helps both humans and AI understand how to build software that fits your team's specific needs, constraints, and patterns.

