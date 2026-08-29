# Google Search Console Page Indexing Overview

Date: 2026-08-29
GSC last update: 21/08/2026
Site: `https://www.searchsarkarinaukri.com/`

## Latest GSC Summary

| Reason | Source | Validation | Pages | Folder | Status |
|---|---|---|---:|---|---|
| Not found (404) | Website | Started | 613 | `01_Not found (404)` | Audit/fix package exists |
| Soft 404 | Website | Started | 81 | `02_Soft 404` | Audit/fix package exists |
| Excluded by noindex tag | Website | Started | 56 | `03_Excluded by noindex tag` | Audit/fix package exists |
| Redirect error | Website | Started | 1 | `04_Redirect error` | Audit/fix package exists |
| Alternative page with proper canonical tag | Website | Started | 1 | `05_Alternative page with proper canonical tag` | Audit/fix package exists |
| Discovered - currently not indexed | Google systems | Started | 896 | `06_Discovered - currently not indexed` | 896 URL package exists |
| Crawled - currently not indexed | Google systems | Started | 136 | `07_Crawled - currently not indexed` | 136 scope documented; 16 visible URLs extracted; 120 need full export |
| Duplicate, Google chose different canonical than user | Google systems | Started | 1 | `08_Duplicate_Google_chose_different_canonical` | Audit/fix package exists |
| Server error (5xx) | Website | N/A | 0 | No folder required | Monitor only |

## Total Non-Indexed Pages Reported

Known affected pages excluding 5xx zero-count row: `1785`.

Breakdown:

- Website-source issues: `752` pages.
- Google-systems issues: `1033` pages.
- Server error 5xx: `0` pages.

## Priority Order

1. P0: Fix valid URLs returning 404 and remove invalid URLs from sitemap/internal links.
2. P0: Fix accidental noindex and noindex/sitemap mismatch.
3. P0: Fix redirect error for `/jobs?district_slug=pune`.
4. P0: Fix the 896 admit-card discovered-not-indexed set through content/canonical/sitemap/internal-link decisions.
5. P0: Complete the full 136 URL export for crawled-not-indexed before final per-URL work.
6. P1: Improve Soft 404 landing pages with useful crawlable content.
7. P1: Fix duplicate canonical conflicts for `/jobs/1689` and `/jobs/862` style numeric/slug variants.
8. P2: Monitor 5xx; no active 5xx package is needed because GSC reports 0 pages.

## Developer Rules Across All Issues

- Do not bulk-index every URL.
- Do not add noindex, redirected, duplicate, 404, 410, thin, or canonicalized-away URLs to sitemap.
- Do not redirect unrelated URLs to homepage or broad hubs.
- Do not delete useful expired job pages automatically.
- Do not publish duplicate FAQ blocks across programmatic pages.
- For indexable pages, require `200 OK`, `index,follow`, self-canonical, sitemap inclusion, useful unique content, structured data, and contextual internal links.
- For non-indexable pages, require intentional noindex/redirect/404/410/canonical handling and sitemap exclusion.

## Final Validation Flow

1. Fix each issue folder separately.
2. Run root `01_ROUND_1_AUDIT_CHECKLIST.md`.
3. Record failures in `02_ROUND_1_FIX_TRACKER.md`.
4. Fix failures.
5. Run `03_ROUND_2_RE_AUDIT_CHECKLIST.md`.
6. Complete `04_ROUND_2_FINAL_FIX_AND_SIGNOFF.md`.
7. Submit sitemap and request GSC validation only after live checks pass.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix a specific Google Search Console indexing issue. Keep changes limited to routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, redirects, and QA for the affected URL sets.
