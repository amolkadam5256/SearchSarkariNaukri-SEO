# 12 — ACCEPTANCE TESTS & QA CHECKLIST

**Target Canonical URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Test Suite:** Automated CI/CD Assertions & Manual QA Verification  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P0 Release Blocker & P1/P2 Quality Assurance

---

## 1. Automated Engineer-Readable Assertions (CI/CD Suite)

The engineering pipeline must execute and pass the following test assertions before promoting code to production:

```text
ASSERT canonical_url == "https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030"
ASSERT original_deadline == "2026-06-26"
ASSERT as_of("2026-10-18") pageStatus == CLOSED
ASSERT visible_title_contains("DGFT Recruitment 2026")
ASSERT visible_deadline_notice == true
ASSERT active_apply_button == false
ASSERT has_official_org_link == true
ASSERT no_unverified_selection_claim == true
ASSERT no_unverified_salary_claim == true
ASSERT no_fabricated_location == true
ASSERT no_fabricated_notification_pdf == true
ASSERT structured_data.JobPosting == absent UNTIL officially verified specific role
ASSERT structured_data.WebPage.url == canonical_url
ASSERT structured_data.BreadcrumbList.valid == true
ASSERT current_related_jobs.every(x => x.status == OPEN && x.target_http_status == 200)
ASSERT page_has_independent_publisher_disclaimer == true
ASSERT existing_category_nav_preserved == true
ASSERT original_page_slug_preserved == true
ASSERT schema_matches_visible_content == true
```

---

## 2. P0: Data Integrity & Trust Checklist (Release Blockers)

- [ ] **Prominent Closed Banner:** Banner stating `Applications closed — last date 26 June 2026` is visible above the fold and screen-reader accessible (`role="status"`).
- [ ] **No Fabricated Post Roles:** Posts are described honestly as "2 reported posts"; no unsubstantiated designations (Clerk/MTS/Assistant) are invented.
- [ ] **No Generic Salary Claims:** Removed unsupported references to 7th Central Pay Commission scales.
- [ ] **No Generic Selection Claims:** Removed unsupported references to written tests, interviews, or physical endurance tests.
- [ ] **No Misleading Apply Buttons:** Disabled all active "Apply Now" buttons pointing to third-party or generic portals.
- [ ] **Authentic Source Links:** Contains clean external link to `https://www.dgft.gov.in/` labeled `Visit DGFT Official Website` with `rel="noopener noreferrer"`.
- [ ] **Independence Disclaimer:** Displays unambiguous statement that SearchSarkariNaukri is an independent career platform not affiliated with DGFT.

---

## 3. P1: Headings, Semantic Structure & Technical SEO Checklist

- [ ] **Single H1:** Page has exactly one H1 tag: `DGFT Recruitment 2026 (DGFT भरती २०२६) — 2 Posts, Eligibility, Last Date & Official Updates`.
- [ ] **Logical Heading Hierarchy:** All subordinate sections utilize H2 and H3 tags without skipped heading levels.
- [ ] **Bilingual Clarity:** Marathi summary and English guidance are cleanly separated and grammatically sound.
- [ ] **Immutable Canonical Link:** `<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030">` is in the document `<head>`.
- [ ] **Alias 301 Redirect:** Route `/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online` returns `HTTP 301` to canonical.
- [ ] **Robots Directives:** `<meta name="robots" content="index, follow, ...">` correctly configured without conflicting headers.
- [ ] **Mobile Responsive Tables:** All tables wrapped in containers with `overflow-x: auto;` and proper `<th scope="row/col">` markup.
- [ ] **Touch Target Sizing:** All links, buttons, and accordion headers have a minimum tap area of 48px × 48px.
- [ ] **Core Web Vitals:** First Contentful Paint (FCP) < 1.5s, Largest Contentful Paint (LCP) < 2.2s, CLS < 0.05.

---

## 4. P0/P1: Structured Data Validation Checklist

- [ ] **Withhold JobPosting:** Zero `JobPosting` schema nodes emitted in the rendered DOM.
- [ ] **Valid WebPage Node:** Emits schema.org `WebPage` with valid `@id`, `name`, and `description`.
- [ ] **Valid BreadcrumbList Node:** Emits schema.org `BreadcrumbList` matching the on-page navigation hierarchy:
  1. `Home` -> `https://www.searchsarkarinaukri.com/`
  2. `Government Jobs` -> `https://www.searchsarkarinaukri.com/jobs`
  3. `DGFT Recruitment 2026` -> `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`
- [ ] **Validator Verification:** Canonical URL tested and passed in both:
  - Google Rich Results Test (`https://search.google.com/test/rich-results`)
  - Schema.org Validator (`https://validator.schema.org/`)

---

## 5. P1: Internal Linking & Dynamic Query Checklist

- [ ] **Existing Navigation Preserved:** Sitewide category navigation, exam links, age calculators, and footer are 100% functional.
- [ ] **Dynamic Active Jobs Widget:**
  - Queries only records where `category_or_type = 'CENTRAL_GOVERNMENT'` and `application_status = 'OPEN'`.
  - Excludes jobs where deadline is in the past.
  - Excludes self-referencing job ID.
  - Returns graceful fallback when zero jobs match.
- [ ] **Safe Guide Links:** Contextually links to confirmed URLs:
  - `https://www.searchsarkarinaukri.com/jobs-in-maharashtra`
  - `https://www.searchsarkarinaukri.com/blogs/district-wise-government-jobs-maharashtra-guide`
  - `https://www.searchsarkarinaukri.com/blogs/government-jobs-in-pune-2026`

---

## 6. P2: GEO, AEO & Answer Retrieval Checklist

- [ ] **Immediate Direct Answer:** First 60-100 words clearly answer `What / Vacancies / Status / Deadline / Official Source`.
- [ ] **Stable Anchor IDs:** Deep-link anchors present on all sections: `#overview`, `#vacancies`, `#eligibility`, `#age-limit`, `#important-dates`, `#salary`, `#selection-process`, `#official-notification`, `#how-to-check`, `#documents`, `#expired`, `#related-jobs`, `#related-guides`, `#faq`, `#sources`.
- [ ] **Visible 12 FAQs:** All 12 FAQs rendered in server-side HTML with comprehensive answers.
- [ ] **Audit Trail & Timestamps:** Explicit review date (`18 October 2026`) and correction reporting mechanism visible.

---

## 7. Post-Launch Performance Monitoring Protocol

Track the following milestones in Google Search Console:

| Milestone | Check Date | Key Metrics & Objectives | Corrective Action if Failing |
|---|---|---|---|
| **Day 7** | 25 Oct 2026 | Googlebot crawl inspection; canonical resolution; zero indexing errors in Search Console. | If not crawled, request manual URL inspection recrawl. |
| **Day 28** | 15 Nov 2026 | Snippet accuracy in SERP; traffic referral to active central government jobs; CTR analysis. | Adjust title/description if Google rewrites with misleading text. |
| **Day 56** | 13 Dec 2026 | Organic query spread; impressions for `DGFT Recruitment 2026` vs active jobs; user engagement time. | Review E-E-A-T signals and refresh dynamic links. |
