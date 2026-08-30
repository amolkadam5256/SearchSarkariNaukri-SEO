# AI, LLM, AEO, GEO and SEO Ranking Requirements for Redirect Error Fix

## 1. Purpose

This file explains how the redirect fix for `https://www.searchsarkarinaukri.com/jobs?district_slug=pune` should support Google indexing, AI Overviews, ChatGPT/Bing/Perplexity-style citation, answer engines, and local SEO.

The query URL must not become a ranking page. The AI/SEO target is:

`https://www.searchsarkarinaukri.com/districts/pune`

## 2. LLM and AI Visibility Principle

LLM systems and answer engines need one clear crawlable source for each topic. For Pune government jobs, the site should send every signal to one canonical URL:

- Redirect source: `/jobs?district_slug=pune`
- Canonical destination: `/districts/pune`
- Sitemap URL: `/districts/pune`
- Internal links: `/districts/pune`
- Breadcrumb URL: `/districts/pune`
- Schema URL: `/districts/pune`
- OG/Twitter URL: `/districts/pune`

Do not split signals between `/jobs?district_slug=pune`, `/jobs-in-pune`, `/district/pune`, and `/districts/pune` unless there is a deliberate canonical strategy. For this issue, `/districts/pune` is the required canonical page.

## 3. llms.txt Recommendation

No dedicated `llms.txt` file was found in this workspace during this review. If the production site uses or plans to add `llms.txt`, include the canonical Pune district page and important hub pages, not query-parameter URLs.

Recommended `llms.txt` style entries:

```text
# SearchSarkariNaukri

SearchSarkariNaukri is an independent government job information portal for India and Maharashtra recruitment updates.

## Core pages
- https://www.searchsarkarinaukri.com/
- https://www.searchsarkarinaukri.com/jobs
- https://www.searchsarkarinaukri.com/districts
- https://www.searchsarkarinaukri.com/districts/pune

## Pune government job pages
- https://www.searchsarkarinaukri.com/districts/pune
- https://www.searchsarkarinaukri.com/districts/pune/zp
- https://www.searchsarkarinaukri.com/districts/pune/police
- https://www.searchsarkarinaukri.com/districts/pune/health
- https://www.searchsarkarinaukri.com/districts/pune/education
- https://www.searchsarkarinaukri.com/districts/pune/mpsc
- https://www.searchsarkarinaukri.com/districts/pune/ssc
- https://www.searchsarkarinaukri.com/districts/pune/railway
- https://www.searchsarkarinaukri.com/districts/pune/banking
- https://www.searchsarkarinaukri.com/districts/pune/talathi
- https://www.searchsarkarinaukri.com/districts/pune/central
```

Do not add `/jobs?district_slug=pune` to `llms.txt` because it is a redirect source, not the final answer page.

## 4. Robots and AI Crawler Requirements

Preserve current AI-crawler accessibility unless business policy says otherwise. The prior GEO audit found the site allows or prerenders for major AI/search crawlers, including Googlebot, Bingbot, GPTBot/OAI-SearchBot, Perplexity, Anthropic/ClaudeBot, CCBot, Google-Extended, and Applebot-Extended.

Developer checks:

- Do not block `/districts/pune` in `robots.txt`.
- Do not add `noindex` to `/districts/pune`.
- Do not send `X-Robots-Tag: noindex` for `/districts/pune`.
- Keep `max-snippet:-1` for snippet and AI answer extraction.
- Ensure prerendered/raw HTML contains visible Pune content for crawlers that do not execute JavaScript.

## 5. AEO Requirements

Answer Engine Optimization needs direct, extractable answers. The Pune page should answer user questions in short, self-contained paragraphs.

Required answer style:

- Put the direct answer in the first sentence.
- Use absolute dates when discussing deadlines; do not use vague phrases like `today`, `tomorrow`, or `next week` unless paired with an exact date.
- Keep FAQ answer text visible on-page and identical in FAQPage schema.
- Use headings that match natural questions: eligibility, age limit, last date, how to apply, salary, official notification, documents.

Add 10-15 Pune-specific FAQs from the master report. Use FAQPage schema only for visible FAQs.

## 6. GEO Requirements

Generative Engine Optimization needs clear entity facts and source confidence.

