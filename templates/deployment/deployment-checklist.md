# Deployment Checklist

**Service/Component**: [Service Name]  
**Version**: [Version Number]  
**Environment**: [dev/staging/production]  
**Deployment Date**: [Date/Time]  
**Deployed By**: [Name]

---

## Pre-Deployment

- [ ] Pre-deployment checklist completed
- [ ] Deployment window confirmed
- [ ] Team available for support
- [ ] Monitoring dashboards open

## Deployment Steps

### Step 1: Backup (Production Only)

- [ ] Database backup created
- [ ] Configuration backed up
- [ ] Current version tagged
- [ ] Backup verified

### Step 2: Code Deployment

- [ ] Code pulled from repository
- [ ] Version tag verified: `[version]`
- [ ] Dependencies installed
- [ ] Build completed successfully
- [ ] Artifacts created

### Step 3: Database Migration (If Applicable)

- [ ] Migration plan reviewed
- [ ] Migration executed: `[migration command]`
- [ ] Migration verified
- [ ] Data integrity checked

### Step 4: Service Deployment

- [ ] Service deployed: `[deployment command]`
- [ ] Deployment verified
- [ ] Health checks passing
- [ ] Service status: ✅ Healthy

### Step 5: Post-Deployment Verification

- [ ] Health endpoint responding
- [ ] Smoke tests passing
- [ ] Key features verified
- [ ] No errors in logs
- [ ] Performance metrics normal

## Monitoring

### Immediate Checks (First 5 minutes)

- [ ] Error rate: [%] (baseline: [%])
- [ ] Response time P95: [ms] (baseline: [ms])
- [ ] CPU usage: [%] (limit: [%])
- [ ] Memory usage: [%] (limit: [%])
- [ ] Request rate: [req/s] (expected: [req/s])

### Ongoing Monitoring (First hour)

- [ ] Error rate stable
- [ ] Performance metrics stable
- [ ] No alerts triggered
- [ ] Logs show normal operation

## Verification Tests

- [ ] Test 1: [Description] - ✅ Pass / ❌ Fail
- [ ] Test 2: [Description] - ✅ Pass / ❌ Fail
- [ ] Test 3: [Description] - ✅ Pass / ❌ Fail

## Rollback Readiness

- [ ] Rollback procedure ready
- [ ] Rollback owner identified: [Name]
- [ ] Previous version available
- [ ] Rollback tested (if possible)

## Communication

- [ ] Deployment started notification sent
- [ ] Deployment status updated
- [ ] Deployment completed notification sent
- [ ] Status page updated (if applicable)

## Deployment Completion

**Deployment Status**: ✅ Success / ❌ Failed / ⚠️ Partial

**Completion Time**: [Date/Time]

**Deployed Version**: [Version]

**Deployed By**: [Name]

---

## Post-Deployment

- [ ] Monitoring for [duration]
- [ ] Team available for support
- [ ] Post-deployment review scheduled
- [ ] Issues logged (if any)

## Issues Encountered

- [ ] Issue 1: [Description] - [Resolution]
- [ ] Issue 2: [Description] - [Resolution]

## Notes

[Any additional notes or observations]

