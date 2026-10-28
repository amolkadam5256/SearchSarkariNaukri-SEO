# Internal Linking — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 9. Internal Linking Checklist

- [ ] Ensure every important indexable page is reachable through relevant internal links.
- [ ] Link listing pages to individual detail pages.
- [ ] Link detail pages to genuinely relevant syllabus, admit-card, result, answer-key, and application resources.
- [ ] Connect state-wise, organization-wise, exam-wise, and category-wise content where useful.
- [ ] Add breadcrumbs where appropriate.
- [ ] Use descriptive, natural anchor text.
- [ ] Avoid excessive exact-match keyword anchors.
- [ ] Identify orphan pages and pages with very few useful internal links.
- [ ] Review links in the header, navigation, footer, related-content sections, and article body.
- [ ] Check for broken internal links, redirecting links, and links to noncanonical URLs.
- [ ] Ensure important links are actual crawlable anchors with valid destinations.
- [ ] Avoid relying only on JavaScript click handlers for navigation.
- [ ] Ensure related-content modules are genuinely relevant.
- [ ] Prevent circular, repetitive, or automatically generated link blocks that add no value.
- [ ] Verify that pagination and filters do not create uncontrolled URL duplication.

## Detailed developer instructions

Inspect navigation, breadcrumbs, body links and related modules. Find broken, redirected, noncanonical, orphaned, deep or irrelevant links. Verify descriptive crawlable anchors and controlled filter/pagination URLs. Preserve working routes and avoid bulk keyword-anchor changes.

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