Add or preserve these labeled facts on `/districts/pune`:

- Page topic: Pune Government Jobs 2026.
- Location entity: Pune district, Maharashtra, India.
- Job categories: ZP, Police Bharti, Health, Education, MPSC, SSC, Railway, Banking, Talathi, Forest, UPSC, Central Government.
- Qualification entities: 10th pass, 12th pass, ITI, diploma, graduate, engineering, post graduate.
- Recruiting entities where data exists: Pune Zilla Parishad, Maharashtra Police, MPSC, PMC/PCMC, ESIC, DIAT, NCRA/TIFR, Railway, SSC, central government departments.
- Editorial source note: SearchSarkariNaukri summarizes official recruitment notifications and users must verify details on official authority websites.
- Freshness note: show a real `last updated` or `last reviewed` date tied to the live job dataset.

## 7. SEO Requirements

For `/districts/pune`:

- HTTP 200.
- Self canonical exactly `https://www.searchsarkarinaukri.com/districts/pune`.
- Title focused on `Pune Government Jobs 2026` or `Pune Sarkari Naukri 2026`.
- Meta description near 120-155 characters with Pune, Maharashtra, job categories, eligibility, and latest updates.
- One H1.
- H2 sections for latest jobs, categories, eligibility, application process, important dates, related districts, and FAQs.
- Breadcrumbs: Home > District Jobs > Pune.
- XML sitemap includes `/districts/pune` only, not `/jobs?district_slug=pune`.
- Internal links use clean canonical URLs.

## 8. Internal Linking for AI and SEO

Replace old internal links to `/jobs?district_slug=pune` with `/districts/pune`.

Add contextual links using descriptive anchors:

- Pune Government Jobs 2026
- Pune Sarkari Naukri
- Pune ZP Recruitment
- Pune Police Bharti
- MPSC Jobs in Pune
- SSC Jobs in Pune
- Railway Jobs in Pune
- Health Department Jobs in Pune
- Education Jobs in Pune
- Central Government Jobs in Pune

Do not create unrelated footer/navbar changes. Only update existing links if they already point to the old query URL or if the current page already has a related-links section.

## 9. Structured Data Requirements

Use structured data that matches visible content:

- `Organization` for SearchSarkariNaukri.
- `WebSite` with SearchAction for the main site search.
- `BreadcrumbList` for Home > District Jobs > Pune.
- `ItemList` for active Pune job listings.
- `FAQPage` for visible Pune FAQs only.

Do not mark up hidden FAQs. Do not invent job facts. Do not use JobPosting schema on the district page unless each listed job has accurate structured job data and links to the full job detail page.

## 10. Ranking Content Sections to Add or Verify

The Pune page should have these visible sections:

1. Short direct summary: `Pune Government Jobs 2026 lists the latest verified government recruitment updates for Pune district, Maharashtra.`
2. Latest Pune jobs from real job data.
3. Pune job categories.
4. Eligibility by qualification.
5. How to apply for Pune government jobs.
6. Important dates and deadline guidance.
7. Salary and selection process overview.
8. Documents usually required.
9. Official notification and verification note.
10. Related Pune category pages.
11. Nearby Maharashtra district links.
12. 10-15 FAQs.
13. Last updated/reviewed date.

## 11. Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required to fix redirect/indexing/AI visibility for this exact issue. If shared redirect or SEO utilities must be changed, regression-test unrelated district, department, qualification, job detail, sitemap, and robots behavior.

## 12. Validation Checklist

- [ ] `/jobs?district_slug=pune` redirects in one server-side 301/308 hop to `/districts/pune`.
- [ ] `/districts/pune` returns HTTP 200.
- [ ] `/districts/pune` is self-canonical and indexable.
- [ ] `/jobs?district_slug=pune` is excluded from sitemap and `llms.txt`.
- [ ] `/districts/pune` appears in sitemap and, if used, `llms.txt`.
- [ ] Raw/prerendered HTML contains Pune-specific content.
- [ ] FAQPage schema exactly matches visible FAQs.
- [ ] Internal links point to `/districts/pune`, not the query URL.
- [ ] No redirect chain, redirect loop, soft 404, noindex, robots block, or broken internal links.
- [ ] Google Search Console live test succeeds for both source redirect and destination page.
