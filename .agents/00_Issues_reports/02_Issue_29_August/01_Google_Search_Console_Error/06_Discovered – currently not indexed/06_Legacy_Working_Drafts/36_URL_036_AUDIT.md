# URL 036 — FIRST-50 BATCH AUDIT

> Replace `{
SUPPLIED_URL_36
}` with the exact URL from the user's first-50 URL list. Do not invent or reorder the URL.

## Exact URL
`{SUPPLIED_URL_36}`

## Audit Requirement
Perform the complete audit defined in `00_MASTER_PROMPT.md` and `01_INDIVIDUAL_URL_AUDIT_TEMPLATE.md`.

### Mandatory checks
- HTTP/status/redirects
- canonical/robots/sitemap
- title/meta/H1
- H2/H3/H4-H6 hierarchy
- semantic HTML
- content completeness
- unique content
- 10–15 FAQs where supported
- official source
- dates/status
- internal links
- related pages
- GEO
- AEO
- JSON-LD/schema
- accessibility
- Next.js SSR/rendering
- Core Web Vitals/performance
- duplicate/thin/historical classification
- exact developer fix
- validation method

### Output
Provide:
1. Evidence
2. Problem
3. Severity
4. Exact fix
5. Expected after-state
6. Acceptance test

Do not mark anything "fixed" without testing it.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
