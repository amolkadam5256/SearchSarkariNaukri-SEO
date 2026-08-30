# URL Brief - /jobs/1689 Canonical Conflict

## URL

`https://www.searchsarkarinaukri.com/jobs/1689`

## GSC Issue

`Duplicate, Google chose different canonical than user`

## Last Crawled

`9 Jun 2026`

## Required Tests

1. Fetch `/jobs/1689` and record status, redirects, canonical, robots meta, X-Robots-Tag.
2. Find job ID `1689` in DB/CMS.
3. Find generated slug URL for job ID `1689`.
4. Compare title, H1, body content, JobPosting schema, BreadcrumbList, OG URL, Twitter URL, and sitemap URL.
5. Check internal links and sitemap for numeric/slug variants.
6. Decide whether `/jobs/1689` should redirect or be the final canonical.

## Recommended Fix

Most likely: if a descriptive slug URL exists for job ID `1689`, redirect `/jobs/1689` directly to that slug URL and remove `/jobs/1689` from sitemap/internal links.

## Content Requirements If Kept Indexable

- H1 with organization, post, year.
- Status: active/expired/closed.
- Vacancy, qualification, age, salary, location, dates, fee, selection process.
- Official notification/source link.
- How to apply section.
- Related jobs/results/admit cards.
- Last updated date.
- 10-15 job-specific FAQs, not duplicate generic FAQs.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
