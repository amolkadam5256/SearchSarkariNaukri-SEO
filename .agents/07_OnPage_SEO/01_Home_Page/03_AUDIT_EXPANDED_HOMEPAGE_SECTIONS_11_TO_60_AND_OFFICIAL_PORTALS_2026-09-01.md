# Expanded Homepage Sections 11-60 And Official Portals Audit

Date: 2026-09-01
Folder: `.agents/07_OnPage_SEO/01_Home_Page`
Page: `https://www.searchsarkarinaukri.com/`

## Final Audit Verdict

Status: `GUIDANCE ADDED / EXISTING SECTIONS MUST NOT BE REPLACED`

The current workspace contains detailed homepage implementation briefs for Sections `01-10`. The uploaded guidance describes an expanded homepage architecture through Sections `11-60`, including `32_OFFICIAL_GOVERNMENT_JOB_PORTALS`.

This audit confirms the next development work should:

- preserve Sections `01-10`
- add or complete Sections `11-60`
- add an official government portals section as a trust/reference module
- keep the homepage fast, semantic, crawlable, and visually attractive
- avoid bulk external-link dumping
- avoid changing navbar, footer, header, logo, analytics, tracking, or global layout

## Critical Guardrail

Do not delete, rename, replace, or rewrite these approved existing modules:

1. `01_Hero`
2. `02_LIVE_STATISTICS`
3. `03_DAILY_ASSESSMENT`
4. `04_DIGITAL_LIBRARY`
5. `05_JOB_ALERTS`
6. `06_EXAM_COUNTDOWN`
7. `07_CLOSING_SOON_JOBS`
8. `08_EXISTING_TALATHI_FEATURED_RECRUITMENT`
9. `09_QUICK_JOB_FINDER`
10. `10_LATEST_SARKARI_NAUKRI`

Only correct an existing section if there is a proven technical, factual, accessibility, performance, SEO, AEO, GEO, schema, or broken-link issue.

## Expanded Homepage Architecture

Add or complete these additional sections as modular homepage blocks:

11. Career Command Center
12. Department And Exam
13. Qualification
14. Job Type
15. Age Eligibility
16. Freshers
17. Women Jobs
18. Maharashtra Jobs
19. District Jobs
20. City Jobs
21. State Jobs
22. Organization / Recruiter Directory
23. Admit Cards
24. Results
25. Exam Calendar
26. Tools
27. Study Material
28. How It Works
29. Verification
30. Trust / Why Choose Us
31. SEO Introduction
32. Official Government Job Portals
33. UPSC
34. SSC
35. Railways / RRB
36. Banking
37. Defence
38. Police / CAPF
39. Maharashtra Recruitment Authorities
40. Maharashtra Department-Wise Jobs
41. Complete District SEO
42. City SEO
43. All India State SEO
44. Qualification SEO
45. Post-Wise SEO
46. Government Jobs Without Written Exam
47. Document Guide
48. How To Apply
49. Recruitment Verification Process
50. Application Journey
51. Exam Preparation Hub
52. Popular Searches
53. Admit Card Result Discovery
54. Internal Linking Hub
55. UPSC Updates
56. Videos
57. Job News
58. AEO Direct Answers
59. Expanded FAQ
60. Share Alert CTA

## Official Government Portals Audit

Section `32_OFFICIAL_GOVERNMENT_JOB_PORTALS` must be a trust and verification section, not a giant external-link directory.

Purpose:

- help users verify recruitment from official sources
- strengthen entity trust
- support E-E-A-T and AEO/GEO understanding
- route users to one internal official-portals page for the full directory

Homepage display rule:

- Show only curated portal groups on the homepage.
- Link to one internal page such as `/official-government-job-portals` for the complete directory.
- External government links should be contextual, limited, and verified.
- Add external links with proper attributes such as `rel="noopener noreferrer"` and use `nofollow` or `sponsored` only if required by policy. Official-source references can remain normal editorial links if verified and useful.

Recommended homepage portal groups:

1. Central Recruitment
2. Railway Recruitment
3. Banking Recruitment
4. Defence Recruitment
5. Science And PSU Recruitment
6. Maharashtra Recruitment Authorities
7. State Employment Portals

## Government Portal Entities To Include

Central Government:

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

## SEO And UX Rule For Government Links

Do not make the homepage look like a link farm.

Better architecture:

- homepage shows a concise trust module
- full internal page stores verified official portal directory
- job detail pages link to the exact official notification/source
- department pages link to official department/career pages
- state/district pages link to relevant official state portals

## Fast Loading Requirements

The expanded homepage must remain fast:

- lazy-load lower sections
- avoid heavy carousels
- avoid loading all 60 sections with expensive database queries at once
- server-render critical SEO text
- cache counts and list queries
- use pagination or compact previews where content is large
- reserve image/card dimensions to avoid CLS
- use modern image formats and responsive sizes
- do not block initial rendering with analytics, animations, or portal-directory data
- render only summary cards on homepage and link to deeper pages

## Semantic HTML Requirements

Use:

- one `h1` on the homepage
- logical `h2` for each major section
- `section` with accessible labels
- real anchor links for internal navigation
- lists for grouped links
- tables only for tabular data
- `time` elements for dates where possible
- `article` or list items for job cards where appropriate
- visible text matching schema

Avoid:

- keyword-stuffed headings
- hidden SEO text
- duplicate FAQ blocks
- random external links
- fake government branding
- presenting SearchSarkariNaukri as an official government website

## 404 And Removed URL Rule

If any homepage section points to a page or URL that returns `404`:

- remove the link if the page is not needed
- restore the page to `200 OK` if it is valid and useful
- redirect with one-hop `301` only if there is a close relevant replacement
- return `410 Gone` if it is permanently removed
- remove the URL from sitemap, schema, breadcrumbs, related links, and internal-link hubs

Do not redirect unrelated URLs to the homepage.

## Signoff Checklist

Before approving the expanded homepage:

- Sections 01-10 are preserved.
- Sections 11-60 are added only as modular blocks.
- Government portal links are verified and grouped.
- Full portal directory is moved to an internal page, not dumped on homepage.
- All links return live status or are removed.
- No 404/410/noindex/redirect URL is included in sitemap.
- Homepage remains mobile friendly.
- Lighthouse/PageSpeed is checked.
- Schema validates.
- FAQ matches visible text.
- SearchSarkariNaukri is clearly described as an independent information portal.
- Navbar/footer/header/global styles are not changed.

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
