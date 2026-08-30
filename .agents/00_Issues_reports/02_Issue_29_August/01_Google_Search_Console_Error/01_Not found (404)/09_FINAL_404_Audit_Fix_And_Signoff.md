# SearchSarkariNaukri - Final 404 Audit, Fix Plan, Retest, and Sign-Off

## Issue Summary

Google Search Console reports `613` URLs under:

`Page indexing -> Not found (404)`

Site:

`https://www.searchsarkarinaukri.com/`

Source export:

`https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-29.xlsx`

Generated audit source:

`01-all-613-urls-master-audit.csv`

## URL Pattern Summary

| Pattern | Count | Meaning |
|---|---:|---|
| Numeric job ID URL | 557 | Example: `/jobs/835` |
| Slug with job ID URL | 31 | Example: `/jobs/...-110` |
| Other/non-standard URL | 25 | URLs without a clear numeric job ID |
| Total | 613 | Full GSC export |

## Confirmed GSC Evidence

| URL | Evidence | Required Fix |
|---|---|---|
| `https://www.searchsarkarinaukri.com/jobs/835` | GSC URL Inspection: URL is not on Google. Page indexing: Not found (404). Last crawl: 22 July 2026, 03:08:51. No referring sitemap detected. | Verify job ID `835` in DB/CMS. If valid, restore `200` or redirect to exact canonical URL. If deleted, return intentional `410` or `404`. |
| `https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110` | GSC live inspection on 29 August 2026, 11:14:18: Page cannot be indexed because Not found (404). | Verify job ID `110`. If job exists, restore route or `301` to canonical job URL. Do not redirect to homepage. |

## Final Decision Categories

Every URL must end in exactly one category:

| Category | Use When | HTTP Result |
|---|---|---|
| `KEEP_200` | URL is valid, canonical, useful, and already works | `200` |
| `RESTORE_200` | Job/content exists but route currently returns 404 | `200` |
| `REDIRECT_301` | Old URL has a close, relevant canonical replacement | `301 -> 200` |
| `REMOVE_410` | Page/job is intentionally and permanently removed | `410` |
| `REMOVE_404` | URL is genuinely invalid/random/nonexistent | `404` |

## Critical Fix Rule: Expired Is Not Missing

Expired job pages must not show a confusing `Job not found` message when the job record still exists.

If a job exists but the application deadline has passed:

- Return `200` if the page still contains useful job information.
- Show the complete job details.
- Show a clear expired notice, for example: `This job's application deadline has passed`.
- Do not show `Job not found`.
- Do not render an empty placeholder page.
- Use a canonical URL that returns `200`.

If expired jobs should not be indexed:

- Use `<meta name="robots" content="noindex, follow" />`.
- Remove those expired `noindex` URLs from XML sitemaps.
- Keep useful internal links crawlable with `follow`.

## Sitemap Fix Rule

The sitemap must contain only canonical, indexable `200` URLs.

Remove from sitemap:

- `404` URLs
- `410` URLs
- `301` or `302` redirect URLs
- `noindex, follow` expired job URLs
- duplicate URL variants
- old numeric URLs when a canonical slug URL exists
- empty/placeholder pages

Keep in sitemap only when all are true:

- URL returns `200`.
- URL is canonical.
- URL is indexable.
- URL has useful content.
- URL is intended to appear in Google.

## Implementation Fix Checklist

### Application Routes

- Verify route support for `/jobs/{id}`.
- Verify route support for `/jobs/{slug}-{id}` or the current canonical format.
- Resolve slug URLs by final job ID when possible.
- Split job page behavior into three states:
  - active existing job
  - expired existing job
  - missing/deleted job
- Fix valid existing records that incorrectly return `404`.
- Do not solve broken route/database lookup problems with homepage redirects.

### Database/CMS Checks

For every URL in `01-all-613-urls-master-audit.csv`, check:

- numeric job ID
- slug
- published status
- deleted status
- expiry/closing date
- canonical URL
- replacement job/page
- internal-link references

### Redirects

- Add `301` only when a relevant replacement exists.
- Redirect directly to the final canonical `200` URL.
- Do not redirect unrelated jobs.
- Do not redirect all deleted jobs to `/` or `/jobs`.
- Avoid redirect chains and loops.

### Removed Pages

- Return `410 Gone` for intentionally and permanently removed pages.
- Return `404 Not Found` for genuinely invalid URLs.
- Remove removed URLs from sitemap, internal links, breadcrumbs, related jobs, and structured data.

### Internal Links

Search all site templates and content for the 613 URLs.

Fix references in:

- homepage
- jobs listing
- category/filter pages
- related jobs
- breadcrumbs
- search results
- XML sitemap generation
- structured data

## Retest Plan

### Round 1

- Test all 613 URLs.
- Update `Current HTTP Status`.
- Update `Exists in DB`.
- Update `Content Exists`.
- Update `Replacement URL`.
- Update `Final Category`.
- Fix all P0 failures.

### Round 2

- Re-test all P0 and failed Round 1 URLs.
- Re-test redirect chains and loops.
- Re-crawl sitemap output.
- Re-crawl internal links.
- Fix remaining failures.

### Round 3

- Re-test all 613 URLs again.
- Confirm final category for every URL.
- Confirm sitemap contains no invalid URLs.
- Confirm no valid job page still returns 404.
- Confirm no expired existing job says `Job not found`.

## Required Production Test Commands

```bash
curl -I https://www.searchsarkarinaukri.com/jobs/835
curl -I https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110
curl -I https://www.searchsarkarinaukri.com/sitemap.xml
curl -s https://www.searchsarkarinaukri.com/sitemap.xml | grep "/jobs/835"
curl -s https://www.searchsarkarinaukri.com/sitemap.xml | grep "indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110"
```

Expected:

- Restored valid jobs return `200`.
- Redirected old URLs return `301 -> 200`.
- Permanently removed URLs return `410`.
- Genuinely invalid URLs return `404`.
- Sitemap returns `200`.
- Sitemap does not contain `404`, `410`, redirect, duplicate, or `noindex` URLs.

## Final Audit Table Status

Main working file:

`01-all-613-urls-master-audit.csv`

Current known status:

| Metric | Status |
|---|---:|
| Total URLs exported from GSC | 613 |
| URLs documented in CSV audit | 613 |
| Confirmed GSC examples added | 2 |
| Final DB/content verification | Pending production DB/CMS access |
| Production route fixes | Pending application access |
| Production sitemap fixes | Pending application/sitemap generator access |
| Full retest completed | Pending production deployment |

## Final Sign-Off

| Check | Status |
|---|---|
| Every GSC URL documented | PASS |
| `/jobs/835` evidence added | PASS |
| `/jobs/...-110` evidence added | PASS |
| Expired job rule documented | PASS |
| Sitemap removal rule documented | PASS |
| 3-round retest process documented | PASS |
| DB/CMS verification completed | PENDING |
| Production fixes deployed | PENDING |
| Full crawl completed after deployment | PENDING |
| GSC validation started after deployment | PENDING |

## Final Result

`PENDING PRODUCTION IMPLEMENTATION`

This audit pack is ready for the developer/admin with application, database, sitemap, and deployment access. The project is complete only after production verifies:

- all valid jobs return `200`
- relevant old URLs redirect with `301`
- removed URLs return `404` or `410`
- no expired existing job displays `Job not found`
- sitemap contains only canonical, indexable `200` URLs
- internal links no longer point to removed URLs

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
