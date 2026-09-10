# 03 — SEO METADATA SPECIFICATION

**Section:** Technical SEO Metadata  
**Priority:** P0  
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

## Main Job Updates Page Metadata

### Page URL
```
https://www.searchsarkarinaukri.com/job-updates
```

### Title Tag
**Primary Option:**
```
Sarkari Naukri & Government Job Alerts 2026 | Search Sarkari Naukri
```

**Alternative Option:**
```
Latest Sarkari Naukri 2026 – Free Government Job Alerts
```

### Meta Description
```
Find the latest Sarkari Naukri and government job alerts for 2026. Check vacancies, recruitment updates, deadlines and free WhatsApp & Telegram job alerts.
```

### H1
```
Sarkari Naukri & Government Job Alerts 2026
```

### Canonical URL
```
https://www.searchsarkarinaukri.com/job-updates
```

### Robots Meta Tag
```
<meta name="robots" content="index, follow">
```

### Open Graph Tags
```html
<meta property="og:title" content="Sarkari Naukri & Government Job Alerts 2026 | Search Sarkari Naukri">
<meta property="og:description" content="Find the latest Sarkari Naukri and government job alerts for 2026. Check vacancies, recruitment updates, deadlines and free WhatsApp & Telegram job alerts.">
<meta property="og:url" content="https://www.searchsarkarinaukri.com/job-updates">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Search Sarkari Naukri">
<meta property="og:image" content="[appropriate social share image]">
<meta property="og:locale" content="en_IN">
```

### Twitter Card Tags
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Sarkari Naukri & Government Job Alerts 2026 | Search Sarkari Naukri">
<meta name="twitter:description" content="Find the latest Sarkari Naukri and government job alerts for 2026. Check vacancies, recruitment updates, deadlines and free WhatsApp & Telegram job alerts.">
<meta name="twitter:image" content="[appropriate social share image]">
```

### Viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Character Set
```html
<meta charset="UTF-8">
```

---

## Additional Technical SEO Requirements

### URL Structure
- Keep URL as `/job-updates`
- Do not change URL unnecessarily
- Ensure URL is lowercase and hyphen-separated
- No trailing slash (unless server requires it)

### Canonical Implementation
- Self-referencing canonical
- Absolute URL (including domain)
- No parameters in canonical
- No HTTP/HTTPS mixed content

### Robots.txt
Ensure `/job-updates` is allowed in robots.txt:
```
Allow: /job-updates
```

### Sitemap
Include `/job-updates` in XML sitemap with:
- lastmod date (dynamic)
- changefreq: daily
- priority: 0.8

### Internal Linking
Link to `/job-updates` from:
- Header navigation
- Footer navigation
- Related content sections
- Job detail pages (breadcrumbs)
- Category pages
- State pages

---

## Breadcrumb Structure

### Breadcrumb HTML
```html
<nav aria-label="Breadcrumb">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a href="/" itemprop="item">
        <span itemprop="name">Home</span>
      </a>
      <meta itemprop="position" content="1" />
    </li>
    <li aria-current="page" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name">Job Updates</span>
      <meta itemprop="position" content="2" />
    </li>
  </ol>
</nav>
```

### Breadcrumb Text
```
Home → Job Updates
```

---

## Keywords in Metadata

### Primary Keyword in Title
- "Sarkari Naukri" - appears once near the beginning

### Secondary Keywords in Description
- "government job alerts"
- "vacancies"
- "recruitment updates"
- "deadlines"
- "WhatsApp"
- "Telegram"

### Natural Placement
- Keywords appear naturally
- No keyword stuffing
- No repetition
- Readable for humans
- Descriptive of page content

---

## Performance Metadata

### Preconnect
```html
<link rel="preconnect" href="https://www.searchsarkarinaukri.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
```

### DNS Prefetch
```html
<link rel="dns-prefetch" href="https://www.searchsarkarinaukri.com">
```

### Preload Critical Resources
```html
<link rel="preload" href="[critical CSS]" as="style">
<link rel="preload" href="[critical font]" as="font" crossorigin>
```

---

## Accessibility Metadata

### Language
```html
<html lang="en">
```

### ARIA Labels
```html
<nav aria-label="Breadcrumb">
<nav aria-label="Main navigation">
<button aria-label="Join WhatsApp Community">
<button aria-label="Join Telegram Channel">
```

---

## Security Headers

### Content Security Policy
Implement appropriate CSP headers for production

### X-Frame-Options
```http
X-Frame-Options: SAMEORIGIN
```

### X-Content-Type-Options
```http
X-Content-Type-Options: nosniff
```

---

## Implementation Notes

### Dynamic Elements
- Last updated date should be dynamic
- Job listings should be dynamically rendered
- No hardcoded recruitment data
- Real vacancy counts from database

### Page Speed
- Optimize images (WebP/AVIF)
- Lazy load below-the-fold content
- Minimize JavaScript
- Critical CSS inline
- Defer non-critical JavaScript

### Mobile Optimization
- Responsive viewport
- Touch-friendly buttons
- Readable font sizes
- No horizontal scrolling

---

**Implementation Priority:** P0  
**Validation Required:** Yes  
**Tools:** Google Rich Results Test, URL Inspection Tool
