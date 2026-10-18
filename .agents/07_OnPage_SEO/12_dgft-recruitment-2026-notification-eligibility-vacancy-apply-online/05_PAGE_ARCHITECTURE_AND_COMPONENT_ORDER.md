# 05 — PAGE ARCHITECTURE & COMPONENT ORDER SPECIFICATION

**Target URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Layout Hierarchy:** Next.js / React Server Components (RSC) Architecture  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P1 Information Architecture & UI/UX

---

## 1. Master Component Hierarchy (16 Blocks in Exact Sequence)

To provide maximum user clarity, search indexation efficiency, and AEO retrieval, the page must render the following 16 components in sequential order within the server-side DOM:

```text
[Header / Global Navigation (Existing)]
    │
    ▼
1.  Breadcrumb Navigation (<JobBreadcrumb />)
    │
    ▼
2.  Hero Header & Closed Status Banner (<JobHeroHeader />)
    ├── H1 Heading
    ├── Prominent Closed Alert Badge (<ClosedApplicationBanner />)
    └── Dated Direct Answer Paragraph (<QuickAnswerText />)
    │
    ▼
3.  Original Factual Snapshot & Source Disclaimer (<FactualSnapshot />)
    │
    ▼
4.  Quick Facts Summary Table (<JobQuickFactsTable />)
    │
    ▼
5.  Interactive Table of Contents (<TableOfContents />)
    │
    ▼
6.  Marathi Summary Section (<MarathiSummaryBlock />)
    │
    ▼
7.  Official Portal & Source Verification Panel (<SourceVerificationPanel />)
    │
    ▼
8.  Vacancy Details & Breakdown Section (<VacancyDetailsSection />)
    ├── Vacancy Breakdown Table
    └── Category Reservation Notice
    │
    ▼
9.  Eligibility, Age Limit, Dates, Salary & Selection Modules (<JobCriteriaModules />)
    ├── Qualification Checklist (<QualificationSection />)
    ├── Age Limit Guidance (<AgeLimitSection />)
    ├── Important Dates Table (<ImportantDatesSection />)
    ├── Salary & Benefits Disclosure (<SalarySection />)
    └── Selection Methodology (<SelectionProcessSection />)
    │
    ▼
10. How to Check Official DGFT Notification (<HowToCheckSection />)
    └── Action Buttons (Visit Official Site / Browse Active Jobs)
    │
    ▼
11. Document Preparation Checklist & Expired Notice (<DocumentAndExpiredGuide />)
    │
    ▼
12. Dynamic Active Central Government Jobs (<DynamicRelatedJobsWidget />)
    │
    ▼
13. Curated Career Guides & Educational Links (<RelatedGuidesGrid />)
    │
    ▼
14. 12 Crawlable Frequently Asked Questions (<AccessibleFAQAccordion />)
    │
    ▼
15. Editorial Metadata, Timestamps & Correction Mechanism (<EditorialFooterMeta />)
    │
    ▼
16. Sitewide Category Navigation & Global Footer (Existing)
```

---

## 2. Component Anchor IDs & Scroll Targets

Every major section must implement an explicit, immutable `id` attribute to support accessible in-page navigation, deep linking, and AI direct-snippet targeting:

