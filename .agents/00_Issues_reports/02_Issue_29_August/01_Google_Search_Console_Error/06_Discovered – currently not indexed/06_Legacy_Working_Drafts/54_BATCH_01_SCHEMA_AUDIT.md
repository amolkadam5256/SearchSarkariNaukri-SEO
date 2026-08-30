# BATCH 01 — SCHEMA AUDIT

Validate every first-50 page for:
- JSON-LD syntax
- BreadcrumbList
- WebPage/appropriate type
- Organization
- author only if real/displayed
- FAQPage only when appropriate and identical to visible FAQ

Remove:
- JobPosting
- QAPage when inappropriate
- fake reviews/ratings/events/authors/dates

Check schema against visible content.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
