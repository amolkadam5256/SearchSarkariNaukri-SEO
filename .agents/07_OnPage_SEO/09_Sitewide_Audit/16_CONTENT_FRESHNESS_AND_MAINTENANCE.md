# Content Freshness and Maintenance — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 19. Content Maintenance and Expired Information

- [ ] Identify outdated recruitment notifications and examination dates.
- [ ] Confirm whether each expired page still provides historical or reference value.
- [ ] Keep useful historical content when it helps users.
- [ ] Clearly label closed applications and completed examination stages.
- [ ] Update information only after verifying the new source.
- [ ] Preserve stable URLs when practical.
- [ ] Avoid redirecting every expired page to the homepage.
- [ ] Remove or redirect pages only under an approved policy.
- [ ] Record who verified the content and when, where the workflow supports it.
- [ ] Establish a recurring review process for high-impact pages.

## Detailed developer instructions

Find expired dates, closed applications and completed stages. Assess historical value before exclusion/removal/redirect. Preserve useful history and URLs, verify updates from official sources, label statuses, record verification when supported and set review cadence.

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
