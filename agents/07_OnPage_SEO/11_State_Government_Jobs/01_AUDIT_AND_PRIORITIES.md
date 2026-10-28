# 01 — State Government Jobs Page Audit & Priority Plan

**Target Hub:** `https://www.searchsarkarinaukri.com/state-government-jobs`  
*(Production URL Note: The existing indexed route is `https://www.searchsarkarinaukri.com/category/state-government-jobs`. If maintaining or migrating to `/state-government-jobs`, ensure a 301 redirect or self-canonical alignment is strictly configured).*  
**Audit Status:** Comprehensive Revision Required  
**Implementation Priority:** P0  

---

## 1. Non-Negotiable Implementation Rule

**DO NOT DELETE, REMOVE, OR OVERWRITE ANY EXISTING CONTENT.**  
Keep everything already on the page:
1. Existing Hero / H1 (`State Wise Sarkari Naukri 2026 — Government Jobs by State and UT`)
2. Existing introductory paragraphs
3. “Most Searched States” section
4. “All States and Union Territories” directory with all live vacancy counts
5. Existing Maharashtra highlight section
6. Existing Central vs State recruitment comparison
7. Existing FAQs (expand around them)
8. Existing footer, breadcrumbs, and community links

This audit and implementation plan is strictly **additive**. It wraps around and embeds underneath existing content to transform the page from a simple directory into India's most authoritative, exhaustive **State Government Jobs Topic Hub** optimized for Search (SEO), Generative AI (GEO), and Answer Engines (AEO).

---

## 2. Comprehensive Audit of the 20 Core Requirements

| # | Section / Requirement | Previous Status in Repo | Audit Finding & Action Required |
|---|---|---|---|
| 1 | **State Government Jobs 2026 – Quick Overview** | Partially drafted | Was generic. Must include 2–3 paragraphs targeting exact terms: `state government jobs 2026`, `state wise government jobs`, `latest state govt vacancies`, `state sarkari naukri`, `government jobs by state`. Must delineate State PSCs, departments, boards, police, teaching, health, municipal, and district-level jobs. |
| 2 | **Latest State Government Jobs by Qualification** | Drafted | Verify all 7 links (10th, 12th, Graduate, Diploma, ITI, Engineering, Postgraduate) are correctly mapped to canonical URLs and positioned right after the All States directory. |
| 3 | **Government Jobs by Major Recruitment Type** | Incomplete | Previously included central types (Railway, Banking). **Must feature all 10 state types**: State PSC, Police, Teacher, Health, Revenue, Municipal Corporation, District/Zilla Parishad, State PSU, High Court/Judiciary, Forest Department. |
| 4 | **How State Government Recruitment Works** | Split / Vague | Needs a clear, human-written linear workflow pipeline: *Notification → Eligibility Check → Online Application → Written Exam → Skill/Physical Test → Document Verification → Merit List → Appointment* with AEO-optimized explanatory blocks. |
| 5 | **State Government Jobs vs Central Government Jobs** | Placeholder only | Previously told developer to insert after, but omitted the expanded content! **Must provide full comparison table** covering: Recruiting Authority, Posting Area, Language Requirements, Domicile Rules, Transfer Possibilities, Exam Pattern, Examples + internal links to All Govt Jobs, UPSC, SSC, Railway, Banking. |
| 6 | **Domicile Rules for State Government Jobs** | Merged with language | Needs dedicated, nuanced guide explaining: compulsory vs open posts, local reservation quotas, state certificates, category validation, notification primacy. Avoid universal claims. |
| 7 | **Language Requirements in State Recruitment** | Minor bullet | Needs dedicated block with real-world examples (Marathi in Maharashtra, Hindi in north states, regional language qualifying papers) and reading/writing proficiency checks. |
| 8 | **Age Limits & Age Relaxation** | Missing dedicated block | Add comprehensive breakdown for Minimum/Maximum age, SC/ST (+5), OBC (+3), PwBD (+10), Ex-servicemen, state-specific women/domicile relaxations, plus strong CTA to `/age-calculator`. |
| 9 | **How to Check Eligibility** | Vague | Add systematic criteria: Age, Qualification, Nationality, Domicile, Experience, Physical Standards, Category conditions + prominent CTA to `/eligibility-checker`. |
| 10 | **How to Apply for State Government Jobs** | Abbreviated | Implement 6–8 clear, actionable numbered steps from Official Notification to Confirmation Slip. |
| 11 | **Documents Usually Required** | Bullet points only | Provide full candidate document checklist with file format, date cutoffs, and issuing authority rules. |
| 12 | **Official State PSC / Recruitment Websites** | External list only | Embed high-authority directory table covering all 28 states (MPSC, UPPSC, BPSC, MPPSC, RPSC, GPSC, KPSC, TNPSC, WBPSC, OPSC, PPSC, HPSC, JPSC, CGPSC, TSPSC, APPSC, Kerala PSC, Assam PSC, etc.) clearly labeled **Official Website**. |
| 13 | **Popular State Government Exams** | **COMPLETELY MISSING** | **Must Add**: Dedicated cards and internal links for major recruitment exams: MPSC Rajyaseva, UPPSC PCS, BPSC CCE, MPPSC State Service, RPSC RAS, State Police Recruitment, State TET, State Health Recruitment. |
| 14 | **Jobs by Location / District** | Underdeveloped | Expand Maharashtra section with prominent links to Pune, Mumbai, Nagpur, Nashik, and `/districts` (All District Government Jobs). |
| 15 | **Upcoming State Government Jobs** | **COMPLETELY MISSING** | **Must Add**: Expected notifications, upcoming examinations, application deadlines, exam dates + internal link to `/exam-calendar`. |
| 16 | **Recently Closed Recruitment / What to Do Next** | Conflated with after-apply | Dedicated guidance for candidates landing on expired job postings: Check latest jobs, Exam Calendar, Admit Cards, Results, Subscribe to Alerts. |
| 17 | **How SearchSarkariNaukri Verifies Listings** | Short note | Add official E-E-A-T declaration: verification against official gazette/notifications, independent platform disclaimer, reporting discrepancies. |
| 18 | **Last Updated / Freshness Section** | Template tag only | Add complete UI strip with real dynamic refresh date, active listing computation logic, and notification lifecycle explanation. |
| 19 | **Related Government Job Resources** | **COMPLETELY MISSING** | **Must Add**: Contextual link hub linking to all 14 site features: All Jobs, State Wise, District Wise, Exams, Exam Calendar, Admit Cards, Results, Answer Keys, Current Affairs, Daily Quiz, Eligibility Checker, Age Calculator, Career Guidance, Govt Jobs Guide. |
| 20 | **15 Detailed FAQs** | Mismatched questions | Align exactly with the user's 15 required questions, ensuring in-depth, authoritative, crawlable HTML answers. |

