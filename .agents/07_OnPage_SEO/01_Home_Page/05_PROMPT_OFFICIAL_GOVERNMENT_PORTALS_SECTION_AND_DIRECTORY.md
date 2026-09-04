# Prompt 4 - Official Government Portals Section And Directory

Use this prompt to implement Section `32_OFFICIAL_GOVERNMENT_JOB_PORTALS` and the supporting full directory page.

## Prompt

You are creating the official government portals trust/reference system for SearchSarkariNaukri.

Primary objective:

Add a concise homepage Section 32 that points users toward official recruitment sources, and create or update one full internal directory page such as:

`/official-government-job-portals`

Do not dump every external government link directly onto the homepage. The homepage section should be a fast-loading summary that links to the full internal directory.

## Homepage Section 32 Requirements

Section heading:

`Official Government Job Portals`

Short description:

`Find recruitment information from official government sources, including central recruitment bodies, railway boards, banking recruiters, defence portals, Maharashtra authorities and state employment portals. Always verify eligibility, dates, fees and official notification details before applying.`

Primary CTA:

`View All Official Government Portals`

CTA destination:

`/official-government-job-portals`

Recommended groups:

1. Central Recruitment
2. Railway
3. Banking
4. Defence
5. Science And PSU
6. Maharashtra
7. State Employment Portals

Homepage should show only the top 4-6 entities per group and link to the full internal directory for the complete list.

## Full Directory Page Requirements

Create a structured internal page with:

1. H1: `Official Government Job Portals`
2. Intro explaining SearchSarkariNaukri is an independent information portal.
3. Official-source verification note.
4. Central Government section.
5. Railway recruitment section.
6. Banking recruitment section.
7. Defence recruitment section.
8. Science, technical, and PSU recruitment section.
9. Maharashtra authorities section.
10. State employment portals section.
11. Last verified date for each portal.
12. Source status: verified, needs review, temporarily unavailable.
13. Search/filter by category or state if the list is long.
14. FAQ.
15. Breadcrumbs.

## Portal Entities

Central:

- National Career Service
- Employment News / Rozgar Samachar
- UPSC
- UPSC Online
- SSC
- National Government Services Portal
- India.gov.in
- MyGov
- Digital India
- DoPT
- Ministry of Labour and Employment

Railway:

- Railway Recruitment Control Board
- RRB Mumbai
- RRB Ahmedabad
- RRB Prayagraj
- RRB Bengaluru
- RRB Bhopal
- RRB Bhubaneswar
- RRB Chandigarh
- RRB Chennai
- RRB Guwahati
- RRB Hyderabad
- RRB Kolkata
- RRB Patna
- RRB Ranchi
- RRB Secunderabad

Banking:

- IBPS
- SBI Careers
- RBI
- RBI Opportunities
- NABARD
- SEBI
- SIDBI
- LIC
- NIACL
- GIC Re

Defence:

- Indian Army
- Join Indian Navy
- Indian Air Force
- Indian Coast Guard
- DRDO
- Ministry of Defence
- Territorial Army
- NCC

Science, Technical, And PSU:

- ISRO
- CSIR
- BARC
- ICMR
- DBT
- DST
- NPCIL
- HAL
- BEL
- BHEL
- GAIL
- ONGC
- NTPC
- Coal India

Maharashtra:

- Maharashtra Government
- MPSC
- Maharashtra Police
- Mahaswayam Rojgar
- Maharashtra State Portal
- Maharashtra Public Health Department
- Maharashtra Forest Department
- Maharashtra Revenue Department
- Maharashtra School Education Department
- Maharashtra Skill Development
- Rural Development Maharashtra
- Urban Development Maharashtra

State Employment Portals:

- Gujarat Anubandham
- Haryana HREX
- Kerala Employment
- Madhya Pradesh Rojgar
- Maharashtra Mahaswayam Rojgar
- Odisha Employment
- Punjab Employment
- Rajasthan Employment
- Tamil Nadu Employment
- Uttar Pradesh Sewayojan
- West Bengal Employment Bank

## Database Recommendation

Use a structured table or config, not hard-coded scattered links:

```text
official_government_portals
- id
- name
- category
- state
- official_domain
- official_url
- recruitment_url
- description
- last_verified_at
- verification_status
- display_priority
```

## Link Policy

For external government links:

- verify the official domain before publishing
- use descriptive anchor text
- open safely with `rel="noopener noreferrer"` when using `target="_blank"`
- do not add unverified copied URLs
- do not hide affiliate/tracking links in official-source blocks
- do not route official government links through misleading redirects
- do not make external links the homepage's primary content

Internal link architecture:

- Homepage Section 32 links to `/official-government-job-portals`.
- Job detail pages link to exact official notifications.
- Department pages link to official department/career pages.
- State pages link to relevant state employment portals.
- Result/admit card pages link to official result/admit card sources.

## Structured Data

Use schema only when it matches visible content:

- `Organization` for SearchSarkariNaukri
- `WebPage` for the directory page
- `ItemList` for portal lists
- `FAQPage` only if FAQs are visible
- `BreadcrumbList` if breadcrumbs are visible

Do not use schema to imply SearchSarkariNaukri is an official government body.

## 404 And URL Cleanup

If an official portal URL fails:

- mark it `needs_review`
- do not publish the broken external link until verified
- remove broken links from homepage summary
- keep historical reference only if useful and clearly labelled

If an internal directory page or category page returns 404:

- restore it if useful
- redirect it if replaced
- remove it if not needed
- exclude it from sitemap if 404, 410, redirect, noindex, duplicate, or thin

## Final Validation

Return:

1. Section 32 implemented or updated
2. Full directory page created or updated
3. Portal entities added
4. External URLs verified
5. Broken portal links removed or marked needs review
6. Internal links added
7. Schema added and validated
8. Sitemap decision confirmed
9. Performance impact checked
10. Accessibility checked

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
