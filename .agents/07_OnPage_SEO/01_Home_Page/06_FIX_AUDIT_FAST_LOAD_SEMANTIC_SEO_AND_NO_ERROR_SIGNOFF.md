# Fix Audit - Fast Load Semantic SEO And No Error Signoff

Date: 2026-09-01
Scope: Homepage Sections 01-60 and official portals integration

## Purpose

Use this file after implementation to confirm the expanded homepage is complete, fast, crawlable, semantic, attractive, and free from broken URL mistakes.

## Signoff Status

Status: `READY FOR DEVELOPER QA`

Do not mark complete until the live implementation or application source is checked.

## Preservation Checks

- Sections 01-10 remain present.
- Existing creative specs are not overwritten.
- Hero content remains approved.
- Live statistics remain database-driven.
- Latest jobs remain database-driven.
- No navbar change.
- No footer change.
- No header change.
- No global layout change.
- No global CSS/design-system rewrite.

## Expanded Section Checks

For Sections 11-60:

- Section exists or has a deliberate not-needed decision.
- Section has clear user purpose.
- Section uses semantic HTML.
- Section has one logical heading.
- Section includes useful internal links.
- Section avoids duplicate content.
- Section avoids keyword stuffing.
- Section has truthful data.
- Section has a mobile layout.
- Section does not slow initial load.

## Official Portal Checks

- Homepage has a concise Official Government Job Portals section.
- Full directory exists on an internal URL.
- External official links are verified.
- Official links are grouped by category.
- Maharashtra official sources are included.
- NCS/Employment News/UPSC/SSC/RRB/MPSC/IBPS/SBI/RBI/Army/Navy/Air Force entities are included where verified.
- SearchSarkariNaukri is described as independent.
- No text implies the site is a government website.
- Broken/unverified official links are not shown on homepage.

## Technical SEO Checks

- Homepage returns `200 OK`.
- Homepage canonical is correct.
- Homepage robots allows indexing.
- Homepage is in sitemap.
- Sitemap has only canonical 200 indexable URLs.
- No homepage-linked URL returns unexpected 404.
- No homepage-linked URL returns unexpected 410.
- No homepage-linked URL has accidental noindex.
- No homepage-linked URL redirects through chains.
- No homepage link points to a duplicate canonicalized-away page unless intentional for users.

## 404 / Remove / Redirect Checks

For every URL connected from the homepage:

- If true 404 and not needed: remove from homepage, sitemap, schema, breadcrumbs, related links, and internal-link hubs.
- If true 404 but valid/useful: restore `200 OK`.
- If obsolete with close equivalent: add one-hop `301`.
- If permanently removed: return `410 Gone` and remove from sitemap/internal links.
- Do not redirect unrelated dead pages to the homepage.

## Performance Checks

- Critical homepage text appears quickly on mobile.
- Heavy lower sections are lazy-loaded.
- Expensive database queries are cached or batched.
- Images use responsive sizes.
- Images have width/height or aspect-ratio.
- Layout shifts are controlled.
- No video embed loads by default.
- Animations use lightweight opacity/transform.
- Portal directory data is not fully loaded on first paint.
- JavaScript does not block crawlable content.

## Semantic SEO Checks

- One homepage `h1`.
- Every major module uses `h2`.
- Links use descriptive anchor text.
- Job cards include organization, post, location, date/status where visible.
- Government portal links use official entity names.
- Page explains source verification.
- Internal links reinforce topic clusters:
  - jobs
  - districts
  - states
  - qualifications
  - departments
  - exams
  - admit cards
  - results
  - study material
  - official sources

## AEO/GEO Checks

- Direct answer near the top explains what SearchSarkariNaukri provides.
- Official-source note is visible.
- FAQ answers real user questions.
- FAQ schema matches visible FAQ text.
- Important entities are clear.
- The homepage routes users to focused pages instead of trying to answer every topic fully.

## Accessibility Checks

- Search input has label.
- CTAs have accessible names.
- Keyboard focus is visible.
- Cards and chips are reachable by keyboard.
- Mobile chips can scroll without trapping focus.
- Images have meaningful alt text or empty alt when decorative.
- Color contrast passes.
- No horizontal overflow.

## Final Developer Output

Developer must provide:

1. Changed files
2. New sections added
3. Existing sections preserved
4. Internal URLs added
5. Official government portal URLs added
6. URLs removed because 404/not needed
7. Redirects added
8. Pages restored to 200
9. Sitemap updates
10. Schema updates
11. Lighthouse/PageSpeed result
12. Mobile screenshot
13. Desktop screenshot
14. Remaining risks

## Final Decision

Only mark `PASS` when every section is implemented or deliberately excluded, every broken URL is handled, and the live homepage remains fast, accessible, semantic, indexable, and visually consistent.

---

## Universal Developer Guardrail

Apply this rule before using this file for implementation:

1. Audit the existing homepage/component first.
2. Do not delete existing sections, components, internal links, SEO copy, metadata, schema, job data, or URLs without explicit approval.
3. Preserve approved Sections `01-10`; patch only verified issues.
4. If this section already exists in code, improve the existing component instead of rebuilding it unnecessarily.
5. Never invent vacancies, dates, salary, eligibility, age limits, selection process, official links, job counts, subscriber counts, exam dates, or government approval.
6. Verify every internal URL and official external URL before publishing.
7. Remove or replace links to true `404`/`410` pages; keep those URLs out of sitemap, schema, breadcrumbs, related links, and internal-link hubs.
8. Use one-hop `301` only when there is a close relevant replacement.
9. Do not create thin doorway pages, duplicate SEO pages, keyword-stuffed sections, or fake urgency.
10. Do not change navbar, footer, header, logo, global menu, global styles, analytics, tracking, or unrelated routes unless a documented bug requires it and regression QA is completed.
11. SearchSarkariNaukri must be described as an independent information portal, not an official government website.
12. Final signoff requires audit, implementation, live URL/status checks, sitemap/canonical/robots/schema validation, mobile QA, accessibility QA, and performance QA.
