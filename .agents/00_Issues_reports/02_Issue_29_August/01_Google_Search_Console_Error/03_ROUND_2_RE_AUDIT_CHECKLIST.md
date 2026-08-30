# Round 2 Re-Audit Checklist - After First Fix Pass

Date: 2026-08-29
Purpose: Verify that Round 1 fixes actually solved the GSC issues and did not create new problems.

## Round 2 Re-Audit Steps

1. Re-crawl every URL changed in Round 1.
2. Re-crawl all affected sitemaps.
3. Re-check redirect maps for chains, loops, mixed protocol, and irrelevant targets.
4. Re-check all indexable pages for `200 OK`, self-canonical, `index,follow`, title, H1, and useful content.
5. Re-check noindex pages are excluded from sitemap.
6. Re-check 404/410 pages are excluded from sitemap and internal links.
7. Re-check admit-card URLs against the 896 decision/migration map.
8. Record remaining failures in `04_ROUND_2_FINAL_FIX_AND_SIGNOFF.md`.

## Regression Checks

- No new 404s created by redirects or slug migrations.
- No sitemap includes old numeric URLs after semantic URL migration unless numeric URL is the final canonical.
- No canonical points to a redirected, noindex, 404, or unrelated URL.
- No page has empty FAQ answers.
- No landing page relies only on `0 Active Jobs` as main content.
- No valid expired job shows `Job not found`.

## Round 2 Pass Criteria

- All Round 1 tracker rows are closed with evidence.
- Remaining failures are documented with final action.
- A representative GSC URL Inspection sample passes live checks.
- Sitemap is ready for resubmission.
- GSC validation can be requested safely.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix a specific Google Search Console indexing issue.
