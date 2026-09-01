# Homepage Technical SEO AEO GEO Audit

Date: 2026-09-01
Page: `https://www.searchsarkarinaukri.com/`
Folder: `.agents/07_OnPage_SEO/01_Home_Page`
Purpose: technical, on-page, AEO, GEO, and crawl-quality audit for the homepage and every homepage-linked section/page.

## Current Local Evidence

The homepage documentation folder currently contains section briefs for:

1. `01_Hero`
2. `02_LIVE_STATISTICS`
3. `03_DAILY_ASSESSMENT`
4. `04_DIGITAL_LIBRARY`
5. `05_JOB_ALERTS`
6. `06_EXAM_COUNTDOWN`
7. `07_CLOSING_SOON_JOBS`
8. `08_EXISTING_TALATHI_FEATURED_RECRUITMENT`
9. `09_QUICK_JOB_FINDER`
10. `10_LATEST_SARKARI_NAUKRI`

The older homepage section documentation files were removed or replaced in the current worktree, so implementation must confirm that the new folder names and section order are intentional before deployment.

## Final Audit Verdict

Status: `AUDIT CREATED / IMPLEMENTATION MUST BE VERIFIED IN WEBSITE SOURCE`

This workspace contains homepage planning/specification files, but it does not contain the production website source code. Therefore, this audit can define the required checks and fixes, but live implementation cannot be marked complete until the actual website code or crawl evidence is available.

## Technical SEO Checklist

### 1. Crawl And Indexing

Pass conditions:

- Homepage returns `200 OK`.
- Homepage is not blocked by `robots.txt`.
- Homepage has no `noindex`.
- Homepage has no `nofollow`.
- No `X-Robots-Tag: noindex`.
- Canonical points to `https://www.searchsarkarinaukri.com/`.
- Homepage appears in XML sitemap.
- Sitemap contains only live, indexable, canonical URLs.
- No sitemap URL should return 404, 410, redirect, noindex, or canonicalize elsewhere.
- Staging, preview, test, admin, private, and backend pages are not indexable.

Required action:

- If any homepage-linked URL returns true `404` and has no useful replacement, remove it from homepage links, sitemap, breadcrumbs, schema, related links, and internal link blocks.
- If the page has a close replacement, use a direct one-hop `301` to the closest relevant live URL.
- Do not redirect dead pages to the homepage unless the homepage is genuinely the closest equivalent.

### 2. URL Architecture And Internal Linking

Pass conditions:

- Important pages are reachable within three clicks from homepage.
- URLs are lowercase, readable, stable, and canonical.
- No duplicate URL variants are linked from homepage.
- No parameter URLs are used as ranking URLs unless intentionally canonicalized.
- Anchor text describes the target page.
- Homepage section CTAs point to live destination URLs.
- No orphan important page exists only in sitemap without internal links.

Homepage links to verify:

- `/jobs`
- `/districts`
- `/eligibility-checker`
- `/daily-assessment`
- `/digital-library`
- `/job-alerts`
- `/exam-calendar`
- `/latest-government-jobs`
- any Talathi recruitment URL
- any latest job detail URL rendered dynamically

### 3. Redirects And Status Codes

Pass conditions:

- HTTP redirects to HTTPS in one hop.
- non-www redirects to www in one hop if www is canonical.
- trailing-slash behavior is consistent.
- retired pages redirect to closest relevant replacement.
- real missing pages return true `404` or `410`.
- 404 page must return real `404`, not `200` with error text.

Required action for 404 pages:

- Remove homepage links to true 404/410 URLs.
- Remove 404/410 URLs from sitemap.
- Remove 404/410 URLs from schema references.
- Remove 404/410 URLs from related job blocks.
- If URL represents a deleted job with no replacement, keep `410 Gone`.
- If URL represents a valid page accidentally missing, restore `200 OK` with useful content.

### 4. Page Speed And Core Web Vitals

Pass conditions:

- Text content renders quickly on mobile.
- LCP element is optimized.
- Homepage hero image is sized correctly and served in a modern format.
- Images use width/height or aspect-ratio to prevent layout shift.
- No heavy animation delays main content.
- No unnecessary render-blocking scripts.
- Dynamic job/stat sections do not block first meaningful content.
- CLS is controlled for cards, counters, images, tickers, ads, and lazy-loaded content.

Required action:

- Do not hard-code fake counters.
- Use database values for statistics.
- Cache expensive homepage queries.
- Load non-critical widgets after primary content.

### 5. Structured Data

Pass conditions:

- Organization schema uses correct site name, URL, logo, and sameAs links.
- WebSite schema includes SearchAction if site search is available.
- Breadcrumb schema matches visible breadcrumbs when used.
- JobPosting schema is not added to homepage unless representing actual visible job cards correctly.
- FAQ schema must match visible FAQ text exactly.
- Schema URLs match canonical URLs.

Required action:

