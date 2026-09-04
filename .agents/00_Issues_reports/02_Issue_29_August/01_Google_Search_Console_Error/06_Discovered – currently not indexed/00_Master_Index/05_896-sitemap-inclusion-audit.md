# Final Sitemap Inclusion Audit - 896 Discovered Admit Card URLs

Date: 2026-08-29
Issue folder: `06_Discovered - currently not indexed`
GSC issue: `Discovered - currently not indexed`
Page type: Admit card detail pages
Scope: 896 URLs

## Result

| Check | Result |
|---|---:|
| GSC URLs audited | 896 |
| Unique source URLs from 896 index | 896 |
| URLs found in existing saved sitemap exports | 141 |
| URLs not found in existing saved sitemap exports | 755 |
| Sitemap source files checked | 2 |

## Files Checked

- `SEO_Audit_Review_2026-08-25\outputs\raw-crawl-data\raw-sitemap-admit-cards.xml`
- `SEO_Audit_Review_2026-08-25\outputs\raw-crawl-data\sitemap-urls-full-list.csv`

## Output File

The per-URL sitemap result is here:

`00_Master_Index/05_896-sitemap-inclusion-audit.csv`

## Final Developer Decision

Do not add all 896 current numeric URLs blindly to the live sitemap.

Many URLs are numeric admit-card detail URLs and the final implementation plan recommends migrating qualifying pages to meaningful canonical URLs where reliable entity data exists. Therefore the sitemap must contain the final canonical URL, not necessarily the old numeric source URL.

## Required Fix

For every URL in `02_896-url-decision-and-migration-map.csv`:

1. Resolve final page decision: `INDEX`, `IMPROVE_FIRST`, `REDIRECT`, `CANONICALIZE`, `NOINDEX`, `404`, or `410`.
2. If the page is selected for indexing, make sure the final canonical page returns `200 OK`.
3. Make sure the page uses `index,follow`.
4. Make sure the canonical tag points to itself.
5. Add only that final canonical URL to the admit-card sitemap.
6. Do not add redirected, noindex, thin, duplicate, expired-invalid, parameter, or canonicalized-away URLs to sitemap.
7. If a numeric URL is replaced by a semantic URL, add the semantic URL to sitemap and 301/308 redirect the old numeric URL to it.
8. Set accurate `lastmod` based on the admit-card record update date.
9. Keep sitemap URLs consistent with internal links, breadcrumb URLs, canonical tags, and structured data URLs.
10. Resubmit sitemap in Google Search Console after deployment and run URL Inspection on a sample of fixed pages.

## Sitemap Logic Required In Code

The sitemap generator should include admit-card detail pages only when all conditions are true:

- The admit-card record is real and has a valid ID.
- The page has a crawlable final canonical URL.
- The HTTP status is `200`.
- The page is not blocked by `robots.txt`.
- The page does not include a `noindex` directive.
- The canonical URL equals the URL emitted in the sitemap.
- The page has enough unique content using the approved admit-card content schema.
- Duplicate or near-duplicate records have been consolidated.
- The page is not only a thin placeholder.

## Priority

- P0: Fix sitemap/canonical mismatch for indexable pages.
- P0: Exclude noindex, redirected, duplicate and thin pages from sitemap.
- P1: Add missing final canonical URLs for qualified admit-card pages.
- P1: Update internal links to use the same final canonical URLs.
- P2: Add `lastmod` and validate sitemap XML.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
