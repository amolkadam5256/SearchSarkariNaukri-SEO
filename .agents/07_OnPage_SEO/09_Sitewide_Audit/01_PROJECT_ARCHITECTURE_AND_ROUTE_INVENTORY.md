# Project Architecture and Route Inventory — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 2. First: Understand the Existing Project

Before making changes, inspect the repository and document its current architecture.

- [ ] Identify the React framework: React, Next.js, Vite, or another setup.
- [ ] Identify the package manager and inspect package scripts and dependencies.
- [ ] Map the application routes and dynamic routes.
- [ ] Identify all public-facing pages, page templates, and content types.
- [ ] Inspect shared layouts, navigation, footer, cards, tables, forms, and reusable components.
- [ ] Identify the CMS, database, APIs, content files, or other data sources.
- [ ] Identify the rendering strategy for each page: server-rendered, static, client-rendered, or hybrid.
- [ ] Review metadata generation, canonical URL handling, robots directives, sitemap generation, and structured data.
- [ ] Inspect existing analytics, Search Console integrations, and consent mechanisms.
- [ ] Identify redirects, legacy URLs, duplicate pages, broken routes, and known technical issues.
- [ ] Check existing project rules, agent instructions, documentation, and development conventions.
- [ ] Establish the current baseline before modifying code.

Deliverable: a route inventory, architecture summary, baseline findings, and prioritized audit checklist.

## 3. Website-Wide Page Inventory

Create a central inventory of all discoverable routes. Include, where applicable:

- [ ] Homepage.
- [ ] Government exam listings.
- [ ] Individual exam detail pages.
- [ ] Latest government jobs and recruitment notifications.
- [ ] Individual job detail pages.
- [ ] Admit cards.
- [ ] Results and merit lists.
- [ ] Answer keys.
- [ ] Syllabus and exam patterns.
- [ ] Previous-year question papers.
- [ ] Exam calendars and important dates.
- [ ] Eligibility, age limits, application fees, and selection processes.
- [ ] State-wise recruitment pages.
- [ ] Organization- or department-wise pages.
- [ ] Category and archive pages.
- [ ] Search results and filters.
- [ ] Educational articles and guides.
- [ ] About, contact, editorial policy, corrections policy, and privacy pages.
- [ ] Other existing routes discovered in the project.

For each route, record its URL, page type, purpose, indexability, canonical URL, title, meta description, H1, content status, internal links, source references, schema, performance, and audit status.

Do not assume that every route should be indexed. Determine indexation based on actual value, uniqueness, search intent, and the site's technical rules.

## Detailed developer instructions

Inspect framework, package scripts, routes, templates, components, data sources, rendering, metadata, analytics and existing rules. Inventory every discovered public route and compare code routes with sitemap/crawl/Search Console evidence. Record purpose, indexability decision/reason, canonical, metadata, content/source status, links, schema, performance evidence and audit state. Do not assume every URL should index.

## Pass 1 — Audit and implementation

- [ ] Inspect current code/data and capture reproducible baseline evidence.
- [ ] Identify affected routes/components; preserve useful content, records, URLs and working behavior.
- [ ] Record confirmed findings and distinguish evidence from assumptions.
- [ ] Assign priority; document fix, expected result, dependencies and approvals.
- [ ] Implement only scoped approved changes using project conventions.
- [ ] Run applicable local checks; record exact commands/results.
- [ ] Record changed files/components and unresolved items.

## Pass 2 — Independent verification

- [ ] Recheck the original issue against rendered routes or actual system behavior.
- [ ] Verify content/data preservation and applicable metadata, schema and links.
- [ ] Exercise desktop/mobile, keyboard and relevant loading/empty/error/success states.
- [ ] Inspect relevant console/network output and regression paths.
- [ ] Attach reproducible evidence; mark passed, failed, blocked or untested.
- [ ] Keep unresolved items open; code changes or a passing build alone do not prove success.

## Completion record

- Pass 1 owner/date/status: ____________________
- Pass 1 evidence: ____________________
- Pass 2 reviewer/date/status: ____________________
- Pass 2 evidence: ____________________
- Open issues/dependencies: ____________________
