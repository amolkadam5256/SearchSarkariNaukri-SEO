# Complete Redirect Error Audit and Developer Fix Specification

## 1. GSC Issue Summary

Google Search Console reports one affected URL under `Redirect error`:

- URL: `https://www.searchsarkarinaukri.com/jobs?district_slug=pune`
- Last crawled: 7 June 2026, 09:07:11
- Crawled as: Googlebot smartphone
- Crawl allowed: Yes
- Page fetch: Failed - Redirect error
- Indexing allowed: N/A
- User-declared canonical: N/A
- Google-selected canonical: N/A
- Validation started: 14 June 2026
- Last update shown: 21 August 2026

## 2. Correct URL Architecture

The query URL is not the SEO page. It should resolve like this:

```text
https://www.searchsarkarinaukri.com/jobs?district_slug=pune
301 or 308, single server-side hop
https://www.searchsarkarinaukri.com/districts/pune
```

Important: use `/districts/pune`, not `/district/pune`. Existing live crawl evidence shows `/districts/pune` is the canonical 200 URL.

## 3. Current Destination Evidence

Local audit evidence from `SEO_Audit_Review_2026-08-25/outputs/raw-crawl-data/url-audit-all.csv` shows:

- Destination URL: `https://www.searchsarkarinaukri.com/districts/pune`
- HTTP status: 200
- Canonical: `https://www.searchsarkarinaukri.com/districts/pune`
- Robots: `index, follow, max-snippet:-1, max-image-preview:large`
- Indexable: true
- H1: `Pune Government Jobs 2026 - Latest District Sarkari Naukri`
- Current sections: latest jobs, category links, related Maharashtra searches, FAQ
- Word count: about 1159
- Internal links: about 48

This means the destination is the right ranking target, but the redirect source still needs a clean server-side permanent redirect and the Pune landing page should be strengthened for local intent.

## 4. Root Cause Areas to Audit

Search the repository and deployment config for:

- `district_slug`
- `/jobs?`
- `/districts/`
- `/district/`
- `/jobs-in-pune`
- `canonical`
- `metadata`
- `generateMetadata`
- `redirect`
- `permanentRedirect`
- `NextResponse.redirect`
- `middleware`
- `sitemap`
- `robots`
- `FAQPage`
- `BreadcrumbList`

Map every usage before changing code. Do not patch Pune only if the same `district_slug` redirect logic affects other districts.

## 5. Redirect Implementation Requirements

- Redirect must happen server-side before page render.
- Do not use `window.location`, `useEffect`, client router redirects, loading pages, meta refresh, or JavaScript-only redirects.
- Use exactly one redirect layer: framework redirect, middleware redirect, route handler, or server/CDN redirect.
- Do not stack CDN + middleware + app redirects for the same rule.
- Preserve query URL as a redirect source only; do not add it to sitemap.
- Destination must be absolute or canonicalized consistently to `https://www.searchsarkarinaukri.com/districts/pune`.
- Avoid chains such as `/jobs?district_slug=pune` -> `/jobs?district=pune` -> `/districts/pune`.
- Avoid loops where `/districts/pune` redirects back to `/jobs` or a trailing slash variant.

## 6. Reusable Redirect Logic

Build a reusable district mapping function. Do not hard-code only Pune.

Required examples:

```text
/jobs?district_slug=pune -> /districts/pune
/jobs?district_slug=mumbai -> /districts/mumbai
/jobs?district_slug=nagpur -> /districts/nagpur
/jobs?district_slug=nashik -> /districts/nashik
```

If a district has a renamed canonical slug, map old slug to the current canonical district slug, for example:

```text
/jobs?district_slug=ahmednagar -> /districts/ahilyanagar
```

Use the same source of truth as district pages and sitemap generation. Invalid district slugs should not redirect to unrelated pages.

## 7. Destination Page SEO Requirements

The destination page `/districts/pune` should include or preserve these sections:

