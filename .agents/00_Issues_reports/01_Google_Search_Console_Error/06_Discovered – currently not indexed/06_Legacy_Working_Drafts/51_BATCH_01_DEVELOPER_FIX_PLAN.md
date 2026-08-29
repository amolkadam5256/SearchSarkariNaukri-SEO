# BATCH 01 — DEVELOPER FIX PLAN

After auditing URLs 1–50, group fixes into:
1. Shared template/component fixes
2. Data/database fixes
3. URL/canonical fixes
4. Content fixes
5. Internal linking fixes
6. Schema fixes
7. Sitemap/robots fixes
8. Accessibility fixes
9. Performance fixes
10. Validation/testing

Do not implement the same shared template correction 50 times. Identify shared root causes, then apply record-specific data/content fixes individually.

Every fix must identify:
- file/component
- current behavior
- desired behavior
- implementation
- test
- affected URLs
- rollback risk

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
