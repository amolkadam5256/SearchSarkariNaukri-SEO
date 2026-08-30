# Round 2 - Re-Audit Remaining Fixes

Use this pass only for failures discovered in Round 1. Do not widen the scope unless new broken URLs are caused by the fix.

## Re-Audit Tasks
- Re-test all P0 URLs.
- Re-test all redirects for chains and loops.
- Re-crawl sitemap URLs.
- Re-crawl internal links from homepage, job listing, category, related jobs, breadcrumbs, results, and admit-card templates.
- Update unresolved rows in the CSV.

## Required Outcome
Every Round 1 failure has either a confirmed fix or a documented reason for intentional 404/410.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
