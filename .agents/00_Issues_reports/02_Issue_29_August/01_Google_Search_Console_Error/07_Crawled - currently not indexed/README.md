# Crawled - Currently Not Indexed Developer Handoff

Date: 2026-08-29
GSC issue: `Crawled - currently not indexed`
Source workbook: `https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-29 (6).xlsx`
GSC affected pages reported: 136
Parsed page URLs from visible pasted evidence: 16
Scope status: INCOMPLETE until the full 136-row export is readable

## What This Folder Contains

- `00_Master_Index/00_MASTER_AUDIT_AND_FIX_PLAN.md` - main issue audit and developer fix plan.
- `00_Master_Index/crawled-currently-not-indexed-url-index.csv` - per-URL index and action tracker.
- `01_URL_Briefs_All/` - one separate markdown brief for every page URL found in the supplied evidence.
- `02_Source_Evidence/` - pasted GSC/export evidence and live HTML evidence.
- `03_QA_Checklists/01_TWO_ROUND_TEST_AUDIT.md` - audit, fix, re-audit workflow.
- `04_AI_AEO_GEO_SEO_Ranking/01_AEO_GEO_SEO_REQUIREMENTS.md` - ranking and content requirements.

## Main Finding

The supplied live HTML evidence shows an indexability contradiction for job `1730`: Google reported the URL as indexed in one view, but live testing rejected indexing, and the pasted HTML contains `<meta name="robots" content="noindex, follow" />`. That means the first developer check must be whether useful pages are accidentally outputting noindex.

## Developer Rule

Do not treat `Crawled - currently not indexed` as a request to force-index every URL. First identify why Google crawled but did not select the page: noindex, thin content, duplicate canonical, weak internal links, low value, sitemap mismatch, structured data mismatch, or crawl/render issues.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to affected URL routing, HTTP status handling, canonical logic, robots/indexability, sitemap, metadata, structured data, contextual internal links, page content quality, redirects, and QA.


## Important Scope Gap

Read `00_Master_Index/01_IMPORTANT_136_URL_SCOPE_GAP_AND_NEXT_STEP.md`. The issue has 136 affected URLs, but only 16 actual page URLs were extractable from the provided visible paste here. Do not treat the 16 briefs as complete.


## Final 136 Scope Status

Read `00_Master_Index/02_FINAL_136_SCOPE_STATUS_AND_HANDOFF.md`. GSC reports 136 affected pages. This package currently contains real URL briefs only for the 16 URLs extractable from the supplied visible evidence; the remaining 120 URLs require the full GSC CSV export.



## Added Full Testing And Content Files

- `03_QA_Checklists/02_FULL_PER_URL_TECHNICAL_SEO_TEST_MATRIX.md` - all per-URL technical SEO tests.
- `03_QA_Checklists/03_PAGE_SPEED_AND_TECHNICAL_PERFORMANCE_AUDIT.md` - page speed and Core Web Vitals testing.
- `04_AI_AEO_GEO_SEO_Ranking/02_CONTENT_FAQ_MATRIX.md` - page-type sections and non-duplicate FAQ rules.
- `00_Master_Index/03_REGENERATE_ALL_136_URL_BRIEFS_INSTRUCTION.md` - how to regenerate all 136 URL briefs when the full CSV export is available.

