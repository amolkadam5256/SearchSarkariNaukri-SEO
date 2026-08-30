# Google Search Console Error - Master Audit And Developer Handoff

Date: 2026-08-29
Site: `https://www.searchsarkarinaukri.com/`
Root folder: `01_Google_Search_Console_Error`

## Executive Summary

This root folder contains six Google Search Console indexing issue packages. The developer should fix them as separate issue types, not as one bulk indexing job. The common pattern across the folder is weak URL governance: broken job URLs, soft-404 thin landing pages, noindex/canonical mismatches, redirect errors, sitemap gaps, and many admit-card pages that need record-specific content before indexing.

No implementation should change unrelated pages, footer, navbar, header, global layout, global styling, tracking, analytics, or shared components unless strictly required for the specific GSC indexing fix.


## Final All-Pages Audit Checklist

Before any implementation, read `..\00_FINAL_ALL_PAGES_SEO_AEO_GEO_TECHNICAL_AUDIT_CHECKLIST.md`. This is the cross-project audit guardrail for crawlability, indexability, content quality, AEO/GEO, page speed, and non-duplicate FAQs.

## Latest Page Indexing Dashboard

Read `00_PAGE_INDEXING_OVERVIEW_2026-08-29.md` first for the latest 9-row GSC Page Indexing summary and page counts. It confirms 1,785 known affected non-indexed pages, plus 0 server-error pages.

## Folder Health Check

| Issue Folder | Files | Markdown | CSV | XLSX | TXT | Missing Guardrail |
|---|---:|---:|---:|---:|---:|---:|
| `01_Not found (404)` | 12 | 10 | 1 | 1 | 0 | 0 |
| `02_Soft 404` | 89 | 88 | 0 | 1 | 0 | 0 |
| `03_Excluded by ‘noindex’ tag` | 64 | 62 | 1 | 1 | 0 | 0 |
| `04_Redirect error` | 7 | 6 | 0 | 0 | 1 | 0 |
| `05_Alternative page with proper canonical tag` | 6 | 5 | 0 | 0 | 1 | 0 |
| `06_Discovered – currently not indexed` | 1041 | 1033 | 5 | 1 | 2 | 0 |
| `07_Crawled - currently not indexed` | 33 | 27 | 1 | 1 | 4 | 0 |
| `08_Duplicate_Google_chose_different_canonical` | 6 | 6 | 0 | 0 | 0 | 0 |

## Priority Order For Developer

| Priority | Folder | Main Problem | Exact Fix Direction |
|---|---|---|---|
| P0 | `01_Not found (404)` | 613 URLs reported as not found, mostly job numeric IDs and job slug variants | Verify every job ID in DB/CMS, restore valid records, redirect exact replacements, keep real removed URLs as 404/410, remove invalid URLs from sitemap/internal links |
| P0 | `04_Redirect error` | Query URL `/jobs?district_slug=pune` fails as redirect error | Create one clean server-side redirect to `/districts/pune`, remove chains/loops, ensure target 200/self-canonical/indexable |
| P1 | `02_Soft 404` | Valid landing pages look empty/thin when 0 active jobs are available | Keep valid pages as 200 but add useful crawlable content, recent/expired jobs, related links, FAQs, and correct sitemap/canonical logic |
| P1 | `03_Excluded by noindex tag` | Useful pages may be excluded by noindex, or intentionally excluded pages need cleanup | Decide page-by-page: remove noindex only for useful indexable pages; keep noindex for thin/duplicate/private/invalid pages; align sitemap/canonical |
| P1 | `08_Duplicate_Google_chose_different_canonical` | Google selected a different canonical for `/jobs/1689` | Pick one final canonical URL, redirect/canonicalize duplicates, align sitemap/internal links/schema |
| P2 | `05_Alternative page with proper canonical tag` | `/jobs/862` is treated as an alternate canonical page | Decide whether numeric URL should redirect to final job canonical or be self-canonical if it is the preferred URL |

## Exact Issue-By-Issue Instructions

### 01_Not found (404)

Use this for job URLs returning true 404. The audit says there are 613 affected URLs. Do not redirect all of them to the homepage. For each URL, check the real database/CMS record.

Developer must do:

1. Check whether the job ID exists.
2. If the job is valid and published, restore the page to `200 OK`.
3. If the job is expired but useful, show the full job page with an expired/deadline-passed notice, not `Job not found`.
4. If an exact replacement canonical URL exists, add a direct `301/308` redirect.
5. If the job was permanently removed and has no replacement, return `410` or intentional `404`.
6. Remove all 404/410/redirect/noindex URLs from sitemap.
7. Update internal links so they do not point to broken URLs.

### 02_Soft 404

Use this for valid pages that return 200 but look empty to Google. Examples include qualification/location landing pages with `0 Active Jobs` and very thin text.

Developer must do:

1. Keep legitimate landing pages as `200 OK`.
2. Add unique crawlable HTML content for the specific qualification/location/topic.
3. Show active jobs when available.
4. Show recent/expired/historical recruitment links where useful.
5. Add related jobs, categories, locations, qualifications, and FAQs.
6. Make FAQ answers non-empty and specific.
7. Keep canonical self-referencing for valid landing pages.
8. Include in sitemap only if useful, indexable, and self-canonical.

### 03_Excluded By Noindex Tag

