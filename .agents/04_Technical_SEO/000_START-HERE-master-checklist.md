# Technical SEO Fix Pack - searchsarkarinaukri.com

Compiled from the full audit (Google Search Console, PageSpeed Insights, Bing
Webmaster Tools, GTmetrix, SSL Labs, security-header scan, Rank Math analyzer,
hreflang/sitemap/robots validators) run on 8 August 2026.

Each issue below has its own file with step-by-step instructions, code, and a
verification method. Work top to bottom - later fixes assume the earlier
ones are done.

## Master checklist

| # | File | Issue | Priority | Est. effort |
|---|------|-------|----------|--------------|
| 1 | `01-javascript-rendering-ssr.md` | Page content only exists after JS runs; simple/AI crawlers see an empty page | High | Large (dev sprint) |
| 2 | `02-core-web-vitals-performance.md` | Real users fail Core Web Vitals (LCP 6.0s, INP 275ms, CLS 0.19) despite perfect lab scores | High | Medium |
| 3 | `03-indexing-crawl-budget.md` | 1,980 pages not indexed; 612 pages 404; 1,099 stuck "discovered, not crawled" | High | Medium |
| 4 | `04-structured-data-schema.md` | JobPosting schema missing streetAddress, postalCode, baseSalary; invalid credentialCategory | Medium | Small |
| 5 | `05-hreflang-international.md` | hreflang missing region-independent en/mr tags | Medium | Small |
| 6 | `06-security-headers-csp.md` | Content-Security-Policy header missing | Medium | Small |
| 7 | `07-ssl-tls-certificate.md` | Cert auto-renewal not confirmed; no CAA record | Medium / Low | Small |
| 8 | `08-email-authentication-spf-dmarc.md` | SPF record missing (DMARC set to quarantine without it) | Medium | Small |
| 9 | `09-sitemap-robots-canonical.md` | Sitemap/robots.txt are valid but need ongoing hygiene; canonical tag invisible to simple crawlers | Low (maintenance) | Small |
| 10 | `10-onpage-technical-metadata.md` | Title tag 75 chars, meta description 205 chars, duplicate H1s | Medium | Small |
| 11 | `11-mobile-seo-ux.md` | Mobile-friendly foundation exists, but touch targets, prompts, forms, images, and mobile JS need cleanup | Medium | Medium |
| 12 | `12-redirects-pagination-internal-linking.md` | Old query-param URLs, pagination, and cross-hub links need a cleaner crawl path | High | Medium |
| 13 | `13-cross-functional-seo-readiness.md` | Older docs add sequencing, analytics, consent, CDN/cache, and release QA dependencies | Medium | Medium |

## Priority legend

- **High** - fix first; blocks indexing, ranking, or real-user experience directly.
- **Medium** - fix within the next sprint; measurable but not urgent.
- **Low** - housekeeping/defense-in-depth; do when time allows.

## How to verify you're done (after all fixes)

1. Re-run PageSpeed Insights (mobile + desktop) on the live URL and confirm the
   field data Core Web Vitals assessment says "Passed", not "Failed".
2. Re-crawl the homepage with a simple HTTP-only fetch:
   `curl -s https://www.searchsarkarinaukri.com/ | grep -i "<h1"`
3. Confirm the H1, canonical tag, and primary nav links are present without
   executing JavaScript.
4. Re-run the Google Rich Results Test on a job-posting page and confirm 0
   "improve item appearance" warnings.
5. Check Search Console > Settings > Ownership verification shows verified.
6. Check Search Console > Indexing > Pages weekly for 4 weeks; confirm the
   "Discovered - currently not indexed" bucket is shrinking, not growing.
