# Re-Audit Live-Test Findings and Developer Fixes

## Re-Audit Date

29 August 2026

## Scope

This update is based on the latest pasted live-page extraction and Google/Search crawl evidence for valid SEO landing pages that risk or trigger Soft 404 classification.

Primary affected URL examples:

- `https://www.searchsarkarinaukri.com/10th-pass-jobs-in-kolkata`
- `https://www.searchsarkarinaukri.com/graduate-jobs-in-gurgaon`
- `https://www.searchsarkarinaukri.com/iti-jobs-in-west-bengal`

Related crawl-risk example:

- `https://www.searchsarkarinaukri.com/category/defence-jobs`

## Confirmed Live-Page Pattern

The pasted live extraction shows these pages render a full page shell and a valid SEO heading, but the main result area is thin when no active jobs are available.

Observed pattern:

- URL loads as a page, not a hard 404.
- Breadcrumb is present.
- H1 is present and matches query intent.
- Page says `0 Active Jobs`.
- Page says `No active jobs right now. Check back soon`.
- Related job/category links are present.
- FAQ questions are present, but some answers appear missing or empty.
- No referring sitemap was reported in GSC for inspected Soft 404 examples.

## Problem

Google can classify these pages as Soft 404 because the main content looks like an empty results page:

```text
Valid landing URL
-> 200 response
-> H1 and template load
-> 0 Active Jobs
-> No active jobs right now
-> limited unique helpful content
-> incomplete FAQ answers
-> possible missing sitemap discovery
-> Soft 404 risk
```

This is not fixed by changing the URL, deleting the page, or adding fake jobs.

## Required Developer Changes

### 1. Keep Valid SEO Landing Pages as 200

Valid qualification/location pages should return `200` when they represent real search demand and a real taxonomy page, even when active jobs are currently zero.

Do not return `404` merely because no active job currently matches.

### 2. Add Useful Zero-Result Content

When active jobs count is zero, the page must still provide useful crawlable content:

- explanation of the qualification/location job category
- recent expired or historical jobs for the same qualification/location/state
- related current jobs with close topical relevance
- related location pages
- related qualification pages
- related exams or recruiter categories
- last updated date
- complete FAQ answers

### 3. Add Recent/Expired Job Section

For pages such as `10th Pass Government Jobs in Kolkata`, show a crawlable section like:

`Recent and Closed 10th Pass Government Jobs in Kolkata / West Bengal`

Rules:

- Use real expired jobs only.
- Label each as `Closed` or `Expired`.
- Keep original closing date.
- Link only to useful job pages that return `200`.
- Do not present expired jobs as active vacancies.

### 4. Fix Empty FAQ Answers

The pasted extraction shows FAQ questions where answers are missing or not visible, for example:

- `How many 10th Pass (SSC / Matric) jobs are there in Kolkata?`
- `Can I apply from outside Kolkata?`

Every FAQ question must have a direct, useful answer in crawlable HTML.

### 5. Make Job Data Crawlable Without Client Failure

Search crawl evidence for a category page shows:

`Could not load jobs. Please check your connection.`

This is a Soft 404/thin-content risk if Googlebot receives the fallback instead of job data.

Developer must ensure:

- critical job lists are server-rendered or pre-rendered
- API failure fallback still shows useful static links/content
- no indexable page depends only on client-side fetch for its primary content
- crawler-visible HTML contains enough unique page-specific content

### 6. Sitemap Policy

Include these pages in sitemap only after they are:

- `200`
- canonical
- indexable
- useful when active jobs are zero
- not blocked by robots
- not `noindex`

Remove from sitemap if:

- page is intentionally `noindex`
- page is duplicate/thin and not intended for indexing
- page redirects
- page returns `404` or `410`

### 7. Canonical Policy

Each valid page should self-canonicalize:

- `/10th-pass-jobs-in-kolkata`
- `/graduate-jobs-in-gurgaon`
- `/iti-jobs-in-west-bengal`

Do not canonicalize to `/jobs` only because active jobs are zero.

## Retest Requirements

After developer fixes:

1. Run live URL inspection in GSC for each example URL.
2. Confirm page fetch succeeds.
3. Confirm indexing is allowed.
4. Confirm user-declared canonical is self.
5. Confirm sitemap discovery is present if page is intended indexable.
6. Confirm visible/crawlable content is no longer just `0 Active Jobs`.
7. Confirm all FAQ questions have answers.
8. Confirm related jobs are relevant.
9. Confirm no `Could not load jobs` fallback appears in crawler-visible output for indexable category pages.

## Current Status

`PENDING DEVELOPER IMPLEMENTATION AND GSC RETEST`

No production code or sitemap was changed from this audit workspace.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
