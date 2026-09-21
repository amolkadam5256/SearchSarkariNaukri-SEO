# 06 — SCHEMA MARKUP SPECIFICATION

**Section:** Structured Data Implementation  
**Priority:** P1  
**Type:** Technical Implementation  
**Status:** Implementation Ready

---

## CONTENT EDITING RULES

**IMPORTANT:** When updating or creating any content based on this specification, follow these human editing guidelines:

### Primary Objective
Transform draft content into natural, original, reader-first writing while preserving factual meaning, important facts, numbers, dates, names, terminology, search intent, primary topic, important keywords, useful supporting information, intended audience, actual purpose of the page, and legitimate claims supported by source material.

### Key Requirements
1. **Remove generic AI-style openings** - Avoid predictable openings like "In today's digital world...", "In this comprehensive guide...", "Let's dive in...". Start with direct, useful information.
2. **Remove repetition** - Check for repeated ideas, keywords, conclusions, explanations, adjectives, sentence structures, headings, and calls to action.
3. **Vary sentence structure** - Mix short, medium, and long sentences. Avoid predictable grammatical patterns.
4. **Improve paragraph flow** - Use transitions only when genuinely helpful. Avoid excessive use of "Furthermore", "Moreover", "Additionally", etc.
5. **Remove formulaic "rule of three" writing** - Avoid unnecessary lists of three similar adjectives unless they provide genuinely different information.
6. **Remove filler** - Delete unnecessary phrases like "It is worth mentioning that", "It should be noted that", "Needless to say", etc.
7. **Use specific language** - Replace vague statements with precise information. Do not add unsupported facts.
8. **Preserve factual accuracy** - Never change dates, statistics, percentages, names, official terminology, URLs, product names, organization names, exam names, job titles, application requirements, eligibility conditions, fees, or deadlines.
9. **Make writing contextual** - Write according to the actual subject (informational, SEO, product, news, educational, job/exam content).
10. **SEO requirements** - Maintain important target keywords naturally. Never stuff keywords or sacrifice readability for SEO.
11. **Heading structure** - Keep logical hierarchy (H1, H2, H3). Use descriptive headings, not generic ones like "Introduction" or "Conclusion".
12. **Lists and tables** - Use bullet points when information is easier to scan as a list. Use tables for structured comparisons.
13. **Remove robotic phrases** - Rewrite templated or generic phrases naturally.
14. **Do not over-humanize** - Do not add random typos, grammar mistakes, excessive slang, fake personal stories, or fake opinions.
15. **Add human-like specificity** - Prefer concrete explanations over generic claims when supported by source material.
16. **Control tone** - Use professional, clear, direct, helpful, natural, confident tone without exaggeration.
17. **Readability** - Make content easy to scan with short paragraphs, clear headings, direct sentences, useful lists, concrete explanations, and logical ordering.
18. **Preserve author's intent** - Do not change the message simply because of personal style preference.
19. **Originality** - Perform genuine rewriting, not superficial synonym replacement. Understand the idea, identify purpose, reorganize wording, rewrite sentence structures, combine repetitive statements, improve clarity, add specificity only when supported, preserve important terminology, and produce genuinely original phrasing.
20. **Final quality check** - Verify content (meaning preserved, no important info removed, no unsupported claims, no changed facts), writing (natural, varied sentences, purposeful paragraphs, no repetition, appropriate formality, no templates), SEO (search intent satisfied, keywords natural, no stuffing, useful headings, crawlable structure), readability (quick understanding, broken long sentences, reasonable paragraph sizes, useful lists), and quality (precise wording, qualified claims, genuinely useful, valuable sections).

### Output Rule
Return ONLY the rewritten content unless explicitly asked for explanation or audit. Do not mention AI detection, humanization, or bypassing detectors. The objective is high-quality human-readable content, not detector manipulation.

---

## Structured Data Types to Implement

## 21 September 2026 Schema Boundary Update

`/job-updates` is a multi-job alert/listing hub. It must not contain `JobPosting` schema.

- [ ] Use `WebPage` for the page.
- [ ] Use `BreadcrumbList` for `Home -> Job Updates`.
- [ ] Use `ItemList` only for visible job-list links when useful.
- [ ] Use `FAQPage` only when FAQ content is visible and eligible.
- [ ] Do not use `JobPosting` on `/job-updates`.
- [ ] Use `JobPosting` only on individual job detail pages that describe one job/recruitment.
- [ ] Keep `datePosted` and `validThrough` accurate on job detail pages.
- [ ] Remove expired jobs from active listings.

Freshness fields:

- `lastReviewed` and `dateModified` must reflect real page/content/job-alert dataset updates.
- Do not generate schema freshness with current render time on every request.

### 1. WebPage Schema
**Priority:** High  
**Implementation:** Required

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Sarkari Naukri & Government Job Alerts 2026",
  "description": "Find the latest Sarkari Naukri and government job alerts for 2026. Check vacancies, recruitment updates, deadlines and free WhatsApp & Telegram job alerts.",
  "url": "https://www.searchsarkarinaukri.com/job-updates",
  "lastReviewed": "[dynamic date]",
  "dateModified": "[dynamic date]",
  "breadcrumb": {
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
        "name": "Job Updates",
        "item": "https://www.searchsarkarinaukri.com/job-updates"
      }
    ]
  }
}
```

### 2. BreadcrumbList Schema
**Priority:** High  
**Implementation:** Required

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
      "name": "Job Updates",
      "item": "https://www.searchsarkarinaukri.com/job-updates"
    }
  ]
}
```

