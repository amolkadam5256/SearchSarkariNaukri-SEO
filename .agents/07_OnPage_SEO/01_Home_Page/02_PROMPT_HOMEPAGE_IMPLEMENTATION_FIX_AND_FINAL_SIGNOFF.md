# Prompt 2 - Homepage Implementation Fix And Final Signoff

Use this prompt after the technical audit is complete.

## Prompt

You are implementing and validating fixes for the SearchSarkariNaukri homepage and its homepage-linked URLs.

Primary goal:

Fix technical SEO, on-page SEO, AEO, GEO, accessibility, performance, and broken URL problems without changing unrelated site areas.

Required source guidance:

- Read `00_HOMEPAGE_TECHNICAL_SEO_AEO_GEO_AUDIT_2026-09-01.md`.
- Read every section brief under `.agents/07_OnPage_SEO/01_Home_Page`.
- Preserve approved copy and section intent unless the audit requires a correction.

## Implementation Tasks

1. Homepage status and metadata
   - Ensure homepage returns `200 OK`.
   - Ensure canonical is `https://www.searchsarkarinaukri.com/`.
   - Ensure homepage is indexable.
   - Ensure title and meta description match `Sarkari Naukri 2026` and latest government job intent.

2. Homepage sections
   - Implement or verify all documented homepage sections.
   - Keep section order logical.
   - Use crawlable HTML for important text.
   - Do not put SEO copy inside images.
   - Use semantic headings.

3. Dynamic data
   - Pull active jobs, organizations, closing soon jobs, and Maharashtra district count from the database.
   - Do not hard-code old numbers.
   - Cache expensive queries.
   - Show truthful empty states.

4. Latest jobs and related links
   - Render only live, canonical, useful job URLs.
   - Remove links to deleted, private, draft, duplicate, noindex, 404, or 410 pages.
   - Add related links only when the destination exists and is relevant.

5. 404 and removed page handling
   - For true missing pages with no replacement, return real `404` or `410`.
   - Remove those URLs from homepage links, sitemap, schema, breadcrumbs, related jobs, and internal-link blocks.
   - For valid pages accidentally returning 404, restore `200 OK`.
   - For obsolete pages with a close replacement, create one-hop `301` redirects.
   - Never redirect unrelated URLs to the homepage just to reduce errors.

6. Sitemap and robots
   - Include only canonical, indexable, 200 OK URLs.
   - Exclude 404, 410, redirected, noindex, duplicate, private, and thin pages.
   - Confirm `robots.txt` allows important public pages and lists the sitemap.

7. Structured data
   - Add or verify Organization schema.
   - Add or verify WebSite schema with SearchAction if search exists.
   - Add ItemList schema only for visible live job listings.
   - Ensure schema URLs match canonical URLs.
   - Remove schema entries for dead or hidden content.

8. Accessibility and mobile
   - Ensure search, CTAs, buttons, filters, chips, and cards are keyboard accessible.
   - Add accessible labels where needed.
   - Ensure no horizontal overflow on mobile.
   - Keep mobile and desktop content equivalent.
   - Ensure focus states are visible.

9. Performance
   - Optimize hero/background images.
   - Use correct image dimensions or aspect ratios.
   - Prevent layout shifts from counters, cards, ads, and lazy content.
   - Defer non-critical scripts.
   - Keep important homepage text visible quickly on mobile.

10. AEO/GEO readiness
   - Add a direct answer near the top explaining what the site provides.
   - Use factual tables or compact summaries for counts and latest updates.
   - Add official-source verification note.
   - Link to focused pages for jobs, districts, qualifications, departments, results, admit cards, alerts, and exam calendar.
   - Add useful FAQs with visible matching text if FAQ schema is used.

## Final Validation

Run or produce evidence for:

1. Homepage HTTP status
2. Homepage canonical
3. Homepage robots meta
4. Homepage sitemap inclusion
5. Homepage schema validation
6. Homepage mobile screenshot
7. Homepage desktop screenshot
8. Lighthouse/PageSpeed result
9. List of homepage-linked URLs checked
10. List of removed 404/410 links
11. List of redirects added
12. List of noindex pages excluded from sitemap

## Final Report Format

Return:

1. Files changed
2. URLs changed
3. URLs removed because 404/no longer needed
4. URLs redirected with destination
5. URLs restored to 200
6. Sitemap changes
7. Schema changes
8. Performance/accessibility changes
9. Tests run
10. Remaining risks

## Guardrail

Do not change navbar, footer, header, logo, global menu, global layout, global styles, analytics, tracking, unrelated routes, unrelated database logic, or unrelated templates unless the audit proves the homepage issue cannot be fixed otherwise. If a shared file must change, regression-test job detail, district, qualification, department, admit card, result, sitemap, robots, and 404 behavior.

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
