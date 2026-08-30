# SearchSarkariNaukri - Excluded by noindex Tag Fix Package

Google Search Console issue: `Excluded by noindex tag`.
Reported affected pages: 56.
Latest package update: 29 August 2026.

## Professional Folder Format

- `00_Master_Index/` - master remediation report and URL index CSV.
- `01_URL_Briefs/` - all URL-specific markdown briefs in one place.
- `02_Source_Exports/` - original Search Console/source export files.

## Main Files

- `00_Master_Index/00_NOINDEX_COVERAGE_REMEDIATION_2026-08-29.md` - master remediation note for the latest GSC noindex coverage issue.
- `00_Master_Index/url-remediation-index-2026-08-29.csv` - index of the 56 URL candidates and their brief files.
- `01_URL_Briefs/` - page-level fix briefs with indexing fix, missing sections, internal links, SEO/GEO/AEO notes, schema notes, and validation checklist.
- `02_Source_Exports/gsc-noindex-coverage-2026-08-29.xlsx` - Search Console export evidence retained separately from working briefs.

## Evidence Note

The pasted GSC text showed 10 visible example URLs while reporting 56 affected pages. The package separates confirmed visible GSC examples from supplemental local crawl indexability evidence. Replace supplemental candidates with exact GSC rows if the full spreadsheet export is available.

## Developer Scope Guardrail

Do not change any unrelated page, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, or shared component unless it is strictly required to remove the noindex problem for this exact URL. Keep the fix limited to this page's indexing directives, canonical/sitemap entry, missing content sections, structured data, and relevant internal links. If a shared template must be edited, verify that it does not alter unrelated pages visually or functionally.

## Recommended Fix Order

1. Find and fix shared `noindex` generation logic in page templates, prerender output, CDN/server headers, or route guards.
2. Crawl all 56 URLs and confirm status, canonical, robots meta, and X-Robots-Tag.
3. For pages that should rank, remove `noindex` and strengthen missing content sections.
4. Add internal links from parent hubs and sibling location/category pages.
5. Keep only canonical 200 indexable URLs in XML sitemaps.
6. Deploy, inspect live HTML, then request GSC validation.

