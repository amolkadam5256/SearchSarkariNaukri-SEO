# Round 1 - Testing and Validation

Run after the first implementation pass. Update `01-all-613-urls-master-audit.csv` columns `Current HTTP Status`, `Replacement URL`, `Final Category`, and `Round 1 Result`.

## Tests
- Test every URL with `curl -I -L` or crawler export.
- Confirm restored URLs return 200 with useful content.
- Confirm expired jobs return the intended status and message: useful existing records should not display "Job not found" merely because the application deadline passed.
- Confirm expired jobs that intentionally use `noindex, follow` are not present in XML sitemaps.
- Confirm redirects are 301 and land directly on relevant 200 URLs.
- Confirm removed URLs return intentional 404/410.
- Crawl internal links and sitemap for broken references.
- Search all sitemap files for every URL marked 404, 410, redirect, or noindex.

## Stop Conditions
- Any valid DB record still returns 404.
- Any expired-but-existing job page shows "Job not found" or an empty placeholder.
- Any redirect target is unrelated or not 200.
- Sitemap contains 404/410/301/302 URLs.
- Sitemap contains noindex expired-job URLs.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