1. H1: Pune Government Jobs 2026 - Latest District Sarkari Naukri.
2. Short Pune-specific intro mentioning Pune district, Maharashtra, government recruitment, and live job updates.
3. Latest Pune government jobs list from real data only.
4. Pune job categories: ZP, Police Bharti, Health, Education, MPSC, SSC, Railway, Banking, Talathi, Central Government.
5. Eligibility overview: 10th pass, 12th pass, ITI, diploma, graduate, engineering, post graduate.
6. Important dates guidance: notification date, apply start date, last date, exam/admit card/result where available.
7. Application process: official notification, eligibility check, documents, online application, fee, final submission.
8. Pune-specific recruiting authorities/entities: Pune Zilla Parishad, Maharashtra Police, MPSC, PMC/PCMC where applicable, ESIC, DIAT, NCRA/TIFR, Railway, SSC, Central Government departments.
9. Salary and selection process overview without fabricating job-specific data.
10. Internal links to Pune category pages and nearby Maharashtra district pages.
11. Editorial verification/disclaimer: SearchSarkariNaukri summarizes official notifications; applicants must confirm on official authority websites.
12. FAQ section with 10-15 useful questions.
13. Last updated/reviewed date tied to real data refresh.
14. Breadcrumbs: Home > District Jobs > Pune.
15. Structured data: BreadcrumbList, ItemList, FAQPage only when FAQ is visible on-page.

## 8. Missing / Weak Sections to Strengthen

The current Pune page already has useful structure and about 1159 words, but the developer should verify these are visible in rendered HTML and not only client-side after hydration:

- Real latest jobs block with current Pune vacancies.
- Category-specific Pune links.
- Nearby district links for Maharashtra discovery.
- Eligibility and application guidance.
- Official source/disclaimer block.
- 10-15 FAQ answers, not only 3 short FAQs.
- Structured data matching visible content.

## 9. Internal Link Requirements

Update internal links that still point to the old query URL:

- Replace `/jobs?district_slug=pune` with `/districts/pune` in homepage, jobs page, district lists, job cards, breadcrumbs, footer-like link collections only if those links exist there already.
- Do not redesign footer/navbar or add new global UI blocks.
- Add contextual links from relevant job detail pages to `/districts/pune` where job location includes Pune.
- Add category links from `/districts/pune` to:
  - `/districts/pune/zp`
  - `/districts/pune/police`
  - `/districts/pune/health`
  - `/districts/pune/education`
  - `/districts/pune/mpsc`
  - `/districts/pune/ssc`
  - `/districts/pune/railway`
  - `/districts/pune/banking`
  - `/districts/pune/talathi`
  - `/districts/pune/central`
- Add nearby/related Maharashtra links where supported by existing page design: Mumbai, Thane, Nashik, Nagpur, Kolhapur, Jalgaon, Jalna, Amravati.

## 10. Keyword Map

Primary keyword:

- Pune government jobs 2026

Secondary keywords:

- Pune sarkari naukri
- govt jobs in Pune
- latest government jobs in Pune district
- Maharashtra government jobs Pune
- Pune ZP recruitment
- Pune Police Bharti
- MPSC jobs in Pune
- SSC jobs in Pune
- Railway jobs in Pune
- Banking jobs in Pune
- Health department jobs Pune
- Education jobs Pune
- Talathi jobs Pune
- Central government jobs Pune
- 10th pass government jobs Pune
- 12th pass government jobs Pune
- ITI government jobs Pune
- graduate government jobs Pune
- engineering government jobs Pune

Marathi/Hinglish support terms where the site already uses them:

- Pune Sarkari Naukri
- Pune Bharti 2026
- Pune Zilla Parishad Bharti
- Maharashtra Sarkari Naukri Pune

## 11. FAQ Content to Add to Pune Page

Add 10-15 visible FAQs. Use FAQPage schema only for the FAQs that are visible on the page.

1. Where can I find the latest government jobs in Pune?
   Answer: The Pune district page lists current government job updates matched to Pune, including district, state, and central recruitment where Pune is a relevant location.

