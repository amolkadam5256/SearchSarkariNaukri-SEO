# 10 — Developer Master Implementation Prompt

**Target Hub:** `https://www.searchsarkarinaukri.com/category/state-government-jobs` (or `/state-government-jobs`)  
**Implementation Priority:** P0 (Core Directory Upgrade)  
**Task Type:** On-Page SEO / GEO / AEO Expansion & Topic Hub Transformation

---

## 1. Developer Hard Rules (Non-Negotiable)

1. **PRESERVE ALL EXISTING CONTENT:** Do NOT delete, shorten, hide, or replace any existing page elements. You must keep:
   - Existing Hero H1 (`State Wise Sarkari Naukri 2026 — Government Jobs by State and UT`)
   - Existing introductory paragraphs
   - Existing "Most Searched States" cards
   - Existing "All States and Union Territories" directory with all dynamic vacancy counts
   - Existing Maharashtra highlight section (append only)
   - Existing Central vs State recruitment section (expand into full comparison)
   - Existing FAQ query coverage (expand around them into 15 total)
   - Existing navigation, footer, breadcrumbs, and community links
2. **STRICT SERVER-SIDE RENDERING:** All new content blocks, headings, internal links, the PSC table, and the 15 FAQs must be rendered in the server-side HTML response. Never render them via client-only lazy fetch.
3. **EXACT FLOW SEQUENCE:** You must implement the 20 master additions according to the recommended page flow defined below.

---

## 2. Master Page Component Sequence

```text
[Existing Breadcrumb: Home › State Government Jobs]
[Existing Hero / H1: State Wise Sarkari Naukri 2026 — Government Jobs by State and UT]
    ↓
1. NEW: State Government Jobs 2026 – Quick Overview (<StateJobsOverview />)
18. NEW: Last Updated / Freshness Strip (<FreshnessBanner />)
    ↓
[Existing Component: Most Searched States Grid]
[Existing Component: All States & Union Territories Directory with Dynamic Counts]
    ↓
2. NEW: Latest State Government Jobs by Qualification (<JobsByQualification />)
3. NEW: Government Jobs by Major Recruitment Type (<JobsByRecruitmentType />)
13. NEW: Popular State Government Exams (<PopularStateExams />)
    ↓
5. EXPANDED: State Government Jobs vs Central Government Jobs (<CentralVsStateComparison />)
    ↓
6. NEW: Domicile Rules for State Government Jobs (<DomicileRulesGuide />)
7. NEW: Language Requirements in State Government Recruitment (<LanguageRequirementsGuide />)
8. NEW: Age Limits & Age Relaxation with CTA (<AgeLimitsSection />)
9. NEW: How to Check Eligibility with CTA (<EligibilityGuideSection />)
11. NEW: How to Apply for State Government Jobs 8-Step Guide (<HowToApplySection />)
10. NEW: Documents Usually Required Checklist (<DocumentsRequiredSection />)
12. NEW: Official State PSC / Recruitment Websites Directory Table (<OfficialPSCDirectory />)
    ↓
14. EXPANDED: Maharashtra Highlight & District Jobs (<DistrictJobsSection />)
    ↓
15. NEW: Upcoming State Government Jobs & Expected Notifications (<UpcomingStateJobs />)
16. NEW: Recently Closed Recruitment / What to Do Next (<RecentlyClosedJobs />)
17. NEW: How SearchSarkariNaukri Verifies Listings (<VerificationMethodology />)
19. NEW: Related Government Job Resources 14-Link Grid (<RelatedResourcesMatrix />)
    ↓
20. EXPANDED: 15 Detailed FAQs in Accessible Accordions (<FAQSection />)
    ↓
[Existing Community Section & Footer]
```

---

## 3. Component Specifications & Code References

### Component 1: Quick Overview & Freshness Strip
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Sections 1 & 18).
- **Functionality:** 2–3 human-written paragraphs integrating target phrases (`state government jobs 2026`, `state wise government jobs`, `latest state govt vacancies`, `state sarkari naukri`, `government jobs by state`) plus dynamic `{{last_updated_date}}`.
- **Dynamic Field:** Hydrate `<time datetime="{{ISO_DATE}}">{{HUMAN_DATE_IST}}</time>` with the actual database refresh date (e.g., `October 8, 2026`).

### Component 2: Qualification Hub
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Section 2) & `04_INTERNAL_LINKING_ARCHITECTURE.md`.
- **Links to Wire:**
  - `/10th-pass-government-jobs`
  - `/12th-pass-government-jobs`
  - `/graduate-government-jobs`
  - `/diploma-government-jobs`
  - `/iti-government-jobs`
  - `/engineering-government-jobs`
  - `/post-graduate-government-jobs`

