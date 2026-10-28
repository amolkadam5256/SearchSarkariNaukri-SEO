# 04 — Structured Data / Schema.org Audit

Output file: `outputs/final-reports/04-structured-data-schema-audit-REPORT.md`
Validate every item using Google's Rich Results Test AND Schema Markup
Validator (schema.org validator) — log both tool outputs.

## A. JobPosting Schema (highest priority for this site)
- [ ] Confirm `JobPosting` JSON-LD is present on every individual job listing page
- [ ] Required fields present: `title`, `description`, `datePosted`,
  `validThrough`, `hiringOrganization`, `jobLocation`, `employmentType`
- [ ] `validThrough` matches the visible "Last date" — flag mismatches
  (Google actively penalizes expired JobPosting markup left live)
- [ ] Check Google for Jobs eligibility status in Search Console (Enhancements
  → Job Postings report) — export error/warning counts
- [ ] Confirm expired job postings' `JobPosting` markup is removed or updated
  (not left indexed with expired `validThrough` dates)

## B. FAQPage Schema
- [ ] Confirm the 12 FAQs visible on the homepage (and any per-category FAQs)
  are marked up with `FAQPage` JSON-LD
- [ ] Validate exact question/answer text in markup matches visible on-page text
  (Google requires visible parity)

## C. Organization / WebSite Schema
- [ ] `Organization` schema present with logo, name, sameAs (social profiles)
- [ ] `WebSite` schema with `SearchAction` (sitelinks search box eligibility)
- [ ] Confirm brand name consistency across schema vs meta tags vs visible
  content (cross-ref finding in `00-live-seed-findings.md` #8)

## D. BreadcrumbList Schema
- [ ] Present on job listings, category pages, district pages
- [ ] Matches visible breadcrumb trail exactly

## E. Article / NewsArticle (for results & admit card update posts, if written as articles)
- [ ] Check if applicable; if content is presented as news/update posts, verify
  `datePublished`, `dateModified`, `author`

## F. Local/Table data
- [ ] If job listings present structured info (eligibility, age limit, fee,
  vacancy count) as tables, evaluate whether `Table` or a custom
  `DefinedTermSet`/dataset markup would help AI/answer engines extract facts
  correctly (informs file `08` GEO recommendations)

## G. Validation & Error Log
- [ ] Full list of schema errors (blocking rich results) — per template, with
  exact error message from Google's validator
- [ ] Full list of schema warnings (non-blocking but recommended fixes)
- [ ] Screenshot of Rich Results Test "eligible for rich results" confirmation
  per template type
