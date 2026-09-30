# Developer instructions — Answer Keys hub

**Route:** `/answer-keys`  
**Priority:** P1  

## Build

- New page; link from nav/footer (see pack `02_NAV_AND_FOOTER_LINKS.md`).  
- Dynamic table from exams/results module: columns in `PAGE_COPY.md`.  
- Cross-link every row to `/results` or exam page when available.  
- Do **not** remove or redirect existing result pages.

## Copy source

`PAGE_COPY.md` + `SEMANTIC_HTML_AND_SCHEMA.md`

## DB fields (additive)

On exam/result entities: `answer_key_status` (expected | provisional | final), `answer_key_url`, `objection_start`, `objection_end`.
