# 3. Indexing & Crawl Budget

**Priority: 🔴 High**

## The problem
| Reason | Pages |
|---|---|
| Discovered – currently not indexed | 1,099 |
| Not found (404) | 612 |
| Crawled – currently not indexed | 125 |
| Soft 404 | 82 |
| Excluded by 'noindex' tag | 59 |
| Redirect error | 1 |
| Alternative page with proper canonical tag | 1 |
| Duplicate, Google chose different canonical | 1 |
| **Total not indexed** | **1,980** |
| **Indexed** | **664** |

Only 25% of known pages are indexed. Sitemap declares 1,819 discovered
pages, so the site is generating far more URLs than Google is willing to
index right now.

## Fix 1 — Clean up the 612 "Not found (404)" pages
These are internal or external links pointing at URLs that no longer
resolve.
1. Export the full 404 list: Search Console → Indexing → Pages → "Not
   found (404)" → download the table (or use the URL Inspection API /
   `site:searchsarkarinaukri.com` search operator + a crawler like
   Screaming Frog to find them faster).
2. For each 404 URL, decide:
   - **Content moved/renamed** → add a 301 redirect to the new URL.
   - **Content genuinely gone (expired job posting)** → either keep a
     thin "this vacancy has closed" page (better for SEO, users searching
     for that exact title still land somewhere useful) or 301-redirect to
     the closest live equivalent (e.g. the parent category page).
   - **Never should have existed (bad internal link, old test URL)** →
     fix/remove the internal link that points to it; let the 404 stand
     (a small number of true 404s is fine).
3. Crawl your own sitemap and site with Screaming Frog / Sitebulb monthly
   and fix new 404s before Google finds them.

### Nginx redirect example
```nginx
# One-off redirects for retired job postings
location = /jobs/old-slug {
    return 301 /jobs/new-slug;
}

# Or maintain a redirect map file for bulk redirects
map $request_uri $redirect_uri {
    include /etc/nginx/redirects.map;
}
server {
    if ($redirect_uri) {
        return 301 $redirect_uri;
    }
}
```

## Fix 2 — Fix the 82 "Soft 404" pages
A soft 404 is a page that returns HTTP 200 but has little/no real content
(Google treats it as if it were a 404). This is common for **expired job
postings** that still resolve but show an empty/near-empty page once the
listing is pulled from the database.
1. For expired postings, do NOT just blank the page. Either:
   - Show a clear "This vacancy has closed — browse similar current
     openings" message with 3–5 real internal links to live, related job
     postings (keeps the page useful and out of soft-404 territory), or
   - Return a real `404` status code (not 200) if you want the URL
     removed, or a `410 Gone` if it's permanently retired.
2. Given this is likely tied to the JS-rendering issue in file 01: if the
   page's real content only renders after a client-side data fetch fails
   silently, Google's crawler may see an empty shell and flag it as soft
   404 even for pages you consider "live." Confirm server-rendered HTML
   contains real content for every indexable URL.

## Fix 3 — The 1,099 "Discovered – currently not indexed" pages
This is not a technical error — it means Google knows the URL exists (via
your sitemap or internal links) but has decided **not to spend crawl
budget on it yet**. Causes, in order of likely relevance for a new site
like this:
1. **Domain is new/low-authority** (property added to GSC on 22 Jul 2026,
   thin backlink profile — see main audit report Section 6). Google
   crawls new/low-trust domains conservatively at first. This will
   improve naturally as the domain accumulates age, authority, and
   click-through history — but you can speed it up:
   - [ ] Strengthen internal linking so your most important pages
         (highest-value job categories, high-search-volume districts)
         get more internal links, signalling priority.
   - [ ] Submit your most important URLs individually via Search Console
         → URL Inspection → "Request indexing" (rate-limited, so use
         selectively on your highest-value pages, not all 1,099 at once).
   - [ ] Reduce near-duplicate pages (see Fix 4) — Google is less willing
         to index pages that look very similar to ones it already has.
2. **Slow server response** — a slow TTFB (see file 02) makes crawling
   more expensive for Googlebot, which can reduce how many pages it's
   willing to crawl per visit. Fixing performance also helps indexing.
3. **Sitemap hygiene** — make sure the sitemap only lists canonical,
   indexable URLs (see file 09) so Google isn't wasting attention on URLs
   you don't actually want indexed.

## Fix 4 — Reduce near-duplicate / thin pages
With 1,980 non-indexed pages against only 664 indexed, some portion is
likely near-duplicate content (e.g. many small district or category pages
with very similar boilerplate and few unique job listings).
- [ ] Audit low-value programmatic pages (e.g. districts/categories with
      0–1 job postings). Either enrich them with genuinely unique content
      (local application tips, deadlines specific to that district) or
      `noindex` them until they have enough unique content to be worth
      indexing.
- [ ] Consolidate near-identical pages via canonical tags where one page
      is clearly the "main" version.

## Fix 5 — The 59 "Excluded by 'noindex' tag" pages
Confirm this is intentional. Check which URLs these are:
```bash
curl -s https://www.searchsarkarinaukri.com/some-url | grep -i noindex
```
If any of these are pages you actually want indexed, remove the
`<meta name="robots" content="noindex">` tag or the `X-Robots-Tag: noindex`
HTTP header.

## Fix 6 — The 1 "Redirect error" and 1 "Duplicate, Google chose different
canonical than user" page
Small counts, but worth a quick manual check via URL Inspection in Search
Console to confirm they're not symptomatic of a wider redirect-chain or
canonicalization bug.

## Ongoing monitoring
- [ ] Check Search Console → Indexing → Pages weekly for the first
      2 months after these fixes ship.
- [ ] Target: "Discovered – currently not indexed" trending down, not up,
      week over week. If it keeps growing, you're generating URLs faster
      than Google will index them — slow down programmatic page creation
      until the ratio improves.
