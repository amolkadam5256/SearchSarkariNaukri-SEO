# 12 — DGFT Recruitment 2026 Developer Implementation Package

**Target URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Alias / SEO URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`  
**Audit Date:** 18 October 2026 (IST)  
**Status:** IMPLEMENTATION SPECIFICATION — READY FOR ENGINEERING SPRINT  
**Priority:** P0 Data Integrity & Expired-Job Handling; P1 Content, Schema & Linking; P2 GEO/AEO & Ongoing Monitoring.

---

## 1. Directory Overview & Package Index

This directory contains the complete, production-grade implementation specifications, editorial copy, technical SEO requirements, structured data guidelines, and developer instructions for the **DGFT Recruitment 2026** job page on SearchSarkariNaukri.

### Master Implementation Files

| File | Purpose | Key Content |
|---|---|---|
| [`00_MASTER_DGFT_RECRUITMENT_2026_AUDIT.md`](./00_MASTER_DGFT_RECRUITMENT_2026_AUDIT.md) | Executive Master Spec | Page identity, critical truth conditions, audit snapshot, P0/P1/P2 priorities, no-delete policy. |
| [`01_AUDIT_EVIDENCE_AND_FACTUAL_ACCURACY.md`](./01_AUDIT_EVIDENCE_AND_FACTUAL_ACCURACY.md) | Evidence & Truth Conditions | Snapshot of current live page, verified vs unverified assertions, expired status rules, source attribution. |
| [`02_SEO_METADATA_AND_CANONICAL_SPECIFICATION.md`](./02_SEO_METADATA_AND_CANONICAL_SPECIFICATION.md) | Metadata & URL Rules | Literal SEO title, meta description, H1, canonical URL logic, Open Graph, Twitter cards, robots directives. |
| [`03_KEYWORD_STRATEGY_AND_SEARCH_INTENT_MAP.md`](./03_KEYWORD_STRATEGY_AND_SEARCH_INTENT_MAP.md) | Keyword & Intent Architecture | Primary, secondary, and supporting keywords, user intent mapping, Marathi phrases, anti-stuffing rules. |
| [`04_COMPLETE_PAGE_CONTENT_BILINGUAL.md`](./04_COMPLETE_PAGE_CONTENT_BILINGUAL.md) | Complete Page Copy | Full bilingual copy (English & Marathi) ready to render, including quick answer, tables, checklist, 12 FAQs. |
| [`05_PAGE_ARCHITECTURE_AND_COMPONENT_ORDER.md`](./05_PAGE_ARCHITECTURE_AND_COMPONENT_ORDER.md) | UI/UX & Component Wireframe | 16-block component sequence, anchor IDs, mobile responsiveness, accessibility, responsive table layout. |
| [`06_INTERNAL_LINKING_AND_DYNAMIC_RELATED_JOBS.md`](./06_INTERNAL_LINKING_AND_DYNAMIC_RELATED_JOBS.md) | Linking Strategy & Widgets | Safe existing URLs, dynamic active central jobs widget filtering rules, guide cross-links, link contracts. |
| [`07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md`](./07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md) | Schema.org & JSON-LD | Safe `WebPage` + `BreadcrumbList` JSON-LD, conditional `JobPosting` TS engine, FAQPage and Article guidance. |
| [`08_INDEXING_API_AND_CRAWL_MANAGEMENT.md`](./08_INDEXING_API_AND_CRAWL_MANAGEMENT.md) | Google Indexing API & Crawl | Strict eligibility rules, OAuth 2.0 service account setup, URL notifications, XML sitemap `<lastmod>`. |
| [`09_DATA_MODEL_AND_DATABASE_SCHEMA.md`](./09_DATA_MODEL_AND_DATABASE_SCHEMA.md) | TypeScript Types & DB Schema | `RecruitmentRecord` type definition, field provenance, source hierarchy, publishing status gates. |
| [`10_RELATED_BLOG_BRIEFS_AND_TOPICAL_CLUSTER.md`](./10_RELATED_BLOG_BRIEFS_AND_TOPICAL_CLUSTER.md) | Topical Cluster & Blog Briefs | 4 content briefs for supporting articles (PDF verification, DGFT careers, central jobs, corrigenda). |
| [`11_DEVELOPER_MASTER_PROMPT.md`](./11_DEVELOPER_MASTER_PROMPT.md) | Master Developer Instructions | Step-by-step developer build guide, engineering hard rules, SSR requirements, component pseudocode. |
| [`12_ACCEPTANCE_TESTS_AND_QA_CHECKLIST.md`](./12_ACCEPTANCE_TESTS_AND_QA_CHECKLIST.md) | Acceptance Tests & QA Suite | Executable developer assertions, P0/P1/P2 QA checklists, release gate criteria, 7/28/56-day tracking. |

---

## 2. Core Implementation Rules (Non-Negotiable)

1. **NO DELETE POLICY:** Do NOT delete the page, its original factual content, or its existing slug. Preserve internal page identity, redirects, publication history, and existing category navigation.
2. **HONEST EXPIRED STATUS:** Display `Applications closed — last date 26 June 2026` prominently above the fold. Never edit closing dates or published dates to make expired jobs look fresh.
3. **NO FABRICATED FACTS:** No official recruitment PDF corroborating the two posts, qualifications, selection method, or salary was found during this review. All such fields must be explicitly labeled **NOT VERIFIED**. Never guess, invent, or infer details from generic government hiring practices.
4. **NO MISLEADING APPLY CTAS:** Do NOT display an active `Apply Now` button pointing to a generic DGFT homepage or expired portal. Replace with `Visit DGFT Official Website` and `Browse Active Government Jobs`.
5. **DO NOT EMIT JOBPOSTING SCHEMA FOR THIS EXPIRED ARCHIVE:** Google `JobPosting` structured data requires a single, specific, verified active opening. Emitting synthetic JobPosting markup on this unverified expired record violates Google Webmaster Guidelines. Emit safe `WebPage` and `BreadcrumbList` schema only.

---

## 3. Engineering Sprint Workflow

```text
[Sprint 1: P0 Data Integrity & Status Patch]
  ├── Update SEO title and meta description to reflect expired status
  ├── Render prominent "Applications Closed" banner above fold
  ├── Replace active "Apply Now" button with informational official link
  ├── Correct unverified salary and selection claims in FAQs and copy
  └── Ensure canonical tag points to https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030

[Sprint 2: P1 Content Expansion & Semantic Architecture]
  ├── Server-side render all 16 component blocks from 05_PAGE_ARCHITECTURE_AND_COMPONENT_ORDER.md
  ├── Integrate complete bilingual copy from 04_COMPLETE_PAGE_CONTENT_BILINGUAL.md
  ├── Render verified internal links & dynamic active Central Govt Jobs widget
  └── Deploy safe WebPage + BreadcrumbList JSON-LD from 07_STRUCTURED_DATA_JSONLD_SPECIFICATION.md

[Sprint 3: P2 QA, Validation & Monitoring]
  ├── Run automated test assertions in 12_ACCEPTANCE_TESTS_AND_QA_CHECKLIST.md
  ├── Validate Rich Results and Schema Validator (no JobPosting errors)
  ├── Inspect URL in Google Search Console & request normal recrawl (no Indexing API misuse)
  └── Monitor performance at Days 7, 28, and 56
```
