# 11 — International SEO / Bilingual (Marathi-English) Audit — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: 25 August 2026
Auditor: Codex + custom Googlebot crawler + Lighthouse 13.4.1 + read-only source/server/database review
Checklist source: 11-international-hreflang-audit.md
Total items checked: 7
Total Pass: 0 | Total Warning: 1 | Total Fail: 4 | Total N/A: 2

| # | Checklist Item | Status | Evidence | Affected URL(s) | Severity | Recommended Fix | Effort (S/M/L) |
|---:|---|---|---|---|---|---|:---:|
| 1 | `<html lang="...">` value checked site-wide — confirm it matches actual dominant page language (currently og:locale suggests Marathi-primary while visible content is majority English — resolve this discrepancy) | ❌ Fail | `url-audit-all.csv`: 3,141 200 pages en-IN and 1,679 mr-IN; homepage is mr-IN although title/H1/body are predominantly English. | site-wide | Medium | For mixed same-URL content, use the actual dominant html lang and remove same-URL en/mr alternates; add reciprocal hreflang only if distinct translations are launched. | S |
| 2 | Consistent `lang` attribute across all templates (not varying randomly) | ❌ Fail | Language value changes by backend template/data group rather than a user-visible language-specific URL strategy. | site-wide | Medium | Derive html lang from the actual dominant page language, use it consistently per canonical URL, and regression-test every backend template. | M |
| 3 | Confirm whether the site serves Marathi and English as: (a) mixed content on the same URL (current apparent state — no hreflang needed, but then `og:locale:alternate` usage should be reviewed for accuracy), or (b) separate URLs per language (would require full hreflang implementation) | ❌ Fail | Same URLs carry mixed content and declare en-IN + mr-IN + x-default alternates to themselves; no separate translation URLs. | site-wide | Medium | For mixed same-URL content, use the actual dominant html lang and remove same-URL en/mr alternates; add reciprocal hreflang only if distinct translations are launched. | L |
| 4 | If separate URLs exist anywhere in the site, verify: reciprocal hreflang tags, `x-default` tag present, hreflang values use correct ISO codes (mr-IN, en-IN) | N/A | No separate EN/MR URL pairs exist; reciprocal alternate validation is therefore not applicable. Existing same-URL alternates should be removed/reworked. | N/A | Info | Provide read-only authenticated access/export from the named platform, rerun this exact check, and attach the dated export. | S |
| 5 | Check that mixed bilingual content doesn't create a confusing UX/crawl signal — e.g., are Marathi phrases translations of the same info or supplementary? Document the actual content strategy observed. | ⚠️ Warning | Mixed English/Marathi copy is supplementary in many pages but the mismatched html lang/OG locale creates a confusing machine signal. | site-wide | Medium | Have a qualified Marathi/English editor review a representative sample, record issues, and enforce editorial QA before publishing. | M |
| 6 | Confirm Google Search Console international targeting settings (if any geo-targeting is set, confirm it's appropriate — site targets Maharashtra + broader India) | N/A | Authenticated GSC regional/international targeting settings unavailable. | N/A | Info | Provide read-only authenticated access/export from the named platform, rerun this exact check, and attach the dated export. | S |
| 7 | Confirm district/city pages (`/jobs-in-pune`, `/districts/nashik`, etc.) have genuinely unique, location-specific content, not templated boilerplate with only the place name swapped (thin/duplicate content risk — cross-ref file 09) | ❌ Fail | 418 self-canonical district/category combination URLs are linked but absent from sitemap; many location pages are templated, and 419 free-text district links return 404. | site-wide | Medium | Deduplicate source rows/content, assign one primary intent per URL, redirect or canonicalize true duplicates, then regenerate titles/meta/sitemaps. | M |

## Summary
- Critical issues: 0 — none
- High issues: 0 — none
- Medium issues: 5 — 1, 2, 3, 5, 7
- Low issues: 0 — none
- Top 3 priority fixes for this audit area:
  1. Item 1: For mixed same-URL content, use the actual dominant html lang and remove same-URL en/mr alternates; add reciprocal hreflang only if distinct translations are launched.
  2. Item 2: Derive html lang from the actual dominant page language, use it consistently per canonical URL, and regression-test every backend template.
  3. Item 5: Have a qualified Marathi/English editor review a representative sample, record issues, and enforce editorial QA before publishing.
