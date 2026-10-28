# 02 — SEO METADATA & CANONICAL SPECIFICATION

**Target Canonical URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Alias / Inbound Slug:** `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`  
**Page Type:** Expired Job Archive & Informational Record (`WebPage` / `Article`)  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P0 Technical SEO

---

## 1. Primary SEO Metadata (Literal Ready-to-Use Copy)

All metadata fields must be placed inside the `<head>` of the server-rendered HTML document:

```html
<!-- Primary Title Tag -->
<title>DGFT Recruitment 2026: 2 Posts, Eligibility & Last Date</title>

<!-- Meta Description -->
<meta name="description" content="DGFT Recruitment 2026: Check details of 2 reported posts, eligibility guidance, original 26 June deadline and official DGFT verification. Applications closed.">

<!-- Canonical Tag (Absolute URL, No Trailing Slash, No Query Parameters) -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030">

<!-- Robots Directives -->
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
```

### Metadata Character Counts & Validation

| Field | Recommended Value | Character Length | Pixel Width Estimate |
|---|---|---|---|
| **SEO Title** | `DGFT Recruitment 2026: 2 Posts, Eligibility & Last Date` | 55 characters | ~485px (Safe under 600px desktop / 550px mobile limit) |
| **Meta Description** | `DGFT Recruitment 2026: Check details of 2 reported posts, eligibility guidance, original 26 June deadline and official DGFT verification. Applications closed.` | 155 characters | ~920px (Safe under 960px desktop limit; communicates closed status early) |
| **H1 Heading** | `DGFT Recruitment 2026 (DGFT भरती २०२६) — 2 Posts, Eligibility, Last Date & Official Updates` | N/A (Body H1) | Primary document heading (1 per page) |

---

## 2. Open Graph & Social Sharing Tags

```html
<!-- Open Graph Metadata -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="Search Sarkari Naukri">
<meta property="og:url" content="https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030">
<meta property="og:title" content="DGFT Recruitment 2026 — 2 Posts | Applications Closed">
<meta property="og:description" content="Review the archived DGFT recruitment summary, original last date, verification guidance and links to currently active government vacancies.">
<meta property="og:locale" content="en_IN">
<meta property="og:locale:alternate" content="mr_IN">
<meta property="og:image" content="https://www.searchsarkarinaukri.com/images/jobs/dgft-recruitment-2026-banner.webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="DGFT Recruitment 2026 Status and Overview">

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@SearchSarkariN">
<meta name="twitter:url" content="https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030">
<meta name="twitter:title" content="DGFT Recruitment 2026 — 2 Posts | Applications Closed">
<meta name="twitter:description" content="Review the archived DGFT recruitment summary, original last date, verification guidance and links to currently active government vacancies.">
<meta name="twitter:image" content="https://www.searchsarkarinaukri.com/images/jobs/dgft-recruitment-2026-banner.webp">
```

> **Image Rule:** Use an authentic, existing site-controlled banner image URL. Never invent or inject non-existent CDN image paths.

---

## 3. Canonical & URL Alias Management Rules

1. **Canonical Self-Reference:**  
   The page hosted at `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030` must contain a self-referencing canonical tag pointing exactly to itself.
2. **Inbound URL Alias Handling:**  
   For requests arriving at:  
   `https://www.searchsarkarinaukri.com/jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online`  
   Configure the Next.js / Edge routing layer to issue an immediate `HTTP 301 Moved Permanently` redirect:
   ```nginx
   # Nginx / Edge redirect rule
   location = /jobs/dgft-recruitment-2026-notification-eligibility-vacancy-apply-online {
       return 301 https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030;
   }
   ```
3. **Query Parameter Stripping:**  
   UTM tags, tracking tokens, and pagination flags must resolve canonically to the clean base URL:
   `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`.

---

## 4. Indexing & Quality Directives

- **Indexing Status:** `index, follow` is justified **only when** the page provides substantive historical analysis, source verification trails, and contextual discovery links to active jobs.
- **Editorial `noindex` Evaluation Criteria:**  
  If the editorial team cannot substantiate any part of the DGFT record and chooses not to expand the historical reference content, the page must be assigned:
  ```html
  <meta name="robots" content="noindex, follow">
  ```
  This preserves link equity across internal links while preventing thin-content index bloat.
- **Sitemap Inclusion:**  
  Include the canonical URL in `sitemap-jobs.xml` with `<lastmod>` reflecting the actual editorial update date (e.g., `2026-10-18T18:17:11+05:30`). Do not deploy automated daily timestamps without real content edits.

---

## 5. Breadcrumb Navigation Trail

```text
Home (https://www.searchsarkarinaukri.com/)
  └── Government Jobs (https://www.searchsarkarinaukri.com/jobs)
        └── DGFT Recruitment 2026 (https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030)
```

**Route Verification:** The engineering team must confirm that `https://www.searchsarkarinaukri.com/jobs` responds with `HTTP 200`. If `/jobs` redirects or returns 404, replace with an active 200-status route such as `/category/central-government-jobs` or `https://www.searchsarkarinaukri.com/`.
