# 00 — MASTER STATE GOVERNMENT JOBS PAGE AUDIT

**Page Target:** `/category/state-government-jobs` (or `/state-government-jobs`)  
**Audit Date:** October 2026  
**Priority:** P0 (Core Hub)  
**Status:** Audit Completed & Developer Implementation Spec Ready  

---

## 1. Executive Summary

The State Government Jobs page is one of the highest-value directory hubs on SearchSarkariNaukri. It currently serves as a state navigation index showing vacancy counts across Indian states and Union Territories, with an existing comparison between central and state jobs, a Maharashtra highlight block, and three initial FAQs.

However, from an **SEO, GEO (Generative Engine Optimization), AEO (Answer Engine Optimization), and user-intent** perspective, the page previously lacked substantive educational depth, qualification shortcuts, exam pathways, domicile/language rules, step-by-step application instructions, and comprehensive official verification sources.

### Core Implementation Rule
**DO NOT DELETE OR OVERWRITE ANY EXISTING CONTENT.**  
All existing state cards, vacancy counts, introduction copy, Maharashtra section, and Central vs State text must be preserved. The new sections are added around and underneath the existing content to transform the page into an authoritative national State Government Jobs topic hub.

---

## 2. Requirement-by-Requirement Audit & Implementation Status

| # | Master Section Required | Purpose & Intent | Status in Implementation Pack |
|---|---|---|---|
| 1 | **State Government Jobs 2026 – Quick Overview** | Captures broad queries (`state government jobs 2026`, `state wise government jobs`, `latest state govt vacancies`, `state sarkari naukri`, `government jobs by state`) and explains recruiting bodies. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 2 | **Latest State Government Jobs by Qualification** | 7 internal link anchors (10th, 12th, Graduate, Diploma, ITI, Engg, PG) capturing dual-intent search. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` & `04_INTERNAL_LINKING_ARCHITECTURE.md` |
| 3 | **Government Jobs by Major Recruitment Type** | 10 state recruitment categories (PSC, Police, Teacher, Health, Revenue, Municipal, District/ZP, State PSU, Judiciary, Forest). | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 4 | **How State Government Recruitment Works** | Linear 8-stage recruitment pipeline formatted for AEO / AI search citation. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 5 | **State Government Jobs vs Central Government Jobs** | Expanded side-by-side comparison matrix across 7 dimensions + internal links to All Jobs, UPSC, SSC, Railway, Banking. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 6 | **Domicile Rules for State Government Jobs** | Authoritative guidance on compulsory vs open posts, local reservation, certificates, and notification primacy. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 7 | **Language Requirements in State Recruitment** | Regional language tests, reading/writing proficiency, Marathi/Hindi examples. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 8 | **Age Limits & Age Relaxation** | Minimum/maximum age breakdown, category relaxations (SC/ST, OBC, PwBD, Ex-SM) + Age Calculator CTA. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 9 | **How to Check Eligibility** | 7 key eligibility criteria checklist + Eligibility Checker CTA. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 10 | **How to Apply for State Government Jobs** | Practical 8-step application walkthrough. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 11 | **Documents Usually Required** | Complete 12-item document readiness checklist. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 12 | **Official State PSC / Recruitment Websites** | Comprehensive 28-state table with verified official URLs labeled "Official Website". | Ready in `03_PAGE_CONTENT_ADDITIONS.md` & `05_EXTERNAL_AUTHORITY_LINKS.md` |
| 13 | **Popular State Government Exams** | Major exam family cards (MPSC Rajyaseva, UPPSC PCS, BPSC CCE, MPPSC, RPSC RAS, Police Bharti, TET, Health). | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 14 | **Jobs by Location / District** | Expanded Maharashtra section with links to Pune, Mumbai, Nagpur, Nashik, and `/districts`. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 15 | **Upcoming State Government Jobs** | Expected notifications, exam dates, deadlines + link to Exam Calendar. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 16 | **Recently Closed Recruitment / What to Do Next** | Post-application / expired result guidance: latest jobs, admit cards, results, alerts. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 17 | **How SearchSarkariNaukri Verifies Listings** | E-E-A-T trust block explaining editorial verification against official government notifications. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 18 | **Last Updated / Freshness Section** | Dynamic timestamp, active vacancy count logic, notification update cycle note. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 19 | **Related Government Job Resources** | Comprehensive 14-link internal resource grid connecting candidate tools and hubs. | Ready in `03_PAGE_CONTENT_ADDITIONS.md` |
| 20 | **15 Detailed FAQs** | 15 exhaustive, crawlable FAQs with matching JSON-LD structured data. | Ready in `07_FAQ_15.md` & `08_SCHEMA_JSONLD.md` |

---

## 3. Sprint Roadmap for Engineering

### Sprint 1: P0 (Immediate Delivery)
1. Server-side render all new content blocks from `03_PAGE_CONTENT_ADDITIONS.md` around existing components.
2. Render the 15 complete FAQs in `07_FAQ_15.md` as accessible HTML accordions.
3. Inject validated `BreadcrumbList`, `CollectionPage`, `ItemList`, and `FAQPage` JSON-LD from `08_SCHEMA_JSONLD.md`.
4. Deploy the metadata updates (Title, Meta Description, Open Graph, Canonical).

### Sprint 2: P1 (Dynamic Modules & Linking)
1. Connect dynamic `{{last_updated_date}}` and ensure active counts stay in sync with database queries.
2. Build the optional dynamic "Closing Soon" state job cards module.
3. Validate all internal links across qualifications, departments, districts, exams, and candidate tools.
4. Verify all 28+ official PSC external URLs open with `rel="noopener noreferrer"`.

### Sprint 3: P2 (QA, Indexing & Monitoring)
1. Run full QA checklist in `09_IMPLEMENTATION_AND_QA_CHECKLIST.md`.
2. Inspect URL in Google Search Console and verify server-rendered HTML.
3. Submit updated URL to IndexNow and refresh XML sitemap lastmod.
