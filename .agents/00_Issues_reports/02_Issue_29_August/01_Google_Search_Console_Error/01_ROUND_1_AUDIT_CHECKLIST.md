# Round 1 Audit - Full GSC Error Folder

Date: 2026-08-29
Scope: All six Google Search Console issue folders under `01_Google_Search_Console_Error`
Purpose: Check whether the developer implementation is complete before the first fix pass.

## Round 1 Audit Steps

1. Review `00_GSC_ERROR_MASTER_AUDIT_AND_DEVELOPER_HANDOFF.md`.
2. Confirm all six issue folders still exist.
3. Confirm each issue folder has developer instructions, source evidence, and QA notes.
4. Check every affected URL set against live production behavior.
5. Export HTTP status, canonical, robots meta, sitemap inclusion, redirect target, title, H1, word count, structured data, and internal-link source.
6. Compare live output against the correct issue-specific fix rule.
7. Mark every failed URL or template issue in `02_ROUND_1_FIX_TRACKER.md`.

## Required Checks By Issue

| Folder | Round 1 Check |
|---|---|
| `01_Not found (404)` | Valid jobs restored to 200, exact replacements redirected, real missing pages return 404/410 |
| `02_Soft 404` | Valid zero-result pages have useful crawlable content, related links, FAQs, and self-canonical 200 |
| `03_Excluded by noindex tag` | Noindex removed only from useful indexable pages; intentional noindex pages removed from sitemap |
| `04_Redirect error` | `/jobs?district_slug=pune` redirects once to `/districts/pune` with no chain or loop |
| `05_Alternative page with proper canonical tag` | `/jobs/862` has correct final canonical or direct redirect |
| `06_Discovered - currently not indexed` | 896 admit-card URLs have decisions; only final canonical indexable pages are in sitemap |

## Pass Criteria

- No sitemap contains 404, 410, redirected, noindex, or canonicalized-away URLs.
- All indexable pages return `200 OK`.
- All indexable pages are self-canonical.
- Structured data URLs match canonical URLs.
- Internal links use final canonical URLs.
- Thin pages are improved before indexing request.

## Fail Criteria

- Any valid record still returns 404.
- Any useful page remains noindex by mistake.
- Any redirected/noindex/404 URL remains in sitemap.
- Any redirect chain, loop, or irrelevant redirect exists.
- Any admit-card page is submitted to sitemap before content/canonical QA passes.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix a specific Google Search Console indexing issue.
