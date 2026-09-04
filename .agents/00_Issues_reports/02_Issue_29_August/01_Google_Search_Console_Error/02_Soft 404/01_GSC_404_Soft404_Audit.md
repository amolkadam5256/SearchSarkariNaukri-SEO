# SearchSarkariNaukri — GSC 404 + Soft 404 Audit

## Objective
Audit every affected GSC URL and classify it as KEEP/RESTORE (200), relevant 301, genuine 404, or intentional 410.

**Critical:** Do not delete old job pages only because the recruitment has expired. Preserve useful historical recruitment pages unless there is a specific reason to remove them.

## Confirmed Soft 404 Examples
- `/10th-pass-jobs-in-kolkata`
- `/graduate-jobs-in-gurgaon`
- `/iti-jobs-in-west-bengal`

GSC reports Soft 404 even though the pages fetch successfully, are crawlable, and allow indexing. The common pattern is a valid landing page with `0 Active Jobs` and very little unique content.

## Required URL Audit
For every URL record:
- HTTP status
- page type
- database record
- active job count
- expired/historical job count
- organic traffic/impressions
- internal links
- sitemap presence
- canonical
- noindex
- replacement URL, if any
- final action and reason

## Decision Rules

| Situation | Action |
|---|---|
| Valid landing page with 0 active jobs | Keep, improve, 200 |
| Valid active job | Keep, 200 |
| Valid expired job | Keep useful historical content, 200 |
| Old URL with genuinely equivalent replacement | 301 to closest relevant page |
| Truly nonexistent URL | 404 |
| Permanently intentionally removed URL | 410 |
| Existing page incorrectly returning 404 | Restore to 200 |

## Zero-Job Landing Pages
Do not manufacture vacancies. Instead make the page useful with:
1. Breadcrumb
2. Search-intent H1
3. Unique qualification/location introduction
4. Current job status
5. Active jobs section
6. Relevant recent/expired jobs when available
7. Keyword-based related jobs
8. Related categories
9. Related locations
10. Related qualifications/exams
11. Complete FAQs
12. Last updated information

## Related Job Relevance
Prioritize:
1. Qualification
2. Location
3. Job category
4. Organization
5. Skill/trade
6. Exam/recruitment topic

Do not show unrelated jobs simply because they are recent.

## Sitemap
Intended indexable landing pages must be included in the XML sitemap, provided they return 200, are canonical, indexable, and useful.

Never put 404, 410, redirect, noindex, or duplicate URLs in the sitemap.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
