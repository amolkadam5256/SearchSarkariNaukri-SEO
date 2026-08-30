# SearchSarkariNaukri — Final SEO + Developer Audit

## Final Principle
**Fix the cause, not the GSC number.**

Success means Google can discover, crawl and understand useful recruitment content while genuinely nonexistent URLs are correctly removed.

## Required Page Architecture

```text
Breadcrumb
↓
H1
↓
Unique introduction
↓
Current job status
↓
Active Jobs
↓
Recent / Expired Recruitment
↓
Related Jobs
↓
Related Categories
↓
Related Locations
↓
Related Qualifications / Exams
↓
Useful FAQs
↓
Last Updated
```

## SEO Expert Sign-Off
- [ ] Search intent is genuine.
- [ ] H1 matches qualification/location/topic.
- [ ] Content is unique and useful.
- [ ] No keyword stuffing.
- [ ] No fabricated jobs.
- [ ] Expired jobs are clearly labeled.
- [ ] Related jobs are genuinely relevant.
- [ ] Related category/location/qualification links are relevant.
- [ ] FAQs are answered.
- [ ] Canonical is correct.
- [ ] Intended pages are in sitemap.

## Developer Sign-Off
- [ ] Valid routes return 200.
- [ ] Expired jobs are not automatically deleted.
- [ ] Missing jobs return 404.
- [ ] Intentional permanent removals use 410 where appropriate.
- [ ] Relevant old URLs use direct 301.
- [ ] SEO sections are crawlable/server-rendered.
- [ ] Related jobs use relevance logic.
- [ ] Sitemap excludes invalid URLs.
- [ ] No redirect chains or loops.
- [ ] No soft 404 pattern remains.

## Confirmed URL Final Checks

### `/10th-pass-jobs-in-kolkata`
Expected:
`200 + useful content + related jobs + crawlable sections + self canonical + sitemap`

### `/graduate-jobs-in-gurgaon`
Expected:
`200 + useful content + related jobs + crawlable sections + self canonical + sitemap`

### `/iti-jobs-in-west-bengal`
Expected:
`200 + useful content + related jobs + crawlable sections + self canonical + sitemap`

## Sitemap Requirement
Add these exact URLs without changing their structure, provided they are intended indexable pages:
- `https://www.searchsarkarinaukri.com/10th-pass-jobs-in-kolkata`
- `https://www.searchsarkarinaukri.com/graduate-jobs-in-gurgaon`
- `https://www.searchsarkarinaukri.com/iti-jobs-in-west-bengal`

Do not modify unrelated URLs as part of this task.

## Old Job Preservation Requirement
**Do not remove old jobs only because they are expired.**

Preferred model:
`Old job → keep URL → mark Expired/Closed → retain useful details → add relevant current jobs → add related category/topic links`

## Final Audit Table

| Area | Before | After | Status |
|---|---|---|---|
| GSC 404 URLs | 613 reported | TBD | ⏳ |
| Soft 404 pages | 3+ confirmed | TBD | ⏳ |
| Valid landing pages | TBD | 200 | ⏳ |
| Useful expired jobs preserved | TBD | Yes | ⏳ |
| Related job relevance | TBD | Verified | ⏳ |
| Crawlable sections | TBD | All critical sections | ⏳ |
| Sitemap | Missing URLs possible | Valid URLs included | ⏳ |
| Invalid sitemap URLs | TBD | 0 | ⏳ |
| Broken internal links | TBD | 0 target | ⏳ |
| Redirect chains | TBD | 0 | ⏳ |

## Final PASS
Project is PASS only when:
- valid pages return 200
- useful expired jobs remain accessible
- nonexistent URLs return 404
- permanent removals are intentional
- no fake jobs are created
- no useful old jobs are deleted
- related jobs are relevant
- all critical sections are crawlable
- FAQs are complete
- canonical is correct
- sitemap is clean
- internal links are clean
- production crawl passes
- GSC live inspection passes

## Latest Re-Audit Addendum

New evidence from live extraction confirms the main developer fixes still required:

- Valid zero-result SEO landing pages must stay `200`, but the page body must become useful enough to avoid Soft 404.
- Add crawlable historical/expired jobs and relevant alternatives when active jobs are zero.
- Complete empty FAQ answers.
- Prevent API/client failure messages from becoming the primary crawler-visible content.
- Include intended indexable pages in sitemap only after they are useful, canonical, and indexable.
- Remove `noindex`, redirect, `404`, and `410` URLs from sitemap.

Final status remains:

`PENDING DEVELOPER IMPLEMENTATION AND GSC LIVE RETEST`

## 81 Page Briefs

The detailed page-by-page developer/content briefs are in:

`06_81_Unique_Page_Content_Sitemap_Briefs`

Use `00_INDEX_81_PAGES.md` as the master list and `00_SITEMAP_URLS_TO_ADD_AFTER_FIX.md` as the sitemap candidate list.

Important: add a URL to the production sitemap only after that exact page is `200`, self-canonical, indexable, useful, and no longer a Soft 404 risk.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
