# Page Speed And Technical Performance Audit

Date: 2026-08-29
Issue: Crawled - currently not indexed

## Why Speed Matters

Slow pages, layout shifts, heavy JavaScript, blocked rendering, and delayed content can reduce crawl quality and make programmatic pages look thin. Speed alone does not guarantee indexing, but poor performance can worsen discoverability and page quality signals.

## Tests To Run

1. Lighthouse mobile test for representative URLs from each page type.
2. PageSpeed Insights for live production examples.
3. Chrome DevTools performance trace for slow templates.
4. Crawl rendered HTML to confirm content appears without user interaction.
5. Check image sizes, lazy loading, script weight, CSS blocking, and font loading.
6. Check server response time and caching headers.

## Required Targets

- LCP: improve toward under 2.5s where possible.
- CLS: avoid visible layout shifts.
- INP: keep interactions responsive.
- HTML must include critical SEO content or render it reliably for Googlebot smartphone.
- Structured data must be available in initial/rendered HTML.
- Do not load unnecessary heavy scripts on job/result/landing pages.

## Fix Ideas

- Compress and properly size images.
- Use caching for static assets and sitemap output.
- Avoid blocking scripts before main content.
- Server-render or pre-render important SEO sections.
- Remove duplicate analytics/tracking snippets if any exist, but do not change tracking unless verified necessary.
- Avoid layout shifts from ads/images/cards by setting width/height/aspect-ratio.
- Paginate large related lists cleanly.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
