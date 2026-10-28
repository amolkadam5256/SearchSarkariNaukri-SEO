# 01 — AUDIT EVIDENCE & FACTUAL ACCURACY SPECIFICATION

**Target URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Alias / Requested URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`  
**Audit Date:** 18 October 2026 (IST)  
**Status:** FACTUAL BASELINE AUDIT — P0 DATA INTEGRITY

---

## 1. Evidence Snapshot: What Is Actually on the Live Page

A thorough inspection of the accessible live page on SearchSarkariNaukri reveals the following elements and data points:

| DOM Element / Field | Live Content / Value Found | Factual Assessment |
|---|---|---|
| **Page Title** | `२ पदांकरिता DGFT भरती अपडेट २०२६ — DGFT` | Matches internal Marathi naming; lacks explicit expired warning in snippet. |
| **Organization Name** | `DGFT` (Directorate General of Foreign Trade) | Verifiable central government department under Ministry of Commerce & Industry. |
| **Vacancies Reported** | `2` | Recorded in legacy database; individual post names and breakdown absent. |
| **Qualification Clause** | `शैक्षणिक पात्रता पदाच्या आवश्यकतेनुसार आहे .(मूळ जाहिरात वाचावी.)` | Generic advisory to check original ad; no specific degree or criteria identified. |
| **Job Type** | `Full-time` | Display label; permanent vs contract status not confirmed. |
| **Application Deadline** | `2026-06-26` (26 June 2026) | Original recorded closing date. |
| **Notified By URL** | `https://www.dgft.gov.in/` | General organization homepage; not a direct recruitment circular or PDF. |
| **Language & Description** | Short Marathi job summary with 5 basic FAQs. | Contains unverified claims regarding selection process and 7th CPC salary. |
| **Navigation Links** | Categories: jobs, admit cards, results, exams, eligibility, age calculator. | Active and functional sitewide components. Must be preserved. |
| **Disclaimer** | Independent information disclaimer stating applicants should verify with DGFT. | Legally sound; needs to be reinforced with explicit source verification status. |
| **Expired Warning** | Basic banner indicating application deadline has passed. | Needs elevated prominence above the fold with clear CTA redirection to active jobs. |

---

## 2. Critical Truth Conditions (As of 18 October 2026)

### A. Temporal Truth Condition: Listing Is Strictly Closed
- **Original Deadline:** 26 June 2026.
- **Current Audit Date:** 18 October 2026.
- **Fact:** October 18, 2026 is **114 days after** June 26, 2026.
- **Rule:** This recruitment listing is **CLOSED / EXPIRED**. There is no verified official corrigendum extending this recruitment window.
- **Constraint:** Never edit the original `validThrough`, closing date, or `datePosted` to make an expired posting appear active.

### B. Verification Limitations: Specifics Not Verified
During the research and audit phase, no authentic recruitment circular or official PDF published by DGFT corroborating these specific two vacancies, designations, qualification clauses, selection process, or pay structure was identified.

| Field | Previous Site Assumption | Verified Fact / Corrective Action |
|---|---|---|
| **Post Designations** | Often inferred as Clerk/Steno/MTS | **NOT VERIFIED.** Keep designations generic until primary notice is located. |
| **Educational Qualification** | Assumed Graduate or 10th/12th | **NOT VERIFIED.** State clearly that qualifications depend on the post in original notice. |
| **Selection Process** | Claimed Written Exam, Interview, Physical Test | **NOT VERIFIED.** Remove fabricated multi-stage claims; replace with verified notice checklist. |
| **Salary / Pay Scale** | Claimed 7th Central Pay Commission matrix | **NOT VERIFIED.** Remove unsupported salary figures; government hiring includes contracts/deputation. |
| **Application Fee** | Inferred generic government fees | **NOT VERIFIED.** Do not state any fee amount. |
| **Application Mode** | Implied Online Portal | **NOT VERIFIED.** DGFT applications may be offline/deputation/email/online depending on post. |
| **Duty Station / Location** | Inferred Maharashtra / New Delhi | **NOT VERIFIED.** Do not attach Maharashtra location tags without official notice backing. |
| **Official PDF Notice** | Linked to general homepage | **NOT VERIFIED.** Explicitly mark PDF as pending verification; do not treat homepage as the PDF. |

---

## 3. Editorial & URL Protection Rules

1. **Retain Canonical URL:**
   - Keep the canonical URL strictly set to `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`.
   - Any secondary alias (e.g., `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`) must issue a `301 Permanent Redirect` to the canonical target or include a strict canonical link pointing to it.
2. **Preserve Legacy Record Integrity:**
   - Retain the original vacancy count (`2`) and original closing date (`26 June 2026`) as recorded by SSN, accompanied by the verification status note.
   - Do NOT delete the page; doing so causes a 404 error, degrades topical relevance, and loses historical search equity.
3. **Audit Trail & Timestamps:**
   - Maintain original publication date (`datePublished`).
   - Update `dateModified` only when substantive editorial corrections and new sections are deployed.
4. **Elevated Above-the-Fold Expired Banner:**
   - Place a high-contrast, screen-reader-accessible banner immediately below the H1 heading clearly announcing:
     > **Applications Closed:** The original application deadline for this DGFT recruitment was **26 June 2026**. This page is maintained as a historical reference.
5. **Neutralize Misleading CTAs:**
   - Disable and remove any active `Apply Now` button that links to `https://www.dgft.gov.in/` or third-party forms.
   - Replace with two clear, transparent action buttons:
     1. `Visit DGFT Official Website` (External link to official homepage with `rel="noopener noreferrer"`).
     2. `Browse Active Government Jobs` (Internal link to `https://www.searchsarkarinaukri.com/`).
6. **No-Delete Policy for Sitewide Infrastructure:**
   - Retain the existing breadcrumbs (`Home > Government Jobs > DGFT Recruitment 2026`).
   - Retain all category navigation links, exam links, calculator shortcuts, and footer architecture.

---

## 4. Official Sources & Reference Baseline

- **Live SSN Page:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`
- **Official Recruiting Authority:** Directorate General of Foreign Trade (DGFT), Ministry of Commerce and Industry, Government of India.
- **Official Portal:** `https://www.dgft.gov.in/`
- **Regulatory Framework:** Central Government Recruitment Norms & DoPT Guidelines.
