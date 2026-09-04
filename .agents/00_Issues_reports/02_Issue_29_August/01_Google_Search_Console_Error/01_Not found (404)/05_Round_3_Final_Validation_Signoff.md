# Round 3 - Final Validation and Sign-Off

## Final Categories
- KEEP_200
- RESTORE_200
- REDIRECT_301
- REMOVE_410
- REMOVE_404

## Final Checks
- Valid job records resolve correctly.
- Numeric ID and slug routes behave as intended.
- Expired job records render an expired notice, not a missing-job error.
- Expired job robots policy is consistent: if `noindex, follow`, the URL is not in sitemap; if `index, follow`, the page has useful unique content and a valid canonical.
- Deleted records do not render empty pages.
- Redirects are relevant, permanent, and chain-free.
- Sitemap contains only canonical indexable 200 URLs.
- Internal links, breadcrumbs, related jobs, and structured data do not reference removed URLs.
- No soft 404 pages or unexpected 5xx errors remain.

## Sign-Off Counts
- Total URLs audited: 613
- Keep/restore: TBD
- 301 redirects: TBD
- 410 removals: TBD
- 404 removals: TBD
- Unresolved: TBD
- Final result: PASS / FAIL

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep implementation changes limited to the affected URL type, routing, HTTP status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, contextual internal links, page content quality, and QA needed for this issue.
