# 00 — MASTER DGFT RECRUITMENT 2026 AUDIT & IMPLEMENTATION MAP

**Target URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Alias / User URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`  
**Audit Date:** 18 October 2026 (IST)  
**Status:** IMPLEMENTATION SPECIFICATION — READY FOR DEPLOYMENT  
**Priority:** P0 Data Accuracy & Expired-Job Handling; P1 Content, Schema & Internal Linking; P2 Ongoing Optimization.

---

## 1. Executive Summary

This master implementation specification covers the on-page remediation, technical SEO, Generative Engine Optimization (GEO), Answer Engine Optimization (AEO), and structured data requirements for the **DGFT Recruitment 2026** listing on SearchSarkariNaukri (SSN).

The Directorate General of Foreign Trade (DGFT) is a key central government agency under the Ministry of Commerce and Industry. The existing SSN page records **2 vacancies** with an original application deadline of **26 June 2026**.

Because the current date is **18 October 2026**, this recruitment record is **CLOSED / EXPIRED**. Furthermore, an in-depth audit revealed that no public recruitment PDF corroborating the two specific posts, qualification, selection procedure, or salary was verified. The previous page asserted standard 7th Pay Commission pay scales and generic written/physical tests without citation.

This implementation pack provides the complete engineering and content solution to:
1. **Preserve page history, traffic equity, and canonical URLs** without deleting the page or changing existing slugs.
2. **Transition the listing into an authoritative, honest historical archive** with explicit expired-job notices and verification status tags.
3. **Remove misleading active application CTAs** and replace unverified assertions with honest, transparent guidance.
4. **Deploy compliant `WebPage` and `BreadcrumbList` schema** while withholding Google `JobPosting` structured data until a single verified active role exists.
5. **Add rich bilingual content (English & Marathi)**, dynamic links to open central government vacancies, and 12 visible AEO FAQs.

---

## 2. Fundamental Architectural Rules (Non-Negotiable)

```text
+-----------------------------------------------------------------------------------+
|                            DEVELOPER HARD CONSTRAINTS                             |
+-----------------------------------------------------------------------------------+
| 1. NO DELETE: Do NOT delete the page, its route, or its original core facts.     |
| 2. NO SLUG OVERWRITE: Canonical stays /jobs/dgft-dgft-2026--2030 (301 aliases).  |
| 3. NO DATE MANIPULATION: Never alter 26 June 2026 to make an old job seem active. |
| 4. EXPIRED STATUS ABOVE FOLD: Clearly state "Applications Closed" above fold.     |
| 5. NO FABRICATION: Mark unconfirmed pay, selection, and posts as NOT VERIFIED.   |
| 6. NO MISLEADING APPLY BUTTON: No "Apply Now" to generic DGFT homepages.          |
| 7. NO FAKE JOBPOSTING SCHEMA: Withhold JobPosting JSON-LD on expired archives.     |
| 8. STRICT SSR: All content, tables, and FAQs must be present in initial HTML DOM. |
+-----------------------------------------------------------------------------------+
```

---

## 3. Scope of Work & Deliverables Map

The remediation has been divided into 13 modular specifications:

| Doc # | File Name | Key Focus Areas |
|---|---|---|
| `00` | [`00_MASTER_DGFT_RECRUITMENT_2026_AUDIT.md`](./00_MASTER_DGFT_RECRUITMENT_2026_AUDIT.md) | Master overview, hard constraints, sprint roadmap, release gates. |
| `01` | [`01_AUDIT_EVIDENCE_AND_FACTUAL_ACCURACY.md`](./01_AUDIT_EVIDENCE_AND_FACTUAL_ACCURACY.md) | Baseline DOM audit, verified vs unverified items, truth conditions. |
| `02` | [`02_SEO_METADATA_AND_CANONICAL_SPECIFICATION.md`](./02_SEO_METADATA_AND_CANONICAL_SPECIFICATION.md) | SEO Title, Meta Description, Canonical URL, OpenGraph, Twitter Cards. |
| `03` | [`03_KEYWORD_STRATEGY_AND_SEARCH_INTENT_MAP.md`](./03_KEYWORD_STRATEGY_AND_SEARCH_INTENT_MAP.md) | Primary/secondary keywords, Marathi phrases, anti-stuffing rules. |
| `04` | [`04_COMPLETE_PAGE_CONTENT_BILINGUAL.md`](./04_COMPLETE_PAGE_CONTENT_BILINGUAL.md) | Ready-to-render English/Marathi copy, tables, checklist, 12 FAQs. |
| `05` | [`05_PAGE_ARCHITECTURE_AND_COMPONENT_ORDER.md`](./05_PAGE_ARCHITECTURE_AND_COMPONENT_ORDER.md) | 16-component wireframe, DOM structure, anchor IDs, responsive CSS. |
| `06` | [`06_INTERNAL_LINKING_AND_DYNAMIC_RELATED_JOBS.md`](./06_INTERNAL_LINKING_AND_DYNAMIC_RELATED_JOBS.md) | Confirmed safe URLs, dynamic active Central Govt widget query logic. |
| `07` | [`07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md`](./07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md) | Safe WebPage + BreadcrumbList JSON-LD, conditional JobPosting engine. |
| `08` | [`08_INDEXING_API_AND_CRAWL_MANAGEMENT.md`](./08_INDEXING_API_AND_CRAWL_MANAGEMENT.md) | Indexing API compliance policy, service account rules, XML sitemap. |
| `09` | [`09_DATA_MODEL_AND_DATABASE_SCHEMA.md`](./09_DATA_MODEL_AND_DATABASE_SCHEMA.md) | `RecruitmentRecord` TypeScript type, source provenance, publishing gates. |
| `10` | [`10_RELATED_BLOG_BRIEFS_AND_TOPICAL_CLUSTER.md`](./10_RELATED_BLOG_BRIEFS_AND_TOPICAL_CLUSTER.md) | 4 editorial briefs for supporting blog articles & cluster authority. |
| `11` | [`11_DEVELOPER_MASTER_PROMPT.md`](./11_DEVELOPER_MASTER_PROMPT.md) | Step-by-step developer implementation instructions and code snippets. |
| `12` | [`12_ACCEPTANCE_TESTS_AND_QA_CHECKLIST.md`](./12_ACCEPTANCE_TESTS_AND_QA_CHECKLIST.md) | Automated assertion test suite, P0/P1/P2 checklist, monitoring plan. |

---

## 4. Sprint Execution Plan

### Sprint 1: P0 Truth, Trust & Expired Status Patch (Hours 0–24)
- **Goal:** Neutralize misleading recruitment information and eliminate Google penalty risks.
- **Tasks:**
  1. Update Title and Meta Description in page header to reflect closed status.
  2. Inject prominent `<ClosedApplicationBanner />` above the fold.
  3. Swap active "Apply Now" button for informational links (`Visit DGFT Official Website` / `Browse Active Jobs`).
  4. Correct unverified salary and selection answers in visible FAQ block.
  5. Validate canonical link points strictly to `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`.

### Sprint 2: P1 Content Expansion & Schema Architecture (Hours 24–72)
- **Goal:** Server-side render all comprehensive educational and navigational modules.
- **Tasks:**
  1. Render the complete bilingual copy from `04_COMPLETE_PAGE_CONTENT_BILINGUAL.md`.
  2. Implement the 16 structured components in sequence with assigned anchor IDs.
  3. Deploy the dynamic `Latest Central Government Jobs` query component.
  4. Inject validated `WebPage` and `BreadcrumbList` JSON-LD from `07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md`.
  5. Ensure zero JobPosting markup is emitted on this archived page.

### Sprint 3: P2 QA, Validation & Search Monitoring (Hours 72–120)
- **Goal:** Verify production correctness and search engine recrawl.
- **Tasks:**
  1. Execute all test assertions from `12_ACCEPTANCE_TESTS_AND_QA_CHECKLIST.md`.
  2. Test URL in Google Rich Results Test and Schema Validator.
  3. Check mobile viewport rendering, table horizontal scroll, and touch target sizes.
  4. Update XML sitemap `<lastmod>` with authentic ISO timestamp.
  5. Monitor Google Search Console indexing and performance at 7, 28, and 56 days.
