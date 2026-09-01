# Section 32 - Official Government Job Portals

## Purpose

Add a trust/reference section that helps users verify recruitment from official government sources.

## Recommended UI

- Heading: `Official Government Job Portals`
- Description: `Find recruitment information from official sources including central recruitment bodies, railway boards, banking recruiters, defence portals, Maharashtra authorities and state employment portals.`
- Groups: Central Recruitment, Railway, Banking, Defence, Science And PSU, Maharashtra, State Employment Portals.
- CTA: `View All Official Government Portals`
- CTA URL: `/official-government-job-portals`

## SEO Keywords

- official government job portals
- official recruitment websites
- UPSC SSC RRB MPSC official portal
- government employment portals

## Portal Entities

Central: National Career Service, Employment News, UPSC, UPSC Online, SSC, India.gov.in, MyGov, Digital India, DoPT, Ministry of Labour and Employment.

Railway: Railway Recruitment Control Board, RRB Mumbai, RRB Ahmedabad, RRB Prayagraj, RRB Bengaluru, RRB Bhopal, RRB Chennai, RRB Kolkata, RRB Patna, RRB Secunderabad.

Banking: IBPS, SBI Careers, RBI, NABARD, SEBI, SIDBI, LIC, NIACL, GIC Re.

Defence: Indian Army, Join Indian Navy, Indian Air Force, Indian Coast Guard, DRDO, Ministry of Defence, Territorial Army, NCC.

Science/PSU: ISRO, CSIR, BARC, ICMR, DBT, DST, NPCIL, HAL, BEL, BHEL, GAIL, ONGC, NTPC, Coal India.

Maharashtra: Maharashtra Government, MPSC, Maharashtra Police, Mahaswayam Rojgar, Public Health Department, Forest, Revenue, Education, Skill Development, Rural Development, Urban Development.

State Employment: Gujarat Anubandham, Haryana HREX, Kerala Employment, MP Rojgar, Maharashtra Mahaswayam, Odisha Employment, Punjab Employment, Rajasthan Employment, Tamil Nadu Employment, UP Sewayojan, West Bengal Employment Bank.

## Rules

Do not dump all external links on homepage. Show grouped highlights and link to the internal directory. Verify official URLs before publishing.

## Performance And Accessibility

Use static grouped cards. Do not fetch the full portal directory during initial homepage render.

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
