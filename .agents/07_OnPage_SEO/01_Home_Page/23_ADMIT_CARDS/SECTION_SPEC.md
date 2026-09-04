# Section 23 - Admit Cards

## Purpose

Surface latest admit card updates and connect job seekers to exam next steps.

## Recommended UI

- Heading: `Latest Admit Cards`
- Description: `Check admit card release updates, exam dates, download status and official source details.`
- Show latest 4-6 admit cards and CTA to all admit cards.

## SEO Keywords

- latest admit card
- government exam admit card
- Sarkari admit card 2026
- exam hall ticket

## Links

- `/admit-cards`
- related visible admit-card detail URLs

## Rules

Do not show an admit card as released unless verified. Remove detail links that return 404/410.

## Performance And Accessibility

Use compact list cards with dates and status.

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
