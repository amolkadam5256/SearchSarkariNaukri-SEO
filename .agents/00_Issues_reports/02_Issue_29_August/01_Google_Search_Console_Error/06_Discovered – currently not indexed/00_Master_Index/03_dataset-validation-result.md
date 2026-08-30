# Final Dataset Validation Result

| Check | Result | Evidence |
|---|---|---|
| Exactly 896 CSV rows | PASS | 896 |
| Exactly 896 unique source URLs | PASS | 896 |
| Exactly 896 markdown briefs in all-896 folder | PASS | 896 |
| Every CSV row maps to existing markdown brief | PASS | missing=0 |
| No duplicate source URLs | PASS | 0 |
| No duplicate all-896 filenames | PASS | 0 |
| Every all-896 brief has guardrail | PASS | checked=896 |
| All 896 URLs have decision rows | PASS | 896 |
| No recommended slug collisions for auto-derived local-evidence URLs | FAIL | 60 |
| Manual review used when page entity unavailable | PASS | 749 URLs require data lookup |

## Interpretation

The 896-row GSC dataset and 896 markdown brief set are complete. Some recommended semantic slugs cannot be safely generated from the GSC export alone because many rows only contain numeric URLs and crawl date. Those records are correctly marked `NEEDS DATA REVIEW` in the migration map. Do not invent slugs without the underlying admit-card record data.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for admit-card indexing/content architecture.
