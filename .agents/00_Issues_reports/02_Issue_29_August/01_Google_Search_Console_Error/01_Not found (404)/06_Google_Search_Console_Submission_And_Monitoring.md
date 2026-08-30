# Google Search Console Submission and Monitoring

## Before Starting GSC Validation
- Production deployment completed.
- Full URL test completed for all 613 rows.
- Sitemap validated clean.
- 404, 410, redirect, and noindex URLs removed from sitemap.
- Internal links validated clean.
- Redirect map validated chain-free.

## GSC Steps
1. Open Google Search Console -> Page indexing -> Not found (404).
2. Inspect representative restored URLs, redirect URLs, and intentionally removed URLs.
3. Submit restored canonical URLs for inspection where needed.
4. Submit the cleaned sitemap.
5. Start validation only after production behavior is confirmed.

## Monitoring Notes
GSC can lag after deployment. A non-zero 404 count immediately after fixes does not prove failure. Treat new errors as failed only after Google recrawls the corrected live URLs and they still return the wrong status.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
