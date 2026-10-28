# 18 - PAGE SECTION AUDIT AND UPDATE REQUIREMENTS

**Section:** `/job-updates` Live Page Section Audit  
**Priority:** P0  
**Type:** Page Section Implementation Requirements  
**Status:** Required Before Next Page Update  
**Audit Date:** 21 September 2026

---

## Current Live Page Assessment

The live `/job-updates` page is already substantial. Do not add more generic Sarkari Naukri paragraphs just to increase word count.

Current strengths:

- Navigation is present.
- Visible breadcrumb exists on the live page: `Home > Job Updates`.
- H1 is present.
- Short page-intent introduction is present.
- WhatsApp and Telegram CTAs are present.
- Benefits and audience targeting are present.
- Active listing count and last updated date are visible on the live page.
- Latest jobs table exists and links to job detail pages.
- Closing-soon section exists and is strong.
- Qualification navigation exists.
- Category navigation exists.
- State navigation exists.
- Maharashtra section exists.
- How alerts work exists.
- Application verification guidance exists.
- Editorial policy and independence disclaimer exist.
- FAQ exists.
- Official government links exist.
- Related resources exist.
- Share section exists.

Main remaining opportunity:

`/job-updates` must feel like a live updates and alerts hub, not another version of `/jobs`.

## P0 Missing or Weak Sections

### 1. Freshness Dashboard

Add a compact freshness dashboard immediately below the H1/intro.

Required cards:

- [ ] Active Government Jobs
- [ ] New Today
- [ ] Updated Today
- [ ] Closing Today
- [ ] Closing This Week

Required timestamp:

```text
Last updated: 21 September 2026, 10:45 PM IST
```

Implementation rules:

- [ ] Use the latest real database/page update time.
- [ ] Do not use `new Date()` on every page load.
- [ ] Active Government Jobs must count open jobs only.
- [ ] New Today must count jobs first published today.
- [ ] Updated Today must count materially changed notifications today.
- [ ] Closing Today must count jobs where deadline equals the current date.
- [ ] Closing This Week must count deadlines in the next seven days.

### 2. New Government Jobs Today

This is the most important missing content section because it separates `/job-updates` from `/jobs`.

Section heading:

```text
New Government Jobs Today
```

Suggested columns:

| Job | Organisation | Posts | Qualification | Location | Last Date |
| --- | --- | --- | --- | --- | --- |

Rules:

- [ ] Show only records actually added today.
- [ ] Link job titles to individual job detail pages.
- [ ] Keep qualification text short.
- [ ] Add a crawlable `View all jobs added today` link where a valid filtered URL exists.
- [ ] If there are no jobs added today, show a useful fallback and link to latest job alerts.

### 3. Recently Updated Government Notifications

Government recruitment updates are not always new jobs. This section should capture meaningful changes.

Section heading:

```text
Recently Updated Government Notifications
```

Suggested columns:

| Recruitment | What Changed | Updated | Important Date |
| --- | --- | --- | --- |

Valid update types:

- Deadline extended
- Vacancy increased or revised
- Exam date announced
- Exam date changed
- Fee date changed
- Corrigendum issued
- Application reopened
- Qualification revised
- Admit card released
- Result announced

Rules:

- [ ] Use real tracked changes only.
- [ ] Do not fabricate update events.
- [ ] Link each recruitment/update to the most relevant detail page.
- [ ] Show update date in human-readable format.

### 4. Deadline Extended / Corrigendum Alerts

Add this as either a standalone block or a filtered subsection inside Recently Updated Government Notifications.

Recommended heading:

```text
Important Recruitment Changes
```

Include:

- Last Date Extended
- Application Reopened
- Corrigendum
- Revised Vacancy
- Exam Postponed
- Exam Date Changed

Rules:

- [ ] Show only real changes from tracked data.
- [ ] If no changes exist, do not show fake examples.
- [ ] Keep the block compact.

### 5. Quick Job Finder

Add near the top, directly after the freshness dashboard.

Recommended heading:

```text
Find Government Jobs Quickly
```

Controls/links:

- [ ] Search jobs input.
- [ ] Qualification chips: 10th, 12th, Graduate, ITI, Diploma, PG.
- [ ] Category chips: Railway, Banking, SSC, Police, UPSC, Defence.
- [ ] Location chips: Maharashtra, UP, Bihar, Rajasthan, Delhi, All India.

Rules:

