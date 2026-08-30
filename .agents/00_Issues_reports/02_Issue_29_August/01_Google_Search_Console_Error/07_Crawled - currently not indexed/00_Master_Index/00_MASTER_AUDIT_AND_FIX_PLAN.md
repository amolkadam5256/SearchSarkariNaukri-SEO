# Master Audit And Fix Plan - Crawled Currently Not Indexed

Date: 2026-08-29
Issue: Google Search Console `Crawled - currently not indexed`

## Scope

The supplied evidence says 136 pages are affected, but only 16 page URLs were visible/extractable from the pasted evidence in this environment. The remaining 120 actual URLs must be exported as CSV or pasted before this package can be considered complete. A separate markdown brief has been created for each page URL in `01_URL_Briefs_All/`.

## Page Type Breakdown

- Department landing page: 1
- District/topic landing page: 6
- Filtered jobs/category URL: 1
- Job detail page: 3
- Other page: 1
- Qualification/location landing page: 2
- Result detail page: 2

## Action Breakdown

- CANONICALIZE_OR_NOINDEX_FILTER: 1
- FIX_NOINDEX_AND_CONTENT_OR_REDIRECT: 3
- IMPROVE_LANDING_PAGE_OR_NOINDEX_IF_THIN: 9
- MANUAL_REVIEW: 1
- VERIFY_RESULT_RECORD_AND_INDEXABILITY: 2

## Root Causes To Check

1. Accidental `noindex, follow` on useful pages.
2. Thin or low-value content after Google renders the page.
3. Duplicate/canonical variants where Google chooses another URL.
4. Sitemap contains non-indexable URLs or misses final canonical URLs.
5. Internal links point to old, duplicate, parameter, or redirected variants.
6. Structured data is present but page is blocked from indexing.
7. JobPosting schema has non-critical or critical field problems.
8. Page title/H1/description are malformed, duplicated, or mixed-language in a way that weakens clarity.
9. Dynamic content is not reliably visible in crawlable HTML.
10. URL quality is weak, especially duplicate slugs like double hyphens or truncated variants.

## Exact Developer Fix Logic

For every URL in `crawled-currently-not-indexed-url-index.csv`:

1. Fetch the live URL and record HTTP status.
2. Check HTML robots meta and HTTP `X-Robots-Tag`.
3. If page is useful and should rank, remove accidental noindex and use `index,follow`.
4. If page is duplicate/thin/filter-only, keep noindex or canonicalize/redirect as appropriate.
5. Check canonical. It must point to the exact final preferred URL.
6. Check sitemap. Add only final canonical indexable URLs; remove noindex, redirect, duplicate, 404/410, and thin URLs.
7. Check content. Add missing record-specific sections and useful FAQs.
8. Check structured data. Breadcrumb and JobPosting/Article/Result schema must match visible content and canonical URL.
9. Check internal links. Link to final canonical URLs only.
10. Run Round 1 audit, fix failures, run Round 2 audit, then request GSC validation.

## Important URL-Specific Notes

- Job detail URLs with useful records should generally be indexable, self-canonical, and included in sitemap after content/schema QA.
- Duplicate job slug variants should use one canonical URL and redirect variants directly to it.
- Parameter URL `/jobs?category=banking` should not be indexed unless intentionally converted into a clean static landing page.
- District/topic and qualification/location pages must not be empty `0 jobs` pages. They need useful crawlable content and related links.
- Result detail pages need result status/date/source/download/context, not thin placeholder content.

## Do Not Do

- Do not add every URL to sitemap blindly.
- Do not remove noindex from thin or duplicate pages.
- Do not redirect unrelated pages to a broad hub.
- Do not create copied FAQ blocks across pages.
- Do not change navbar, footer, header, global layout, analytics, tracking, or unrelated pages.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to affected URL routing, HTTP status handling, canonical logic, robots/indexability, sitemap, metadata, structured data, contextual internal links, page content quality, redirects, and QA.


## Important Scope Gap

Read `00_Master_Index/01_IMPORTANT_136_URL_SCOPE_GAP_AND_NEXT_STEP.md`. The issue has 136 affected URLs, but only 16 actual page URLs were extractable from the provided visible paste here. Do not treat the 16 briefs as complete.


## Final 136 Scope Status

Read `00_Master_Index/02_FINAL_136_SCOPE_STATUS_AND_HANDOFF.md`. GSC reports 136 affected pages. This package currently contains real URL briefs only for the 16 URLs extractable from the supplied visible evidence; the remaining 120 URLs require the full GSC CSV export.

