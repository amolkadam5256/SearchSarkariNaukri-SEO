# Project-Wide Robots Meta Index Follow Audit

## Purpose

Create a project-wide check for robots meta output. Important indexable pages should output:

<meta name="robots" content="index, follow">

But do not add this blindly to every page. Some pages should remain 
oindex, follow or be excluded.

## Pages That Should Be index,follow

- Homepage.
- Valid published job detail pages with useful content.
- Valid result pages with useful result/status/source content.
- Valid admit-card pages with useful record-specific content.
- Valid district/location/category/department landing pages with substantial unique content.
- Important static pages meant to rank.

## Pages That Should Not Be Forced To index,follow

- Backend pages.
- Admin pages.
- Login/account/private pages.
- Staging/dev/test URLs.

- Search/filter parameter URLs unless intentionally converted into static canonical pages.
- Duplicate numeric URLs when a slug canonical exists.
- Thin placeholder pages.
- Admin/private pages.
- 404/410 pages.
- Redirecting URLs.
- Pages intentionally excluded by SEO policy.

## Developer Tests

1. Crawl the full project and export robots meta for every URL.
2. Check HTTP X-Robots-Tag headers.
3. Compare robots directive with canonical, sitemap, and page type.
4. For every useful page wrongly showing 
oindex, change route/template logic to output index, follow.
5. Remove from sitemap any URL that remains noindex.
6. Do not change unrelated UI components.

## Required QA

- No indexable URL has 
oindex.
- No noindex URL is in sitemap.
- No redirected/404/410 URL is in sitemap.
- Canonical and sitemap agree.
- Google/Bing live inspection confirms important pages are indexable.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Bing Webmaster Site Scan issue.

