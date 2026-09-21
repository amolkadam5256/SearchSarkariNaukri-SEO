# 23 - SEARCH CONSOLE QUALITY REMEDIATION CHECKLIST

**Section:** 21 September 2026 Search Console Follow-up  
**Priority:** P0  
**Type:** Developer + SEO Remediation Checklist  
**Status:** Addendum Required Before Next Deployment

---

## Current Search Console Status

The `/districts` page is no longer a basic indexing problem.

- [ ] Treat `/districts` as indexed and eligible to rank.
- [ ] Do not repeatedly request indexing for `/districts` unless a major deployment or URL change occurs.
- [ ] Focus engineering time on quality, freshness, uniqueness, structured data, internal linking, and page experience.
- [ ] Monitor Search Console Performance for the exact page URL: `https://www.searchsarkarinaukri.com/districts`.

## P0 Remediation Items

### 1. Remove Duplicate FAQ Content

The page must not keep both a large "Quick Answers" block and a second FAQ block containing the same questions.

- [ ] Keep only one visible FAQ/direct-answer area on `/districts`.
- [ ] Remove duplicate variants of the same questions.
- [ ] Keep answers concise, factual, and useful.
- [ ] Ensure FAQ schema, if used, matches only visible FAQ content.
- [ ] Do not add FAQ schema for hidden, duplicated, or purely SEO-stuffed content.

Recommended approach:

- Use one section named `Frequently Asked Questions About Maharashtra District Government Jobs`.
- Include the strongest 10-12 questions only.
- Put direct answers first inside each answer.

### 2. Shorten Generic Department and Exam Essays

The `/districts` page should primarily help users choose a district and find current district-wise government jobs.

- [ ] Do not make `/districts` an oversized "everything about Maharashtra government employment" article.
- [ ] Keep department, exam, eligibility, and application guidance concise on this hub page.
- [ ] Move deep department content to dedicated topic pages where available.
- [ ] Link contextually to department pages such as police, health, Zilla Parishad, teaching, forest, revenue, and agriculture pages.

Recommended `/districts` section order:

1. H1
2. Short introduction
3. Live district statistics
4. Top districts
5. All 36 districts
6. Six Maharashtra regions
7. Current Maharashtra vacancies
8. How district recruitment works
9. Qualification shortcuts
10. One FAQ section
11. Marathi summary
12. Official-source and disclaimer section

### 3. Rewrite Marathi Content Naturally

Do not ship awkward or machine-like Marathi. The Marathi section should read like useful candidate guidance.

- [ ] Use `lang="mr"` on the Marathi content wrapper.
- [ ] Use UTF-8 output and Devanagari-capable fonts.
- [ ] Avoid literal English-to-Marathi phrasing.
- [ ] Keep Marathi content short, accurate, and helpful.
- [ ] Verify district names and recruitment terms before publishing.

Approved Marathi replacement:

```html
<section lang="mr" aria-labelledby="maharashtra-district-jobs-marathi">
  <h2 id="maharashtra-district-jobs-marathi">महाराष्ट्रातील जिल्हानिहाय सरकारी नोकरी</h2>
  <p>
    महाराष्ट्रातील सर्व 36 जिल्ह्यांमधील नवीन सरकारी नोकऱ्या आणि भरतीच्या जाहिराती येथे
    जिल्हानिहाय पाहता येतात. पुणे, मुंबई, नागपूर, नाशिक, ठाणे, कोल्हापूर, सोलापूर,
    लातूर आणि इतर जिल्ह्यांतील उपलब्ध भरतीची माहिती संबंधित जिल्हा पृष्ठावर दिली जाते.
  </p>
  <p>
    प्रत्येक भरतीसाठी शैक्षणिक पात्रता, वयोमर्यादा, रिक्त पदांची संख्या, अर्जाची अंतिम
    तारीख आणि अधिकृत जाहिरात तपासा. अर्ज करण्यापूर्वी संबंधित विभागाची अधिकृत जाहिरात
    वाचणे आवश्यक आहे.
  </p>
</section>
```

### 4. Soften Eligibility and Age-Limit Claims

Government recruitment is high-consequence information for candidates. Generic age and reservation claims must be qualified.

- [ ] Do not state universal age limits as if they apply to every recruitment.
- [ ] Do not state reservation relaxations as guaranteed for every job.
- [ ] Always tell users that the official recruitment notification is final.
- [ ] Replace rigid claims with safer wording.

Use this wording:

> Age limits, age relaxation, domicile requirements, reservation rules and educational qualifications vary by recruiting authority, post and notification. Reserved-category candidates may receive relaxation where specified in the official recruitment notification. Candidates should verify every eligibility detail from the official notice before applying.

### 5. Synchronize Freshness Signals

Visible freshness must come from real data changes, not page-load time.

- [ ] `Last updated` must come from the latest real job/district dataset update.
- [ ] Vacancy counts and `Last updated` must use the same data source.
- [ ] Update the date only when a job is added, expired, corrected, or materially updated.
- [ ] Do not use `new Date()` on every render to fake freshness.
- [ ] Sitemap `<lastmod>` must follow the same real-update rule.

