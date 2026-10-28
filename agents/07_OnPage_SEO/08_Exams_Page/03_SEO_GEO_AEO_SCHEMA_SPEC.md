# 03 - SEO, GEO, AEO AND SCHEMA SPEC

**Page:** `/exams`  
**Priority:** P0

---

## Metadata

Title:

```html
<title>Government Exams 2026 - UPSC, SSC, MPSC, Banking, Railway & More</title>
```

Meta description:

```html
<meta name="description" content="Explore major government exams in India including UPSC, SSC, MPSC, Banking, Railway, Defence, Police and Teaching exams. Compare eligibility, syllabus, pattern, dates and preparation resources.">
```

Canonical:

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/exams">
```

Robots:

```html
<meta name="robots" content="index,follow">
```

## SEO Requirements

- One H1 only.
- H1 must match page intent.
- Include major exam categories in body, not only filters.
- Do not keyword-stuff exam names.
- Avoid thin exam cards.
- Avoid empty exam routes.
- Use descriptive anchors: `View UPSC Civil Services exam details`, not `Click here`.
- Link to `/exam-calendar`, `/admit-cards`, `/results`, `/current-affairs`, `/daily-quiz`, `/eligibility-checker`, `/career-guidance`.

## GEO Requirements

Clarify location and coverage:

- UPSC: All India / Central services.
- SSC: Central government / All India postings.
- MPSC: Maharashtra state.
- RRB: Railway zones across India.
- Maharashtra Police: Maharashtra.
- Banking: India-wide or bank-specific.

Do not confuse exam centre city with job location or service coverage.

## AEO Requirements

Add short direct-answer blocks:

- What are the major government exams in India?
- Which exams are available after 12th?
- Which exams can graduates apply for?
- Which exams are conducted by UPSC?
- Which exams are conducted by SSC?
- Which government exams are available in Maharashtra?
- Where can I find exam dates?
- How do I check eligibility?

Answers should be short, self-contained and visible on page.

## FAQ Questions

Use 8-10:

1. What are the major government exams in India?
2. Which government exams can graduates apply for?
3. Which government exams are available after 12th?
4. Which exams are conducted by UPSC?
5. Which exams are conducted by SSC?
6. Which government exams are available in Maharashtra?
7. How can I check government exam eligibility?
8. Where can I find government exam dates?
9. Where can I find syllabus and exam pattern?
10. Is Search Sarkari Naukri an official government website?

## Schema

Use:

- `WebPage`
- `BreadcrumbList`
- `ItemList` for exam directory entries
- `FAQPage` only if visible FAQ exists
- `Organization` and `WebSite` globally if not already present

Do not use:

- `JobPosting` on `/exams`
- Fake `Course` schema unless the page is actually a course
- Hidden FAQ schema

## WebPage Schema Template

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Government Exams 2026 - UPSC, SSC, MPSC, Banking, Railway & More",
  "description": "Explore major government exams in India including UPSC, SSC, MPSC, Banking, Railway, Defence, Police and Teaching exams.",
  "url": "https://www.searchsarkarinaukri.com/exams",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Search Sarkari Naukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

## Breadcrumb Schema

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
      "name": "Government Exams",
      "item": "https://www.searchsarkarinaukri.com/exams"
    }
  ]
}
```

---

**Last Updated:** 21 September 2026
