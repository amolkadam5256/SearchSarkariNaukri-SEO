# Master Homepage Audit-First Implementation Prompt

Date: 2026-09-01
Project: SearchSarkariNaukri
Target page: `https://www.searchsarkarinaukri.com/`
Spec folder: `.agents/07_OnPage_SEO/01_Home_Page`

## Role

Act as a senior technical SEO specialist, semantic SEO architect, GEO/AEO specialist, information architect, UX/UI developer, front-end developer, content architecture specialist, internal-linking specialist, and government recruitment portal SEO consultant.

## Primary Objective

Audit the existing homepage first.

Do not immediately modify code.

Do not delete anything.

Do not replace existing sections.

Do not redesign approved sections unnecessarily.

Do not remove existing content, internal links, SEO content, metadata, or structured data unless it is technically incorrect and the reason is documented.

First determine exactly what is already implemented. Then compare the implementation against the complete 60-section homepage specification in this folder.

## Required Workflow

1. `AUDIT FIRST`
2. `REPORT SECOND`
3. `IMPLEMENT THIRD`
4. `VERIFY FOURTH`

Do not skip the audit/report phase.

## Source Of Truth

Use existing project files as the primary source of truth. Inspect the actual website code when available:

- homepage code
- components
- routes
- content files
- JSON/config files
- database models
- API endpoints
- SEO configuration
- sitemap
- robots configuration
- schema/structured-data components
- internal-link configuration
- job data
- location data
- organization data
- qualification data
- exam data
- admit-card data
- result data
- blog/news data
- image assets
- icons
- existing CSS/design system
- responsive layouts

## Preserve Existing Work

Sections `01-10` are already specified and approved:

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

If already implemented correctly, keep them.

If partially implemented, improve only the missing parts.

If incorrect, fix only what is required.

If visually approved, do not redesign unnecessarily.

The same rule applies to any other section that is already correctly implemented.

## No-Deletion Rule

Absolutely do not:

- delete existing sections
- delete existing components
- delete existing job data
- delete existing URLs
- delete existing internal links
- remove approved SEO copy
- remove existing metadata
- remove existing schema without a valid documented reason
- remove existing homepage modules

If something is weak, improve it.

If something is duplicated, report it first.

Do not silently delete it.

## Audit Status Definitions

Every section must receive exactly one status:

- `GREEN - IMPLEMENTED`: UI, content, functionality, links, SEO, responsive design, and major requirements are substantially complete.
- `YELLOW - PARTIALLY IMPLEMENTED`: section exists but important content, functionality, SEO, internal links, data, mobile, or schema is missing.
- `RED - MISSING`: section does not exist or only an empty placeholder exists.
- `PURPLE - DUPLICATE`: same intent is implemented elsewhere and creates unnecessary duplication.
- `BLACK - INCORRECT`: implementation creates SEO problems, wrong links, fake data, incorrect schema, incorrect semantic HTML, misleading government affiliation, broken functionality, or misleading recruitment information.

## Scoring System

Score every section out of `100`:

- UI/UX: `20`
- Content: `20`
- SEO: `20`
- GEO: `10`
- AEO: `10`
- Data/functionality: `10`
- Technical: `10`

Overall target: `95+/100`.

## Required Section Audit

Audit all 60 sections individually:

1. Hero
2. Live Statistics
3. Daily Assessment
4. Digital Library
5. Job Alerts
6. Exam Countdown
7. Closing Soon Jobs
8. Talathi Featured Recruitment
9. Quick Job Finder
10. Latest Sarkari Naukri
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
53. Admit Card / Result Discovery
54. Internal Linking Hub
55. UPSC Updates
56. Videos
57. Job News
58. AEO Direct Answers
59. Expanded FAQ
60. Share / Alert CTA

## Required Audit Categories

For every section check:

- UI
- content
- SEO
- GEO
- AEO
- internal links
- data/functionality
- mobile
- accessibility
- performance
- schema where applicable
- 404/410/redirect/noindex risks

## Location SEO Audit

Audit whether the homepage properly connects:

`India -> State -> Maharashtra -> District -> City -> Organization -> Department -> Job`

Check all 36 Maharashtra districts:

- Ahmednagar / Ahilyanagar
- Akola
- Amravati
- Aurangabad / Chhatrapati Sambhajinagar
- Beed
- Bhandara
- Buldhana
- Chandrapur
- Dhule
- Gadchiroli
- Gondia
- Hingoli
- Jalgaon
- Jalna
- Kolhapur
- Latur
- Mumbai City
- Mumbai Suburban
- Nagpur
- Nanded
- Nandurbar
- Nashik
- Dharashiv / Osmanabad
- Palghar
- Parbhani
- Pune
- Raigad
- Ratnagiri
- Sangli
- Satara
- Sindhudurg
- Solapur
- Thane
- Wardha
- Washim
- Yavatmal

Use current official district naming where applicable. Do not create duplicate district URLs only because historical and current names differ. Use redirects/canonicalization where necessary.

Also audit important Maharashtra cities, all Indian states and union territories, canonical naming, historical names, duplicate URLs, redirects, breadcrumbs, internal links, and location schema only where appropriate.

## Keyword Audit

Create a keyword coverage matrix with:

- keyword
- search intent
- current page
- current section
- present
- exact match
- semantic variation
- internal link
- priority

Required keyword groups:

