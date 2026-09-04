# Two-Round Test Audit - Crawled Currently Not Indexed

## Round 1 Audit

1. Test every URL from `00_Master_Index/crawled-currently-not-indexed-url-index.csv`.
2. Record status code, robots meta, X-Robots-Tag, canonical, title, H1, word count, structured data, sitemap inclusion, and internal links.
3. Mark failure if a useful/indexable page has noindex.
4. Mark failure if a sitemap URL is noindex, redirected, duplicate, 404/410, or canonicalized away.
5. Mark failure if the page is thin, empty, or only generic boilerplate.
6. Mark failure if structured data URL does not match canonical URL.
7. Fix all failures.

## Round 2 Re-Audit

1. Re-test every changed URL.
2. Re-crawl affected sitemaps.
3. Re-check redirect chains and duplicate variants.
4. Re-check content visibility in rendered/crawlable HTML.
5. Re-check GSC URL Inspection sample.
6. Only request validation when all critical checks pass.

## Final Signoff

- [ ] Useful pages are `200 OK`, `index,follow`, self-canonical, and in sitemap.
- [ ] Non-indexable pages are noindex/redirect/404/410 intentionally and excluded from sitemap.
- [ ] Canonical, sitemap, structured data, breadcrumb, OG/Twitter URL, and internal links agree.
- [ ] No accidental noindex remains on useful pages.
- [ ] No thin page is submitted for indexing.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to affected URL routing, HTTP status handling, canonical logic, robots/indexability, sitemap, metadata, structured data, contextual internal links, page content quality, redirects, and QA.
