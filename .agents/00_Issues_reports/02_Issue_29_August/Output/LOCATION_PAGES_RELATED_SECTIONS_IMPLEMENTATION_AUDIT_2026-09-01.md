# Location Pages Related Sections Implementation Audit

Date: 2026-09-01
Site: `https://www.searchsarkarinaukri.com/`
Audited source folder: `.agents/00_Issues_reports/02_Issue_29_August`
Primary scope: location landing pages, qualification + location landing pages, and district/category pages.

## Final Verdict

Status: `IMPLEMENTATION BRIEF ADDED / LIVE IMPLEMENTATION NOT PROVABLE`

The issue package already contains many per-page briefs for location-style pages, especially in:

- `01_Google_Search_Console_Error/02_Soft 404/06_81_Unique_Page_Content_Sitemap_Briefs/`
- `01_Google_Search_Console_Error/07_Crawled - currently not indexed/`
- `02_Bing_Webmaster_Site_Scan/01_ERROR_Http_400_499_errors/`
- `02_Bing_Webmaster_Site_Scan/02_WARNING_Title_too_long/`

However, this workspace still does not include the actual website application source code, so this audit cannot confirm that the related sections are live on production pages. This file adds the missing detailed implementation standard that developers must apply to every valid indexable location page.

## Pages In Scope

Apply this standard to every public, useful, canonical page matching these patterns:

- `/jobs-in-{location}`
- `/{qualification}-jobs-in-{location}`
- `/{category}-jobs-in-{location}`
- `/districts/{district}`
- `/districts/{district}/{department-or-category}`
- Any state, city, district, qualification-location, category-location, or department-location landing page intended to rank.

Do not apply this to:

- 404 or 410 pages
- redirect source URLs
- duplicate/canonicalized-away pages
- thin pages intentionally kept `noindex`
- private/admin/backend URLs
- parameter/filter URLs unless they are converted into clean canonical landing pages

## Minimum Requirement

Every valid indexable location page must include at least `10` substantial content sections.

Target range: `10-20` sections.

Recommended full implementation: `20` sections for major state/city/district pages and high-value qualification-location pages.

If the page has zero active jobs, it must not look empty. It should still include useful crawlable sections, recent/expired jobs where available, related location links, qualification/category links, department links, FAQs, and official-source guidance. If useful content cannot be created honestly, keep the page `noindex` and exclude it from sitemap.

## Required 20-Section Location Page Template

Use these sections in this order where possible. If a section has no real data, show a truthful fallback or omit only when the page remains above the 10-section minimum.

1. `Hero / Direct Answer`
   State exactly what the page covers, for example `Government Jobs in Pune 2026` or `10th Pass Government Jobs in Ahmedabad 2026`.

2. `Active Job Summary`
   Show active job count, last updated date, and whether applications are open.

3. `Latest Active Jobs`
   List current jobs first. Each item should include post name, department, location, qualification, vacancies if known, last date, status, and link.

4. `Recent Closed Jobs`
   Include expired/closed recruitments for context. Mark them clearly as closed.

5. `Departments Hiring In This Location`
   Link to real department pages only, such as police, railway, health, education, SSC, PSC, banking, defence, municipal, or postal where relevant.

6. `Popular Qualifications In This Location`
   Link to real qualification-location pages such as 10th pass, 12th pass, ITI, diploma, graduate, engineer, medical/MBBS.

7. `Popular Categories In This Location`
   Link to category intent pages such as apprentice, railway, police, teaching, health, defence, banking, central government, state government.

8. `Nearby Locations`
   Link to nearby city/district/state pages that actually exist. Do not generate dead links.

9. `State-Level Jobs`
   Connect city/district pages to the broader state page where relevant.

10. `All-India / Central Government Jobs`
   Include central recruitment alternatives when local openings are low.

11. `Eligibility Guide`
   Explain education, age limit, category relaxation, domicile/location rules, experience, and document checks without inventing values.

12. `Application Process`
   Explain how users should verify notification, check dates, read eligibility, prepare documents, apply, save acknowledgement, and track updates.