- Remove schema references to dead/404 pages.
- Do not mark up hidden or nonexistent content.
- Keep homepage schema broad: Organization, WebSite, SearchAction, ItemList where latest jobs are visible.

### 6. Mobile And Accessibility

Pass conditions:

- No horizontal overflow on mobile.
- CTAs are thumb-friendly.
- Search field has accessible label.
- Buttons and links have visible focus states.
- Images have meaningful alt text or empty alt for decorative images.
- Dynamic counters are readable by screen readers.
- Content parity exists between mobile and desktop.
- Skip link works.

Required action:

- Do not hide important SEO content on mobile.
- Do not put critical text inside images.
- Use semantic sections, headings, lists, tables, and links.

## On-Page SEO Audit

### Homepage Intent

Primary intent:

- Sarkari Naukri 2026
- Latest Government Jobs in India
- Government job vacancies by qualification, district, department, and exam

Homepage should not try to rank for every district, every qualification, every department, and every individual job. It should route users and crawlers to the best focused pages.

### Required Homepage Content Sections

Minimum homepage sections:

1. Hero / direct answer
2. Search box
3. Live statistics
4. Latest Sarkari Naukri
5. Closing soon jobs
6. Featured recruitment
7. Quick job finder
8. Government job alerts
9. Exam countdown or exam calendar
10. Daily assessment
11. Digital library / study material
12. Popular qualifications
13. Popular departments
14. Popular states/districts
15. Results/admit cards links
16. Verification/editorial trust note
17. FAQ

If any section links to a URL that is dead or not needed, remove the link or replace it with the closest live equivalent.

## AEO And GEO Audit

Pass conditions:

- Homepage answers what the site does near the top.
- Important entities are clear: SearchSarkariNaukri, Sarkari Naukri, Government Jobs, Maharashtra Jobs, UPSC, MPSC, SSC, Railway, Banking.
- Page includes direct factual summaries instead of vague marketing copy.
- Job cards include source verification status where available.
- Latest jobs, closing jobs, exam dates, and counts are data-backed.
- FAQs answer real user questions.
- Internal links use descriptive anchors that help AI systems understand page relationships.

Required action:

- Add a visible editorial note: users must verify dates, eligibility, fees, and official links from official recruitment notifications.
- Add related links to focused pages instead of stuffing all keywords into the homepage.

## Off-Page And Authority Audit

This is not a homepage code fix, but it affects SEO and AI visibility.

Required checks:

- Audit backlink profile.
- Identify competitor backlink gaps.
- Build links to useful assets such as job calendars, eligibility tools, district job guides, and exam resources.
- Monitor unlinked brand mentions.
- Improve forum/community visibility with genuinely useful answers.
- Keep brand name, site purpose, and official social profiles consistent.

## Final Homepage Signoff

Mark homepage ready only when:

- Homepage returns `200 OK`.
- Canonical, robots, sitemap, and schema are correct.
- No homepage CTA or internal link points to unnecessary 404/410 pages.
- Every visible section has useful crawlable content.
- Dynamic data is database-backed.
- Mobile rendering is complete and does not hide key content.
- PageSpeed/Lighthouse issues are reviewed and prioritized.
- Structured data validates.
- Related links point only to live, useful canonical pages.

## Developer Guardrail

Keep fixes limited to homepage content, homepage-linked URL cleanup, page-level metadata, structured data, sitemap eligibility, canonical/indexability, internal links, accessibility, and performance. Do not change navbar, footer, header, logo, global menu, global styles, analytics, tracking, or unrelated routes unless the issue is directly caused by those shared components and regression testing is completed.

---

## Universal Developer Guardrail

Apply this rule before using this file for implementation:

1. Audit the existing homepage/component first.
2. Do not delete existing sections, components, internal links, SEO copy, metadata, schema, job data, or URLs without explicit approval.
3. Preserve approved Sections `01-10`; patch only verified issues.
4. If this section already exists in code, improve the existing component instead of rebuilding it unnecessarily.
5. Never invent vacancies, dates, salary, eligibility, age limits, selection process, official links, job counts, subscriber counts, exam dates, or government approval.
6. Verify every internal URL and official external URL before publishing.
7. Remove or replace links to true `404`/`410` pages; keep those URLs out of sitemap, schema, breadcrumbs, related links, and internal-link hubs.
8. Use one-hop `301` only when there is a close relevant replacement.
9. Do not create thin doorway pages, duplicate SEO pages, keyword-stuffed sections, or fake urgency.
10. Do not change navbar, footer, header, logo, global menu, global styles, analytics, tracking, or unrelated routes unless a documented bug requires it and regression QA is completed.
11. SearchSarkariNaukri must be described as an independent information portal, not an official government website.
12. Final signoff requires audit, implementation, live URL/status checks, sitemap/canonical/robots/schema validation, mobile QA, accessibility QA, and performance QA.
