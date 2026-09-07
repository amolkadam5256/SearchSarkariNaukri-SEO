# Developer Execution Runbook - Full SEO Fix

Use this runbook to execute `06_PRODUCTION_SITE_SEO_UPGRADE_DEVELOPER_PROMPT.md` on the project.

## Step 1 - Read Required Instructions

Read these files before coding:

1. `.agents/04_Technical_SEO/00_SEMRUSH_TECHNICAL_SEO_MASTER_AUDIT.md`
2. `.agents/04_Technical_SEO/01_PRIORITY_FIX_PLAN.md`
3. `.agents/04_Technical_SEO/02_DUPLICATE_METADATA_AND_CONTENT_FIXES.md`
4. `.agents/04_Technical_SEO/03_CRAWL_INDEX_SITEMAP_ROBOTS_FIXES.md`
5. `.agents/04_Technical_SEO/04_PERFORMANCE_GEO_SECURITY_AND_EXTERNAL_FIXES.md`
6. `.agents/04_Technical_SEO/05_FINAL_TECHNICAL_SEO_QA_CHECKLIST.md`
7. `.agents/04_Technical_SEO/06_PRODUCTION_SITE_SEO_UPGRADE_DEVELOPER_PROMPT.md`
8. `.agents/07_OnPage_SEO/04_Jobs_Page/00_MASTER_PROMPT_JOBS_PAGE_UPGRADE.md`

For `/jobs`, do not change header/navbar/main navigation/footer.

## Step 2 - Create Inventory

Create an internal inventory before edits:

- Routes/pages
- Page types
- Important URLs
- Existing metadata
- Canonicals
- Sitemap generation
- robots.txt generation
- Structured data
- Job data fields
- Taxonomy fields
- Search/filter behavior
- Pagination behavior
- Existing internal-link sources

Required output:

- List affected files/components.
- List current SEO implementation points.
- List missing data needed from Semrush export.

## Step 3 - Fix P0 Errors First

Fix in this order:

1. Duplicate canonical tags
2. Duplicate title tags
3. Duplicate meta descriptions
4. Duplicate content groups
5. Uncrawlable page
6. Sitemap/robots consistency

Do not move to content expansion until these are understood.

## Step 4 - Implement Metadata Generator

Create or update reusable metadata helpers for:

- Homepage
- Jobs page
- Job detail page
- State page
- District page
- City page
- Qualification page
- Category/department page
- Organization page
- Exam page
- Result page
- Admit card page
- Answer key page
- Syllabus page
- Blog/article page

Rules:

- Unique title per indexable page
- Unique meta description per indexable page
- Exactly one canonical per indexable page
- OG/Twitter tags use canonical URL
- No duplicate injections from layout and page component

## Step 5 - Fix Duplicate Content

For every duplicate group, decide:

- Unique content
- Canonical
- 301 redirect
- Noindex
- Merge/consolidate
- Pagination strategy
- Parameter strategy

Document the decision.

Do not delete pages without redirect/canonical/noindex reasoning.

## Step 6 - Fix Sitemap And Robots

Ensure:

- `/sitemap.xml` works
- robots.txt works
- robots.txt includes canonical sitemap URL
- Sitemap includes canonical indexable URLs only
- Sitemap excludes noindex/private/duplicate/parameter URLs
- Jobs and taxonomy pages update automatically

## Step 7 - Improve Low-Word And Content Optimization Pages

For the 19 low-word-count pages:

- Add meaningful, page-specific content if page is important.
- Noindex/merge/canonicalize if page is thin and not worth indexing.
- Avoid generic filler.

For the 2 content optimization pages:

- Improve headings, intro, entity clarity, internal links, FAQs, and metadata.
- Keep content concise and user-useful.

## Step 8 - Strengthen Internal Linking

For 11 pages with only one incoming link:

- Add contextual links from relevant pages.
- Use descriptive anchors.
- Avoid footer stuffing.
- Add related-job and related-taxonomy links where appropriate.

## Step 9 - Improve Jobs And Taxonomy Architecture

Implement data-driven links between:

- Job -> state
- Job -> district
- Job -> city
- Job -> qualification
- Job -> department/category
- Job -> organization
- Job -> exam
- Job -> post/designation
- Job -> job type
- Job -> related jobs

All links must point to real existing or properly generated valid pages.

## Step 10 - Performance, GEO, Security

Performance:

- Reduce duplicate scripts.
- Defer non-critical scripts.
- Server-render important content where possible.
- Lazy-load below-fold widgets.
- Avoid loading all jobs client-side.
- Optimize images.

GEO:

- Ensure important content and internal links exist in initial HTML where possible.
- Validate `llms.txt`.

Security/DNS:

- Investigate HSTS subdomain issue.
- Add SPF only after confirming mail provider.
- Keep DMARC valid.

## Step 11 - Local Verification

Run available project checks:

- Build
- Typecheck
- Lint
- Unit tests, if present
- Route smoke tests, if available
- Sitemap generation check
- Metadata/canonical smoke check

If a check cannot be run, document why.

## Step 12 - Production Verification

After deployment:

- Run Semrush Site Audit.
- Run SEOptimer again.
- Check Google Search Console:
  - Sitemaps
  - Page indexing
  - URL inspection
  - Mobile usability
  - Core Web Vitals
  - Structured data
  - Breadcrumbs
  - JobPosting where applicable

Document before/after:

- Duplicate title issues
- Duplicate meta issues
- Duplicate content issues
- Crawl failures
- Low word-count pages
- Low text-to-HTML pages
- Sitemap status
- Nofollow review
- One-incoming-link pages
- Content optimization pages
- HSTS issue

## Done Definition

The work is done only when:

- Core Semrush errors are fixed or documented with exact reason.
- No new SEO errors are created.
- Existing data and URLs are preserved.
- Metadata and canonicals are unique and correct.
- Sitemap/robots are valid.
- Important pages are crawlable and internally linked.
- `/jobs` and job detail pages are stronger but still data-driven.
- No fake data or thin pages are introduced.
