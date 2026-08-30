# Remove 404 and Noindex URLs From Sitemap and Retest

## Purpose

The XML sitemap must contain only canonical, indexable URLs that return `200`.

Remove these URL types from all sitemap files and sitemap generators:

- `404 Not Found`
- `410 Gone`
- `301` or `302` redirect URLs
- Expired job URLs using `<meta name="robots" content="noindex, follow" />`
- Duplicate/non-canonical job URL variants
- Empty or placeholder job pages

## Immediate Evidence URLs

| URL | Current Issue | Sitemap Action | Retest Required |
|---|---|---|---|
| `https://www.searchsarkarinaukri.com/jobs/835` | GSC reports `404`; no referring sitemap detected | Keep out of sitemap unless restored to canonical `200` | Yes |
| `https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110` | GSC live test reports `404` | Remove from sitemap unless restored or redirected to canonical replacement | Yes |

## Sitemap Fix Rules

### Keep In Sitemap

Keep a job URL in the sitemap only when all are true:

- URL returns `200`.
- URL is canonical.
- Page is indexable.
- Page has useful content.
- Page is intended to appear in Google.

### Remove From Sitemap

Remove a job URL from the sitemap when any are true:

- URL returns `404`.
- URL returns `410`.
- URL redirects.
- URL has `noindex`.
- URL is an old numeric/slug variant replaced by another canonical URL.
- URL is an expired job page intentionally set to `noindex, follow`.

## Developer Implementation Steps

1. Find sitemap source:
   - Static `sitemap.xml`
   - Dynamic sitemap route
   - CMS sitemap export
   - Build-time sitemap generator

2. Add filtering before sitemap output:
   - Include only published jobs intended for indexing.
   - Exclude deleted jobs.
   - Exclude permanently removed jobs.
   - Exclude expired jobs if expired jobs use `noindex, follow`.
   - Exclude redirect source URLs.
   - Exclude numeric legacy URLs when canonical slug URLs exist.

3. Regenerate sitemap.

4. Verify no removed URL remains in:
   - `sitemap.xml`
   - sitemap index files
   - job sitemap files
   - category sitemap files
   - cached sitemap copies

5. Deploy sitemap update after route/redirect fixes.

## Required Retest Commands

Replace sitemap URLs if production uses a sitemap index or multiple sitemap files.

```bash
curl -I https://www.searchsarkarinaukri.com/sitemap.xml
curl -s https://www.searchsarkarinaukri.com/sitemap.xml | grep "/jobs/835"
curl -s https://www.searchsarkarinaukri.com/sitemap.xml | grep "indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110"
curl -I https://www.searchsarkarinaukri.com/jobs/835
curl -I https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110
```

Expected:

- `sitemap.xml` returns `200`.
- Removed 404/noindex URLs are not present in sitemap output.
- Valid restored URLs return `200`.
- Redirected URLs return `301` directly to relevant `200` URLs.
- Removed URLs return intentional `404` or `410`.

## Full 613-URL Retest

After implementation, test every URL from:

`01-all-613-urls-master-audit.csv`

For each row, update:

- `Current HTTP Status`
- `Replacement URL`
- `Final Category`
- `Round 1 Result`
- `Round 2 Result`
- `Round 3 Result`
- `Sign-off`

## Pass Criteria

- Sitemap contains `0` 404 URLs.
- Sitemap contains `0` 410 URLs.
- Sitemap contains `0` redirect URLs.
- Sitemap contains `0` noindex URLs.
- No internal links point to intentionally removed URLs.
- Google Search Console validation is started only after production sitemap and URL behavior are both verified.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
