# Getting Started with AI Engineering Operations

Welcome! This guide will help you get started with the AI Engineering Operations Handbook.

## Quick Start (5 minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/push-ai/ai-eng-ops.git
cd ai-eng-ops
```

### 2. Set Up Cursor IDE
1. Download and install [Cursor IDE](https://cursor.sh/) if you haven't already
2. Open the repository in Cursor
3. Cursor will automatically detect the `.cursor/rules/` directory

### 3. Connect Your Engineering Tools (Optional)
Connect to your engineering tools using your AI platform's supported integration methods. For Cursor IDE users, you can configure tool integrations via Model Context Protocol (MCP). See the main README for configuration details.

**Example Configuration** (`.cursor/mcp.json` for Cursor IDE):
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

Note: Tool integrations are optional. The core value comes from structured markdown files and Cursor rules.

### 4. Customize for Your Team
1. Update `contexts/standards/coding-standards.md` with your team's standards
2. Review `.cursor/rules/*.mdc` files and adjust to your processes
3. Add your architecture decisions to `contexts/architecture/`

## Next Steps

### Week 1: Foundation
- [ ] Read the main [README.md](../README.md)
- [ ] Review all Cursor rules in `.cursor/rules/`
- [ ] Customize coding standards for your team
- [ ] (Optional) Set up tool integrations for your engineering stack

### Week 2: Integration
- [ ] Try using AI to generate code following your standards
- [ ] Test code review workflow with a sample PR
- [ ] Customize test generation for your stack
- [ ] Document your team's architecture decisions

### Week 3: Optimization
- [ ] Gather feedback from team members
- [ ] Refine rules based on usage patterns
- [ ] Add team-specific templates
- [ ] Measure impact on development velocity

## Key Concepts

### Cursor Rules
Cursor Rules (`.cursor/rules/*.mdc`) enforce process discipline:
- `general-operations.mdc` - Always active, universal standards
- `code-review.mdc` - PR review process
- `testing.mdc` - Test generation and coverage
- `deployment.mdc` - CI/CD and deployment workflows

### Context Files
Context files (`contexts/`) provide engineering knowledge:
- Coding standards and conventions
- Architecture decisions and patterns
- Infrastructure and deployment guidelines
- Security requirements

### Templates
Templates (`templates/`) standardize outputs:
- Code review checklists
- Test templates
- Deployment runbooks
- Documentation formats

## Common Workflows

### Code Review Workflow
1. AI analyzes PR against standards
2. Generates review comments
3. Suggests improvements with examples
4. Posts comments to GitHub PR

### Test Generation Workflow
1. AI analyzes code changes
2. Reads testing strategy from context
3. Generates comprehensive test suite
4. Ensures coverage requirements met

### Deployment Workflow
1. AI checks pre-deployment requirements
2. Validates CI/CD pipeline status
3. Monitors post-deployment metrics
4. Initiates rollback if issues detected

## Getting Help

- **Documentation**: Check the [README.md](../README.md) for detailed guides
- **Examples**: See [examples/](../examples/) for implementation patterns
- **Issues**: Open an issue on GitHub for bugs or questions
- **Discussions**: Start a discussion for feature requests or ideas

## Contributing

We welcome contributions! See the main README for contribution guidelines.

---

*Ready to accelerate your engineering operations with AI? Start customizing the handbook for your team today!*