- Primary: Sarkari Naukri 2026, Latest Sarkari Naukri, Government Jobs 2026, Latest Government Jobs
- Maharashtra: Maharashtra Government Jobs 2026, Maharashtra Sarkari Naukri, MPSC Recruitment 2026, MPSC Bharti, Police Bharti 2026, Talathi Bharti 2026, ZP Recruitment 2026
- Qualification: 10th Pass Government Jobs, 12th Pass Government Jobs, ITI Government Jobs, Diploma Government Jobs, Graduate Government Jobs
- Exam: UPSC Jobs, SSC Jobs, Railway Jobs, RRB Jobs, Banking Jobs, Defence Jobs, Police Jobs
- Location: Government Jobs in Pune, Mumbai, Nagpur, Nashik, Maharashtra
- Tracking: Government Admit Card, Government Exam Result, Government Exam Calendar, Recruitment Notification

## Official Link Audit

For every official government portal check:

1. URL exists.
2. HTTPS works.
3. Domain belongs to the correct authority.
4. Page loads.
5. Destination is relevant.
6. Recruitment information is current or correctly labelled.
7. No redirect goes to a suspicious site.

Maintain:

- official_url
- source_name
- authority
- category
- last_verified

Never invent URLs. Never link to suspicious recruitment domains.

## Internal Link Audit

Generate:

- orphan pages
- weak pages with only 1-2 internal links
- strong pages with meaningful contextual connections
- broken links
- redirect chains
- wrong canonical targets
- wrong slugs
- anchor text issues

Avoid excessive exact-match anchors and vague anchors such as `click here`.

Use descriptive contextual anchors.

## Technical SEO Audit

Check:

- title
- meta description
- H1
- H2/H3
- canonical
- robots
- sitemap
- pagination
- indexability
- noindex
- redirects
- status codes
- duplicate URLs
- query parameters
- trailing slash consistency
- HTTPS
- Open Graph
- Twitter/X metadata
- hreflang if applicable
- structured data
- breadcrumbs

## Structured Data Audit

Check appropriate use of:

- Organization
- WebSite
- SearchAction
- BreadcrumbList
- Article
- JobPosting
- Event
- VideoObject
- FAQPage where appropriate

Do not add schema merely for SEO. Schema must accurately represent visible page content. Do not create fake JobPosting data.

## AEO Audit

Check whether important answers can be extracted easily:

- question-based H2/H3
- direct answer first
- short paragraphs
- lists
- tables
- clear entities
- factual statements
- source references
- update timestamps

## Performance And Mobile Audit

Check:

- LCP
- INP
- CLS
- images
- fonts
- JavaScript
- CSS
- third-party scripts
- ads if applicable
- lazy loading
- preloading
- DOM size
- hydration
- API calls
- client-side rendering

Mobile widths to test:

- 320px
- 360px
- 375px
- 390px
- 412px
- 768px

## Accessibility Audit

Check:

- semantic HTML
- heading hierarchy
- keyboard navigation
- focus state
- contrast
- labels
- alt text
- ARIA
- screen reader behavior
- button names
- link names
- form errors

## Data Integrity Rules

Never fabricate:

- vacancies
- dates
- salary
- eligibility
- age
- selection process
- government approval
- subscriber count
- number of jobs
- exam dates

If unavailable, use:

- `Not specified`
- `To be announced`
- `Check official notification`

## Government Disclaimer

Audit whether the site clearly communicates:

SearchSarkariNaukri is an independent information portal.

It is not an official government website.

Users should verify recruitment information from the official recruiting authority before applying.

This must be visible and understandable.

## Implementation Phase

Only after audit and report:

1. Implement P0 and P1 issues first.
2. Implement missing sections.
3. Improve partial sections.
4. Improve internal linking.
5. Improve SEO/GEO/AEO.
6. Run final QA.

## Final Acceptance Criteria

Do not mark complete until:

- all 60 sections audited
- existing Sections 01-10 preserved
- missing sections identified
- missing sections implemented
- partial sections improved
- no duplicate SEO architecture introduced
- Maharashtra architecture complete
- all 36 Maharashtra districts audited
- major Maharashtra cities audited
- all Indian states and UTs audited
- qualification, post, organization, department architecture audited
- UPSC, SSC, Railway/RRB, Banking, Defence, Police/CAPF audited
- Admit Cards, Results, Exam Calendar, Study Material, Tools audited
- official government portals audited
- official URLs verified
- internal linking audited
- orphan pages identified
- broken links identified
- canonicals, sitemap, robots, structured data audited
- AEO questions implemented
- GEO location/entity relationships implemented
- image ALT attributes audited
- accessibility audited
- mobile audited
- Core Web Vitals audited
- no fake recruitment information
- no fake government affiliation
- no fake statistics
- no keyword stuffing
- no thin doorway pages
- final score calculated
- before/after score documented
- change log generated

## Most Important Instruction

Do not assume a section exists because a folder, component name, or menu item exists.

A section counts as implemented only when its UI, content, functionality, SEO, links, and responsive behavior are actually implemented.

A link counts as implemented only when it resolves to the correct live destination.

A keyword counts as implemented only when it is naturally integrated into useful content.

A location counts as implemented only when the corresponding useful page, data, and link exist.

An official government portal counts as implemented only when the URL has been verified.

A schema type counts as implemented only when valid structured data is actually generated.

An AEO section counts as implemented only when actual question-answer content exists.

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