---

## 3. Recommended Master Page Flow

Developers must structure the page in the following sequence:

```text
Existing Breadcrumb (`Home › State Government Jobs`)
↓
Existing Hero / H1 (`State Wise Sarkari Naukri 2026 — Government Jobs by State and UT`)
↓
1. NEW: State Government Jobs 2026 – Quick Overview (2–3 paragraphs targeting key terms)
↓
NEW: Freshness & Verification Status Strip (`{{last_updated_date}}`)
↓
Existing “Most Searched States”
↓
Existing “All States and Union Territories Directory” (Dynamic Vacancy Counts)
↓
2. NEW: Latest State Government Jobs by Qualification (10th, 12th, ITI, Diploma, Graduate, Engg, PG)
↓
3. NEW: Government Jobs by Major Recruitment Type (10 State Categories)
↓
4. NEW: Popular State Government Exams (MPSC, UPPSC, BPSC, MPPSC, RPSC, Police Bharti, TET, Health)
↓
5. EXPANDED: State Government Jobs vs Central Government Jobs (Full Comparison Table & Links)
↓
6. NEW: Domicile Rules for State Government Jobs
↓
7. NEW: Language Requirements in State Government Recruitment
↓
8. NEW: Age Limits & Age Relaxation (with Age Calculator CTA)
↓
9. NEW: How to Check Eligibility (with Eligibility Checker CTA)
↓
10. NEW: How to Apply for State Government Jobs (8-Step Guide)
↓
11. NEW: Documents Usually Required (Checklist)
↓
12. NEW: Official State PSC / Recruitment Websites Directory (Table with 28+ Official Links)
↓
13. EXPANDED: Maharashtra Highlight & District Jobs (Pune, Mumbai, Nagpur, Nashik, All Districts)
↓
14. NEW: Upcoming State Government Jobs (Expected notifications, Exam Calendar link)
↓
15. NEW: Recently Closed Recruitment / What to Do Next (Expired notice recovery & alerts)
↓
16. NEW: How SearchSarkariNaukri Verifies Listings (E-E-A-T Trust Section)
↓
17. NEW: Related Government Job Resources (14 Contextual Tool & Hub Links)
↓
18. EXPANDED: 15 Detailed FAQs (Visible HTML Accordions + JSON-LD)
↓
Existing Footer & Community Links
```

---

## 4. Metadata & Canonical Strategy

- **Primary URL:** `https://www.searchsarkarinaukri.com/category/state-government-jobs` (or `/state-government-jobs` if configured with clean redirect).
- **SEO Title:** `State Government Jobs 2026: State Wise Sarkari Naukri & PSC Vacancies` (66 characters)
- **Meta Description:** `Browse state government jobs 2026 across all 28 states & 8 UTs. Find State PSC, police, teaching, 10th/12th/graduate vacancies, eligibility, domicile rules & official links.` (160 characters)
- **H1:** `State Wise Sarkari Naukri 2026 — Government Jobs by State and UT` (Preserved)
- **Canonical:** Self-referencing canonical tag matching the live page URL.
