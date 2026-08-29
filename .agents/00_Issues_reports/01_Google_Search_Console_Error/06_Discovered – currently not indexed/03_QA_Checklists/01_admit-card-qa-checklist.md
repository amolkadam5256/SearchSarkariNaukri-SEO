# Admit Card Discovered-Not-Indexed QA Checklist

## Required Crawl Tests

For every URL in the 896 export and every local brief:

- HTTP status.
- Final URL after redirects.
- Canonical.
- Robots meta and X-Robots-Tag.
- H1 count.
- Word count.
- Visible key facts.
- FAQ count.
- Schema types.
- Sitemap inclusion.
- Internal incoming links.

## Quality Gate

A URL should not be submitted for indexing until it has:

- Unique exam/admit-card intent.
- Real conducting authority.
- Official source link.
- Status and dates.
- Download instructions.
- Exam-day guidance.
- Record-specific FAQs.
- Breadcrumb and internal links.
- Self canonical and index/follow.

## GSC Validation

1. Fix template and data issues first.
2. Crawl a sample of active, historical, duplicate, and invalid pages.
3. Update sitemap.
4. Inspect representative URLs in GSC.
5. Request indexing for high-quality canonical pages only.
6. Validate the issue after deployment.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required.
