# Section 12 - Department And Exam

## Purpose

Help users browse government jobs by department, recruiting authority and exam category.

## Recommended UI

- Heading: `Government Jobs By Department And Exam`
- Description: `Explore recruitment updates from major departments, commissions and exam authorities.`
- Group links into tabs or compact chips: UPSC, MPSC, SSC, Railway, Banking, Police, Defence, Teaching, Health.

## SEO Keywords

- government jobs by department
- recruitment exam notifications
- UPSC MPSC SSC Railway jobs
- department wise Sarkari Naukri

## Links

Use only existing canonical department/exam pages. Suggested targets: `/department/mpsc`, `/department/ssc`, `/department/railway`, `/department/police`, `/department/banking`, `/department/defence`, `/upsc`, `/ssc`.

## Rules

Do not create fake department pages. Remove links to 404 pages or keep them out until implemented.

## Performance And Accessibility

Chips must be keyboard reachable. Use descriptive anchors, not `click here`.

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
