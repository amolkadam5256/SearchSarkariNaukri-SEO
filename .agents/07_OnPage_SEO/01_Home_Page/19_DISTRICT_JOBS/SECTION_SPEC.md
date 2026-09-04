# Section 19 - District Jobs

## Purpose

Route users to district-level government job pages, especially Maharashtra districts.

## Recommended UI

- Heading: `Government Jobs By District`
- Description: `Browse district-wise job updates, local departments, recent recruitment and nearby opportunities.`
- Use a searchable compact district list or priority grid.

## SEO Keywords

- district wise government jobs
- Maharashtra district jobs
- Sarkari Naukri by district
- local government jobs

## Links

Use existing `/districts/{district}` pages only. Link to `/districts` for the full index.

## Rules

Do not generate links for districts that return 404. District pages must have useful content before being indexable.

## Performance And Accessibility

Do not render a huge list above the fold. Use progressive disclosure.

---

## Universal Developer Guardrail

Apply this rule before using this file for implementation:

1. Audit the existing homepage/component first.
2. Do not delete existing sections, components, internal links, SEO copy, metadata, schema, job data, or URLs without explicit approval.
3. Preserve approved Sections `01-10`; patch only verified issues.
4. If this section already exists in code, improve the existing component instead of rebuilding it unnecessarily.
5. Never invent vacancies, dates, salary, eligibility, age limits, selection process, official links, job counts, subscriber counts, exam dates, or government approval.
6. Verify every internal URL and official external URL before publishing.
7. Remove or replace links to true `404`/`410` pages; keep those URLs out of sitemap, schema, breadcrumbs, related links, and internal-link hubs.
8. Use one-hop `301` only when there is a close relevant replacement.
9. Do not create thin doorway pages, duplicate SEO pages, keyword-stuffed sections, or fake urgency.
10. Do not change navbar, footer, header, logo, global menu, global styles, analytics, tracking, or unrelated routes unless a documented bug requires it and regression QA is completed.
11. SearchSarkariNaukri must be described as an independent information portal, not an official government website.
12. Final signoff requires audit, implementation, live URL/status checks, sitemap/canonical/robots/schema validation, mobile QA, accessibility QA, and performance QA.
