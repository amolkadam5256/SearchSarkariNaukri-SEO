# Master Canonical Audit And Fix Plan

## Issue

Google Search Console reports `Duplicate, Google chose different canonical than user` for:

`https://www.searchsarkarinaukri.com/jobs/1689`

Last crawled: `9 Jun 2026`

## Root Cause To Investigate

Google is receiving mixed canonical signals. Common causes:

- Numeric URL `/jobs/1689` duplicates a slug URL.
- Sitemap includes one URL but canonical points to another.
- Internal links point to the numeric URL while canonical points to slug URL.
- Breadcrumb, JobPosting schema, OG URL, Twitter URL, and canonical disagree.
- The declared canonical is redirected, noindex, weak, or not in sitemap.
- Multiple slug variants exist for the same job record.

## Exact Developer Decision

Check job ID `1689` in DB/CMS and choose one final canonical URL.

| Situation | Final Action |
|---|---|
| `/jobs/1689` is old numeric duplicate | 301/308 redirect to exact slug canonical URL |
| `/jobs/1689` is preferred URL | Make it 200, index/follow, self-canonical, in sitemap |
| Job exists but expired/useful | Keep 200 with expired notice and full content; choose index/noindex by expired-job policy |
| Job removed with no replacement | Return 404/410 and remove from sitemap/internal links |
| Multiple variants exist | Pick one canonical and redirect all variants directly to it |

## Fix Steps

1. Find job record `1689`.
2. Identify generated slug URL and all known variants.
3. Test numeric URL and slug URL with `curl -I -L`.
4. Capture status, robots meta, X-Robots-Tag, canonical, redirect target, sitemap presence.
5. Pick one canonical URL.
6. Align canonical tag, sitemap, internal links, BreadcrumbList, JobPosting URL, OG URL, Twitter URL, and redirect target.
7. Remove duplicate/redirected URL from sitemap.
8. Run GSC URL Inspection after deployment.

## Do Not Do

- Do not canonicalize this job to homepage or `/jobs` hub.
- Do not keep numeric and slug versions both indexable.
- Do not put redirected or duplicate URLs in sitemap.
- Do not change footer/navbar/global layout.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
