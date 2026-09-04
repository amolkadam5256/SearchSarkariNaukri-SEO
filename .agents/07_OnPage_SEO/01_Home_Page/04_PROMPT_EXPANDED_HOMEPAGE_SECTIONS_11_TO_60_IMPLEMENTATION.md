# Prompt 3 - Expanded Homepage Sections 11-60 Implementation

Use this prompt to complete the expanded homepage without damaging existing approved sections.

## Prompt

You are implementing the expanded SearchSarkariNaukri homepage.

Primary objective:

Preserve existing Sections `01-10` exactly as approved, then add and implement Sections `11-60` as fast-loading, semantic, SEO-friendly, AEO/GEO-ready homepage modules.

Do not delete existing sections. Do not replace the creative direction. Do not change navbar, footer, header, logo, global menu, analytics, tracking, global layout, global CSS, or unrelated pages.

## Read First

Read every file in:

`C:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\07_OnPage_SEO\01_Home_Page`

Required existing specs:

- `01_Hero/herosection.md`
- `02_LIVE_STATISTICS/homepage-live-statistics-db.md`
- `03_DAILY_ASSESSMENT/daily-assessment-section.md`
- `04_DIGITAL_LIBRARY/digital-library-section.md`
- `05_JOB_ALERTS/government-job-alerts-section.md`
- `06_EXAM_COUNTDOWN/exam-countdown-section.md`
- `07_CLOSING_SOON_JOBS/closing-soon-jobs-section.md`
- `08_EXISTING_TALATHI_FEATURED_RECRUITMENT/talathi-bharti-featured-section.md`
- `09_QUICK_JOB_FINDER/quick-job-finder-section.md`
- `10_LATEST_SARKARI_NAUKRI/latest-sarkari-naukri-section.md`
- `03_AUDIT_EXPANDED_HOMEPAGE_SECTIONS_11_TO_60_AND_OFFICIAL_PORTALS_2026-09-01.md`

## Required Section Build

Add these homepage modules after Section 10:

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

## Content Rules

For every new section:

- use one clear `h2`
- write concise helpful copy
- include useful internal links
- use real database-backed counts where needed
- avoid fake numbers
- avoid keyword stuffing
- avoid duplicate paragraphs
- avoid duplicate FAQ content
- avoid doorway-page patterns
- clearly mention official-source verification where relevant
- do not claim SearchSarkariNaukri is a government website

## Creative And UX Rules

Make each section useful and scannable:

- compact job-board style
- fast cards or dense link groups
- status labels for active, closing soon, result, admit card, guide
- horizontally scrollable chips on mobile
- equal-height cards where needed
- accessible controls and links
- no oversized marketing hero sections after the first hero
- no nested cards
- no heavy carousels
- no layout shifts

## Performance Rules

The page must load fast:

- server-render critical text
- lazy-load lower non-critical sections
- cache homepage queries
- batch database calls
- use responsive images
- reserve dimensions for images/cards
- limit animation to lightweight opacity/transform
- do not load video embeds by default
- do not fetch full official-portal data on first paint
- use internal summary pages for long lists

## URL And 404 Rules

For every link added:

- verify destination exists
- use canonical URL
- do not link to noindex pages unless intentionally useful for users and excluded from SEO blocks
- do not link to 404 or 410 pages
- if a linked page is no longer needed, remove it
- if it has a close replacement, redirect one-hop 301
- if it is permanently removed, return 410 and remove from sitemap

## Final Output Required

Return:

1. Files changed
2. Sections implemented
3. Existing Sections 01-10 preservation confirmation
4. New internal links added
5. External official portal links added
6. 404/410 links removed
7. Redirects added
8. Sitemap/schema changes
9. Accessibility fixes
10. Performance checks
11. Remaining risks

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