Freshness update triggers:

- New job added.
- Job expired or closed.
- Application deadline changed.
- Vacancy count changed.
- Official notice updated.
- District mapping or district page content changed.

### 6. Canonical Rules

- [ ] `/districts` must self-canonical to `https://www.searchsarkarinaukri.com/districts`.
- [ ] Every district page must self-canonical to its own URL.
- [ ] Never canonical district child pages to `/districts`.
- [ ] Canonicals must not include tracking parameters.

Examples:

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/districts">
<link rel="canonical" href="https://www.searchsarkarinaukri.com/districts/pune">
```

### 7. JobPosting Schema Rules

- [ ] Do not add `JobPosting` schema to `/districts`.
- [ ] Do not add `JobPosting` schema to multi-job district listing pages such as `/districts/pune`.
- [ ] Add `JobPosting` only to individual job detail pages describing one job/recruitment.
- [ ] Keep `datePosted` and `validThrough` accurate.
- [ ] Expired jobs must stop appearing as active jobs.

### 8. Strengthen All 36 District Pages

Every district page must be useful even when the active count is zero.

- [ ] Unique title per district.
- [ ] Unique H1 per district.
- [ ] Unique meta description per district.
- [ ] Unique introduction per district.
- [ ] Current district vacancies shown from real data.
- [ ] Latest recruiters shown where available.
- [ ] Related nearby districts linked with crawlable anchors.
- [ ] District page links back to `/districts`.
- [ ] Zero-job district pages remain useful and indexable unless there is no long-term value.

Example zero-job treatment:

> No active Wardha-specific vacancies are currently listed. Candidates can also check Maharashtra statewide jobs, nearby Nagpur jobs, police recruitment, Zilla Parishad recruitment, and qualification-wise government jobs while waiting for the next Wardha notification.

### 9. Add Nearby District Links

Nearby district links help users and crawlers move naturally through the district cluster.

- [ ] Add a "Nearby Government Job Locations" section to each district page.
- [ ] Use descriptive anchor text.
- [ ] Use real `<a href>` or framework links that render crawlable anchors.

Examples:

- Pune: Satara, Ahilyanagar, Solapur, Raigad, Mumbai.
- Nagpur: Wardha, Bhandara, Chandrapur, Gondia.
- Mumbai City: Mumbai Suburban, Thane, Palghar, Raigad.
- Nashik: Dhule, Jalgaon, Ahilyanagar, Thane, Palghar.

### 10. SSR/Prerender and API-Failure Resilience

Important SEO routes should not render only a loading spinner to crawlers.

- [ ] Prerender or server-render `/`, `/districts`, `/districts/*`, `/jobs/*`, `/jobs-in-maharashtra`, `/current-affairs`, `/exams/*`, and `/qualification/*` where practical.
- [ ] Render H1, introduction, metadata, breadcrumbs, district links, and key job links in initial HTML where possible.
- [ ] If a jobs API fails, still render evergreen district guidance and related links.
- [ ] Unknown routes must return a real HTTP 404, not an SPA fallback 200.

### 11. Core Web Vitals Targets

- [ ] LCP is at or below 2.5 seconds.
- [ ] INP is below 200 ms.
- [ ] CLS is below 0.1.
- [ ] JavaScript bundles are reviewed for unused code.
- [ ] Fonts do not cause layout shifts.
- [ ] Images are optimized and lazy-loaded where appropriate.
- [ ] Ads or third-party scripts reserve stable layout space.

### 12. Trust and Editorial Transparency

- [ ] Every job detail page shows recruiting authority.
- [ ] Every job detail page links to the official notification or official website when available.
- [ ] Every job detail page shows a last verified date.
- [ ] Add or link an `/editorial-policy` page.
- [ ] Clearly disclose that SearchSarkariNaukri is not a government website.
- [ ] Explain how vacancies are sourced, verified, updated, corrected, and expired.

## Monitoring Checklist

Review monthly in Google Search Console:

- [ ] Page performance for `https://www.searchsarkarinaukri.com/districts`.
- [ ] Query groups for district-wise government jobs.
- [ ] Query groups for Marathi district-wise job searches.
- [ ] Index coverage for all 36 district pages.
- [ ] Soft 404 reports.
- [ ] Duplicate/canonical reports.
- [ ] `Crawled - currently not indexed`.
- [ ] `Discovered - currently not indexed`.
- [ ] Structured-data errors and warnings.
- [ ] Core Web Vitals field data.

## Final Priority Order

1. Remove duplicate/repetitive FAQ and boilerplate.
2. Fix Marathi quality.
3. Synchronize live vacancy counts and timestamps.
4. Strengthen all 36 district child pages.
5. Fix JobPosting schema architecture.
6. Improve SSR/prerendering and Core Web Vitals.
7. Build stronger official-source and editorial trust.
8. Measure real Search Console ranking/query performance.

---

**Last Updated:** 21 September 2026  
**Status:** Required Addendum
