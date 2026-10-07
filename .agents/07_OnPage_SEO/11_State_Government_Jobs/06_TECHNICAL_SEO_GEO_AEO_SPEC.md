# 06 — Technical SEO + GEO + AEO Developer Specification

**Target Hub:** `https://www.searchsarkarinaukri.com/category/state-government-jobs` (or `/state-government-jobs`)  
**Standard:** Enterprise Technical SEO, Google Search Essentials, Bing Webmaster Guidelines, Generative AI Optimization (GEO), Answer Engine Optimization (AEO).

---

## 1. URL Architecture & Canonicalization

### Current State & Production Mapping
- **Active Indexed URL in Sitemap:** `https://www.searchsarkarinaukri.com/category/state-government-jobs`
- **Clean Alias / Alternative Route:** `https://www.searchsarkarinaukri.com/state-government-jobs`

### Developer Rule
1. If `/state-government-jobs` is the preferred target URL, developers must implement a permanent **301 HTTP redirect** from `/category/state-government-jobs` to `/state-government-jobs`, and update internal links and sitemap entries accordingly.
2. If maintaining `/category/state-government-jobs`, the canonical tag must strictly point to itself:
```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/category/state-government-jobs" />
```
Never allow both URLs to be crawled with self-referential canonicals simultaneously, as this causes index splitting and keyword dilution.

---

## 2. Meta Tags & Social Graph

```html
<title>State Government Jobs 2026: State Wise Sarkari Naukri & PSC Vacancies</title>
<meta name="description" content="Browse state government jobs 2026 across all 28 states & 8 UTs. Find State PSC, police, teaching, 10th/12th/graduate vacancies, eligibility, domicile rules & official links." />
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website" />
<meta property="og:site_name" content="SearchSarkariNaukri" />
<meta property="og:title" content="State Government Jobs 2026: State Wise Sarkari Naukri & PSC Vacancies" />
<meta property="og:description" content="Explore verified state government jobs across 28 Indian states. Discover State PSC, police, and teaching vacancies with qualifications, domicile rules, and official links." />
<meta property="og:url" content="https://www.searchsarkarinaukri.com/category/state-government-jobs" />
<meta property="og:image" content="https://www.searchsarkarinaukri.com/og-image-state-jobs.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:locale" content="en_IN" />

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="State Government Jobs 2026: State Wise Sarkari Naukri & PSC Vacancies" />
<meta name="twitter:description" content="Browse state-wise Sarkari Naukri across all 28 Indian states. Verified State PSC, police, teaching, and clerical vacancies with official application links." />
<meta name="twitter:image" content="https://www.searchsarkarinaukri.com/og-image-state-jobs.png" />
```

---

## 3. Heading Hierarchy (Strict H1–H3 Architecture)

Ensure that exactly **one `<h1>`** exists on the page, and all subsequent sections follow semantic hierarchy without skipping levels:

```text
H1: State Wise Sarkari Naukri 2026 — Government Jobs by State and UT (Preserved)
  ├── H2: State Government Jobs 2026 – Quick Overview
  ├── H2: Most Searched States (Preserved)
  ├── H2: All States and Union Territories (Preserved Directory)
  ├── H2: Latest State Government Jobs by Qualification
  │     ├── H3: 10th Pass Government Jobs
  │     ├── H3: 12th Pass Government Jobs
  │     ├── H3: Graduate Government Jobs
  │     ├── H3: Diploma Government Jobs
  │     ├── H3: ITI Government Jobs
  │     ├── H3: Engineering Government Jobs
  │     └── H3: Postgraduate Government Jobs
  ├── H2: Government Jobs by Major Recruitment Type
  │     ├── H3: State PSC Jobs
  │     ├── H3: Police Jobs
  │     ├── H3: Teacher Jobs
  │     └── ... [All 10 Categories]
  ├── H2: Popular State Government Exams
  │     ├── H3: MPSC Rajyaseva / Civil Services
  │     ├── H3: UPPSC Combined State (PCS)
  │     ├── H3: BPSC Combined Competitive Examination (CCE)
  │     └── ... [Major Exam Families]
  ├── H2: State Government Jobs vs Central Government Jobs: Key Differences (Expanded)
  ├── H2: Domicile Rules for State Government Jobs: What Candidates Must Know
  ├── H2: Language Requirements in State Government Recruitment
  ├── H2: Age Limits & Age Relaxation for State Government Jobs
  ├── H2: How to Check Eligibility Before You Apply
  ├── H2: How to Apply for State Government Jobs: 8-Step Walkthrough
  ├── H2: Documents Usually Required for State Government Job Applications
  ├── H2: Official State Public Service Commission (PSC) Websites
  ├── H2: Maharashtra & District-Level Government Jobs (Expanded)
  ├── H2: Upcoming State Government Jobs & Expected Notifications 2026
  ├── H2: Recently Closed Recruitment: What to Do Next?
  ├── H2: How SearchSarkariNaukri Verifies Job Information (E-E-A-T Commitment)
  ├── H2: Related Government Job Resources & Candidate Tools
  └── H2: Frequently Asked Questions: State Government Jobs 2026
        ├── H3: 1. What are state government jobs?
        ├── H3: 2. Where can I find latest state government jobs?
        └── ... [Through H3: 15. How frequently is this page updated?]
```

---

## 4. Server-Side Rendering (SSR) & Crawlability Directives

1. **Initial HTML Payload:** All section copy, heading tags, internal anchor links, the official PSC table, and the full 15 FAQ texts **must be present in the initial server-rendered HTML**. Googlebot and Bingbot must not rely on client-side JavaScript execution or user interaction to discover this text.
2. **Accessible Accordions:** If FAQ items use collapsible accordion UI, render questions and answers in semantic HTML (`<details><summary>` or `<button aria-expanded="...">` with an associated content container in the DOM). The text must never be dynamically fetched via AJAX only upon user click.
3. **No Cumulative Layout Shift (CLS):** Reserve CSS min-height for dynamically loaded state counts and any optional "Closing Soon" job cards to achieve a CLS score `< 0.05`.

---

## 5. Generative Engine Optimization (GEO) & AEO Principles

Answer engines (Google AI Overviews, Perplexity, ChatGPT, Microsoft Copilot) extract content directly when it follows strict semantic clarity:
- **Direct Answer First:** Every section and FAQ opens with a definitive 1–2 sentence factual summary before elaborating with nuances.
- **Entity Density:** Unambiguously name formal entities: *Constitution of India (Article 16 & Article 315)*, specific state commissions (*MPSC, UPPSC, BPSC*), and job classifications (*Group A Gazetted, Group C Non-Gazetted*).
- **Tabular Data:** Use properly captioned `<table>` structures with `<th scope="col">` headers for the Central vs State comparison and Official PSC directory, enabling zero-click table extraction by AI engines.
- **Ordered Step Pipelines:** Use `<ol class="checklist-steps">` for multi-step processes (*Application Walkthrough, Eligibility Check*), which search engines parse directly into featured snippets.

---

## 6. Freshness Signal Architecture

```html
<p class="last-updated-block">
  Last Directory Refresh: 
  <time datetime="2026-10-08T06:00:00+05:30">October 8, 2026</time>
</p>
```
- **Dynamic Rule:** The `datetime` attribute and visible date must correspond to the actual time when the database recalculates active vacancies.
- **Sitemap `<lastmod>`:** Update the XML sitemap timestamp only when the page code or underlying job inventory changes materially. Do not alter timestamps artificially on every HTTP GET request.
