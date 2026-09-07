# Priority Technical SEO Fix Plan

## P0 - Duplicate Canonical Tags

Issue:

- SEOptimer found more than one canonical tag on the homepage.
- Both reported values are `https://www.searchsarkarinaukri.com/`.

Why it matters:

- Multiple canonicals create ambiguity even when values match.
- Search engines may ignore canonical hints when implementation is inconsistent.

Fix:

- Inspect root layout, SEO component, page metadata export, and any manual `<Head>`/helmet usage.
- Ensure each page emits exactly one canonical tag.
- Keep homepage canonical as `https://www.searchsarkarinaukri.com/`.
- Keep `/jobs` canonical as `https://www.searchsarkarinaukri.com/jobs`.
- Avoid duplicate canonical injection from both app layout and page component.

QA:

- View source for homepage and key landing pages.
- Confirm exactly one `<link rel="canonical">` per indexable page.

## P0 - Duplicate Title Tags

Issue:

- Semrush found 6 duplicate title tag issues.

Fix:

- Export the affected URL list from Semrush.
- Group pages with exact matching titles.
- Write unique titles based on page intent:
  - Homepage
  - Jobs page
  - Qualification pages
  - Category pages
  - District pages
  - Exam pages
  - Blog/resource pages
- Keep titles concise and natural.

Title rules:

- Unique per indexable page.
- Usually 50-60 characters where practical.
- Include primary page entity.
- Avoid stuffing repeated terms.
- Do not use the same title template without a unique entity.

Examples:

- Homepage: `Sarkari Naukri 2026 - Govt Jobs in India`
- Jobs: `Latest Government Jobs 2026 - Sarkari Naukri`
- Pune district: `Government Jobs in Pune 2026 - Latest Vacancies`
- Banking category: `Banking Jobs 2026 - SBI, IBPS & RBI Recruitment`

QA:

- Crawl titles after deployment.
- Confirm no exact duplicates remain.

## P0 - Duplicate Meta Descriptions

Issue:

- Semrush found 4 duplicate meta description issues.
- SEOptimer found homepage description is too long at 180 characters.

Fix:

- Export affected URL list.
- Write unique descriptions matching each page topic.
- Shorten homepage description to 120-160 characters.
- Avoid generic repeated descriptions across category/location pages.

Meta description rules:

- Unique for each indexable page.
- Around 120-160 characters where possible.
- Mention the page entity: qualification, city, category, exam, or tool.
- Avoid duplicate boilerplate.

Example homepage description:

`Find Sarkari Naukri 2026, latest government jobs, MPSC, SSC, railway, banking and police recruitment updates with official apply links.`

QA:

- Crawl descriptions after deployment.
- Confirm no exact duplicate meta descriptions remain.

## P0 - Duplicate Content

Issue:

- Semrush found 4 pages with duplicate content issues.
- Pages are considered duplicates when content is at least 85% identical.

Fix decision tree:

1. If duplicate URL is an alternate version of same page, canonicalize to the primary.
2. If duplicate URL has no independent value, 301 redirect to primary.
3. If duplicate is a paginated page, ensure correct crawlable pagination and self/series canonical strategy.
4. If duplicate is a real landing page, add unique useful content and entity-specific job data.
5. If duplicate is a thin filter combination, noindex or canonical appropriately.

Do not:

- Delete existing indexed pages without redirect strategy.
- Create doorway pages.
- Add spun/repetitive text.

QA:

- Re-crawl duplicate content group.
- Confirm each indexable page has unique visible content or a clear canonical/redirect/noindex decision.

## P0 - Uncrawlable Page

Issue:

- Semrush reported 1 page could not be crawled.

Possible causes:

- Server response time above 5 seconds
- Temporary server refusal
- Firewall/bot-blocking
- Auth/session issue
- Misconfigured route

Fix:

- Export the exact URL from Semrush.
- Test with browser, curl, Googlebot user agent, and SemrushBot if possible.
- Check server logs.
- Fix server error, timeout, route issue, or bot access rule.
- If the page should not be crawlable, document why and ensure it is intentionally blocked/noindexed.

QA:

- Page returns a stable 200, 301, 410, or intentional block.
- No accidental crawl failure remains.

## P0 - Sitemap And Robots Consistency

Issue:

- Semrush says `Sitemap.xml not found` in one warning section.
- SEOptimer says `https://www.searchsarkarinaukri.com/sitemap.xml` exists.
- Semrush also reports no sitemap format errors and robots sitemap indication is clean.

Fix:

- Confirm canonical sitemap URL over HTTPS and WWW.
- Ensure `https://www.searchsarkarinaukri.com/sitemap.xml` returns 200.
- Ensure `https://www.searchsarkarinaukri.com/robots.txt` returns 200.
- Ensure robots.txt contains:
  `Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml`
- Redirect HTTP/non-WWW sitemap/robots requests consistently where appropriate.
- Include important indexable URLs only.

QA:

- Validate sitemap in Google Search Console.
- Re-crawl with Semrush.

## P1 - Low Word Count Pages

Issue:

- 19 pages have fewer than 200 words.

Fix:

- Export affected URLs.
- Classify each page:
  - Important landing page: add useful unique content.
  - Utility/action page: low word count may be acceptable if intent is satisfied.
  - Thin duplicate/filter page: canonical/noindex/merge.
  - Obsolete page: redirect or 410 only if appropriate.

Content additions should be:

- Specific to the page entity.
- Useful to users.
- Internally linked.
- Not keyword stuffed.

QA:

- Important indexable pages exceed 200 meaningful words.
- Thin pages are not indexed unnecessarily.

## P1 - One Incoming Internal Link

Issue:

- 11 pages have only one incoming internal link.

Fix:

- Export affected URLs.
- Add contextual internal links from relevant hub pages, not random footer stuffing.
- Prefer links from:
  - `/jobs`
  - Qualification pages
  - State/district pages
  - Category pages
  - Exam pages
  - Related job blocks
  - Relevant blog/resource pages

QA:

- Important pages receive at least 2-3 relevant internal links.
- Link anchors are descriptive.

## P1 - Low Text-to-HTML Ratio

Issue:

- 2 pages have text-to-HTML ratio at or below 10%.

Fix:

- Identify URLs.
- Reduce unnecessary markup where practical.
- Move inline JSON/config/scripts out of visible HTML where possible.
- Server-render important text.
- Add meaningful visible content if the page is important.
- Avoid hiding content just to change the ratio.

QA:

- Pages remain fast and crawlable.
- Text-to-HTML ratio improves without UX regression.

## P2 - Performance

Issue:

- Desktop PageSpeed flagged poor.
- All scripts complete around 5.5s.
- Rendered content percentage is 336%.

Fix:

- Audit JS bundle and third-party scripts.
- Defer non-critical scripts.
- Remove duplicate analytics/script injections.
- Server-render important content.
- Lazy-load non-critical components.
- Avoid duplicate data fetching.
- Optimize images.
- Minimize route-level JS for static SEO sections.

QA:

- Lighthouse/PSI improves.
- Important content visible in initial HTML.
- No hydration errors.

## P3 - SPF, HSTS, Social, Local Schema

Fix:

- Add SPF DNS record only through DNS provider.
- Confirm HSTS on all canonical production hostnames/subdomains.
- Keep nofollow on external links when intentional, especially official apply/notification links if policy requires it.
- Add Local Business schema only if there is a real eligible local business profile/address.
- Add social profile links only for official accounts.

QA:

- DNS records validate.
- Security headers validate.
- No fake social/entity schema added.
