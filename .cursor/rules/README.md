# Cursor Rules Directory

This directory contains modular **Cursor Rules** that enforce process-driven AI engineering operations across different engineering domains. Each rule file focuses on specific operational contexts to maximize efficiency and minimize token usage.

## Rule Structure by Account

### 🎯 **`general-operations.mdc`** (Always Applied)
- **Scope**: Universal standards across all engineering functions
- **When Active**: Always loaded for every AI interaction
- **Purpose**: Core quality principles, collaboration standards, and risk management
- **Token Impact**: Minimal - only essential universal guidelines

### 👨‍💻 **`code-review.mdc`** (Context-Aware)
- **Scope**: Pull requests, code reviews, quality checks, security audits
- **When Active**: Working with `/pull-requests/`, `/reviews/`, code files, or PR-related directories
- **Purpose**: Systematic code review process, quality assurance, security checks
- **Key Process**: Analyze → Check Standards → Security Scan → Test Coverage → Suggest Improvements → Approve/Request Changes

### 🧪 **`testing.mdc`** (Context-Aware)
- **Scope**: Test creation, test suites, coverage requirements, TDD workflows
- **When Active**: Working with `/tests/`, `/spec/`, `*.test.*`, `*.spec.*` files
- **Purpose**: Comprehensive test generation, coverage requirements, testing best practices
- **Key Process**: Analyze Requirements → Design Test Strategy → Generate Tests → Verify Coverage → Run Tests → Document

### 🔀 **`pull-request.mdc`** (Context-Aware)
- **Scope**: Pull request creation, PR standards, git workflow, branch management
- **When Active**: Working with markdown files, `.github/` directory, or when creating PRs
- **Purpose**: Consistent PR creation process, proper issue linking, commit standards
- **Key Process**: Check Issues → Commit Changes → Format PR Body → Create Draft/Open PR → Verify Markdown

### 🚀 **`deployment.mdc`** (Context-Aware)
- **Scope**: CI/CD workflows, release processes, deployment pipelines, rollback procedures
- **When Active**: Working with `/ci/`, `/deploy/`, `.github/workflows/`, `.gitlab-ci.yml`, deployment configs
- **Purpose**: Structured deployment workflows, release management, rollback planning
- **Key Process**: Pre-deployment Checks → Build → Test → Security Scan → Deploy → Verify → Monitor

### 🚨 **`incident-response.mdc`** (Context-Aware)
- **Scope**: On-call procedures, debugging workflows, incident management, post-mortems
- **When Active**: Working with `/incidents/`, `/oncall/`, `/runbooks/`, emergency debugging
- **Purpose**: Systematic incident response, root cause analysis, post-mortem documentation
- **Key Process**: Detect → Assess → Contain → Investigate → Resolve → Document → Learn

### 📝 **`documentation.mdc`** (Context-Aware)
- **Scope**: Technical documentation, API docs, architecture decisions, runbooks
- **When Active**: Working with `/docs/`, `/documentation/`, `README.md`, doc-related files
- **Purpose**: Clear, maintainable documentation that stays current with code
- **Key Process**: Plan Structure → Write Content → Review Accuracy → Link Code → Update Process

## Why This Modular Approach?

### ✅ **Token Efficiency**
- Only relevant rules load based on file context
- Reduces AI context overhead for better performance
- Focuses AI attention on applicable processes

### ✅ **Scalability**
- Easy to add new engineering domains (e.g., `security.mdc`, `performance.mdc`)
- Team-specific rules without affecting other functions
- Maintainable and focused rule sets

### ✅ **Context Relevance**
- Rules activate when working on relevant files/directories
- No confusion from irrelevant process guidelines
- Precise guidance for specific work types

## How Rules Activate

According to [Cursor's documentation](https://docs.cursor.com/context/rules), rules can be triggered by:

- **`alwaysApply: true`**: Rules always included (general-operations.mdc)
- **`globs` patterns**: Rules activate when working with matching file paths
- **Manual reference**: Using `@ruleName` in conversations
- **Agent decision**: AI chooses relevant rules based on task context

## Adding New Engineering Domains

To create a new engineering domain rule:

1. **Identify the domain** (e.g., "security", "performance", "accessibility")
2. **Define file/directory patterns** that should trigger the rule
3. **Create focused process steps** specific to that domain
4. **Include quality standards** relevant to that type of work
5. **Test activation** by working in relevant directories

### Template for New Rules:
```markdown
---
description: [Domain] process rules for [specific activities]
globs: ["**/[relevant-directories]/**", "**/*.[relevant-extensions]"]
alwaysApply: false
---

# [Domain] Process Rules

## Multi-Step [Operation Type] Workflow
1. **Step 1**: Description and requirements
2. **Step 2**: Description and requirements
[...continue with 3-8 steps]

## Quality Standards
- Specific standards for this domain

## Emergency Procedures
- Fast-track options for urgent work
```

## Rule Maintenance

### Regular Review
- **Quarterly Assessment**: Evaluate rule effectiveness and usage patterns
- **Team Feedback**: Gather input on process pain points and improvements
- **Usage Analytics**: Monitor which rules are most/least used
- **Process Evolution**: Update rules as engineering needs change

### Best Practices
- **Keep Focused**: Each rule should cover one engineering domain
- **Be Specific**: Provide concrete steps rather than vague guidance
- **Include Examples**: Show what good process execution looks like
- **Balance Automation**: Enforce process without being overly rigid
- **Document Decisions**: Record why specific rules were chosen

## Integration with AI Engineering Operations Handbook

These rules work together with the handbook's other components:

- **`/contexts/`**: Provide engineering knowledge and background information
- **`/templates/`**: Offer starting points for common deliverables  
- **`/briefs/`**: Capture initial requirements for engineering projects
- **`/examples/`**: Demonstrate successful implementations

The rules ensure that AI engineering operations are **deliberate, reviewable, and consistently high-quality** across all engineering functions while maintaining efficiency through focused, context-aware activation.