13. `Important Documents`
   List common documents: ID proof, education certificates, caste/category certificate where applicable, domicile, photo, signature, experience certificate, medical certificate where applicable.

14. `Selection Process Patterns`
   Explain common selection stages for the location/category: written exam, skill test, physical test, interview, document verification, medical exam, merit list.

15. `Salary / Pay Level Guidance`
   Give non-fabricated pay guidance. If salary is unavailable, say it must be verified in the official notification.

16. `Official Source Verification`
   Tell users to confirm all dates, fees, eligibility, and links on official authority websites.

17. `Related Jobs`
   Add a dedicated related jobs section using the rules below.

18. `Related Pages / Resources`
   Link to relevant admit cards, results, exam calendar, job alerts, syllabus/study material, and original notifications only where they exist.

19. `FAQ`
   Add 10-15 page-specific FAQs. Questions must mention the actual location and/or qualification/category where useful.

20. `Last Updated / Editorial Note`
   Show last updated/reviewed date and a short verification note.

## Dedicated Related Section Rules

Every valid indexable location page must have a related section with at least `10` useful links/items when enough real pages or jobs exist.

Minimum related section target:

- `3-5` closely related jobs
- `2-4` nearby location pages
- `2-4` qualification/category pages
- `1-3` department pages
- `1-2` admit card/result/exam-calendar/job-alert resources

Do not show random links. Related items must be selected using:

1. same location + same qualification/category
2. same location + similar qualification/category
3. nearby location + same qualification/category
4. same state + same category/department
5. same department/authority in nearby locations
6. active jobs first, then recently closed jobs

## Related Section Layout

Use one clear page section, for example:

`Related Government Jobs And Resources In {Location}`

Recommended subsections:

- `Related active jobs`
- `Nearby locations`
- `Qualification wise jobs`
- `Department wise jobs`
- `Admit cards, results and alerts`

Each link item should have:

- visible title
- short context line
- status where relevant: active, closed, result, admit card, guide
- destination URL

## Location Page Indexing Decision

Use this decision rule after adding sections:

- `INDEX`: page has 10+ useful sections, real related links, unique metadata, self-canonical, `index, follow`, 200 OK, and sitemap inclusion.
- `IMPROVE_FIRST`: page has valid intent but fewer than 10 useful sections or weak related links.
- `NOINDEX`: page is thin, duplicate, or has no honest useful content yet.
- `REDIRECT`: page is a duplicate or zero-match page with a better canonical destination.
- `404/410`: location/entity is invalid or removed and has no replacement.

## Metadata Requirements

Every indexable location page must have:

- unique title under 70 characters where possible
- unique meta description
- one visible H1
- self-canonical URL
- `index, follow` or equivalent non-blocking robots behavior
- Open Graph URL matching canonical
- breadcrumb structured data
- page-type structured data where appropriate
- sitemap inclusion only if indexable and canonical

## Quality Checks Before Signoff

For each location page, verify:

1. HTTP status is correct.
2. No redirect chain or loop.
3. Canonical matches final URL.
4. Robots does not block indexable pages.
5. Sitemap does not include noindex, redirected, duplicate, 404, or 410 URLs.
6. Page has at least 10 useful sections.
7. Major pages have 15-20 useful sections.
8. Related section has real, relevant links.
9. No dead related links are generated.
10. FAQ is specific to the location/page.
11. Content is crawlable/rendered HTML.
12. Schema matches visible page content.
13. Internal links point to canonical URLs.
14. Empty-state text is useful and not soft-404-like.
15. Title and H1 match search intent.

## Audit Finding

The existing report package is strong on identifying location-page content needs, but this exact requirement was not centralized before:

`Every location page must include a related section and at least 10-20 useful content sections.`

This file now adds that central standard for developer implementation and future QA.

## Developer Scope Guardrail

Implement only page-level location content, page-level metadata, contextual related links, schema, canonical/indexability, sitemap eligibility, and internal links needed for location-page SEO. Do not change navbar, footer, header, global layout, global styles, analytics, tracking, logo, menu, or unrelated routes unless strictly required and separately tested.
