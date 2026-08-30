# BATCH 01 — INTERNAL LINK AUDIT

Build the topical graph:
Admit Cards Hub → Admit Card → Exam → Recruitment/Jobs → Result → Calendar.

For each URL report:
- hub link
- exam link
- jobs link
- results link
- calendar link
- related admit cards
- descriptive anchor quality
- broken links
- orphan status

Do not add unrelated links merely for link count.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
