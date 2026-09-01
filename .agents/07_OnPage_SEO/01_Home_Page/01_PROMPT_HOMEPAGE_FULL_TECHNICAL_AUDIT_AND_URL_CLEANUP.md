# Prompt 1 - Homepage Full Technical Audit And URL Cleanup

Use this prompt with a developer or AI coding agent before making homepage changes.

## Prompt

You are auditing the SearchSarkariNaukri homepage and every URL linked from the homepage.

Workspace folder:

`C:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\07_OnPage_SEO\01_Home_Page`

Primary page:

`https://www.searchsarkarinaukri.com/`

Read all homepage section specification files in this folder before auditing:

- `01_Hero/herosection.md`
- `02_LIVE_STATISTICS/homepage-live-statistics-db.md`
- `03_DAILY_ASSESSMENT/daily-assessment-section.md`
- `04_DIGITAL_LIBRARY/digital-library-section.md`
- `05_JOB_ALERTS/government-job-alerts-section.md`
- `06_EXAM_COUNTDOWN/exam-countdown-section.md`
- `07_CLOSING_SOON_JOBS/closing-soon-jobs-section.md`
- `08_EXISTING_TALATHI_FEATURED_RECRUITMENT/talathi-bharti-featured-section.md`
- `09_QUICK_JOB_FINDER/quick-job-finder-section.md`
- `10_LATEST_SARKARI_NAUKRI/latest-sarkari-naukri-section.md`

Run a complete technical SEO audit using these areas:

1. Crawlability and indexing
2. Robots.txt and robots meta
3. XML sitemap eligibility
4. Canonical tags
5. HTTP status codes
6. Redirect chains and redirect loops
7. 404/410 handling
8. URL casing, trailing slash, and parameter cleanup
9. Internal linking and crawl depth
10. Homepage CTA destination checks
11. Structured data validation
12. Page speed and Core Web Vitals
13. Image sizing and alt text
14. Mobile rendering and content parity
15. Accessibility and focus states
16. AEO/GEO direct-answer readiness
17. FAQ visibility and schema matching
18. Dynamic data correctness
19. Related links relevance
20. Off-page/authority follow-up opportunities

For every homepage-linked URL, assign one decision:

- `KEEP_INDEXABLE`
- `RESTORE_200`
- `REDIRECT_301`
- `REMOVE_LINK`
- `REMOVE_FROM_SITEMAP`
- `NOINDEX`
- `404`
- `410`
- `MANUAL_REVIEW`

Rules:

- If a page/URL returns 404 and is not needed, remove it from homepage links, sitemap, schema, breadcrumbs, related links, and any generated internal-link block.
- If a page/URL returns 404 but has a close replacement, create one direct 301 redirect to the closest relevant live page.
- If a page/URL is valid but accidentally 404, restore it as 200 OK with useful crawlable content.
- If a page/URL is intentionally gone and has no replacement, return 410 and remove it from sitemap and internal links.
- Do not redirect unrelated old URLs to the homepage.
- Do not index thin, duplicate, private, admin, backend, test, or parameter-only pages.
- Do not add noindex pages, redirected pages, duplicate pages, 404 pages, or 410 pages to sitemap.

Create an audit report with:

1. Executive summary
2. List of all homepage sections found
3. List of all homepage-linked URLs
4. Status/canonical/robots/sitemap result for each URL
5. 404/410 URL cleanup table
6. Redirect recommendations
7. Sitemap cleanup recommendations
8. Structured data issues
9. Mobile/accessibility issues
10. Page speed issues
11. AEO/GEO content gaps
12. Final action table

Do not modify unrelated pages, navbar, footer, header, logo, global menu, analytics, tracking, global layout, or global CSS unless the audit proves the issue is caused by a shared component.

Return exact file paths and exact line references for every code change recommendation.

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
