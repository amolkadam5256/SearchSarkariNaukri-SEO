# Proposed Structured Data

This is a **template**, not publish-ready JSON-LD. Replace the image URL after upload, set dates from the CMS only at publication/update time, and confirm that the CMS does not already emit equivalent schema. Do not emit empty or placeholder values.

```json
[
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "What Happens During Probation in a Government Job? Rules Explained",
    "description": "Understand government job probation, training, extension, confirmation and discharge rules in India. Check the terms that apply to your appointment.",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://www.searchsarkarinaukri.com/blogs/what-happens-during-probation-in-a-government-job-can-you-lose-the-job"
    },
    "author": {
      "@type": "Organization",
      "name": "Search Sarkari Naukri"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Search Sarkari Naukri"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.searchsarkarinaukri.com/"},
      {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.searchsarkarinaukri.com/blogs"},
      {"@type": "ListItem", "position": 3, "name": "What Happens During Probation in a Government Job? Rules Explained", "item": "https://www.searchsarkarinaukri.com/blogs/what-happens-during-probation-in-a-government-job-can-you-lose-the-job"}
    ]
  }
]
```

Before deployment, add `image`, `datePublished`, and `dateModified` only when the real image and CMS dates are known. Use the genuine byline if the visible page uses an individual author. FAQPage is intentionally omitted; keep the FAQ visible in the article and do not add FAQ markup unless current policy and eligibility support it. Do not duplicate sitewide Organization/WebSite schema.
