# BATCH 01 — INDEXABILITY AUDIT

For each of the first 50 URLs decide:
INDEX / IMPROVE THEN INDEX / CONSOLIDATE / NOINDEX / 404-410 / DATA CORRECTION / MANUAL VERIFICATION.

Never force indexation.

Create an evidence table:
URL | HTTP | Canonical | Robots | Sitemap | Internal Links | Content Quality | Duplicate | Decision | Reason

Priority is:
1. blocking technical errors
2. duplicate/wrong URLs
3. thin content
4. orphan pages
5. metadata/content improvements

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