Use this for pages blocked by `noindex`. The correct fix is not always removing noindex.

Developer must do:

1. Identify whether each URL should be indexable.
2. If useful and unique, remove `noindex`, set `index,follow`, self-canonical, and include in sitemap.
3. If duplicate/thin/private/filter/search-result style, keep `noindex` and remove from sitemap.
4. Ensure internal links point to the indexable canonical URL where one exists.

### 04_Redirect Error

Use this for `https://www.searchsarkarinaukri.com/jobs?district_slug=pune`.

Developer must do:

1. Redirect source URL directly to `https://www.searchsarkarinaukri.com/districts/pune`.
2. Use one server-side `301` or `308`.
3. Avoid redirect chains, loops, mixed HTTP/HTTPS, or `/district/pune` typo.
4. Make the destination return `200 OK`, self-canonical, indexable, and sitemap-eligible.
5. Do not index the query URL.

### 05_Alternative Page With Proper Canonical Tag

Use this for `https://www.searchsarkarinaukri.com/jobs/862`.

Developer must do:

1. Check the job 862 source record.
2. If `/jobs/862` is not the preferred URL, redirect it to the exact canonical job URL.
3. If it is the preferred URL, make it self-canonical and indexable.
4. Do not canonicalize a useful unique job to an unrelated hub page.
5. Sitemap should contain only the final canonical URL.

### 06_Discovered - currently not indexed

Use this for 896 admit-card URLs. This is the largest package and has the strongest developer handoff.

Developer must do:

1. Read `00_START_HERE_FOR_DEVELOPER.md` first.
2. Use `00_Master_Index/06_EXACT_DEVELOPER_ACTION_CHECKLIST.md` as the implementation checklist.
3. Use `00_Master_Index/02_896-url-decision-and-migration-map.csv` as the 896-row tracker.
4. Join every URL to live admit-card database/API records.
5. Do not blindly add all 896 numeric URLs to sitemap.
6. Improve only valuable pages with full record-specific content.
7. Add 10-15 specific FAQs per indexable page.
8. Use semantic canonical URLs where safe.
9. Redirect old numeric URLs only after slug collision checks.
10. Add only final canonical 200/indexable/self-canonical pages to sitemap.


### 07_Crawled - Currently Not Indexed

Use this for URLs Google has crawled but not selected for indexing. The supplied live HTML evidence shows at least one strong technical blocker: a useful job page outputting `noindex, follow`.

Developer must do:

3. Check each URL for HTTP status, robots meta, X-Robots-Tag, canonical, sitemap presence, content depth, structured data, and internal links.
4. Remove accidental noindex only from useful pages that should rank.
5. Improve thin pages before requesting indexing.
6. Canonicalize or redirect duplicate variants.
7. Exclude noindex, redirected, duplicate, thin, 404/410, and canonicalized-away URLs from sitemap.
8. Run the two-round QA checklist before GSC validation.
### 08_Duplicate Google Chose Different Canonical

Use this for `https://www.searchsarkarinaukri.com/jobs/1689`.

Developer must check the DB/CMS record for job ID `1689`, choose one final canonical URL, then align redirect, canonical tag, sitemap, internal links, BreadcrumbList, JobPosting URL, OG URL, and Twitter URL. If `/jobs/1689` is only an old numeric duplicate, redirect it directly to the exact canonical slug URL and remove the numeric URL from sitemap/internal links.
## Cross-Issue Technical Rules

- A URL in sitemap must be `200 OK`, indexable, self-canonical, useful, and not redirected.
- A noindex URL must not be in sitemap.
- A redirected URL must not be in sitemap.
- A 404/410 URL must not be in sitemap.
- Canonical tags, OG URLs, Twitter URLs, BreadcrumbList URLs, structured data URLs, internal links, and sitemap URLs must agree.
- Expired jobs should not automatically become 404 pages if useful content still exists.
- Thin pages should be improved before requesting indexing.
- Do not generate duplicate boilerplate FAQs across hundreds of pages.
- Do not redirect unrelated URLs to broad hub pages just to reduce GSC counts.


## Two-Round Audit And Fix Workflow

Before requesting Google Search Console validation, use these files:

1. `01_ROUND_1_AUDIT_CHECKLIST.md` - first complete audit after implementation.
2. `02_ROUND_1_FIX_TRACKER.md` - record and fix all first-audit failures.
3. `03_ROUND_2_RE_AUDIT_CHECKLIST.md` - second audit after fixes.
4. `04_ROUND_2_FINAL_FIX_AND_SIGNOFF.md` - final remaining fixes and signoff.

Rule: audit first, fix failures, audit again, fix remaining failures, then request GSC validation only if checks pass.
## Final QA Before GSC Validation

1. Crawl all fixed URL sets.
2. Export HTTP status, canonical, robots meta, sitemap presence, title, H1, word count, structured data, and redirect target.
3. Confirm no sitemap contains 404, 410, noindex, canonicalized-away, or redirected URLs.
4. Confirm redirect maps have no chains or loops.
5. Confirm internal links do not point to removed URLs.
6. Validate XML sitemaps.
7. Inspect representative URLs in Google Search Console.
8. Request validation only after live tests pass.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix a specific Google Search Console indexing issue. Keep changes limited to routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, redirects, and QA for the affected URL sets.