### Component 3: Major Recruitment Types (10 State Categories)
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Section 3).
- **Categories:** State PSC (`/exams`), Police (`/category/police-jobs`), Teacher (`/category/education-research-jobs`), Health (`/category/medical-jobs`), Revenue (`/jobs?search=Revenue`), Municipal (`/jobs?search=Municipal`), District/ZP (`/districts`), State PSU (`/category/psu-jobs`), High Court (`/jobs?search=High+Court`), Forest (`/jobs?search=Forest`).

### Component 4: Popular State Government Exams
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Section 13).
- **Exams to Render:** MPSC Rajyaseva, UPPSC PCS, BPSC CCE, MPPSC State Service, RPSC RAS, State Police Recruitment, State TET, State Health Recruitment. Include exam stages meta tags and internal links to `/exams/...` and `/exam-calendar`.

### Component 5: Central vs State Jobs Comparison
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Section 5).
- **Layout:** Responsive 7-row table with `<th scope="col">` comparing Authorities, Posting, Domicile, Language, Transfers, Exam Pattern, and Examples. Includes contextual links to `/jobs`, `/exams/upsc-cse`, `/exams/ssc-cgl`, `/category/railway-jobs`, `/category/banking-jobs`.

### Component 6 & 7: Domicile & Language Rules
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Sections 6 & 7).
- **Key Points:** Clearly distinguish open vs domicile-restricted posts, state reservation rules, local language exams (Marathi, Tamil, Punjabi, etc.), and emphasize that the official notification is always the final authority.

### Component 8 & 9: Age Relaxation & Eligibility with CTAs
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Sections 8 & 9).
- **Interactive CTAs:**
  - Prominent button linking to `/age-calculator` (*"Open Free Government Job Age Calculator →"*)
  - Prominent button linking to `/eligibility-checker` (*"Check Your Eligibility Online →"*)

### Component 10 & 11: Application Walkthrough & Document Checklist
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Sections 10 & 11).
- **Layout:** 8 numbered step cards + 12-item document readiness grid with file size/format notes.

### Component 12: Official State PSC Directory Table
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Section 12) & `05_EXTERNAL_AUTHORITY_LINKS.md`.
- **Requirement:** 28 states with official PSC URLs clearly labeled **"Official Website ↗"**. All external links must have `target="_blank"` and `rel="noopener noreferrer"`.

### Component 13: Maharashtra District Hub
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Section 14).
- **Links to Wire:** Pune (`/districts/pune`), Mumbai (`/districts/mumbai-city`), Nagpur (`/districts/nagpur`), Nashik (`/districts/nashik`), and All Districts (`/districts`).

### Component 14, 15, 16 & 17: Upcoming Jobs, Closed Jobs Recovery, E-E-A-T & Resources
- **Source File:** `03_PAGE_CONTENT_ADDITIONS.md` (Sections 15, 16, 17, 19).
- **Links to Wire:** `/exam-calendar`, `/admit-cards`, `/results`, `/editorial-policy`, and the 14-link resource grid.

### Component 18: 15 Detailed FAQs
- **Source File:** `07_FAQ_15.md` & `08_SCHEMA_JSONLD.md`.
- **Requirement:** Render all 15 FAQs in accessible `<details><summary>` or `<button aria-expanded="...">` accordions in the DOM. Inject matching `FAQPage` JSON-LD.

---

## 4. Metadata & Structured Data Injection

Inject the validated metadata and JSON-LD payloads:
- **Title:** `State Government Jobs 2026: State Wise Sarkari Naukri & PSC Vacancies`
- **Description:** `Browse state government jobs 2026 across all 28 states & 8 UTs. Find State PSC, police, teaching, 10th/12th/graduate vacancies, eligibility, domicile rules & official links.`
- **Canonical:** `https://www.searchsarkarinaukri.com/category/state-government-jobs` (or `/state-government-jobs` if redirecting).
- **JSON-LD:** Inject `BreadcrumbList`, `CollectionPage` (with 31-item `ItemList`), and `FAQPage` from `08_SCHEMA_JSONLD.md`.

---

## 5. QA Verification Sign-Off

Execute the complete checklist in `09_IMPLEMENTATION_AND_QA_CHECKLIST.md` before merging to staging or production. Confirm:
1. Zero existing content was deleted.
2. All 20 master sections are visible in SSR HTML.
3. Every internal link returns 200.
4. Schema validates with 0 errors in Google Rich Results Test.
5. Mobile viewports display zero horizontal overflow.
