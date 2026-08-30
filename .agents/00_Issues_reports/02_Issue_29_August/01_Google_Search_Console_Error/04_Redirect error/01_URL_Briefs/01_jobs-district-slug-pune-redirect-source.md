# URL Brief - Redirect Source

## Target URL

`https://www.searchsarkarinaukri.com/jobs?district_slug=pune`

## GSC Status

- Issue: Redirect error
- Last crawled: 7 June 2026
- Crawled as: Googlebot smartphone
- Page fetch: Failed - Redirect error
- Indexing allowed: N/A
- Canonical: N/A

## Correct Fix

Do not index this URL. It must be a permanent server-side redirect source.

Expected response:

```text
HTTP/1.1 301 Moved Permanently
Location: https://www.searchsarkarinaukri.com/districts/pune
```

A 308 permanent redirect is also acceptable if the site uses 308 consistently.

## Developer Instructions

- Implement redirect before rendering `/jobs`.
- Read `district_slug` safely from query parameters.
- Validate `pune` against the district slug source of truth.
- Redirect to `/districts/pune` in one hop.
- Do not redirect to `/district/pune`.
- Do not redirect through `/jobs-in-pune`.
- Do not create a redirect chain with trailing slash variants.
- Remove internal links pointing to this query URL and replace them with `/districts/pune`.
- Do not add this query URL to sitemap.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, or shared components unless strictly required for this redirect fix.
