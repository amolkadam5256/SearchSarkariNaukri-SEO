# Master Admit Card Discovered-Not-Indexed Implementation Specification

## 1. Problem

Google Search Console reports 896 URLs under `Discovered - currently not indexed`. The supplied page evidence shows the `/admit-cards` hub and several `/admit-cards/{id}` records. The page architecture is useful but many detail pages appear thin: crawl evidence shows many admit-card detail pages around 138-143 words with only `Related Updates` and `Admit Card FAQ` headings.

The fix is not just adding generic text. The fix is a record-specific content, canonical, sitemap, structured data, and internal-linking architecture.

## 2. First Rule: Do Not Blindly Index 896 URLs

Every URL must be classified before indexing:

| Type | Action |
|---|---|
| Active + useful + unique | Improve content, keep indexable, include in sitemap |
| Historical but useful | Usually index if substantial and accurate |
| Duplicate records | Consolidate, canonicalize, or redirect |
| Thin records | Improve first, then request indexing |
| Invalid/dead records | 404/410 and remove from sitemap/internal links |
| Wrong year/title/source | Fix source record and URL strategy first |

## 3. Required Page Architecture For Good `/admit-cards/{id}` Pages

Each qualifying page should include:

1. H1: `{Exam Name} Admit Card {Year}`.
2. Current Admit Card Status.
3. Exam Date.
4. Admit Card Release Date.
5. Last Updated.
6. Conducting Authority.
7. Official Source / Official Download Link.
8. Short `What you need to know` summary.
9. Important Dates table.
10. How to Download Admit Card - 5 to 8 steps.
11. What to Keep Ready.
12. Details Mentioned on Admit Card.
13. Documents / ID Proof Required.
14. Exam Day Instructions.
15. What to Do If Download Fails.
16. Exam Centre / City Intimation when applicable.
17. Related Exam Information.
18. Related Admit Cards.
19. Related Results.
20. Related Jobs / original notification.
21. Eligibility/context link where relevant.
22. 10-15 genuinely specific FAQs.
23. Official-source verification note.
24. Last updated/reviewed date.
25. Breadcrumb + internal links.
26. Valid BreadcrumbList / appropriate structured data.
27. Self-canonical, index/follow, sitemap inclusion only where appropriate.

## 4. FAQ Rule

Do not copy the same 15 FAQs across all 896 pages. The framework can be shared, but answers must use the actual exam status, exam date, authority, source domain, credentials, release date, and related links.

## 5. Technical SEO Requirements

- Every indexable admit-card detail page returns HTTP 200.
- One self-referencing canonical.
- `index, follow, max-snippet:-1, max-image-preview:large`.
- No redirect chain, no noindex, no robots block, no duplicate canonical.
- Include only quality-passing pages in `sitemap-admit-cards.xml`.
- Remove invalid, duplicate, noindex, redirecting, 404, 410, and soft-404 URLs from sitemap.
- Keep facts visible in raw/prerendered HTML.
- Match schema to visible content.

## 6. Internal Linking Requirements

Strengthen existing relationships to Results, Jobs, WhatsApp updates, Exams, and Eligibility. Do not add random keyword links.

Use contextual links:

- `/admit-cards` hub.
- Related result page if available.
- Related original job notification if available.
- Related exam guide if available.
- Related admit cards from same authority/category.
- Eligibility checker only if it helps the user.
- Job updates/WhatsApp page only as a relevant alert CTA.

## 7. Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for admit-card indexing/content architecture. Do not mass-publish thin duplicate content just to make discovered URLs indexable.

## 8. Definition Of Done

- Full 896 URL export is imported and classified.
- Every kept URL has a record-specific brief and passes quality gate.
- Thin pages are expanded with real record data.
- Duplicate/invalid pages are consolidated or removed correctly.
- Sitemap contains only canonical quality URLs.
- Internal links point to canonical URLs.
- Structured data validates and matches visible content.
- GSC validation is requested only after the fixes are live.
