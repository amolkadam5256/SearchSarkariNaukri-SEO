# Redirect Error QA and GSC Validation Checklist

## Live Redirect Tests

Run after deployment:

```bash
curl -I "https://www.searchsarkarinaukri.com/jobs?district_slug=pune"
curl -IL "https://www.searchsarkarinaukri.com/jobs?district_slug=pune"
curl -I "https://www.searchsarkarinaukri.com/districts/pune"
```

Expected:

```text
/jobs?district_slug=pune -> 301 or 308 -> /districts/pune
/districts/pune -> 200
```

## HTML Signal Tests

```bash
curl -s "https://www.searchsarkarinaukri.com/districts/pune" | grep -Ei "canonical|robots|Pune Government Jobs|FAQPage|BreadcrumbList"
```

Expected:

- Self canonical to `https://www.searchsarkarinaukri.com/districts/pune`.
- Robots allows indexing.
- Visible Pune-specific H1/content appears in HTML.
- BreadcrumbList exists.
- FAQPage exists only if visible FAQs are present.

## Sitemap Tests

- Confirm `/districts/pune` appears in the sitemap.
- Confirm `/jobs?district_slug=pune` does not appear in the sitemap.
- Confirm no sitemap URL redirects.

## Internal Link Tests

Search rendered HTML and source code for old URL:

```bash
grep -R "jobs?district_slug=pune" .
```

Expected: no internal links should use the old query URL, except test fixtures, redirect maps, or documentation.

## GSC Validation Steps

1. Inspect `https://www.searchsarkarinaukri.com/jobs?district_slug=pune`.
2. Run live test.
3. Confirm Googlebot sees the permanent redirect to `/districts/pune`.
4. Inspect `https://www.searchsarkarinaukri.com/districts/pune`.
5. Confirm URL is indexable with self canonical.
6. Request indexing for `/districts/pune` if needed.
7. Validate the Redirect error issue after deployment.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, or shared components unless strictly required for this redirect fix.
