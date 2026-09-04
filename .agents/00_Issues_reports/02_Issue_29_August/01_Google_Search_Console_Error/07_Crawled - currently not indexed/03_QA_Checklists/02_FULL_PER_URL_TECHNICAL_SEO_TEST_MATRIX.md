# Full Per-URL Technical SEO Test Matrix

Date: 2026-08-29
Issue: Crawled - currently not indexed
Scope target: 136 URLs
Current extracted URL briefs: 16 real URLs from visible evidence

## Purpose

Use this matrix for every affected URL before deciding whether it should be indexed. The same test must be run for job pages, result pages, district/topic pages, department pages, qualification/location pages, and filter URLs.

## Per-URL Test Checklist

| Test Area | What To Check | Pass Rule | Fix If Failed |
|---|---|---|---|
| HTTP status | Status code and final URL | Indexable pages return `200 OK` | Restore valid page, redirect duplicate, 404/410 invalid page |
| Redirect | Chain, loop, protocol, www/non-www | Max one direct redirect to relevant canonical | Replace chains with one 301/308 |
| Robots meta | `meta name="robots"` | Useful pages use `index,follow` | Remove accidental noindex only from useful pages |
| X-Robots-Tag | HTTP header robots directives | No index-blocking header on indexable pages | Fix server/header config |
| Canonical | Canonical href | Self-canonical for final indexable page | Point to final canonical URL or redirect duplicate |
| Sitemap | URL presence | Only final canonical indexable 200 URLs included | Add/remove from sitemap based on decision |
| Internal links | Links from hub/category/related pages | Links point to final canonical URL | Update only relevant contextual links |
| Title | Unique page title | Clear, useful, non-duplicated, no encoding break | Generate from real page data |
| Meta description | Unique summary | Useful page-specific summary | Generate from actual facts |
| H1 | Main heading | One clear H1 matching intent | Fix template/content data |
| Content depth | Body sections | Useful, specific, not placeholder/thin | Add required sections from content matrix |
| FAQ quality | FAQ questions/answers | 10-15 specific, no copied generic set | Generate from page facts and intent |
| Structured data | Schema validity | Matches visible content and canonical URL | Fix JSON-LD fields |
| Breadcrumb | Breadcrumb text/URL | Matches hierarchy and canonical path | Update breadcrumb data only |
| Page speed | CWV/Lighthouse/PageSpeed | No severe LCP/CLS/INP issues | Optimize assets, SSR, caching, images, scripts |
| Mobile rendering | Googlebot smartphone output | Critical content visible in HTML/render | Fix rendering/hydration issues |
| Duplicate content | Near-duplicate pages | Each indexable URL has unique value | Consolidate, canonicalize, or improve |
| Language/encoding | Text display | No broken mojibake/garbled text | Fix encoding/source text/template |
| Official source | Source/verifiability | Official link or verification note visible | Add source block, do not fabricate |
| Last updated | Freshness signal | Accurate update date visible | Pull from record update date |

## Tools Developer Should Use

- Google Search Console URL Inspection live test.
- Screaming Frog / Sitebulb / equivalent crawler.
- `curl -I -L` for status, redirects, headers.
- Lighthouse or PageSpeed Insights for speed/Core Web Vitals.
- Rich Results Test for JobPosting/Breadcrumb/schema.
- Mobile-Friendly/Chrome rendering or Playwright snapshot for rendered HTML.
- Sitemap XML validator.
- Internal link crawl export.

## Do Not Delete Or Break Existing Pages

Do not delete existing pages only because GSC reports `Crawled - currently not indexed`. First classify the page. Useful existing pages should be improved. Duplicate pages should redirect/canonicalize. Truly invalid pages can remain 404/410.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
