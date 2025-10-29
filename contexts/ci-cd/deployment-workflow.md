# Deployment Workflow

## Overview

This document defines the deployment workflow for all services, including the steps, checks, and procedures required for safe deployments.

## Deployment Environments

### Development
- **Purpose**: Development and testing
- **Access**: All developers
- **Deployment**: Automatic on merge to `develop`
- **Data**: Test data, can be reset

### Staging
- **Purpose**: Pre-production testing
- **Access**: QA and developers
- **Deployment**: Manual or on merge to `staging`
- **Data**: Production-like data

### Production
- **Purpose**: Live user-facing environment
- **Access**: Restricted (CI/CD and ops)
- **Deployment**: Manual approval required
- **Data**: Real production data

## Pre-Deployment Checklist

### Code Quality

- [ ] All tests passing
- [ ] Code coverage meets threshold (80%)
- [ ] Linting passed
- [ ] Security scan passed
- [ ] Performance tests passed
- [ ] Documentation updated

### Release Preparation

- [ ] Version bumped
- [ ] Changelog updated
- [ ] Release notes prepared
- [ ] Database migrations prepared (if needed)
- [ ] Configuration changes documented
- [ ] Rollback plan prepared

## Deployment Process

### 1. Pre-Deployment Validation

```bash
# Run quality checks
npm run lint
npm run test
npm run test:coverage
npm run security:scan

# Verify build
npm run build
```

### 2. Build Artifacts

```bash
# Create Docker image
docker build -t service-name:version .

# Tag for registry
docker tag service-name:version registry.example.com/service-name:version
```

### 3. Deploy to Staging

```bash
# Deploy to staging
kubectl apply -f k8s/staging/
kubectl rollout status deployment/service-name -n staging

# Verify deployment
./scripts/verify-deployment.sh staging
```

### 4. Staging Verification

- [ ] Health checks passing
- [ ] Smoke tests passing
- [ ] Integration tests passing
- [ ] Performance acceptable
- [ ] No errors in logs

### 5. Production Deployment

```bash
# Deploy to production (requires approval)
kubectl apply -f k8s/production/
kubectl rollout status deployment/service-name -n production

# Verify deployment
./scripts/verify-deployment.sh production
```

### 6. Post-Deployment Verification

- [ ] Health checks passing
- [ ] Monitoring shows normal metrics
- [ ] No error rate increase
- [ ] Key features verified
- [ ] Performance metrics normal

## Rollback Procedure

### Automatic Rollback Triggers

- Health check failures (> 3 consecutive)
- Error rate increase (> 50%)
- Performance degradation (> 2x response time)

### Manual Rollback

```bash
# Rollback to previous version
kubectl rollout undo deployment/service-name -n production

# Verify rollback
kubectl rollout status deployment/service-name -n production
./scripts/verify-deployment.sh production
```

## Deployment Strategies

### Blue-Green Deployment

- **Two environments**: Blue (current) and Green (new)
- **Switch traffic**: All at once or gradually
- **Rollback**: Switch back to Blue

### Canary Deployment

- **Gradual rollout**: 10% → 50% → 100%
- **Monitor metrics**: At each stage
- **Rollback**: Stop rollout if issues

### Rolling Deployment

- **Gradual replacement**: Replace pods gradually
- **Zero downtime**: Maintains service availability
- **Rollback**: Reverse rolling update

## Monitoring During Deployment

### Key Metrics

- **Error rate**: Should not increase
- **Response time**: Should not degrade significantly
- **CPU/Memory**: Should remain within limits
- **Request rate**: Should remain normal

### Alerts

- **Error rate spike**: Alert if > 5% errors
- **Latency increase**: Alert if P95 > 2x baseline
- **Resource exhaustion**: Alert if CPU/Memory > 90%

## Post-Deployment

### Monitoring Period

- **First 15 minutes**: Intense monitoring
- **First hour**: Regular checks
- **First 24 hours**: Standard monitoring
- **Watch for**: Errors, performance issues, user complaints

### Documentation

- **Deployment log**: Record deployment details
- **Issues**: Document any issues encountered
- **Rollback**: Document if rollback was needed
- **Lessons learned**: Update process based on experience

## Emergency Procedures

### Hotfix Deployment

- **Expedited process**: For critical bugs
- **Minimal testing**: Focus on fix verification
- **Fast approval**: Expedited review
- **Monitor closely**: Extra monitoring after deployment

### Production Incident

- **Stop deployments**: Halt all deployments
- **Assess situation**: Understand impact
- **Rollback if needed**: Immediate rollback if deployment caused issue
- **Post-mortem**: Document incident and improve process

## References

- Build Process: `contexts/ci-cd/build-process.md`
- Monitoring: `contexts/monitoring/alerts.md`

