# UI/UX Readability and Engagement — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 13. UI/UX and Readability

### Navigation and page layout

- [ ] Make primary navigation understandable and consistent.
- [ ] Ensure breadcrumbs reflect the actual hierarchy.
- [ ] Make page purpose obvious above the fold.
- [ ] Establish clear visual hierarchy between headings, body text, metadata, and actions.
- [ ] Keep spacing, typography, buttons, colors, and component behaviour consistent.
- [ ] Improve dense sections without deleting useful information.
- [ ] Present important dates, status labels, and actions clearly.
- [ ] Ensure long pages have useful section navigation where appropriate.
- [ ] Make tables readable on small screens.
- [ ] Prevent overlapping, clipped, or horizontally overflowing content.
- [ ] Ensure advertisements or promotional modules do not obscure essential content.
- [ ] Provide clear loading, empty, error, and success states.

### Engagement and usability

- [ ] Make application and notification links easy to identify.
- [ ] Add related content only when useful to the current task.
- [ ] Make search, filtering, and sorting understandable.
- [ ] Preserve user-entered values when validation errors occur.
- [ ] Ensure buttons perform the action described by their labels.
- [ ] Avoid intrusive pop-ups and misleading calls to action.
- [ ] Ensure key information is not hidden behind unnecessary interactions.
- [ ] Test all important journeys from homepage to detail page and official source.

## Detailed developer instructions

Review navigation, visual hierarchy, readability, tables, dates/status, loading/error/empty states, forms and calls to action. Walk homepage-to-detail-to-official-source journeys. Record concrete usability evidence. Restructure dense content without deleting useful information; ensure actions match labels.

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
