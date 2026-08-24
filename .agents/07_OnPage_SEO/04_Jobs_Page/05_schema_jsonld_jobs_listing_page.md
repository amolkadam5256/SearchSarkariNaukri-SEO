# 05 — `/jobs` Page: JSON-LD Structured Data (New Addition)

> Add these `<script type="application/ld+json">` blocks to the `/jobs` page `<head>` or end of `<body>`. **Do not add `JobPosting` schema to this page** — that belongs only on individual job pages (file 06). These blocks are pure additions; they don't touch any existing schema you may already have (Organization/WebSite on the homepage, etc.) — if `/jobs` has none today, all of this is new.

## 1. WebSite

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "SearchSarkariNaukri",
  "url": "https://www.searchsarkarinaukri.com/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.searchsarkarinaukri.com/jobs?search={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

## 2. Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "SearchSarkariNaukri",
  "url": "https://www.searchsarkarinaukri.com/",
  "logo": "https://www.searchsarkarinaukri.com/logo.png"
}
```

## 3. BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.searchsarkarinaukri.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Government Jobs",
      "item": "https://www.searchsarkarinaukri.com/jobs"
    }
  ]
}
```

## 4. CollectionPage + ItemList (represents the job listing, not individual JobPostings)

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Latest Government Jobs 2026 – Sarkari Naukri",
  "url": "https://www.searchsarkarinaukri.com/jobs",
  "description": "Find the latest government jobs 2026 in India. Search active Sarkari Naukri, MPSC, SSC, Railway, Banking, Police Bharti, 10th, 12th, ITI and graduate jobs.",
  "mainEntity": {
    "@type": "ItemList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "url": "https://www.searchsarkarinaukri.com/jobs/ibps-recruitment-2026"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "url": "https://www.searchsarkarinaukri.com/jobs/nmdfc-recruitment-2026"
      }
    ]
  }
}
```

Generate the `ItemList` dynamically from the current job set (top N shown on the page). This is a list of *links*, not full JobPosting objects — that distinction is what keeps this compliant with Google's guidance to avoid JobPosting on listing pages.

## 5. FAQPage (matches the FAQ section added in file 03)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are the latest government jobs available in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SearchSarkariNaukri lists active government job vacancies across MPSC, SSC, Railway, Banking, Police and other departments, updated regularly with eligibility, vacancy count and last date to apply."
      }
    },
    {
      "@type": "Question",
      "name": "Is SearchSarkariNaukri an official government website?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. SearchSarkariNaukri is an independent career-information portal and is not affiliated with any government department. Always verify details on the official recruitment notification."
      }
    }
  ]
}
```

Add one `Question`/`Answer` pair per FAQ item added in file 03 — keep the visible text and the schema text identical.

## Checklist for this file

- [ ] WebSite schema added
- [ ] Organization schema added
- [ ] BreadcrumbList schema added
- [ ] CollectionPage + ItemList schema added (no JobPosting here)
- [ ] FAQPage schema added, matching visible FAQ content exactly
- [ ] Validated in Google's Rich Results Test
