# Complete Canonical Audit and Developer Fix Specification

## 1. GSC Issue Summary

Google Search Console reports one URL under `Alternative page with proper canonical tag`:

- URL: `https://www.searchsarkarinaukri.com/jobs/862`
- Last crawled: 18 May 2026
- Affected pages: 1
- Validation started: 08 June 2026
- Last update shown: 21 August 2026

Google currently treats `/jobs/862` as an alternate URL and has selected another canonical. This may be correct if `/jobs/862` is a duplicate, but it may be wrong if the page is a unique job detail page.

## 2. First Required Inspection

Open and inspect final rendered HTML for `https://www.searchsarkarinaukri.com/jobs/862`.

Record HTTP status, final URL, canonical tag, canonical target status, canonical target indexability, robots meta, X-Robots-Tag, H1, JobPosting schema, Breadcrumb schema, sitemap inclusion, and internal links.

Do not change code until this evidence is known.

## 3. Determine Job Record Status

Find the job record for ID `862` in the production data/source of truth. Record job ID, canonical slug/URL, job title, organization, category, district/location/state, qualification, vacancy count, application dates, official notification URL, official application URL, and active/expired/deleted/archive status.

## 4. Correct Canonical Decision Tree

### Case A: `/jobs/862` is a unique active job URL

Expected final state: HTTP 200, self-canonical, indexable, in job sitemap if intended to rank.

### Case B: `/jobs/862` is an old numeric URL for a newer slug URL

Expected final state: `/jobs/862` permanently redirects in one hop to the exact canonical slug page for the same job. The slug page must be HTTP 200, indexable, and self-canonical.

### Case C: job `862` is expired but useful as an archive

Keep an indexable archive page only if it has real historical value, clear expired status, official details, and unique content. Otherwise use `noindex, follow` or 410/404 based on expired-job policy.

### Case D: job `862` does not exist or is invalid

Return 404 or 410 with proper noindex, remove from sitemap, and remove broken internal links. Do not canonicalize to homepage or `/jobs`.

## 5. Never Canonicalize Unique Job Details to Generic Pages

Do not set `/jobs/862` canonical to `/`, `/jobs`, `/districts/pune`, `/jobs-in-pune`, `/department/*`, or `/qualification/*`. Those pages have different search intent.

## 6. Site-Wide Job Canonical Audit

Do not fix only `/jobs/862`. Search all dynamic job URL patterns: `/jobs/[id]`, `/jobs/[slug]`, `/job/[id]`, `/job/[slug]`, `/jobs?id=862`, `/jobs?job_id=862`, and `/jobs?jobId=862`.

Audit canonical URL, OG URL, Twitter URL, Breadcrumb URL, JobPosting URL, sitemap URL, internal links, expired job behavior, and redirect behavior.

## 7. Job Detail Page Sections Required for Ranking

If the canonical job page is indexable, it should include H1, direct summary, key facts table, important dates, eligibility, age limit, fee, selection process, salary, how to apply, official links, documents required, related jobs, editorial verification note, and FAQ section.

Do not fabricate unavailable job facts. Use `Not specified in official notification` where appropriate.

## 8. SEO, AEO, GEO and AI Requirements

Use one trusted URL per job. Align canonical tag, sitemap URL, internal links, BreadcrumbList URL, JobPosting URL, Open Graph URL, Twitter URL, and `llms.txt` entry if used. Keep content factual, labeled, crawlable in raw/prerendered HTML, and source-backed.

## 9. Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required to fix this canonical issue.

## 10. Definition of Done

- Exact canonical decision for `/jobs/862` is documented.
- If unique/indexable, canonical points to the exact job URL and page is HTTP 200.
- If duplicate, `/jobs/862` redirects in one hop to the exact canonical job URL.
- Canonical target is HTTP 200 and indexable.
- Sitemap includes only the canonical job URL if appropriate.
- Internal links use canonical job URL only.
- JobPosting schema matches visible job data.
- GSC URL Inspection confirms expected canonical behavior.
- The issue is validated after deployment.
