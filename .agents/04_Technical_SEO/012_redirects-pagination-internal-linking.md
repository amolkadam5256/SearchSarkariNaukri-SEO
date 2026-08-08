# 12. Redirects, Pagination & Internal Linking

This file consolidates the useful pieces from the old redirect, pagination, and internal-linking documents. It supports the newer indexing and sitemap/canonical files by making crawl paths cleaner.

## The problem

The old audit found that important listing paths were often exposed as query-parameter URLs. That creates duplicate crawl paths, weakens canonical signals, and makes internal links less descriptive.

High-impact examples:

- `/jobs?category=mpsc` should resolve to `/department/mpsc`.
- `/jobs?category=upsc` should resolve to `/department/upsc`.
- `/jobs?category=ssc` should resolve to `/department/ssc`.
- `/jobs?district_slug=pune` should resolve to `/district/pune`.
- `/jobs?district_slug=mumbai-city` should resolve to `/district/mumbai`.
- `/jobs?district_slug=ahmednagar` should resolve to `/district/ahilyanagar` if that is the canonical district name.
- `/jobs?page=2` should use a consistent pagination URL/canonical strategy.

## Redirect rules

- [ ] Pick one preferred host: `https://www.searchsarkarinaukri.com/` or `https://searchsarkarinaukri.com/`.
- [ ] Force HTTPS and the preferred host with a single 301 hop.
- [ ] 301 old department query URLs to clean department hubs.
- [ ] 301 old district query URLs to clean district hubs.
- [ ] Preserve useful user filters only when they represent a crawl-worthy page.
- [ ] Canonicalize or noindex search result URLs such as `/jobs?search=query`.
- [ ] Keep retired job URLs as 404/410 unless there is a truly equivalent replacement.
- [ ] Avoid redirect chains and loops.

Example Nginx pattern:

```nginx
map $arg_category $department_redirect {
    default "";
    mpsc /department/mpsc;
    upsc /department/upsc;
    ssc /department/ssc;
    railway /department/railway;
    banking /department/banking;
    police /department/police;
    talathi /department/talathi;
    zp /department/zilla-parishad;
    forest /department/forest;
    health /department/health;
    education /department/education;
    central /department/central-govt;
}

location = /jobs {
    if ($department_redirect != "") {
        return 301 $department_redirect;
    }
}
```

Prefer a tested redirect map or application-level redirect handler if the hosting stack makes Nginx `if` rules risky.

## Pagination rules

- [ ] Page 1 should canonicalize to the clean base URL, for example `/jobs`.
- [ ] Page 2+ should be crawlable only if it helps discovery; otherwise use `noindex, follow`.
- [ ] Keep pagination links as real `<a href="">` links in raw/prerendered HTML.
- [ ] Use one URL format consistently, for example `/jobs/page/2` or `/jobs?page=2`, not both.
- [ ] Exclude paginated URLs from XML sitemaps unless there is a deliberate reason to include them.
- [ ] Ensure `og:url` matches the canonical URL.

For large listing archives, the practical default is:

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">
<meta name="robots" content="noindex, follow, max-snippet:-1, max-image-preview:large">
```

Use that pattern on page 2+ only. Page 1 should remain indexable.

## Internal linking rules

- [ ] Replace homepage department links from `/jobs?category=slug` to `/department/slug`.
- [ ] Replace homepage district links from `/jobs?district_slug=slug` to `/district/slug`.
- [ ] Link each job detail page back to its department, district, and the main jobs hub.
- [ ] Add breadcrumb links on job, admit card, result, and study material detail pages.
- [ ] Add related jobs from the same department and district where available.
- [ ] Link admit-card pages to the matching job/result/study-material pages when a relationship exists.
- [ ] Use descriptive anchor text such as `MPSC Bharti 2026`, `Pune Govt Jobs`, and `SSC CGL Admit Card`.
- [ ] Avoid generic anchor text such as `click here`, `read more`, or `details` when the destination topic is known.

## Verification

```bash
# Confirm redirects
curl -I "https://www.searchsarkarinaukri.com/jobs?category=mpsc"
curl -I "https://www.searchsarkarinaukri.com/jobs?district_slug=pune"

# Confirm pagination signals
curl -s "https://www.searchsarkarinaukri.com/jobs?page=2" | grep -Ei "canonical|robots|href=.*/jobs"

# Confirm homepage links use clean URLs
curl -s "https://www.searchsarkarinaukri.com/" | grep -E "/department/|/district/"
```

Expected results:

- Query-parameter category and district URLs return 301 to clean URLs.
- Page 2+ does not compete with page 1 in the index.
- Clean department and district URLs appear in raw/prerendered HTML.
- Search Console's duplicate, discovered-not-indexed, and 404 buckets shrink over the next 4 weekly checks.
