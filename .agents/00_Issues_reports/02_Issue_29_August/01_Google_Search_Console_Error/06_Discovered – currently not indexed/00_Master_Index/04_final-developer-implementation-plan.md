# Final Implementation Plan For 896 Admit Card URLs

## Executive Summary

The folder now contains a complete 896-URL developer handoff for the admit-card `Discovered - currently not indexed` issue. The key problem is not only thin content; it is a combined URL architecture, content quality, canonical, sitemap, internal-linking, and structured-data issue.

The safest path is to treat `/admit-cards/{numeric-id}` URLs as current source URLs, join them to real admit-card records, then decide whether each record deserves indexing and whether it should migrate to a meaningful slug URL.

## Critical Findings

- The GSC export contains 896 unique URLs.
- The all-896 brief folder contains 896 markdown files.
- The current URL pattern is generic/numeric and weak for SEO/AEO/GEO.
- Many local crawl examples are thin, often around 138-143 words.
- GSC discovery does not mean all URLs should be indexed.
- Meaningful slug recommendations require actual record data for many URLs.

## Priority Matrix

| Priority | Work | Reason |
|---|---|---|
| P0 | Join all 896 URLs to real admit-card records | Cannot safely create semantic slugs without entity data |
| P0 | Classify every URL | Prevent indexing thin/duplicate/invalid pages |
| P1 | Fix template content architecture | Most pages need stronger record-specific sections |
| P1 | Build safe canonical slug strategy | Numeric URLs weaken relevance and sharing |
| P1 | Add redirects only after collision checks | Avoid SEO migration damage |
| P2 | Update sitemap/internal links/schema | Consolidate signals on canonical URLs |
| P2 | Add AEO/GEO/LLM facts and FAQs | Improve AI/snippet extraction |
| P3 | Monitor GSC cohorts after release | Indexing improvements can take time |

## URL Architecture Rules

- Current numeric URLs are source URLs, not automatically final SEO URLs.
- Final canonical URL should be meaningful when data is sufficient.
- Use lowercase hyphenated slugs.
- Include year only when it distinguishes the record.
- Avoid keyword stuffing.
- Keep numeric ID only if required for uniqueness and appended consistently.
- Never create duplicate slugs.
- Do not redirect invalid pages to unrelated pages.

## Page Content Rules

Every indexable admit-card page must have record-specific content: status, exam date, release date, authority, official source, download steps, important dates, documents, exam-day guidance, failure handling, related result/job/exam links, and 10-15 specific FAQs.

## Technical Rules

- Indexable pages: HTTP 200, self canonical, index/follow, sitemap included.
- Duplicate migrated pages: 301/308 to canonical URL, not in sitemap.
- Invalid pages: 404/410, noindex, not in sitemap.
- Thin pages: improve first; do not request indexing yet.
- Structured data must match visible content.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for admit-card indexing/content architecture.
