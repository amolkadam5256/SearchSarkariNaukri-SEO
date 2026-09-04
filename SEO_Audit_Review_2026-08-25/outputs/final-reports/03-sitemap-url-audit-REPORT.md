# 03 — Sitemap & URL Reconciliation Audit — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: 25 August 2026
Auditor: Codex + custom Googlebot crawler + Lighthouse 13.4.1 + read-only source/server/database review
Checklist source: 03-sitemap-url-audit.md
Total items checked: 14
Total Pass: 8 | Total Warning: 1 | Total Fail: 4 | Total N/A: 1

| # | Checklist Item | Status | Evidence | Affected URL(s) | Severity | Recommended Fix | Effort (S/M/L) |
|---:|---|---|---|---|---|---|:---:|
| 1 | Fetch `https://www.searchsarkarinaukri.com/robots.txt`, extract every `Sitemap:` line | ✅ Pass | `robots.txt`, `raw-sitemap*.xml`, `sitemap-files.csv`, and `sitemap-xsd-validation.csv` preserve all 12 fetched files, counts, status, XSD validity, and lastmod observations. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 2 | Fetch `https://www.searchsarkarinaukri.com/sitemap.xml` (or whatever the robots.txt points to) | ✅ Pass | `robots.txt`, `raw-sitemap*.xml`, `sitemap-files.csv`, and `sitemap-xsd-validation.csv` preserve all 12 fetched files, counts, status, XSD validity, and lastmod observations. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 3 | If it's a sitemap **index**, list every child sitemap URL and fetch each one | ✅ Pass | `robots.txt`, `raw-sitemap*.xml`, `sitemap-files.csv`, and `sitemap-xsd-validation.csv` preserve all 12 fetched files, counts, status, XSD validity, and lastmod observations. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 4 | For each individual sitemap file, record: - File URL - Total `<url>` / `<loc>` entry count - Whether it validates against the sitemap XML schema - Whether `<lastmod>` values look real (varied, recent) vs fake (all identical/today's date on every entry) | ✅ Pass | `robots.txt`, `raw-sitemap*.xml`, `sitemap-files.csv`, and `sitemap-xsd-validation.csv` preserve all 12 fetched files, counts, status, XSD validity, and lastmod observations. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 5 | Export the **complete list** of every `<loc>` URL across all sitemaps into `outputs/raw-crawl-data/sitemap-urls-full-list.csv` | ✅ Pass | `sitemap-urls-full-list.csv`: all 3,871 unique `<loc>` entries with source sitemap, lastmod, type, duplicate count. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 6 | Run a full site crawl (Screaming Frog "Spider" mode from homepage, unlimited depth, respecting robots.txt) — export the **complete list** of every URL discovered via internal links into `outputs/raw-crawl-data/crawled-urls-full-list.csv` | ✅ Pass | `crawled-urls-full-list.csv`: 5,540 internal URLs discovered/classified by the rate-limited Googlebot crawl; 5,524 were fetched and 16 UTM URLs were intentionally not fetched because robots.txt blocks them. | https://www.searchsarkarinaukri.com/ | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 7 | Pull the **complete indexed URL list** from Google Search Console (Pages report, "Indexed" filter, export all) into `outputs/raw-crawl-data/gsc-indexed-urls-full-list.csv` | N/A | Header-only `gsc-indexed-urls-full-list.csv`; private GSC access was not supplied, documented in `private-platform-data-limitations.md`. | N/A | Info | Provide read-only authenticated access/export from the named platform, rerun this exact check, and attach the dated export. | S |
| 8 | List every URL in sitemap returning 3xx/4xx/5xx — include status code | ❌ Fail | `sitemap-non200-urls.csv`: 11 job URLs return 410. | site-wide / sitemap files | Medium | Regenerate sitemap children from current canonical 200 indexable records only; include missing self-canonical pages, remove 410s/empty files, and validate XSD before publish. | M |
| 9 | List every URL in sitemap that is orphaned (no internal links pointing to it) | ❌ Fail | `sitemap-orphan-urls.csv`: 3,111 URLs; 2,893 are job listings. | site-wide / sitemap files | High | Add contextual hub/category inlinks to valuable URLs; remove low-value/stale URLs from the sitemap; recrawl until every sitemap URL has an intentional path. | M |
| 10 | List every indexable, crawlable, live page **missing** from the sitemap — this is the "which ones are not added" answer the client explicitly wants | ❌ Fail | `crawlable-self-canonical-urls-missing-from-sitemap.csv`: 482 actionable live self-canonical URLs (418 location/category combinations, 50 news, 14 search/category queries). Another 451 parameter variants canonicalize elsewhere. | site-wide / sitemap files | Medium | Regenerate sitemap children from current canonical 200 indexable records only; include missing self-canonical pages, remove 410s/empty files, and validate XSD before publish. | M |
| 11 | List every URL that's in the sitemap AND `noindex`ed (direct contradiction — must be resolved one way or the other) | ✅ Pass | `sitemap-noindex-or-blocked-urls.csv`: zero contradictions. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 12 | List duplicate URLs appearing more than once within the sitemap itself | ✅ Pass | `sitemap-duplicate-urls.csv`: zero duplicate `<loc>` occurrences. | site-wide / sitemap files | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 13 | For job postings whose "Last date" has passed — confirm site policy: are they removed from sitemap, `noindex`ed, redirected to a "closed" status page, or left live and indexable indefinitely? Report current actual behavior (check 10 sample expired listings) vs recommended best practice (Google guidance: don't 404 immediately, mark clearly as closed, keep for historical search value, remove from sitemap once stale). | ❌ Fail | 10 expired samples remain 200/indexable with expired JobPosting; total expired JobPosting pages is 2,782. Eleven removed jobs remain in sitemap as 410. | site-wide / sitemap files | High | At deadline, remove JobPosting markup, show an explicit closed state, remove stale URLs from job sitemap, and preserve/410 pages according to one documented policy. | M |
| 14 | Check how frequently the sitemap is regenerated (compare `lastmod` on today's fetch vs a re-fetch 24–48 hours later, or check server logs for sitemap generation timestamps) — new job postings should appear in the sitemap within hours, not days. | ⚠️ Warning | Jobs sitemap contains lastmod up to audit day and Nginx caches sitemap responses for 10 minutes; only one-day fetch available, and one future admit-card lastmod exists. | site-wide / sitemap files | Low | Regenerate sitemap children from current canonical 200 indexable records only; include missing self-canonical pages, remove 410s/empty files, and validate XSD before publish. | S |

## Sitemap inventory

| Sitemap | Entries | Official XSD | lastmod observation |
|---|---:|---|---|
| sitemap-static.xml | 37 | Pass | none |
| sitemap-jobs.xml | 3,475 | Pass | 58 varied values, 2026-06-29 to 2026-08-25 |
| sitemap-locations.xml | 29 | Pass | none |
| sitemap-qualifications.xml | 10 | Pass | none |
| sitemap-departments.xml | 12 | Pass | none |
| sitemap-cross-filter.xml | 109 | Pass | none |
| sitemap-news.xml | 0 | **Fail** | empty urlset; no lastmod |
| sitemap-blogs.xml | 67 | Pass | 6 varied values, 2026-08-20 to 2026-08-25 |
| sitemap-results.xml | 45 | Pass | 16 varied values |
| sitemap-admit-cards.xml | 37 | Pass | 15 varied values; one future 2026-09-15 |
| sitemap-districts.xml | 50 | Pass | none |

## Reconciliation headline

| Metric | Count |
|---|---:|
| Total unique sitemap URLs | 3,871 |
| Total unique internal URLs discovered/classified | 5,540 (5,524 fetched; 16 robots-blocked UTM URLs not fetched) |
| Total indexed per GSC | N/A — private export unavailable |
| Sitemap + crawlable + indexed | N/A — GSC unavailable |
| Sitemap URLs with zero discovered inlinks | 3,111 |
| Linked 200 self-canonical URLs missing from sitemap | 482 |
| Parameter variants missing but canonicalized elsewhere | 451 |
| Sitemap URLs returning non-200 | 11 |
| Sitemap URLs blocked/noindex | 0 |
| Indexed but not in sitemap | N/A — GSC unavailable |
| Sitemap but not indexed/reason | N/A — GSC unavailable |

The broad crawler count “933 missing” is intentionally split into 482 actionable self-canonical pages and 451 parameter variants canonicalized to another URL.

## Reconciliation by crawler page type

| Page type | In sitemap | Linked/crawlable | Indexable 200 | Self-canonical missing | Broken in sitemap |
|---|---:|---:|---:|---:|---:|
| Job listing | 3,475 | 582 | 3,464 | 0 | 11 |
| Category filter (/jobs?category=) | 0 | 12 | 12 | 12 | 0 |
| Qualification | 5 | 5 | 5 | 0 | 0 |
| Location/cross-filter | 80 | 520 | 498 | 418 | 0 |
| Department | 12 | 5 | 12 | 0 | 0 |
| Static/policy/feature/home/other | 150 | 33 | 148 | 2 | 0 |
| Results | 46 | 1 | 46 | 0 | 0 |
| Admit card | 38 | 1 | 38 | 0 | 0 |
| Blogs | 68 | 512 | 519 | 0 | 0 |
| News | 1 | 51 | 51 | 50 | 0 |

## Summary
- Critical issues: 0 — none
- High issues: 2 — 9, 13
- Medium issues: 2 — 8, 10
- Low issues: 1 — 14
- Top 3 priority fixes for this audit area:
  1. Item 9: Add contextual hub/category inlinks to valuable URLs; remove low-value/stale URLs from the sitemap; recrawl until every sitemap URL has an intentional path.
  2. Item 13: At deadline, remove JobPosting markup, show an explicit closed state, remove stale URLs from job sitemap, and preserve/410 pages according to one documented policy.
  3. Item 8: Regenerate sitemap children from current canonical 200 indexable records only; include missing self-canonical pages, remove 410s/empty files, and validate XSD before publish.