2. Is `/districts/pune` the official Pune jobs page on SearchSarkariNaukri?
   Answer: Yes. `/districts/pune` should be the clean canonical SearchSarkariNaukri landing page for Pune government job updates.

3. Why should `/jobs?district_slug=pune` redirect to `/districts/pune`?
   Answer: The query URL is an old filter URL. Redirecting it to the clean district URL prevents duplicate crawl paths and gives Google one canonical page to index.

4. Which Pune government job categories are covered?
   Answer: The page should cover Pune ZP, Police Bharti, Health, Education, MPSC, SSC, Railway, Banking, Talathi, Forest, UPSC, and Central Government job categories where active data exists.

5. Are the Pune job listings official?
   Answer: SearchSarkariNaukri is an information portal. Each application should be completed only through the official recruiting authority website or notification link.

6. How often are Pune government jobs updated?
   Answer: The page should refresh from the live job dataset whenever jobs are added, updated, expired, or removed.

7. Can 10th pass candidates find government jobs in Pune?
   Answer: Yes, when available, Pune jobs can be filtered or linked by 10th pass eligibility such as support staff, constable, helper, and similar roles.

8. Can 12th pass or ITI candidates apply for Pune government jobs?
   Answer: Yes, many departments publish 12th pass and ITI-level vacancies. Exact eligibility must be verified in the official notification.

9. Are there MPSC jobs in Pune?
   Answer: Pune-related MPSC vacancies should appear on the Pune district page and the Pune MPSC category page when the job data matches Pune.

10. Are there Pune Police Bharti updates?
    Answer: Pune Police Bharti updates should be listed when Maharashtra Police or related authorities publish vacancies connected to Pune district.

11. How do I apply for Pune government jobs online?
    Answer: Open the job detail, read eligibility and dates, verify the official notification, then apply through the official application link.

12. What documents are usually required for Pune Sarkari Naukri applications?
    Answer: Common documents include identity proof, address proof, caste/category certificate if applicable, educational certificates, photo, signature, and experience certificate where required.

13. Does the Pune page include expired jobs?
    Answer: The ranking page should prioritize active jobs. Expired jobs should not create broken internal links; they may be archived only if the archive strategy is intentional.

14. What is the age limit for Pune government jobs?
    Answer: Age limits differ by post, department, category, and recruitment rules. Users must confirm the exact limit in the official notification.

15. Which nearby Maharashtra districts can I check along with Pune?
    Answer: Users can also check Mumbai, Thane, Nashik, Nagpur, Kolhapur, Jalgaon, Jalna, Amravati, and other Maharashtra district job pages.

## 12. Developer Scope Guardrail

Do not change any unrelated page, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, or shared component unless it is strictly required to fix this redirect architecture. Keep the fix limited to redirect behavior, canonical signals, sitemap/internal-link cleanup, the Pune destination page content sections, and matching structured data. If a shared template must be edited, verify that unrelated pages do not change visually or functionally.

## 13. Definition of Done

- `/jobs?district_slug=pune` returns exactly one 301 or 308 redirect.
- Redirect location is `https://www.searchsarkarinaukri.com/districts/pune`.
- `/districts/pune` returns HTTP 200 and does not redirect again.
- `/districts/pune` is indexable and self-canonical.
- `/jobs?district_slug=pune` is not in XML sitemap.
- `/districts/pune` is in XML sitemap.
- Internal links use `/districts/pune`, not the query URL.
- Pune page has strong location content, category links, and 10-15 FAQs.
- BreadcrumbList, ItemList, and FAQPage schema are valid and match visible content.
- No redirect loop, chain, soft 404, noindex, robots block, duplicate canonical, or broken internal links.
## AI / LLM Ranking Addendum

Before implementation, read `../04_AI_AEO_GEO_SEO_Ranking/01_AI_LLM_AEO_GEO_SEO_RANKING_REQUIREMENTS.md`. The redirect fix must consolidate SEO, AEO, GEO, and LLM citation signals on `/districts/pune`. Do not add `/jobs?district_slug=pune` to sitemap, canonical tags, internal links, or `llms.txt` as a ranking URL.

