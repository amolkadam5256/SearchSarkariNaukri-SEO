# 01 — Technical SEO Audit Checklist

Log every item in the Report Table format from `14-developer-final-report-template.md`.
Output file: `outputs/final-reports/01-technical-seo-audit-REPORT.md`

## A. Crawlability & Indexation
- [ ] robots.txt exists at `/robots.txt`, returns HTTP 200, valid syntax
- [ ] robots.txt does not block CSS/JS needed for rendering
- [ ] robots.txt `Disallow` rules reviewed line-by-line — list every disallowed path and confirm intent
- [ ] robots.txt references the sitemap URL (`Sitemap:` directive present)
- [ ] Meta robots tag present and correct on every template (index/noindex, follow/nofollow)
- [ ] X-Robots-Tag HTTP header checked (can silently override meta robots)
- [ ] No orphan pages (pages with 0 internal links pointing to them)
- [ ] Crawl budget check: total crawlable URLs vs total useful/indexable URLs ratio
- [ ] Pagination implemented correctly (rel=next/prev deprecated by Google but verify UX + canonical chain on paginated job listing pages)
- [ ] Infinite scroll / JS-loaded job listings — verify Googlebot can render and access paginated content (test with URL Inspection "Live Test" + rendered HTML)

## B. Indexation Hygiene
- [ ] Google Search Console → Coverage report: count of Valid, Valid w/ warnings, Excluded, Error pages — export full list
- [ ] "Duplicate without user-selected canonical" errors — list every URL
- [ ] "Crawled – currently not indexed" — list every URL + hypothesize why (thin content, duplication, etc.)
- [ ] "Discovered – currently not indexed" — list every URL (crawl budget signal)
- [ ] Soft 404s reported by GSC — list URLs
- [ ] Index bloat check: are `/jobs?category=...` filter URLs being indexed as near-duplicates of `/jobs`?

## C. Canonicalization
- [ ] Every page has exactly one self-referencing OR cross-referencing canonical tag
- [ ] No canonical chains (A→B→C) or canonical loops
- [ ] www vs non-www resolved to single canonical version with 301 redirect
- [ ] HTTP → HTTPS forced with 301 (no mixed content)
- [ ] Trailing slash consistency (`/jobs` vs `/jobs/`) — pick one, enforce via redirect
- [ ] URL parameter handling (`?category=`, `?utm_=`, `?page=`) — confirm canonical strips or correctly targets parameters

## D. URL Structure
- [ ] URLs are lowercase, hyphen-separated, no underscores/spaces/special chars
- [ ] Job listing slugs reviewed for descriptiveness — flag every auto-generated/non-descriptive slug (e.g. `job--5015`)
- [ ] URL length reviewed (flag anything over ~115 characters)
- [ ] No duplicate content served at multiple distinct URLs (check `/graduate-government-jobs` used for two different nav labels — confirm intended)

## E. Redirects
- [ ] Full redirect map exported (source → destination → status code)
- [ ] No redirect chains longer than 1 hop
- [ ] No redirect loops
- [ ] 301s used for permanent moves (not 302)
- [ ] All old/legacy job URLs (expired listings) — confirm proper redirect or intentional 410/404 strategy, not silently left as thin "expired" pages

## F. Error Pages
- [ ] Custom 404 page exists, returns true HTTP 404 status (not 200), includes navigation + search
- [ ] Count of broken internal links (linking to 404s) — full list with source page + target
- [ ] Count of broken external links (linking out to dead official recruiter sites) — full list
- [ ] 5xx server errors during crawl — list

## G. Security & Server
- [ ] Valid SSL certificate, no mixed-content warnings
- [ ] HSTS header present
- [ ] Security headers checked: `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`
- [ ] Server response time (TTFB) measured for homepage + 3 template types
- [ ] Gzip/Brotli compression enabled
- [ ] HTTP/2 or HTTP/3 in use

## H. Mobile & Rendering
- [ ] Mobile-first indexing check — confirm mobile and desktop HTML parity (same content, same structured data, same meta tags)
- [ ] Viewport meta tag present (confirmed present on homepage — verify site-wide)
- [ ] Tap targets sized appropriately (Lighthouse mobile usability)
- [ ] No intrusive interstitials (popups) blocking content on mobile

## I. JavaScript SEO
- [ ] Identify rendering method (SSR / CSR / SSG / hybrid) — check via "View Source" vs rendered DOM diff
- [ ] Confirm critical content (job titles, dates, apply links) is present in initial HTML, not JS-injected-only
- [ ] Test Googlebot rendering via GSC URL Inspection "View Crawled Page" for at least 3 templates

## J. Sitemap Technical Validation (cross-ref with file 03 for URL-level reconciliation)
- [ ] Sitemap XML is valid (passes XML schema validation)
- [ ] Sitemap under 50,000 URLs / 50MB per file (or properly split with sitemap index)
- [ ] Sitemap `lastmod` dates are accurate (not all identical/fake)
- [ ] Sitemap submitted in GSC + Bing Webmaster Tools, "Success" status confirmed
- [ ] Separate sitemaps used for job listings vs static pages vs categories (recommended for a site this size) — confirm current structure

## K. International / Language
- [ ] `<html lang="...">` attribute present and correct on every template (cross-ref file 11)
- [ ] Confirm whether site truly needs hreflang (single-market Marathi/English bilingual content on same URL vs separate URLs)
