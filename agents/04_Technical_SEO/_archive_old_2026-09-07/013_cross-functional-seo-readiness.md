# 13. Cross-Functional SEO Readiness

This file consolidates useful material from the separate `Old` documentation folder that was not already covered by the current technical SEO audit pack.

## Why this matters

Several older files are not direct technical SEO fixes, but they affect whether the audit can be implemented safely. The most useful findings are about sequencing, route ownership, analytics readiness, consent, CDN/cache behavior, and launch QA.

## Rendering fix sequencing

The old project docs identified the same core rendering issue now covered in `01-javascript-rendering-ssr.md`: job detail pages, `/admit-cards`, and `/results` must serve useful page-specific HTML to a non-JavaScript request.

Do these before expanding other SEO systems:

- [ ] Diagnose whether the issue is CSR-only routing, missing server route handlers, CDN/cache misrouting, or another response-layer bug.
- [ ] Verify at least 3 job detail URLs return their own title, H1, body fields, canonical, and status in raw HTML.
- [ ] Verify `/admit-cards` and `/results` have distinct title/meta pairs and non-empty body content in raw HTML.
- [ ] Keep the rendering fix isolated from UI/layout/copy changes.
- [ ] Run a visual regression check in a normal browser after the raw-HTML fix.
- [ ] Do not expand `JobPosting`, `FAQPage`, or detail-page analytics events until the related page content is present in the server response.

## URL and page-type inventory

The older IA files add useful route opportunities that go beyond the first 12 audit files.

Priority route work:

- [ ] Create `/department` as a department index page.
- [ ] Create `/department/[slug]` pages for MPSC, UPSC, SSC, railway, banking, police, talathi, zilla parishad, forest, health, education, and central government jobs.
- [ ] Create `/district/[slug]` pages for canonical district URLs and redirect old query-param versions.
- [ ] Consider `/state/[slug]` pages only after the rendering, canonical, and sitemap foundations are stable.
- [ ] Consider `/qualification/[slug]` pages only after a written filtered-page indexation policy exists.
- [ ] Confirm whether `/districts` should remain as a plural index page or redirect to `/district`.

Guardrail: do not generate state, qualification, or combined-filter landing pages until the site has a clear policy for pagination, expired jobs, empty-result pages, thin pages, and sitemap inclusion.

## Analytics and measurement readiness

The older docs mention that analytics, GTM, and conversion tracking are either absent or need verification. Treat this as a measurement dependency, not a replacement for the SEO fixes.

- [ ] Confirm GA4, GTM, Microsoft Clarity, Meta Pixel, and any ad/conversion tags are intentionally installed or intentionally absent.
- [ ] Confirm Consent Mode V2 or equivalent consent behavior before adding marketing tags.
- [ ] Avoid duplicate page_view events, especially on SPA route changes.
- [ ] Only define per-job view/apply events after job detail pages render unique job data.
- [ ] Track SEO outcomes with Search Console first: indexing, clicks, impressions, query/page pairs, and crawl errors.
- [ ] Add analytics QA to production releases so tracking changes do not regress Core Web Vitals.

Useful production QA checks from the old files:

```text
- GTM backup exported.
- Placeholder IDs replaced.
- Consent Mode V2 configured.
- GA4 DebugView verified.
- Meta Test Events verified.
- Google Ads conversions verified.
- No duplicate PageView.
- No duplicate lead/apply events.
```

## CDN, DNS, and cache readiness

The older hosting files note that Cloudflare/CDN usage was not confirmed. The live stack was observed as nginx/Ubuntu in the older notes, so avoid assuming Cloudflare is active unless DNS/proxy headers confirm it.

- [ ] Confirm DNS owner, zone owner, registrar access, billing owner, recovery contacts, and MFA.
- [ ] Confirm CDN/proxy status for public records.
- [ ] Ensure HTML cache rules do not serve the homepage shell for detail-page URLs.
- [ ] Use long immutable cache for versioned static assets.
- [ ] Use short cache or controlled revalidation for public job/result/admit-card HTML.
- [ ] Do not shared-cache authenticated, admin, personalized, search, or sensitive API responses.
- [ ] Document cache purge permissions and the process for urgent job expiry/correction updates.
- [ ] Re-test official application links and expired/corrected labels after every cache rule change.

## Final release gate

Before marking the SEO audit implemented:

- [ ] Raw HTML checks pass for homepage, `/jobs`, 3 job details, `/admit-cards`, `/results`, one department page, and one district page.
- [ ] Canonical tags, robots meta, sitemap inclusion, and internal links agree for every tested URL.
- [ ] Structured data matches visible page content.
- [ ] PageSpeed mobile field data is monitored after release, not just Lighthouse lab scores.
- [ ] Search Console is checked weekly for 4 weeks after deployment.
- [ ] Analytics/consent QA is complete if tracking changes shipped with the SEO work.
- [ ] CDN/cache behavior is verified after deployment and after one content update.
