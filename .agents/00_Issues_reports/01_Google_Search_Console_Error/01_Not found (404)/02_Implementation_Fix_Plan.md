# SearchSarkariNaukri - 404 Fix Implementation Plan

## Pre-Change Protection
- Create a Git branch/commit before implementation.
- Back up the production database/content source.
- Export current sitemap and route behavior.
- Preserve the original GSC Excel export and the generated CSV audit.
- Do not bulk-delete jobs until DB verification is complete.

## Decision Logic
- Existing valid job returning 404: fix route/database/visibility and return 200.
- Expired job record with useful content: do not show "Job not found"; return 200 with the full job details, an expired/deadline-passed notice, correct canonical, and either `index, follow` or `noindex, follow` based on the site's expired-job SEO policy.
- Old URL with exact replacement: add direct 301 to the final canonical URL.
- Permanently removed job with no replacement: return 410 if intentional, otherwise keep 404.
- Random invalid URL: keep 404 or 410.
- Duplicate/variant URL: canonicalize or redirect to preferred URL.

## Implementation Checklist
- Verify numeric ID route support for `/jobs/{id}`.
- Verify slug route support for `/jobs/{slug}-{id}` or current canonical format.
- Check published/deleted/expired status for every job ID.
- Split missing-job behavior from expired-job behavior in the route/template logic.
- Replace any expired-page copy that says "Job not found" with a clear message such as "This job's application deadline has passed".
- If expired pages use `<meta name="robots" content="noindex, follow" />`, confirm they are excluded from XML sitemaps and still keep internal follow links useful.
- Generate redirect map only for URLs with relevant replacements.
- Remove 404/410/redirect URLs from sitemap generation.
- Remove expired job URLs from sitemap when those pages use `<meta name="robots" content="noindex, follow" />`.
- Remove or update internal links to removed URLs.
- Confirm canonical tags point only to 200 URLs.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
