# URL Inspection Evidence and Expired Job Fix

## Evidence Added

Source: Google Search Console URL Inspection, shared on 29 August 2026.

| URL | GSC Status | Crawl/Test Date | Page Fetch | Sitemap Discovery | Required Action |
|---|---|---|---|---|---|
| `https://www.searchsarkarinaukri.com/jobs/835` | URL is not on Google; Page is not indexed: Not found (404) | Last crawl: 22 July 2026, 03:08:51 | Failed: Not found (404) | No referring sitemaps detected | Verify job ID `835` in DB/CMS. If valid, restore 200 or redirect to canonical job URL. If permanently gone, return intentional 410/404 and keep out of sitemap/internal links. |
| `https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110` | URL is not available to Google; Page cannot be indexed: Not found (404) | Live test: 29 August 2026, 11:14:18 | Failed: Not found (404) | Not checked in live test | Verify job ID `110` and canonical slug. If the job exists, fix route/slug lookup or 301 to the exact canonical job URL. Do not redirect to homepage. |

## Additional Page-State Evidence

Observed job detail breadcrumb/content pattern:

`Home > Jobs > १ पदांकरिता Central Vigilance Commission भरती अपडेट २०२६`

Observed expired message:

`This job's application deadline has passed (25 Jul 2026)`

## Required Fix Rule

Expired is not the same as missing.

If a job record exists and contains useful job information:

- Return `200`.
- Show the complete job details.
- Show a clear expired/deadline-passed notice.
- Do not show "Job not found".
- Do not render an empty placeholder.
- Use a valid canonical URL that returns `200`.

If the site does not want expired jobs indexed:

- Use `<meta name="robots" content="noindex, follow" />`.
- Remove the expired URL from XML sitemaps.
- Keep useful internal links crawlable with `follow`.
- Do not mix `noindex` URLs into indexable sitemap files.

If the job record is deleted or permanently unavailable:

- Return `410 Gone` when the removal is intentional and permanent.
- Return `404 Not Found` for genuinely nonexistent/random URLs.
- Remove all sitemap, breadcrumb, related-job, structured-data, and internal-link references.

## Developer Checklist

- Split route logic into three states: existing active job, existing expired job, missing/deleted job.
- Confirm numeric route `/jobs/{id}` does not 404 when the job exists.
- Confirm slug route resolves by final ID when the slug is old but the ID is valid.
- Add a direct `301` only when a clear canonical replacement exists.
- Confirm expired job pages do not contain "Job not found" in title, H1, body, meta description, or structured data.
- Re-test the two evidence URLs after implementation.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
