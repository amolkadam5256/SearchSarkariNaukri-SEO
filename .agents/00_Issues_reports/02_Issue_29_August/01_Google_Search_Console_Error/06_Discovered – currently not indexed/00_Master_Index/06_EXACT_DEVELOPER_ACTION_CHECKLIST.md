# Exact Developer Action Checklist - 896 Admit Card Indexing Fix

Date: 2026-08-29
Issue: Google Search Console `Discovered - currently not indexed`
Scope: 896 admit-card detail URLs

## What This Folder Does

This folder is the final audit and implementation handoff for the 896 admit-card URLs. It does not change site code. It tells the developer what to check, what to fix, which URLs need sitemap work, which URLs need manual data review, and what rules must be followed before requesting Google indexing validation.

## Exact Files To Use

| File / Folder | What It Does | Developer Action |
|---|---|---|
| `00_START_HERE_FOR_DEVELOPER.md` | Main handoff and read order | Read first |
| `00_Master_Index/03_dataset-validation-result.md` | Confirms the 896-file package is complete and highlights known risks | Use as audit proof |
| `00_Master_Index/02_896-url-decision-and-migration-map.csv` | One row per GSC URL with action/migration notes | Use as the working implementation tracker |
| `00_Master_Index/05_896-sitemap-inclusion-audit.md` | Explains sitemap problem and rules | Implement sitemap logic from this |
| `00_Master_Index/05_896-sitemap-inclusion-audit.csv` | Per-URL sitemap found/missing status | Add only final canonical indexable URLs |
| `00_Master_Index/00_admit-card-master-implementation-spec.md` | Main technical/content spec | Build against this spec |
| `02_Content_Schema_FAQ/01_CONTENT_SCHEMA.md` | Required page sections | Update admit-card detail template |
| `02_Content_Schema_FAQ/03_FAQ_FRAMEWORK.md` | FAQ generation framework | Create 10-15 record-specific FAQs per indexable page |
| `04_AI_AEO_GEO_SEO_Ranking/01_ai-aeo-geo-seo-admit-cards.md` | AEO/GEO/LLM optimization rules | Add factual answer blocks and structured entity content |
| `03_QA_Checklists/01_admit-card-qa-checklist.md` | QA checklist before deployment | Test before GSC validation |
| `01_URL_Briefs_All_896/` | 896 separate URL briefs | Use for URL-by-URL review |

## Exact Implementation Steps

1. Export the live admit-card database/API records.
2. Match each GSC URL from `02_896-url-decision-and-migration-map.csv` to its actual admit-card record.
3. For every one of the 896 URLs, choose one final action: `INDEX`, `IMPROVE_FIRST`, `REDIRECT`, `CANONICALIZE`, `NOINDEX`, `404`, `410`, or `MANUAL_REVIEW`.
4. Do not mark a page `INDEX` until it has enough unique record-specific content.
5. For indexable pages, create or keep one final canonical URL.
6. Prefer meaningful semantic admit-card URLs when reliable exam/entity data exists.
7. Do not invent slugs from numeric IDs when record data is missing.
8. Resolve all slug collisions before redirects or sitemap updates.
9. If an old numeric URL is replaced, add a 301/308 redirect from old URL to final canonical URL.
10. Make final indexable pages return `200 OK`.
11. Make final indexable pages use `index,follow`.
12. Make final indexable pages self-canonical.
13. Update OG URL, Twitter URL, BreadcrumbList URL, structured data URL, and internal links to the final canonical URL.
14. Add only final canonical indexable URLs to the admit-card sitemap.
15. Remove redirected, noindex, duplicate, thin, invalid, non-200, canonicalized-away, and placeholder URLs from sitemap.
16. Add accurate `lastmod` from the admit-card updated date.
17. Update admit-card detail template content using the required schema.
18. Add 10-15 FAQs per indexable page, but make answers specific to the actual exam, authority, date, status, source, and download process.
19. Add related internal links only inside the admit-card experience: related admit cards, related results, related jobs, exam/category/state pages when relevant.
20. Validate sitemap XML and route behavior after deployment.
21. In Google Search Console, submit the updated sitemap.
22. Use URL Inspection on sample fixed URLs before pressing validation.
23. Request GSC validation only after live checks pass.

## Current Audit Numbers

- GSC URLs in scope: 896
- Unique URLs: 896
- URL briefs created: 896
- Decision rows created: 896
- Sitemap audit rows created: 896
- URLs found in existing saved sitemap exports: 141
- URLs not found in existing saved sitemap exports: 755
- Auto-derived slug collision warnings: 60
- URLs requiring live record/data lookup before final slug decision: 749

## What Not To Do

- Do not add all 896 numeric URLs directly to sitemap.
- Do not request indexing for thin pages.
- Do not publish copied/generic FAQ blocks across all pages.
- Do not redirect many unrelated pages to the admit-card hub.
- Do not canonicalize unique useful admit-card pages to `/admit-cards`.
- Do not remove old URLs without redirects when the page has a valid replacement.
- Do not add noindex, redirected, duplicate, invalid, expired-bad, or non-200 URLs to sitemap.
- Do not change navbar, footer, header, global layout, global styles, analytics, tracking, or unrelated pages.

## Final Developer Acceptance Test

The work is complete only when:

- All 896 URLs have a final decision.
- All indexable pages have substantial record-specific content.
- All indexable pages return `200 OK`, self-canonical, and `index,follow`.
- Sitemap contains only final canonical indexable URLs.
- Old numeric URLs redirect when a new canonical URL replaces them.
- Duplicate/thin/invalid URLs are improved, redirected, canonicalized, noindexed, 404, or 410 as appropriate.
- Structured data matches visible content.
- Internal links use final canonical URLs.
- GSC live URL Inspection passes on representative samples.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
