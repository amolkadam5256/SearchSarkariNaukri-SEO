# Audit Findings and Prioritized Action Plan — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 21. Priority and Tracking Format

Every finding must include:

- **ID:** Unique audit reference.
- **Category:** Technical SEO, GEO, AEO, content, links, UI/UX, performance, security, or another applicable category.
- **Affected URL/component:** Exact route or code location.
- **Issue:** Clear description of the problem.
- **Evidence:** Reproducible observation, source, measurement, or test result.
- **Priority:** Critical, High, Medium, or Low.
- **Recommended fix:** Specific implementation steps.
- **Dependencies:** Any data, approval, or technical dependency.
- **Pass 1 status:** Not started, in progress, passed, blocked, or failed.
- **Pass 2 status:** Not started, in progress, passed, blocked, or failed.
- **Verification evidence:** Test result or recorded observation.
- **Owner and date:** Where applicable.

Do not mark an item complete because code was written. Completion requires verification.

## Detailed developer instructions

Log each finding with unique ID, category, exact URL/component, issue, reproducible evidence, priority, fix, dependencies, both pass states, verification evidence, owner and date. Prioritize by severity, user impact, search impact, effort and risk. Separate facts from hypotheses; leave findings pending until evidence is collected.

## Pass 1 — Audit and implementation

- [ ] Inspect current code/data and capture reproducible baseline evidence.
- [ ] Identify affected routes/components; preserve useful content, records, URLs and working behavior.
- [ ] Record confirmed findings and distinguish evidence from assumptions.
- [ ] Assign priority; document fix, expected result, dependencies and approvals.
- [ ] Implement only scoped approved changes using project conventions.
- [ ] Run applicable local checks; record exact commands/results.
- [ ] Record changed files/components and unresolved items.

## Pass 2 — Independent verification

- [ ] Recheck the original issue against rendered routes or actual system behavior.
- [ ] Verify content/data preservation and applicable metadata, schema and links.
- [ ] Exercise desktop/mobile, keyboard and relevant loading/empty/error/success states.
- [ ] Inspect relevant console/network output and regression paths.
- [ ] Attach reproducible evidence; mark passed, failed, blocked or untested.
- [ ] Keep unresolved items open; code changes or a passing build alone do not prove success.

## Completion record

- Pass 1 owner/date/status: ____________________
- Pass 1 evidence: ____________________
- Pass 2 reviewer/date/status: ____________________
- Pass 2 evidence: ____________________
- Open issues/dependencies: ____________________
