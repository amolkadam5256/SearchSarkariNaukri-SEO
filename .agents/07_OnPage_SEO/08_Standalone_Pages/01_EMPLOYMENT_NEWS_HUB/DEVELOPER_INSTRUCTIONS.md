# Developer instructions — Employment News hub

**Route:** `/employment-news`  
**Priority:** P1  
**Do not delete:** `/news`, `/job-updates`, or homepage job sections.

## What to build

1. New static+dynamic page using **existing** inner-page layout (same header/footer as `/results`).  
2. Register route in sitemap (`sitemap-static.xml` or dedicated child) when live.  
3. Add nav/footer link per `09_Developer_Implementation_Pack/02_NAV_AND_FOOTER_LINKS.md`.  
4. Paste copy from `PAGE_COPY.md` into CMS/template; wire `[DYNAMIC]` blocks to admin or manual “Employment News issue” records.

## Semantic structure

See `SEMANTIC_HTML_AND_SCHEMA.md`.

## Files in this folder

| File | Use |
|------|-----|
| `IMPLEMENTATION_SPEC.md` | Short spec (already exists) |
| `DEVELOPER_INSTRUCTIONS.md` | This file |
| `PAGE_COPY.md` | Human-written body copy |
| `SEMANTIC_HTML_AND_SCHEMA.md` | Tags + JSON-LD |
| `04_QA_CHECKLIST.md` | Pre-launch checks |

## Data (additive)

Optional table `employment_news_issues`:

- `title`, `issue_date_start`, `issue_date_end`, `volume`, `issue_number`, `official_url`, `updated_at`

Jobs tagged in EN issue: link from issue row to job IDs.

## Indexing

- `index, follow`, self-canonical `https://www.searchsarkarinaukri.com/employment-news`  
- Minimum ~450 words static copy + at least 1 official issue link before requesting GSC inspection.
