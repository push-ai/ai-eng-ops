# Rollback Strategy

**Service/Component**: [Service Name]  
**Version to Rollback**: [Current Version]  
**Version to Rollback To**: [Previous Version]  
**Environment**: [dev/staging/production]  
**Prepared By**: [Name]  
**Date**: [Date]

---

## Rollback Triggers

Rollback will be triggered if:

- [ ] Health checks fail (> 3 consecutive failures)
- [ ] Error rate increases (> 50% increase)
- [ ] Performance degrades (> 2x response time)
- [ ] Critical functionality broken
- [ ] Data corruption detected
- [ ] Security vulnerability exposed

---

## Pre-Rollback Checklist

- [ ] Current version identified: `[version]`
- [ ] Previous version identified: `[version]`
- [ ] Rollback procedure reviewed
- [ ] Team notified
- [ ] Backup verified (if needed)
- [ ] Rollback tested (if possible)

---

## Rollback Procedure

### Step 1: Stop Current Deployment

```bash
# Command to stop current deployment
[Command]
```

**Expected Result**: [What should happen]

**Verification**: [How to verify]

---

### Step 2: Restore Previous Version

```bash
# Command to restore previous version
[Command]
```

**Expected Result**: [What should happen]

**Verification**: [How to verify]

---

### Step 3: Restore Database (If Applicable)

```bash
# Command to restore database
[Command]
```

**Backup Used**: [Backup location/ID]

**Expected Result**: [What should happen]

**Verification**: [How to verify]

---

### Step 4: Verify Rollback

- [ ] Service health checks passing
- [ ] Error rate returned to baseline
- [ ] Performance metrics normal
- [ ] Key features working
- [ ] No errors in logs

---

### Step 5: Post-Rollback Verification

**Health Checks**:
- [ ] Health endpoint: ✅ / ❌
- [ ] Database connectivity: ✅ / ❌
- [ ] External integrations: ✅ / ❌

**Functional Tests**:
- [ ] Test 1: ✅ / ❌
- [ ] Test 2: ✅ / ❌
- [ ] Test 3: ✅ / ❌

**Performance**:
- [ ] Error rate: [%] (baseline: [%])
- [ ] Response time P95: [ms] (baseline: [ms])
- [ ] CPU usage: [%] (normal: [%])
- [ ] Memory usage: [%] (normal: [%])

---

## Rollback Commands

### Quick Rollback

```bash
# Single command rollback (if available)
[Command]
```

### Manual Rollback Steps

```bash
# Step 1
[Command]

# Step 2
[Command]

# Step 3
[Command]
```

---

## Data Considerations

### Database Rollback

- [ ] **Migration rollback**: `[rollback command]`
- [ ] **Data backup**: [Backup location]
- [ ] **Data verification**: [How to verify data integrity]
- [ ] **Data loss**: [Any data that will be lost]

### State Rollback

- [ ] **State to preserve**: [What state must be preserved]
- [ ] **State to reset**: [What state can be reset]
- [ ] **State migration**: [How to migrate state if needed]

---

## Communication Plan

### During Rollback

- [ ] Team notified: [Time]
- [ ] Status page updated: [Time]
- [ ] Stakeholders notified: [Time]

### After Rollback

- [ ] Rollback completed notification sent
- [ ] Status page updated
- [ ] Post-mortem scheduled

---

## Post-Rollback Actions

- [ ] Service stabilized
- [ ] Root cause identified
- [ ] Fix prepared
- [ ] Re-deployment plan created
- [ ] Post-mortem scheduled

---

## Rollback History

| Date | Version From | Version To | Reason | Duration | Resolved By |
|------|--------------|------------|--------|----------|-------------|
| [Date] | [Version] | [Version] | [Reason] | [Duration] | [Name] |

---

## Emergency Contacts

- **On-Call Engineer**: [Name] - [Contact]
- **Team Lead**: [Name] - [Contact]
- **DevOps**: [Name] - [Contact]

---

## Notes

[Any additional notes, considerations, or special instructions]

