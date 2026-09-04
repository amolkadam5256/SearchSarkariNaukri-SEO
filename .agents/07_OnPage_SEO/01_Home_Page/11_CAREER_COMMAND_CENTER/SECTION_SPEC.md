# Section 11 - Career Command Center

## Purpose

Create a compact dashboard-style section that helps users choose the next best action after landing on the homepage: search jobs, check eligibility, track deadlines, download admit cards, check results, or prepare for exams.

## Recommended UI

- Heading: `Career Command Center`
- Description: `Find jobs, verify eligibility, track important dates and prepare for government exams from one place.`
- Use 6 action cards: Search Jobs, Check Eligibility, Closing Soon, Admit Cards, Results, Exam Calendar.
- Each card should use an icon, short label, one-line explanation and a clear internal link.

## SEO Keywords

- government job search
- Sarkari Naukri dashboard
- government exam updates
- admit card result job alerts

## Links

- `/jobs`
- `/eligibility-checker`
- `/closing-soon`
- `/admit-cards`
- `/results`
- `/exam-calendar`

## Rules

Use live/canonical internal URLs only. If a linked page returns 404 and is not needed, remove the card. If it is useful, restore 200 or redirect to the closest relevant page.

## Performance And Accessibility

Keep cards lightweight, semantic, keyboard-accessible and responsive. Do not load heavy scripts.

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
