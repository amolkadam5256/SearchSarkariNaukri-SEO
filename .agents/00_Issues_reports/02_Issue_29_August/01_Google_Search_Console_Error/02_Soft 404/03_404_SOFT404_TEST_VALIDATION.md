# SearchSarkariNaukri — Testing & Validation

## Confirmed URLs
Test all three:
- `/10th-pass-jobs-in-kolkata`
- `/graduate-jobs-in-gurgaon`
- `/iti-jobs-in-west-bengal`

## HTTP Tests
Expected for valid landing pages:
`200 OK`

Example:
```bash
curl -I https://www.searchsarkarinaukri.com/10th-pass-jobs-in-kolkata
```

## Soft 404 Test
A 200 response alone is not enough. Verify:
- meaningful unique content
- useful zero-job explanation
- relevant expired/recent jobs when available
- relevant related jobs
- related categories/locations
- answered FAQs
- crawlable internal links
- correct canonical

## Crawl Test
Run a production crawl and verify every critical section is discoverable without user interaction.

Check:
- H1
- intro
- active jobs
- expired jobs
- related jobs
- related categories
- related locations
- FAQ
- breadcrumbs
- canonical
- internal links

## Expired Job Test
Select an expired recruitment and confirm:
- URL returns 200
- page clearly says Closed/Expired
- historical recruitment details remain
- current related jobs are offered
- page is not presented as an active vacancy

## Invalid URL Test
A genuinely nonexistent URL such as:
`/jobs/999999999`
should return 404 and must not render a fake job.

## Redirect Test
A genuinely equivalent old URL must:
`old URL → 301 → relevant final URL → 200`

No redirect chain or loop.

## Sitemap Test
Confirm intended pages appear in the sitemap:
- `/10th-pass-jobs-in-kolkata`
- `/graduate-jobs-in-gurgaon`
- `/iti-jobs-in-west-bengal`

Every sitemap URL must be valid, canonical, indexable and return 200.

## Internal Link Test
Ensure no important page links to removed URLs. Related-job links must be topically relevant.

## GSC Validation
After deployment:
1. Inspect the three Soft 404 URLs.
2. Run live URL testing.
3. Confirm crawl/indexing signals.
4. Confirm canonical.
5. Request indexing where appropriate.
6. Monitor Page Indexing after recrawl.

GSC reporting may lag after a fix.

## Pass Criteria
- valid pages = 200
- expired useful jobs = 200
- nonexistent URLs = 404
- intentional permanent removals = 410 where appropriate
- relevant redirects = 301 → 200
- no redirect chains
- no soft-404 pattern on tested landing pages
- all important sections crawlable
- sitemap clean
- internal links clean

## Latest Re-Audit Test Additions

For each Soft 404 example URL, retest and confirm:

- Page is not just `0 Active Jobs` plus `No active jobs right now`.
- Page has crawlable recent/expired jobs or useful related alternatives.
- All FAQ questions have visible crawlable answers.
- Sitemap includes the URL only if it is `200`, canonical, indexable, and useful.
- Sitemap excludes the URL if it is `noindex, follow`.
- Crawler-visible HTML does not show `Could not load jobs. Please check your connection.` as the main content.
- Related links are topically relevant to qualification, city/state, exam, department, or job type.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