- [ ] Chips must be normal crawlable anchors when they link to pages.
- [ ] Search input must have an accessible label.
- [ ] Do not hide important links behind JavaScript-only `onClick`.

### 6. Latest Alerts by Type

The page promises job notifications, exam dates, admit cards and results. Add a compact alert-type section to match that promise.

Recommended heading:

```text
Latest Sarkari Updates
```

Suggested table/card fields:

| Alert Type | Latest Updates | Destination |
| --- | --- | --- |
| New Jobs | Latest job notifications | `/jobs` or filtered updates |
| Admit Cards | Latest admit cards | `/admit-cards` |
| Results | Latest results | `/results` |
| Exam Dates | Recent exam date announcements | `/exam-calendar` |
| Recruitment News | Important recruitment changes | `/news` |

Rules:

- [ ] Use existing destinations.
- [ ] Do not create new URLs unless the destination exists.
- [ ] Use descriptive anchors.

## P1 Improvements

### 7. Shorten Job Table Qualification Text

The latest-jobs and closing-soon tables currently include long qualification paragraphs. Listing pages should scan quickly.

Rules:

- [ ] Keep the full eligibility on the job detail page.
- [ ] Keep listing qualification text concise.
- [ ] Avoid multi-sentence table cells where possible.

### 8. Fix Misleading Category CTAs

Some category CTAs say `View jobs` while the destination is an exam guide.

Preferred option:

- [ ] Build genuine category pages such as `/category/railway-jobs`, `/category/banking-jobs`, `/category/police-jobs`, `/category/ssc-jobs`, `/category/defence-jobs`, `/category/teaching-jobs`.

Fallback option:

- [ ] If keeping exam-guide URLs, change CTA labels:
  - `Explore RRB Exam Guide`
  - `Explore Banking Exam Guide`
  - `Explore Police Bharti Guide`
  - `Explore SSC Exam Guide`

Rule:

- [ ] Do not label an exam guide as `View jobs`.

### 9. Merge Overlapping Trust Sections

The live page has several related trust/verification sections. Keep the trust value, reduce repetition.

Recommended structure:

```text
How We Verify Government Job Updates
Before You Apply
Independent Platform Disclaimer
```

How We Verify should include 4-5 steps. Before You Apply should check qualification, age limit, dates, fees, vacancy, official PDF and official application link.

Rules:

- [ ] Keep editorial policy link.
- [ ] Keep independence disclaimer.
- [ ] Do not repeat the same verification message in three separate blocks.

### 10. Reviewer and Reviewed Date

Add only if truthful.

Suggested copy:

```text
Reviewed by: Search Sarkari Naukri Editorial Team
Reviewed/updated: 21 September 2026
Sources: Official recruitment authorities and government portals
```

Rules:

- [ ] Add reviewer only if a real editorial review process exists.
- [ ] Reviewed date must reflect actual review/update.
- [ ] Do not invent people, credentials or review claims.

### 11. Compact Official Government Links

The official-source directory is already comprehensive. Do not add more links.

Recommended handling:

- [ ] Keep official links.
- [ ] Group them by category.
- [ ] Consider accordion/collapsible layout.
- [ ] Prevent this section from visually dominating the page.

## Recommended Final Page Order

1. Header / navigation
2. Breadcrumb: `Home > Job Updates`
3. H1: `Daily Sarkari Naukri Updates & Government Job Alerts 2026`
4. Short 2-line intro
5. Freshness dashboard
6. Quick job finder
7. Join free alerts: WhatsApp and Telegram
8. New Government Jobs Today
9. Recently Updated / Corrigendum Alerts
10. Government Jobs Closing Soon
11. Latest Government Job Alerts
12. Latest Alerts by Type
13. Jobs by Qualification
14. Jobs by Category
15. Jobs by State
16. Maharashtra Government Job Alerts
17. How Job Alerts Work
18. How We Verify + Before You Apply
19. FAQ
20. Official Government Sources, compact
21. Related Resources
22. Share section
23. Footer

## Do Not Add

- [ ] More generic Sarkari Naukri paragraphs.
- [ ] More FAQs just for keywords.
- [ ] JobPosting schema on `/job-updates`.
- [ ] Duplicate qualification/state/category blocks.
- [ ] Another internal-link farm.
- [ ] Fake update dates or fake daily counts.

---

**Last Updated:** 21 September 2026  
**Status:** Required Addendum
