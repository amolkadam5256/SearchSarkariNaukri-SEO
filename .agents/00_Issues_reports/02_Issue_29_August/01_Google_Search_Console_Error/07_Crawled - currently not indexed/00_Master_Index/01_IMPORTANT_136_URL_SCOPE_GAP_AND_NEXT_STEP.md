# Important Scope Gap - 136 URLs Required

Date: 2026-08-29
GSC issue: `Crawled - currently not indexed`

## Correction

The Google Search Console evidence states there are **136 affected URLs**.

The current generated URL brief set contains only **16 page URL briefs** because the pasted text exposed only the visible example/evidence URLs. The `.xlsx` file is present in the folder, but in this execution environment it is listed by PowerShell and `cmd /x`, yet cannot be opened, copied, stream-read, or opened through Excel COM. Because of that, the remaining URLs could not be extracted safely here.

## Current Status

| Item | Count |
|---|---:|
| GSC affected pages reported | 136 |
| Page URLs extracted from pasted visible evidence | 16 |
| Asset URLs extracted from pasted visible evidence | 1 |
| Missing actual page URLs still needed | 120 |

## Required Developer Action Before Fixing

Export the full GSC table again as CSV or paste all 136 URL rows into this folder. The required columns are:

- URL
- Last crawled

Preferred file name:

`00_Master_Index/full-136-crawled-currently-not-indexed-export.csv`

After that file exists, regenerate `01_URL_Briefs_All/` so it contains exactly 136 markdown files and regenerate `crawled-currently-not-indexed-url-index.csv` with exactly 136 rows.

## Do Not Do

- Do not treat the current 16 URL briefs as the full issue scope.
- Do not request GSC validation for this issue until all 136 URLs are audited.
- Do not invent the missing 120 URLs.
- Do not create placeholder URL briefs without actual URLs.

## What Can Still Be Fixed Now

The existing evidence is enough to fix the confirmed class of problem:

- At least one useful job page outputs `<meta name="robots" content="noindex, follow" />`.
- The developer must audit route-level indexability rules for job detail pages, district/topic pages, department pages, result pages, qualification/location landing pages, and parameter URLs.
- Remove accidental noindex only from useful indexable pages.
- Keep noindex for duplicate, thin, filter-only, or intentionally excluded pages.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to affected URL routing, HTTP status handling, canonical logic, robots/indexability, sitemap, metadata, structured data, contextual internal links, page content quality, redirects, and QA.