### 3. Organization Schema
**Priority:** High  
**Implementation:** Required

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Search Sarkari Naukri",
  "url": "https://www.searchsarkarinaukri.com",
  "logo": "[logo URL]",
  "description": "Government job information and recruitment updates platform",
  "sameAs": [
    "[Facebook URL]",
    "[Twitter URL]",
    "[WhatsApp URL]",
    "[Telegram URL]"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "[contact email]",
    "availableLanguage": "English"
  }
}
```

### 4. WebSite Schema
**Priority:** High  
**Implementation:** Required

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Search Sarkari Naukri",
  "url": "https://www.searchsarkarinaukri.com",
  "description": "Government job information and recruitment updates platform",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.searchsarkarinaukri.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### 5. FAQPage Schema
**Priority:** Medium  
**Implementation:** Conditional (only when visible FAQ content exists and complies with Google's requirements)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Sarkari Naukri?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sarkari Naukri refers to employment opportunities offered through central and state government departments, public-sector organizations and other government bodies in India."
      }
    },
    {
      "@type": "Question",
      "name": "Where can I find the latest Sarkari Naukri?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can browse current government recruitment updates through the Jobs and Job Updates sections of Search Sarkari Naukri. Always check the official recruitment notification before applying."
      }
    },
    {
      "@type": "Question",
      "name": "Are government job alerts free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The Search Sarkari Naukri WhatsApp Community and Telegram Channel promoted on this page are free to join."
      }
    },
    {
      "@type": "Question",
      "name": "How can I get Sarkari Naukri alerts on WhatsApp?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Join the Search Sarkari Naukri WhatsApp Community through the official join link on this page. You can receive daily-curated recruitment updates and deadline reminders."
      }
    },
    {
      "@type": "Question",
      "name": "How can I get government job alerts on Telegram?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Join the official Search Sarkari Naukri Telegram Channel using the Telegram link provided on this page."
      }
    },
    {
      "@type": "Question",
      "name": "Can I find government jobs by qualification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Job seekers can browse opportunities according to qualifications such as 10th pass, 12th pass, Graduate, ITI and Diploma, where the relevant job data is available."
      }
    },
    {
      "@type": "Question",
      "name": "How can I check my eligibility for a government job?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Read the eligibility requirements in the official recruitment notification. Search Sarkari Naukri also provides an Eligibility Checker for a basic profile match."
      }
    },
    {
      "@type": "Question",
      "name": "Are Search Sarkari Naukri and the government the same organization?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Search Sarkari Naukri is an independent government-job information platform. Candidates should verify recruitment information through the official notification and official website before applying."
      }
    }
  ]
}
```

### 6. ItemList Schema (For Job Listings)
**Priority:** Medium  
**Implementation:** Conditional (only for genuine dynamic job listings)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "url": "[job detail page URL]"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "url": "[job detail page URL]"
    }
  ]
}
```

### 7. JobPosting Schema
**Priority:** Low  
**Implementation:** DO NOT use on this page

**Reason:** JobPosting schema should only be used on individual job detail pages where the data genuinely represents a single job posting. Do not put fake/aggregated JobPosting schema on this landing page.

---

## Schema Implementation Requirements

### JSON-LD Format
- Use JSON-LD format
- Place in `<head>` section
- Include in HTML or inject via JavaScript
- Validate with Google Rich Results Test

### Dynamic Fields
Mark these fields as dynamic:
- `lastReviewed`: Last update date
- `dateModified`: Content modification date
- `itemListElement`: Dynamic job listings
- `item.url`: Dynamic job URLs

### Validation
- Validate all schema with Google Rich Results Test
- Validate with Schema.org validator
- Check for syntax errors
- Verify required fields are present
- Verify field types are correct

---

## Schema Placement

### Placement Order
1. WebPage schema
2. BreadcrumbList schema
3. Organization schema
4. WebSite schema
5. FAQPage schema (if applicable)
6. ItemList schema (if applicable)

### HTML Placement
```html
<head>
  <script type="application/ld+json">
    <!-- WebPage schema -->
  </script>
  
  <script type="application/ld+json">
    <!-- BreadcrumbList schema -->
  </script>
  
  <script type="application/ld+json">
    <!-- Organization schema -->
  </script>
  
  <script type="application/ld+json">
    <!-- WebSite schema -->
  </script>
  
  <script type="application/ld+json">
    <!-- FAQPage schema -->
  </script>
  
  <script type="application/ld+json">
    <!-- ItemList schema -->
  </script>
</head>
```

---

## Important Schema Rules

### Do Not Fake Data
- Do not invent job postings
- Do not create fake job listings
- Do not aggregate job data into single JobPosting
- Only use real data from database

### Do Not Use JobPosting on Landing Page
- JobPosting schema is for individual job pages only
- This page is a job alert hub, not a single job posting
- Use ItemList for job listings, not JobPosting

### FAQPage Requirements
- Only implement when visible FAQ content exists
- Questions must match visible FAQ headings
- Answers must match visible FAQ content
- Do not include hidden FAQ content
- Do not include fake questions

### Dynamic Updates
- Update `lastReviewed` and `dateModified` when content changes
- Update `itemListElement` when job listings change
- Keep schema in sync with visible content

---

## Schema Testing

### Pre-Deployment Testing
1. Test with Google Rich Results Test
2. Test with Schema.org validator
3. Test with structured data testing tool
4. Check for syntax errors
5. Verify required fields

### Post-Deployment Testing
1. Run Google Rich Results Test on live URL
2. Check Google Search Console for errors
3. Monitor for warnings
4. Verify rich results display (if applicable)
5. Fix any errors immediately

---

**Implementation Priority:** P1  
**Schema Types:** WebPage, BreadcrumbList, Organization, WebSite, FAQPage (conditional), ItemList (conditional)  
**Validation Required:** Yes  
**Tools:** Google Rich Results Test, Schema.org Validator
