# SearchSarkariNaukri - Discovered Currently Not Indexed Admit Card Fix Package

Google Search Console issue: `Discovered - currently not indexed`.
Reported affected pages: 896.
Confirmed Excel export URL count: 896 unique URLs.
Primary template reviewed: `/admit-cards` and `/admit-cards/{id}` detail pages.
Latest package update: 29 August 2026.

## Professional Folder Format

- `00_Master_Index/` - master implementation prompt, generated URL indexes, and 896-generation summary.
- `01_URL_Briefs_All_896/` - complete set of 896 separate markdown briefs from the GSC export.
- `01_URL_Briefs/` - older/detail briefs preserved for reference.
- `02_Content_Schema_FAQ/` - content schema, sample page, and FAQ framework.
- `03_QA_Checklists/` - technical SEO, GSC, sitemap, schema, and content QA.
- `04_AI_AEO_GEO_SEO_Ranking/` - AI, LLM, AEO, GEO, and SEO ranking requirements.
- `05_Source_Evidence/` - supplied page text and source evidence.

## Core Strategy

Do not blindly index all 896 URLs. Classify first:

- Active + useful + unique: improve and index.
- Historical but useful: usually index if substantial and accurate.
- Duplicate records: consolidate, canonicalize, or redirect.
- Thin records: improve first.
- Invalid/dead records: 404/410.
- Wrong year/title/source records: fix source data and URL strategy.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for admit-card indexing/content architecture. Strengthen existing page sections and internal links without redesigning unrelated site areas.
