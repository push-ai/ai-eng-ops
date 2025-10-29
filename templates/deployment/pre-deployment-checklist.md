# Pre-Deployment Checklist

**Service/Component**: [Service Name]  
**Version**: [Version Number]  
**Environment**: [dev/staging/production]  
**Planned Deployment Date**: [Date/Time]  
**Deployment Lead**: [Name]

---

## Code Quality Checks

- [ ] All tests passing locally
- [ ] Code coverage meets threshold (80%+)
- [ ] Linting passed (`npm run lint` / `pylint`)
- [ ] Type checking passed (`npm run type-check` / `mypy`)
- [ ] Security scan passed (no high/critical vulnerabilities)
- [ ] Performance tests passed (if applicable)

## Code Review

- [ ] PR reviewed and approved
- [ ] All review comments addressed
- [ ] Code merged to target branch
- [ ] CI/CD pipeline passed

## Testing

- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] E2E tests passing (if applicable)
- [ ] Manual testing completed
- [ ] Tested in staging environment (if applicable)

## Documentation

- [ ] README updated (if needed)
- [ ] API documentation updated (if needed)
- [ ] Architecture docs updated (if needed)
- [ ] Changelog updated
- [ ] Release notes prepared

## Configuration

- [ ] Environment variables documented
- [ ] Configuration changes reviewed
- [ ] Secrets updated (if needed)
- [ ] Feature flags configured (if applicable)
- [ ] Third-party integrations verified

## Database Changes

- [ ] Database migrations prepared
- [ ] Migrations tested in staging
- [ ] Rollback migration prepared
- [ ] Backup created (production only)
- [ ] Migration plan documented

## Dependencies

- [ ] Dependencies updated (if applicable)
- [ ] Dependency versions pinned
- [ ] Security vulnerabilities checked
- [ ] Breaking changes reviewed

## Infrastructure

- [ ] Infrastructure changes reviewed (if applicable)
- [ ] Resource allocation sufficient
- [ ] Scaling configuration verified
- [ ] Monitoring/alerts configured

## Security

- [ ] Security review completed (if applicable)
- [ ] No secrets in code
- [ ] Input validation verified
- [ ] Authentication/authorization verified
- [ ] Security scan passed

## Performance

- [ ] Performance benchmarks met
- [ ] Load testing completed (if applicable)
- [ ] Resource usage acceptable
- [ ] No performance regressions

## Communication

- [ ] Team notified of deployment
- [ ] Stakeholders notified (if applicable)
- [ ] Maintenance window scheduled (if needed)
- [ ] Rollback plan communicated

## Rollback Preparation

- [ ] Previous version tagged
- [ ] Rollback procedure documented
- [ ] Rollback tested (if possible)
- [ ] Rollback owner identified

## Final Verification

- [ ] All checks completed
- [ ] Deployment lead approved
- [ ] Team lead approved (production only)
- [ ] Ready to deploy

---

## Pre-Deployment Sign-Off

**Deployment Lead**: [Name] - [Date/Time]  
**Team Lead**: [Name] - [Date/Time] (production only)

---

## Notes

[Any additional notes or concerns]

