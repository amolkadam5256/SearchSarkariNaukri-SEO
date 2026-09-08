# 05 — SEO METADATA SPECIFICATION

**Section:** Technical SEO Metadata  
**Priority:** P0  
**Type:** Technical Implementation  
**Status:** Implementation Ready

---

## Main Districts Page Metadata

### Title Tag
```
Maharashtra Government Jobs by District | District Wise Sarkari Naukri
```

### Meta Description
```
Find Maharashtra government jobs by district. Explore Pune, Mumbai, Nagpur, Nashik and all 36 districts for latest Sarkari Naukri, recruitment, eligibility and vacancy updates.
```

### Canonical URL
```
https://www.searchsarkarinaukri.com/districts
```

### Robots Meta Tag
```
<meta name="robots" content="index, follow">
```

### Open Graph Metadata
```html
<meta property="og:title" content="Maharashtra Government Jobs by District | District Wise Sarkari Naukri">
<meta property="og:description" content="Find Maharashtra government jobs by district. Explore Pune, Mumbai, Nagpur, Nashik and all 36 districts for latest Sarkari Naukri.">
<meta property="og:url" content="https://www.searchsarkarinaukri.com/districts">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.searchsarkarinaukri.com/og-maharashtra-districts.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="SearchSarkariNaukri">
```

### Twitter/X Metadata
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Maharashtra Government Jobs by District | District Wise Sarkari Naukri">
<meta name="twitter:description" content="Find Maharashtra government jobs by district. Explore Pune, Mumbai, Nagpur, Nashik and all 36 districts for latest Sarkari Naukri.">
<meta name="twitter:image" content="https://www.searchsarkarinaukri.com/twitter-maharashtra-districts.jpg">
```

---

## Individual District Page Metadata Template

### Title Tag Template
```
Government Jobs in {District Name}, Maharashtra – {District Name} Sarkari Naukri
```

### Examples
```
Government Jobs in Pune, Maharashtra – Pune Sarkari Naukri
Government Jobs in Mumbai City, Maharashtra – Mumbai Sarkari Naukri
Government Jobs in Nagpur, Maharashtra – Nagpur Sarkari Naukri
Government Jobs in Nashik, Maharashtra – Nashik Sarkari Naukri
```

### Meta Description Template
```
Find latest government jobs in {District Name}, Maharashtra. Browse {District Name} Sarkari Naukri, recruitment, eligibility, vacancies and application updates.
```

### Examples
```
Find latest government jobs in Pune, Maharashtra. Browse Pune Sarkari Naukri, recruitment, eligibility, vacancies and application updates.
Find latest government jobs in Mumbai City, Maharashtra. Browse Mumbai Sarkari Naukri, recruitment, eligibility, vacancies and application updates.
Find latest government jobs in Nagpur, Maharashtra. Browse Nagpur Sarkari Naukri, recruitment, eligibility, vacancies and application updates.
```

### Canonical URL Template
```
https://www.searchsarkarinaukri.com/districts/{district-slug}
```

### Examples
```
https://www.searchsarkarinaukri.com/districts/pune
https://www.searchsarkarinaukri.com/districts/mumbai-city
https://www.searchsarkarinaukri.com/districts/nagpur
https://www.searchsarkarinaukri.com/districts/nashik
```

---

## District Slug Mapping

### Official District Names to Slugs

| District Name | Slug |
|--------------|------|
| Pune | pune |
| Mumbai City | mumbai-city |
| Mumbai Suburban | mumbai-suburban |
| Thane | thane |
| Palghar | palghar |
| Raigad | raigad |
| Ratnagiri | ratnagiri |
| Sindhudurg | sindhudurg |
| Nashik | nashik |
| Dhule | dhule |
| Nandurbar | nandurbar |
| Jalgaon | jalgaon |
| Ahilyanagar | ahilyanagar |
| Satara | satara |
| Sangli | sangli |
| Kolhapur | kolhapur |
| Solapur | solapur |
| Chhatrapati Sambhajinagar | chhatrapati-sambhajinagar |
| Jalna | jalna |
| Beed | beed |
| Latur | latur |
| Dharashiv | dharashiv |
| Nanded | nanded |
| Hingoli | hingoli |
| Parbhani | parbhani |
| Amravati | amravati |
| Yavatmal | yavatmal |
| Buldhana | buldhana |
| Akola | akola |
| Washim | washim |
| Nagpur | nagpur |
| Wardha | wardha |
| Chandrapur | chandrapur |
| Gadchiroli | gadchiroli |
| Bhandara | bhandara |
| Gondia | gondia |

---

## Structured Data Specification

### Main Districts Page

#### WebPage Schema
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Maharashtra Government Jobs by District",
  "description": "Find Maharashtra government jobs by district. Explore Pune, Mumbai, Nagpur, Nashik and all 36 districts for latest Sarkari Naukri.",
  "url": "https://www.searchsarkarinaukri.com/districts",
  "dateModified": "2026-09-08",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SearchSarkariNaukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

#### BreadcrumbList Schema
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
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Maharashtra Districts",
      "item": "https://www.searchsarkarinaukri.com/districts"
    }
  ]
}
```

#### ItemList Schema (For District Links)
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Pune",
      "url": "https://www.searchsarkarinaukri.com/districts/pune"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Mumbai City",
      "url": "https://www.searchsarkarinaukri.com/districts/mumbai-city"
    }
  ]
}
```

---

## Individual District Page Schema

### WebPage Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Government Jobs in {District Name}",
  "description": "Find latest government jobs in {District Name}, Maharashtra.",
  "url": "https://www.searchsarkarinaukri.com/districts/{district-slug}",
  "dateModified": "{dynamic-date}",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SearchSarkariNaukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

### BreadcrumbList Schema Template
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
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Maharashtra Districts",
      "item": "https://www.searchsarkarinaukri.com/districts"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "{District Name}",
      "item": "https://www.searchsarkarinaukri.com/districts/{district-slug}"
    }
  ]
}
```

---

## FAQ Schema Specification

### FAQPage Schema (If Eligible)

**Only implement if:**
- FAQ content is visible on the page
- FAQ meets Google's current requirements
- Questions and answers are genuinely helpful

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How can I find government jobs by district in Maharashtra?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maharashtra government jobs can be searched district-wise by selecting your district from the district directory above and reviewing currently active recruitment notifications."
      }
    },
    {
      "@type": "Question",
      "name": "How many districts are there in Maharashtra?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Maharashtra has 36 districts organized into 6 regions: Mumbai & Konkan, North Maharashtra, West Maharashtra, Marathwada, Vidarbha (Amravati) and Vidarbha (Nagpur)."
      }
    }
  ]
}
```

---

## Implementation Requirements

### Dynamic Metadata
- Title tag should be dynamically generated
- Meta description should be dynamically generated
- Canonical should be self-referencing
- DateModified should be dynamic from database

### URL Consistency
- Use consistent slugs across database, UI, URLs, and sitemap
- Ensure no duplicate URLs for same district
- Implement proper redirects if URLs change

### Image Optimization
- Use WebP/AVIF format for OG images
- Specify width and height
- Use descriptive alt text
- Lazy load below-fold images

### Validation Checklist

- [ ] Title tag implemented
- [ ] Meta description implemented
- [ ] Canonical tag correct
- [ ] Open Graph metadata complete
- [ ] Twitter metadata complete
- [ ] Robots meta tag correct
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] ItemList schema implemented
- [ ] FAQ schema (if eligible)
- [ ] No duplicate metadata
- [ ] No fabricated information

---

**Last Updated:** 8 September 2026  
**Status:** Implementation Ready