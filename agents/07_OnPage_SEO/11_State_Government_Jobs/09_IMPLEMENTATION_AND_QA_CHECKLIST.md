# 09 — Developer Implementation & QA Checklist

**Target Hub:** `https://www.searchsarkarinaukri.com/category/state-government-jobs` (or `/state-government-jobs`)  
**Scope:** Verification of all 20 Master Additions, schema validation, link graph health, and performance budgets.

---

## Pre-Release Gate: Content Preservation Verification

Before pushing any build, developers and QA must verify that **ZERO EXISTING CONTENT HAS BEEN REMOVED**:

- [ ] Existing H1 is intact: `State Wise Sarkari Naukri 2026 — Government Jobs by State and UT`.
- [ ] Existing introductory paragraphs remain visible.
- [ ] Existing "Most Searched States" card grid is untouched.
- [ ] Existing "All States and Union Territories" directory with dynamic vacancy counts is intact.
- [ ] Existing Maharashtra highlight section is preserved and only appended to.
- [ ] Existing Central vs State text is preserved and expanded into the comprehensive comparison matrix.
- [ ] Existing FAQ query intents are fully preserved and answered.
- [ ] Breadcrumbs, footer navigation, and community links are intact.

---

## 20 Master Additions Implementation QA

Verify each of the 20 master sections from `03_PAGE_CONTENT_ADDITIONS.md`:

- [ ] **1. Quick Overview:** 2–3 paragraphs explaining state jobs, recruiting bodies, targeting exact keywords (`state government jobs 2026`, `state wise government jobs`, `latest state govt vacancies`, `state sarkari naukri`, `government jobs by state`).
- [ ] **18. Freshness Strip:** `<time>` tag rendered with dynamic update date, active count computation note, and notification lifecycle explanation.
- [ ] **2. Jobs by Qualification:** 7 cards linking to 10th, 12th, Graduate, Diploma, ITI, Engineering, and Postgraduate pages.
- [ ] **3. Jobs by Major Recruitment Type:** 10 categories (State PSC, Police, Teacher, Health, Revenue, Municipal, District/ZP, State PSU, Judiciary, Forest).
- [ ] **13. Popular State Government Exams:** Cards for MPSC Rajyaseva, UPPSC PCS, BPSC CCE, MPPSC, RPSC RAS, Police Bharti, TET, Health Recruitment.
- [ ] **5. Central vs State Comparison:** Comprehensive 7-row table (Authorities, Posting, Domicile, Language, Transfers, Exam Pattern, Examples) + internal links to All Jobs, UPSC, SSC, Railway, Banking.
- [ ] **6. Domicile Rules:** Authoritative guide covering compulsory vs open posts, local reservation quotas, state certificates, and notification primacy.
- [ ] **7. Language Requirements:** Detailed section on regional language tests, reading/writing proficiency, and Class 10/12 requirements (Marathi, Hindi, etc.).
- [ ] **8. Age Limits & Relaxation:** Full table covering Min/Max age, SC/ST (+5), OBC (+3), PwBD (+10), Ex-SM, and state relaxations + Age Calculator CTA.
- [ ] **9. How to Check Eligibility:** 7-step criteria checklist + Eligibility Checker CTA.
- [ ] **11. How to Apply:** 8 clear, sequential steps from downloading notice to saving confirmation slip.
- [ ] **10. Documents Usually Required:** 12-item document readiness checklist.
- [ ] **12. Official State PSC Directory:** Table of all 28 states with official PSC URLs clearly labeled "Official Website" and `rel="noopener noreferrer"`.
- [ ] **14. Location / District Jobs:** Expanded Maharashtra highlight with links to Pune, Mumbai, Nagpur, Nashik, and `/districts`.
- [ ] **15. Upcoming State Government Jobs:** Section covering expected notifications, upcoming exams, deadlines + link to Exam Calendar.
- [ ] **16. Recently Closed Recruitment:** Expired notice guidance: exam calendar, admit cards, results, alert subscription.
- [ ] **17. Verification Methodology:** E-E-A-T trust block explaining editorial fact-checking against official gazette notifications.
- [ ] **19. Related Resources:** 14-link contextual resource matrix connecting candidate tools and hubs.
- [ ] **20. 15 Detailed FAQs:** All 15 requested FAQs rendered in accessible HTML accordions.

---

## Technical SEO & Indexability QA

- [ ] Target page returns **HTTP 200 OK**.
- [ ] Canonical URL is self-referencing and consistent across sitemaps and headers.
- [ ] Title tag: `State Government Jobs 2026: State Wise Sarkari Naukri & PSC Vacancies`.
- [ ] Meta description is unique, under 160 characters, and contains key target terms.
- [ ] Exactly one `<h1>` tag exists on the page.
- [ ] No broken heading hierarchy (no H2 directly followed by H4).
- [ ] Page is included in `sitemap-static.xml` with appropriate `<lastmod>`.
- [ ] `robots.txt` does not disallow the target page or linked state hubs.
- [ ] All critical body copy, headings, and FAQs exist in the raw SSR HTML response.

---

## Internal Link & External Link QA

- [ ] All internal links return **HTTP 200 OK** without intermediate 301/302 redirects.
- [ ] No internal links contain dev/staging domains or mixed HTTP/HTTPS protocols.
- [ ] Zero internal links have `rel="nofollow"`.
- [ ] Every external State PSC URL points to a verified government domain (`.gov.in`, `.nic.in`).
- [ ] All external links open with `rel="noopener noreferrer"`.
- [ ] All external links are visibly identifiable with an external icon or "Official Website" label.

---

## Structured Data (JSON-LD) QA

- [ ] Validated with **Google Rich Results Test** and **Schema.org Validator** with 0 errors.
- [ ] `BreadcrumbList` matches the visible navigational path.
- [ ] `CollectionPage` contains an `ItemList` with exact item count (31 items).
- [ ] `FAQPage` matches visible HTML FAQ questions and answers verbatim.
- [ ] **NO `JobPosting` structured data** is present on this directory page.
- [ ] `dateModified` reflects the actual last update timestamp.

---

## Mobile UX & Core Web Vitals QA

- [ ] Tested on viewport widths: 360px (mobile small), 390px (iPhone), 768px (tablet), 1200px+ (desktop).
- [ ] Official PSC table and Central vs State comparison table scroll smoothly without causing horizontal page viewport overflow.
- [ ] FAQ accordion toggles operate seamlessly via keyboard (Tab + Enter/Space) and update `aria-expanded`.
- [ ] Touch tap targets for state cards and qualification links are at least 44x44px.
- [ ] Cumulative Layout Shift (CLS) remains `< 0.05` during dynamic count hydration.
- [ ] Largest Contentful Paint (LCP) `< 2.5s` on 4G mobile emulation.
