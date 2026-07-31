# 12 — Structured Data & Schema.org Implementations

## 12.1 Full JSON-LD Schema Suite

### 1. JobPosting Schema JSON-LD (Job Notification Pages)
```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "SSC CGL Recruitment 2026",
  "description": "Staff Selection Commission has released CGL 2026 notification for 5000+ Group B and C posts...",
  "identifier": {
    "@type": "PropertyValue",
    "name": "SSC",
    "value": "SSC-CGL-2026"
  },
  "datePosted": "2026-07-01",
  "validThrough": "2026-08-15T23:59:59+05:30",
  "employmentType": "FULL_TIME",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "Staff Selection Commission",
    "sameAs": "https://ssc.nic.in",
    "logo": "https://www.searchsarkarinaukri.com/images/ssc-logo.png"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "addressCountry": "IN"
    }
  },
  "baseSalary": {
    "@type": "MonetaryAmount",
    "currency": "INR",
    "value": {
      "@type": "QuantitativeValue",
      "minValue": 25500,
      "maxValue": 81100,
      "unitText": "MONTH"
    }
  },
  "qualifications": "Bachelor's Degree from a recognized university",
  "directApply": false
}
```

---

### 2. BreadcrumbList Schema JSON-LD (Sitewide Pages)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.searchsarkarinaukri.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Jobs",
      "item": "https://www.searchsarkarinaukri.com/jobs"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "SSC CGL 2026",
      "item": "https://www.searchsarkarinaukri.com/jobs/ssc-cgl-2026"
    }
  ]
}
```

---

### 3. FAQPage Schema JSON-LD (Q&A Sections)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the last date to apply for SSC CGL 2026?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The last date to apply for SSC CGL 2026 is 15 August 2026."
      }
    },
    {
      "@type": "Question",
      "name": "What is the educational qualification for SSC CGL?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Candidates must hold a Bachelor's degree from a recognized university in India."
      }
    }
  ]
}
```

---

### 4. Organization & WebSite SearchAction Schema (Homepage)
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "SearchSarkariNaukri",
  "url": "https://www.searchsarkarinaukri.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.searchsarkarinaukri.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

### 5. SpeakableSpecification Schema JSON-LD (Voice Search & Google Assistant)
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "MPSC Subordinate Services Recruitment 2026 Notification",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      ".job-summary-headline",
      ".important-dates-list",
      ".eligibility-criteria"
    ]
  },
  "url": "https://www.searchsarkarinaukri.com/jobs/mpsc-subordinate-2026"
}
```

---

### 6. VideoObject Schema JSON-LD (YouTube Video SEO & Exam Guide Embeds)
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to Fill MPSC Subordinate Application Form 2026 Step-by-Step",
  "description": "Complete guide on online application procedure, document upload, and fee payment for MPSC 2026.",
  "thumbnailUrl": [
    "https://www.searchsarkarinaukri.com/images/mpsc-video-thumb.jpg"
  ],
  "uploadDate": "2026-07-15T08:00:00+05:30",
  "duration": "PT8M45S",
  "contentUrl": "https://www.youtube.com/watch?v=example123",
  "embedUrl": "https://www.youtube.com/embed/example123"
}
```

---

## 12.2 Schema Validation SOP

1. **Test Tooling:** Validate all JSON-LD templates using [Google Rich Results Test](https://search.google.com/test/rich-results) and [Schema.org Validator](https://validator.schema.org/).
2. **CI/CD Checks:** Automated pre-deploy linting ensuring JSON-LD formatting contains zero syntax errors.
3. **Search Console Audit:** Review GSC Enhancements report weekly for warnings or errors across JobPosting, FAQPage, BreadcrumbList, and NewsArticle objects.
