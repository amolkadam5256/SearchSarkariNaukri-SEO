# Performance and Core Web Vitals — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 15. Performance and Core Web Vitals

- [ ] Measure representative pages before and after changes.
- [ ] Evaluate Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS).
- [ ] Use field data where available and lab data for debugging.
- [ ] Optimize image dimensions, formats, compression, and loading priority.
- [ ] Lazy-load appropriate below-the-fold images without delaying critical content.
- [ ] Reduce unnecessary JavaScript and large client-side bundles.
- [ ] Avoid hydration errors and excessive client-side rendering where they harm usability or crawlability.
- [ ] Review font loading and layout shifts.
- [ ] Remove unused dependencies only after confirming they are unnecessary.
- [ ] Review caching, compression, and static asset delivery.
- [ ] Avoid unnecessary third-party scripts.
- [ ] Prevent layout shifts caused by ads, images, and dynamic content.
- [ ] Check slow API requests and repeated data fetching.
- [ ] Avoid sacrificing essential functionality for a marginal performance score.

Use current Core Web Vitals guidance and record actual measurements rather than assuming that a build passing means the site is fast.

## Detailed developer instructions

Measure representative routes before and after changes; record LCP/INP/CLS and conditions. Inspect images, fonts, JS, rendering/hydration, third-party scripts, APIs, cache and layout shifts. Make targeted fixes, compare under equivalent conditions and do not sacrifice essential features to chase scores.

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
