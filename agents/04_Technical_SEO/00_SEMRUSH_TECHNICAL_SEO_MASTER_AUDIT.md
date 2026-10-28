# Technical SEO Master Audit - SearchSarkariNaukri

Site: `www.searchsarkarinaukri.com`

Audit source:

- Semrush Site Audit generated on 7 September 2026
- SEOptimer audit generated on 7 September 2026

## Goal

Fix all reported Technical SEO, crawlability, metadata, duplication, sitemap, performance, security, and internal-linking issues without creating new SEO problems.

## Critical Implementation Rule

Do not make broad design or navigation changes while fixing technical SEO.

For page-specific work:

- Preserve existing URLs unless a redirect/canonical fix is required.
- Preserve existing indexed pages.
- Preserve existing jobs, job slugs, categories, district pages, qualification pages, and exam pages.
- Do not create fake pages, fake schema, fake business details, fake social profiles, fake jobs, or thin SEO pages.
- Do not add/remap links in header/navbar/footer unless the task explicitly targets global navigation.
- Prefer page-level metadata, canonical, content, sitemap, and internal-link fixes.

## Semrush Errors

Errors reported:

- 6 issues with duplicate title tags
- 4 pages have duplicate content issues
- 4 pages have duplicate meta descriptions
- 1 page could not be crawled

Passing/clean error checks:

- 0 pages returned 5XX status code
- 0 pages returned 4XX status code
- 0 pages missing title tags
- 0 internal links broken
- 0 DNS crawl issues
- 0 incorrect URL format crawl issues
- 0 internal images broken
- robots.txt format valid
- sitemap.xml format has no reported errors
- 0 incorrect pages found in sitemap.xml
- 0 WWW resolve issues
- viewport configured
- 0 pages with too-large HTML size
- SSL/certificate/security protocol checks passed

## Semrush Warnings

Warnings reported:

- 19 pages have low word count
- 2 pages have low text-to-HTML ratio
- Sitemap.xml not found in one audit context

Passing/clean warning checks:

- 0 external links broken
- 0 external images broken
- 0 HTTPS pages link to HTTP pages
- 0 pages with title too short
- 0 pages with title too long in Semrush
- 0 pages missing H1
- 0 duplicate H1/title issues
- 0 pages missing meta descriptions
- 0 pages with too many on-page links
- 0 temporary redirects
- 0 images missing alt
- 0 URLs with too many parameters
- lang/hreflang baseline mostly clean
- doctype and charset declared
- no frames
- no underscore URL issue
- no outgoing internal nofollow
- sitemap indicated in robots.txt according to Semrush
- HTTPS is active

## Semrush Notices

Notices reported:

- 70 outgoing external links contain nofollow attributes
- 11 pages have only one incoming internal link
- 2 pages require content optimization
- 1 subdomain does not support HSTS
- `llms.txt` notice appears in audit data

Passing/clean notice checks:

- 0 pages with more than one H1
- 0 pages blocked from crawling
- 0 page URLs longer than 200 characters
- 0 orphaned pages in Google Analytics
- 0 orphaned pages in sitemaps
- 0 X-Robots noindex blocks
- 0 broken external JS/CSS
- 0 pages more than 3 clicks deep
- 0 permanent redirect issues
- 0 empty-anchor links
- 0 non-descriptive anchor text

## SEOptimer Issues

SEOptimer recommendations:

- Execute a link-building strategy
- Reduce homepage title tag length
- Remove duplicate canonical tags
- Improve site load speed
- Update link URLs to be more readable
- Reduce rendered content for LLM readability/GEO
- Optimize desktop PageSpeed Insights
- Add SPF mail record
- Reduce homepage meta description length
- Add Local Business schema only if legitimate
- Create/link social profiles only if real official profiles exist
- Facebook Pixel optional only if paid marketing requires it

Important SEOptimer findings:

- Homepage title length: 75 characters
- Homepage meta description length: 180 characters
- Duplicate canonical tags detected on homepage
- Canonical values reported twice as `https://www.searchsarkarinaukri.com/`
- Robots found: `http://searchsarkarinaukri.com/robots.txt`
- Sitemap found: `https://www.searchsarkarinaukri.com/sitemap.xml`
- `llms.txt` found: `http://searchsarkarinaukri.com/llms.txt`
- Language declared: `en-IN`
- Word count on homepage: 4770
- Rendered content percentage: 336%
- Desktop PSI flagged as poor despite reasonable lab metrics
- Page load: all scripts complete around 5.5s
- Valid DMARC exists
- SPF record missing
- HSTS detected by SEOptimer technology list, but Semrush reports 1 subdomain without HSTS

## Priority Order

### P0 - Must Fix First

1. Duplicate canonical tags
2. Duplicate title tags
3. Duplicate meta descriptions
4. Duplicate content pages
5. Uncrawlable page
6. Sitemap availability and robots sitemap consistency

### P1 - High SEO Impact

1. Low word-count pages
2. Pages with only one incoming internal link
3. Content optimization pages
4. Low text-to-HTML ratio pages
5. Friendly/readable URL opportunities, without breaking existing indexed URLs

### P2 - Performance And GEO

1. Improve desktop PageSpeed
2. Reduce rendered content percentage
3. Reduce script completion time
4. Ensure important content exists in crawlable HTML
5. Improve `llms.txt` formatting/content if needed

### P3 - Security, DNS, Social, External

1. Add SPF record
2. Confirm HSTS for all production hostnames/subdomains
3. Review external nofollow usage
4. Add Local Business schema only if accurate
5. Add official social links only if real official profiles exist

## Acceptance Criteria

The audit is complete only when:

- Duplicate titles are resolved.
- Duplicate meta descriptions are resolved.
- Duplicate content groups have unique content, canonical, redirect, or noindex strategy.
- Each indexable page has exactly one canonical tag.
- Uncrawlable page is identified and fixed or intentionally blocked with documentation.
- Sitemap is accessible and declared in robots.txt.
- Low word-count pages have meaningful unique content or are noindexed/merged.
- Important pages have more than one contextual incoming internal link.
- No new broken links, redirects, thin pages, duplicate metadata, fake schema, or crawl blocks are introduced.
