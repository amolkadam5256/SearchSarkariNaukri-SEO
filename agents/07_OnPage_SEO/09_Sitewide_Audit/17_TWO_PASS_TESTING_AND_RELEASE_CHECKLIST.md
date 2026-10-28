# Two-Pass Testing and Release — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 20. Two-Pass Audit and Implementation Verification

Create a separate Markdown checklist for every major page type or implementation area. Each checklist must include both verification passes.

### Pass 1 — Implementation

- [ ] Review the existing implementation and supporting data.
- [ ] Record the issue and its evidence.
- [ ] Assign priority: Critical, High, Medium, or Low.
- [ ] Document the recommended change and expected outcome.
- [ ] Implement approved changes without removing unrelated functionality.
- [ ] Verify the change locally.
- [ ] Record changed files and any unresolved dependency.

### Pass 2 — Independent verification

- [ ] Recheck the original issue against the implemented result.
- [ ] Verify page content and data preservation.
- [ ] Verify metadata, canonical URLs, indexation directives, and schema.
- [ ] Verify internal and external links.
- [ ] Test desktop and mobile behaviour.
- [ ] Test interactions, loading, empty, and error states.
- [ ] Run applicable automated checks.
- [ ] Inspect the browser console and network errors.
- [ ] Confirm no unrelated routes or components were broken.
- [ ] Record evidence of the final result.
- [ ] Mark failed or unverified items as unresolved rather than passed.

A documentation checklist passing is not evidence that the website itself passes.

## 23. Final Acceptance Criteria

The project audit is complete only when:

- [ ] The actual repository and route structure have been inspected.
- [ ] Every discovered public route is inventoried or explicitly excluded with a reason.
- [ ] Each applicable audit category has a detailed checklist.
- [ ] Each checklist has a separate Pass 1 and Pass 2 verification process.
- [ ] Existing page content, sections, records, and functionality are preserved unless an approved change states otherwise.
- [ ] Important official information has a verifiable source or is clearly flagged for verification.
- [ ] Internal and external links have been checked using recorded evidence.
- [ ] SEO metadata, indexability, canonical URLs, and structured data have been tested on representative routes.
- [ ] Responsive layouts, accessibility, and critical user journeys have been tested.
- [ ] Applicable lint, type, test, and production-build checks have been run.
- [ ] Remaining issues are listed with priority, evidence, and recommended actions.
- [ ] The final report distinguishes completed, failed, blocked, and untested items.
- [ ] No claim is made that a ranking, indexing outcome, or performance improvement is guaranteed.

**Final developer instruction:** Start with the audit and documentation. Do not begin a broad redesign or mass content rewrite before establishing the baseline. Use verified project evidence, follow existing repository conventions, implement changes in controlled stages, and independently verify each stage before reporting completion.

## Detailed developer instructions

Pass 1 captures baseline, evidence, priority, proposed fix, dependencies and local verification. Pass 2 independently rechecks original issues against rendered pages, data, metadata/schema, links, devices, interactions, errors and regressions. Keep failed/blocked/untested distinct; a document checklist or successful build alone is not site verification.

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
