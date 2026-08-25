# 03 — Sitemap & URL Reconciliation Audit
### (Answers: "how many pages/URLs are in the sitemap, and which ones are missing")

Output file: `outputs/final-reports/03-sitemap-url-audit-REPORT.md`
This is one of the highest-priority files in this package — execute it precisely.

## Step 1 — Inventory every sitemap
- [ ] Fetch `https://www.searchsarkarinaukri.com/robots.txt`, extract every `Sitemap:` line
- [ ] Fetch `https://www.searchsarkarinaukri.com/sitemap.xml` (or whatever the robots.txt points to)
- [ ] If it's a sitemap **index**, list every child sitemap URL and fetch each one
- [ ] For each individual sitemap file, record:
  - File URL
  - Total `<url>` / `<loc>` entry count
  - Whether it validates against the sitemap XML schema
  - Whether `<lastmod>` values look real (varied, recent) vs fake (all identical/today's date on every entry)

**Report table (fill for every sitemap file found):**

| Sitemap File URL | Entry Count | Valid XML? | lastmod looks accurate? | Notes |
|---|---|---|---|---|
| (fill in) | | | | |

## Step 2 — Full URL export
- [ ] Export the **complete list** of every `<loc>` URL across all sitemaps into
  `outputs/raw-crawl-data/sitemap-urls-full-list.csv`
- [ ] Run a full site crawl (Screaming Frog "Spider" mode from homepage, unlimited
  depth, respecting robots.txt) — export the **complete list** of every URL
  discovered via internal links into
  `outputs/raw-crawl-data/crawled-urls-full-list.csv`
- [ ] Pull the **complete indexed URL list** from Google Search Console (Pages
  report, "Indexed" filter, export all) into
  `outputs/raw-crawl-data/gsc-indexed-urls-full-list.csv`

## Step 3 — Reconciliation (the core deliverable)

Produce these exact counts and lists:

### 3.1 Headline numbers
| Metric | Count |
|---|---|
| Total URLs in sitemap(s) | |
| Total unique URLs discovered by crawler (linked/reachable) | |
| Total URLs indexed per GSC | |
| URLs in sitemap AND crawlable AND indexed (fully healthy) | |
| URLs in sitemap but NOT crawlable/linked anywhere (orphaned in sitemap) | |
| URLs crawlable/linked but NOT in sitemap (missing from sitemap) | |
| URLs in sitemap returning non-200 status | |
| URLs in sitemap but blocked by robots.txt or `noindex` | |
| URLs indexed but not in sitemap | |
| URLs in sitemap but NOT indexed (with GSC-reported reason) | |

### 3.2 Full URL-level lists (attach as CSV in `outputs/raw-crawl-data/`, summarize top offenders in the report body)
- [ ] List every URL in sitemap returning 3xx/4xx/5xx — include status code
- [ ] List every URL in sitemap that is orphaned (no internal links pointing to it)
- [ ] List every indexable, crawlable, live page **missing** from the sitemap — this is the "which ones are not added" answer the client explicitly wants
- [ ] List every URL that's in the sitemap AND `noindex`ed (direct contradiction — must be resolved one way or the other)
- [ ] List duplicate URLs appearing more than once within the sitemap itself

### 3.3 Segment the counts by page type
Break every number above down by template so the developer knows where the
problem concentrates:

| Page Type | In Sitemap | Crawlable | Indexed | Missing from Sitemap | Broken in Sitemap |
|---|---|---|---|---|---|
| Job listings (`/jobs/{slug}--{id}`) | | | | | |
| Category/filter (`/jobs?category=`) | | | | | |
| Qualification pages | | | | | |
| District/location pages | | | | | |
| Department pages | | | | | |
| Static pages | | | | | |
| Results pages | | | | | |
| Admit card pages | | | | | |

## Step 4 — Expired/closed job listings policy check
- [ ] For job postings whose "Last date" has passed — confirm site policy: are
  they removed from sitemap, `noindex`ed, redirected to a "closed" status page,
  or left live and indexable indefinitely? Report current actual behavior
  (check 10 sample expired listings) vs recommended best practice (Google
  guidance: don't 404 immediately, mark clearly as closed, keep for historical
  search value, remove from sitemap once stale).

## Step 5 — Sitemap freshness / re-fetch cadence
- [ ] Check how frequently the sitemap is regenerated (compare `lastmod` on
  today's fetch vs a re-fetch 24–48 hours later, or check server logs for
  sitemap generation timestamps) — new job postings should appear in the
  sitemap within hours, not days.
