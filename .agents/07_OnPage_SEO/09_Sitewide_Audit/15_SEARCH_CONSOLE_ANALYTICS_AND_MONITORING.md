# Search Console Analytics and Monitoring — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 18. Search Console, Analytics, and Monitoring

- [ ] Verify the correct Search Console property where access is available.
- [ ] Review indexing reports and URL inspection for representative pages.
- [ ] Check sitemap processing and crawl anomalies.
- [ ] Review clicks, impressions, CTR, average position, and page-level trends.
- [ ] Review Core Web Vitals and mobile usability signals where available.
- [ ] Confirm analytics events and conversions are implemented correctly.
- [ ] Avoid duplicate page views or duplicate conversion events.
- [ ] Ensure tracking does not block essential functionality.
- [ ] Establish a baseline report before implementation.
- [ ] Compare results after deployment using consistent dates and filters.
- [ ] Record external factors that may affect results.
- [ ] Do not claim improved rankings or indexing without measured evidence.

## Detailed developer instructions

Use authorized data only. Record property, date range and filters. Check indexation, sitemap, crawl, performance, page trends and analytics events for duplication/impact. Compare consistently and note external factors. Do not claim SEO improvement without measured evidence.

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
