# START HERE - Final Developer Handoff

## Issue

Google Search Console reports `Discovered - currently not indexed` for 896 admit-card URLs.

This folder is now the final developer handoff for the admit-card indexing project.

## Scope Confirmation

- 896 URLs in GSC export.
- 896 unique URLs confirmed.
- 896 separate URL briefs generated.
- 896 URL decision rows generated.
- Older detailed briefs preserved for reference.

## Read In This Order

1. `README.md`
2. `00_Master_Index/03_dataset-validation-result.md`
3. `00_Master_Index/02_896-url-decision-and-migration-map.csv`
4. `00_Master_Index/05_896-sitemap-inclusion-audit.md`
5. `00_Master_Index/05_896-sitemap-inclusion-audit.csv`
6. `00_Master_Index/06_EXACT_DEVELOPER_ACTION_CHECKLIST.md`
7. `00_Master_Index/00_admit-card-master-implementation-spec.md`
8. `02_Content_Schema_FAQ/01_CONTENT_SCHEMA.md`
9. `02_Content_Schema_FAQ/03_FAQ_FRAMEWORK.md`
10. `04_AI_AEO_GEO_SEO_Ranking/01_ai-aeo-geo-seo-admit-cards.md`
11. `03_QA_Checklists/01_admit-card-qa-checklist.md`
12. `01_URL_Briefs_All_896/` for URL-by-URL work
13. `01_URL_Briefs/` and `06_Legacy_Working_Drafts/` only when deeper reference is needed

## Most Important Finding

The current public URLs are mostly numeric/generic, such as `/admit-cards/17`. For long-term SEO, AEO, and GEO, each valuable admit-card record should have one meaningful canonical URL based on actual exam/entity data.

However, do not invent slugs from numeric IDs. Many of the 896 rows only include URL and crawl date from GSC. For those, the migration map marks `NEEDS DATA REVIEW` until the developer pulls the actual admit-card record from the database/API.

## Safe Implementation Order

1. Export/read the full admit-card table from production data.
2. Join each GSC URL to its admit-card record by ID/slug.
3. Classify each record: index, improve, redirect/canonicalize, noindex archive, 404/410, or manual review.
4. Generate unique descriptive slugs from actual exam name, authority, stage, year, and intent.
5. Check slug collisions before changing routes.
6. Implement route support for descriptive admit-card URLs.
7. Add 301/308 redirects from old numeric URLs to new canonical URLs only after collision checks pass.
8. Update canonical, OG URL, Twitter URL, BreadcrumbList, structured data, internal links, and sitemap to the final canonical URL.
9. Strengthen every indexable page with record-specific sections and 10-15 record-specific FAQs.
10. Keep invalid/thin/duplicate pages out of the sitemap until fixed.
11. Run technical QA and GSC live tests before requesting validation.

## Do Not Do

- Do not blindly index all 896 URLs.
- Do not publish near-identical FAQ/content across 896 pages.
- Do not rename URLs without redirect and collision checks.
- Do not canonicalize unique admit cards to the hub page.
- Do not add invalid/thin/duplicate URLs to sitemap or llms.txt.
- Do not change footer, navbar, header, global layout, global styling, tracking, analytics, or unrelated pages unless strictly required.

## Final Acceptance Criteria

- 896 URLs in scope -> 896 URLs audited -> 896 URL decisions -> 896 content/SEO records checked -> implementation plan ready.
- Every kept indexable page has unique useful content, self canonical, correct sitemap inclusion, valid structured data, and contextual internal links.
- Every duplicate/invalid/thin page has a safe action: improve, redirect, canonicalize, noindex, 404, or 410.
- GSC validation is requested only after live checks pass.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
