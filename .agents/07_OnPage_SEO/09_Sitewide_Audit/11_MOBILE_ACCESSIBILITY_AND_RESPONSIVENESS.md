# Mobile Accessibility and Responsiveness — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 14. Mobile Responsiveness and Accessibility

- [ ] Test narrow mobile, standard mobile, tablet, laptop, and large desktop layouts.
- [ ] Verify navigation menus, dropdowns, accordions, tables, forms, and modals.
- [ ] Ensure text remains readable without pinch-to-zoom.
- [ ] Check touch target sizes and spacing.
- [ ] Confirm visible keyboard focus and logical tab order.
- [ ] Use semantic buttons, links, form labels, and headings.
- [ ] Add appropriate image alternative text.
- [ ] Ensure sufficient text/background contrast.
- [ ] Do not use color alone to convey status.
- [ ] Verify accessible names and states for interactive controls.
- [ ] Respect reduced-motion preferences.
- [ ] Check accessibility using automated tools and manual keyboard testing.
- [ ] Resolve meaningful WCAG 2.2 AA issues where applicable.

## Detailed developer instructions

Check narrow/standard mobile through desktop. Test menus, forms, tables, accordions and modals with touch and keyboard. Check zoom, focus, semantic labels, contrast, non-color status, alt text, reduced motion, touch targets and meaningful WCAG 2.2 AA issues.

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
