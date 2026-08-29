# Regeneration Instruction For All 136 URL Briefs

Date: 2026-08-29
Issue: Crawled - currently not indexed

## Current Situation

GSC reports 136 affected URLs. Only 16 real page URLs were available in the pasted visible evidence. The remaining 120 actual URLs must be exported from Google Search Console before full per-URL markdown generation can be completed.

## Required Input File

Create this file:

`00_Master_Index/full-136-crawled-currently-not-indexed-export.csv`

Columns:

- URL
- Last crawled

## Generation Requirement

After the full CSV exists:

1. Delete/regenerate only files inside `01_URL_Briefs_All/` for this issue folder.
2. Create exactly 136 markdown files, one per real URL.
3. Regenerate `00_Master_Index/crawled-currently-not-indexed-url-index.csv` with exactly 136 rows.
4. Each brief must include technical SEO tests, content section recommendations, FAQ requirements, sitemap/canonical checks, page speed checks, and final action.
5. Do not create placeholder markdown files without real URLs.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue.