| Component / Section | HTML Element | Mandatory Anchor ID | Purpose |
|---|---|---|---|
| **Overview & Quick Answer** | `<section>` | `#overview` | Deep-link to opening factual summary. |
| **Vacancy Breakdown** | `<section>` | `#vacancies` | Jump to reported 2-post breakdown. |
| **Educational Qualification** | `<section>` | `#eligibility` | Jump to qualification checklist. |
| **Age Limit & Relaxations** | `<section>` | `#age-limit` | Jump to age criteria and calculator. |
| **Important Dates** | `<section>` | `#important-dates` | Jump to recruitment timeline table. |
| **Salary & Pay Matrix** | `<section>` | `#salary` | Jump to salary disclosure note. |
| **Selection Process** | `<section>` | `#selection-process` | Jump to selection methodology. |
| **Official Notification** | `<section>` | `#official-notification` | Jump to primary source panel. |
| **How to Verify** | `<section>` | `#how-to-check` | Jump to verification walkthrough. |
| **Document Checklist** | `<section>` | `#documents` | Jump to preparation guide. |
| **Expired Status Guidance** | `<section>` | `#expired` | Jump to post-deadline advisory. |
| **Dynamic Related Jobs** | `<aside>` | `#related-jobs` | Jump to active central openings. |
| **Related Career Guides** | `<aside>` | `#related-guides` | Jump to educational guides. |
| **Frequently Asked Questions** | `<section>` | `#faq` | Jump to 12 visible FAQs. |
| **Sources & Editorial Policy** | `<footer>` | `#sources` | Jump to E-E-A-T verification footer. |

---

## 3. Detailed Component Specifications

### Component 2: `<ClosedApplicationBanner />`
- **Container:** `<div class="closed-banner" role="status" aria-live="polite">`
- **Design Tokens:**
  - Background: `rgba(239, 68, 68, 0.1)` (Tailored light red alert tint)
  - Border: `1px solid #ef4444` (High-contrast red)
  - Typography: Bold `1.1rem`, font color `#991b1b`
- **Accessible Text:**  
  *"Applications for this DGFT recruitment closed on 26 June 2026. This page is maintained as an archived reference."*

### Component 4: `<JobQuickFactsTable />`
- **Semantics:** Clean `<table>` with `<caption>`, `<th scope="row">`, and `<td>`.
- **CSS Rule:** Wrapped in a responsive container `<div class="table-responsive">` with `overflow-x: auto; -webkit-overflow-scrolling: touch;`.
- **Mobile Behavior:** Minimum width of 550px ensures text does not wrap awkwardly on small phone viewports.

### Component 10: `<HowToCheckSection />` (Action Buttons)
- **Primary Action (External):**  
  `<a href="https://www.dgft.gov.in/" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">Visit DGFT Official Website</a>`
- **Secondary Action (Internal):**  
  `<a href="https://www.searchsarkarinaukri.com/" class="btn btn-primary">Browse Active Government Jobs</a>`
- **Rule:** Strict prohibition of any link labeled `Apply Now` or button triggering an empty application submission.

### Component 12: `<DynamicRelatedJobsWidget />`
- **Container:** `<section id="related-jobs" class="related-jobs-block">`
- **Heading:** `<h2>Latest Central Government Jobs — Currently Accepting Applications</h2>`
- **Cards Rendered:** 3 to 6 active job cards filtered dynamically from the database.
- **Card Elements:** Job Title, Recruiting Department, Vacancy Count, Verified Last Date, and CTA `View Recruitment Details`.

### Component 14: `<AccessibleFAQAccordion />`
- **Container:** `<section id="faq" class="faq-container">`
- **Semantics:** Use standard `<details>` and `<summary>` elements or ARIA-compliant accordion buttons (`aria-expanded="true/false"`, `aria-controls="faq-answer-N"`).
- **Indexing Rule:** FAQ answers must be present in the initial server HTML to ensure indexing by search crawlers.

---

## 4. Mobile Responsiveness & Core Web Vitals Rules

1. **Cumulative Layout Shift (CLS < 0.05):**  
   All banners, tables, and dynamic widgets must have pre-allocated min-heights or CSS aspect-ratios to prevent layout jumps during client hydration.
2. **Largest Contentful Paint (LCP < 2.2s):**  
   Server-side render the H1 and Quick Answer component. Avoid heavy hero carousels or render-blocking scripts before the H1.
3. **Touch Targets (Minimum 48px × 48px):**  
   All interactive links, TOC pills, and accordion summaries must have sufficient padding and margin to prevent misclicks on mobile devices.
4. **No Intrusive Interstitials:**  
   Do not render modal popups or full-screen overlays covering the closed status banner on page entry.
