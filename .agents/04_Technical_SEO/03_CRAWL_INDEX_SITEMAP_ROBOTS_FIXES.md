# Crawl, Indexing, Sitemap, Robots And LLM Files

## Reported Issues

- 1 page could not be crawled.
- Sitemap warning appears in Semrush, while SEOptimer found `https://www.searchsarkarinaukri.com/sitemap.xml`.
- Robots found at `http://searchsarkarinaukri.com/robots.txt`.
- `llms.txt` found at `http://searchsarkarinaukri.com/llms.txt`.
- No major search engines are blocked by robots.txt.
- 0 pages blocked from crawling.

## Crawl Failure Fix

Required data:

- Exact uncrawlable URL from Semrush export.

Checks:

- Browser request
- `curl -I`
- `curl -A "Googlebot"`
- `curl -A "SemrushBot"`
- Server logs around crawl time
- App route logs
- Nginx/access/error logs

Allowed outcomes:

- 200 OK for valid indexable page
- 301/308 to canonical equivalent
- 410 for intentionally removed obsolete page
- 403/401 only if the page is intentionally private
- noindex only when page should exist for users but not search

Do not leave accidental timeout/refusal unresolved.

## Sitemap Fix

Canonical sitemap:

`https://www.searchsarkarinaukri.com/sitemap.xml`

Requirements:

- Returns 200 over HTTPS.
- Uses canonical WWW host if site canonical is WWW.
- Contains only indexable canonical URLs.
- Excludes noindex, duplicate, parameter-only, admin, login, and private URLs.
- Includes important:
  - Homepage
  - `/jobs`
  - Job detail pages
  - Qualification pages
  - State/district/city pages
  - Category pages
  - Exam pages
  - Admit cards/results/resources where indexable
  - Blogs/guides where indexable

If sitemap is split:

- Use sitemap index.
- Keep each child sitemap valid.
- Declare sitemap index in robots.txt.

## Robots.txt Fix

Canonical robots:

`https://www.searchsarkarinaukri.com/robots.txt`

Required line:

`Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml`

Requirements:

- Returns 200.
- Does not block important pages.
- Blocks only private/admin/internal routes as needed.
- Allows key crawlers to access public CSS/JS required for rendering.
- Consistent behavior across HTTP/non-WWW/WWW.

## Canonical Host Consistency

Preferred host appears to be:

`https://www.searchsarkarinaukri.com`

Checks:

- `http://searchsarkarinaukri.com/`
- `http://www.searchsarkarinaukri.com/`
- `https://searchsarkarinaukri.com/`
- `https://www.searchsarkarinaukri.com/`

All non-canonical versions should redirect directly to the canonical version where possible.

Avoid chains:

`http -> https -> www -> trailing slash`

Prefer one direct redirect.

## LLM/GEO File

`llms.txt` appears to exist.

Checks:

- Accessible at canonical HTTPS/WWW URL.
- No formatting issues.
- Mentions key public content areas:
  - Jobs
  - Exams
  - Admit Cards
  - Results
  - Current Affairs
  - Quiz
  - Career Guidance
  - Eligibility Checker
  - Age Calculator
- Does not include private/admin URLs.
- Uses stable canonical URLs.

## Indexing Strategy

Index:

- Homepage
- `/jobs`
- Important qualification pages
- Important state/district/city pages
- Important category pages
- Important exam pages
- Useful tools and guides
- Individual job pages while accurate and useful

Noindex/canonical:

- Thin filter combinations
- Search result pages without unique value
- Duplicate parameter pages
- Login/account pages
- Admin/private pages

Do not accidentally noindex valuable existing pages.

## QA Checklist

- [ ] Uncrawlable URL identified
- [ ] Uncrawlable issue fixed or intentionally documented
- [ ] Canonical sitemap returns 200
- [ ] robots.txt returns 200
- [ ] robots.txt declares sitemap
- [ ] HTTP/non-WWW host behavior is consistent
- [ ] Sitemap includes important canonical URLs
- [ ] Sitemap excludes noindex/private/duplicate URLs
- [ ] `llms.txt` accessible and clean
- [ ] No important route blocked by robots
