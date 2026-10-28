# Technical SEO — Sitewide Developer Audit Instructions

**Scope:** Entire SearchSarkariNaukri project  
**Status:** Instructions prepared; findings require repository and site evidence.

## Complete checklist

## 4. Technical SEO Checklist

### Crawlability and indexation

- [ ] Verify that important pages return the correct HTTP status.
- [ ] Identify accidental 404s, soft 404s, redirect chains, redirect loops, and unnecessary redirects.
- [ ] Check `robots.txt` and ensure important content is not unintentionally blocked.
- [ ] Check page-level `noindex`, `nofollow`, and robots meta directives.
- [ ] Verify canonical URLs and detect conflicting or incorrect canonicals.
- [ ] Identify duplicate URLs caused by query parameters, filters, pagination, trailing slashes, and URL variants.
- [ ] Confirm that important pages can be discovered through crawlable links.
- [ ] Ensure essential content and metadata are available to search engines without requiring unsupported client-side interactions.
- [ ] Review pagination and filtered listing behaviour.
- [ ] Check orphan pages and unnecessarily deep navigation paths.
- [ ] Verify that expired recruitment pages are handled according to their continuing usefulness.
- [ ] Check that removed pages return appropriate responses or redirects based on the replacement and user intent.

### XML sitemaps

- [ ] Verify sitemap validity and accessibility.
- [ ] Include only eligible, canonical, indexable URLs that return successful responses.
- [ ] Exclude redirects, errors, `noindex` pages, and noncanonical duplicates.
- [ ] Use accurate `lastmod` values based on meaningful content updates.
- [ ] Split large sitemaps where necessary and provide a sitemap index.
- [ ] Confirm that important page types are covered.
- [ ] Check that the sitemap is referenced correctly in `robots.txt`.
- [ ] Compare sitemap URLs against actual routes and indexation data.

### URL structure

- [ ] Use stable, readable, descriptive URLs.
- [ ] Maintain a consistent trailing-slash and lowercase policy.
- [ ] Avoid unnecessary URL parameters and duplicate paths.
- [ ] Preserve existing URL equity when routes change.
- [ ] Implement appropriate permanent redirects for approved URL migrations.
- [ ] Avoid changing established URLs solely to insert additional keywords.

### Metadata and HTML structure

- [ ] Provide unique, descriptive title tags for indexable pages.
- [ ] Write useful meta descriptions aligned with the page's actual content.
- [ ] Ensure a clear primary H1 and logical heading hierarchy.
- [ ] Use semantic HTML landmarks and meaningful page structure.
- [ ] Add appropriate language metadata.
- [ ] Verify Open Graph and social sharing metadata where relevant.
- [ ] Check image alternative text and meaningful link text.
- [ ] Avoid duplicate metadata across dynamic routes.
- [ ] Prevent incorrect titles and metadata during loading, errors, or data-fetching failures.

## Detailed developer instructions

Audit status codes, redirects, robots, canonicals, duplicates, sitemap, URL policy, metadata, HTML structure and crawlable rendering across the route inventory. Record observed responses and rendered evidence. Propose scoped fixes first; preserve established URLs and avoid bulk indexing or redirect changes without a value review.

## Pass 1 — Audit and implementation

- [ ] Inspect current code/data and capture reproducible baseline evidence.
- [ ] Identify affected routes/components; preserve useful content, records, URLs and working behavior.
- [ ] Record confirmed findings and distinguish evidence from assumptions.
- [ ] Assign priority; document fix, expected result, dependencies and approvals.
- [ ] Implement only scoped approved changes using project conventions.
- [ ] Run applicable local checks; record exact commands/results.
- [ ] Record changed files/components and unresolved items.

## Pass 2 — Independent verification

- [ ] Recheck the original issue against rendered routes or actual system behavior.
- [ ] Verify content/data preservation and applicable metadata, schema and links.
- [ ] Exercise desktop/mobile, keyboard and relevant loading/empty/error/success states.
- [ ] Inspect relevant console/network output and regression paths.
- [ ] Attach reproducible evidence; mark passed, failed, blocked or untested.
- [ ] Keep unresolved items open; code changes or a passing build alone do not prove success.

## Completion record

- Pass 1 owner/date/status: ____________________
- Pass 1 evidence: ____________________
- Pass 2 reviewer/date/status: ____________________
- Pass 2 evidence: ____________________
- Open issues/dependencies: ____________________
