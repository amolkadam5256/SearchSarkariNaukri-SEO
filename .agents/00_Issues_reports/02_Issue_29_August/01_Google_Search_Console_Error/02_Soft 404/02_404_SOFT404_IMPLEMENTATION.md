# SearchSarkariNaukri — Developer Implementation

## 1. Route Rules
Implement:
- Existing valid page → 200
- Existing expired job → 200
- Valid SEO landing page with zero active jobs → 200
- Equivalent replacement → 301
- Nonexistent URL → 404
- Intentional permanent deletion → 410

**Do not use 404 simply because a job expired.**

## 2. Preserve Expired Jobs
When a recruitment closes:
- keep the original URL where useful
- mark `Closed / Expired`
- retain legitimate recruitment details
- show closing/application dates
- preserve qualification, age, salary, vacancies, selection and location information
- link to relevant current jobs

Do not automatically delete database records when a deadline passes.

## 3. Fix Zero-Result Landing Pages
Pages such as:
- `/10th-pass-jobs-in-kolkata`
- `/graduate-jobs-in-gurgaon`
- `/iti-jobs-in-west-bengal`

must remain 200 if they are legitimate SEO pages.

A page containing only `0 Active Jobs` and `No active jobs right now` is not sufficient.

Add useful, unique content and relevant historical/current job discovery.

## 4. Make All SEO Sections Crawlable
Important content must be available in crawlable HTML/server-rendered output:
- H1
- introduction
- active jobs
- expired/recent jobs
- related jobs
- related categories
- related locations
- related qualification/exam links
- FAQs
- breadcrumbs
- internal links

Do not make critical SEO content dependent only on clicks, hidden tabs, infinite scroll, or client-only API rendering.

## 5. Related Jobs Engine
Use deterministic relevance scoring. Suggested baseline:
- qualification: +30
- location: +25
- job category: +20
- organization: +10
- skill/trade: +10
- exam/topic: +5

For `10th Pass + Kolkata`, prioritize 10th-pass Kolkata/West Bengal government recruitment before unrelated graduate jobs from another state.

## 6. Internal Linking
Generate relevant links from:
- qualification
- location
- state
- category
- exam
- trade/skill
- organization

Use descriptive natural anchor text. Avoid mass-generated irrelevant links.

## 7. FAQ
Every visible FAQ question must have a useful answer. Do not leave empty FAQ headings.

## 8. Canonical
Each valid landing page should self-canonicalize to its preferred absolute URL and the canonical must return 200 and be indexable.

Do not canonicalize a valid landing page to `/jobs` just because there are currently zero active jobs.

## 9. Sitemap
Add these intended URLs without changing their URL structure:
- `https://www.searchsarkarinaukri.com/10th-pass-jobs-in-kolkata`
- `https://www.searchsarkarinaukri.com/graduate-jobs-in-gurgaon`
- `https://www.searchsarkarinaukri.com/iti-jobs-in-west-bengal`

Only include them when they are 200, canonical, indexable and intentionally part of the SEO architecture.

Exclude 404/410/redirect/noindex/duplicate URLs.

## 10. Implementation Order
1. Fix route/status behavior.
2. Preserve expired job records.
3. Improve zero-result landing pages.
4. Add crawlable related jobs.
5. Add related categories/locations/qualifications.
6. Complete FAQs.
7. Fix canonical.
8. Update sitemap.
9. Clean internal links.
10. Deploy.
11. Run full crawl.
12. Validate in GSC.

## 11. Latest Re-Audit Developer Updates

Based on the latest live-page extraction, developers must also fix these specific issues:

- Zero-active-job landing pages must not be thin templates. Add crawlable recent/expired jobs, related current jobs, related locations, related qualifications, and useful explanatory content.
- Empty FAQ questions must be completed. Confirmed examples needing visible answers include `How many 10th Pass (SSC / Matric) jobs are there in Kolkata?` and `Can I apply from outside Kolkata?`.
- Indexable pages must not expose only client/API failure text such as `Could not load jobs. Please check your connection.` to crawlers.
- If a page is intended to rank, it should be `200`, self-canonical, indexable, and included in sitemap after quality fixes.
- If a page is intentionally `noindex, follow`, remove it from sitemap.
- Do not delete or 404 valid qualification/location pages only because active jobs are currently zero.

## 12. 81 Page Briefs Created

Use the folder below for the individual page-level instructions:

`06_81_Unique_Page_Content_Sitemap_Briefs`

It contains:

- one separate Markdown brief for each of the 81 Soft 404 URLs
- unique H1 guidance for every page
- H1 to H6 heading structure
- semantic HTML requirements
- 10 to 15+ content-section requirements
- related jobs instructions
- location/topic-specific content instructions
- expired jobs preservation rules
- self-canonical requirements
- sitemap add-after-fix instructions

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
