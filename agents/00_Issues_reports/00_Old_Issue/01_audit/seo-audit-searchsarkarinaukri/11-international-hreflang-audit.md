# 11 — International SEO / Bilingual (Marathi-English) Audit

Output file: `outputs/final-reports/11-international-hreflang-audit-REPORT.md`
The site mixes English and Marathi content on the same URLs and declares
`og:locale=mr_IN` with `og:locale:alternate=en_IN` — this section verifies
that's implemented correctly and consistently.

## A. Language Declaration
- [ ] `<html lang="...">` value checked site-wide — confirm it matches actual
  dominant page language (currently og:locale suggests Marathi-primary while
  visible content is majority English — resolve this discrepancy)
- [ ] Consistent `lang` attribute across all templates (not varying randomly)

## B. hreflang Implementation (if separate EN/MR URLs exist or are planned)
- [ ] Confirm whether the site serves Marathi and English as: (a) mixed content
  on the same URL (current apparent state — no hreflang needed, but then
  `og:locale:alternate` usage should be reviewed for accuracy), or (b) separate
  URLs per language (would require full hreflang implementation)
- [ ] If separate URLs exist anywhere in the site, verify: reciprocal hreflang
  tags, `x-default` tag present, hreflang values use correct ISO codes (mr-IN, en-IN)

## C. Content Parity
- [ ] Check that mixed bilingual content doesn't create a confusing UX/crawl
  signal — e.g., are Marathi phrases translations of the same info or
  supplementary? Document the actual content strategy observed.

## D. Regional Targeting
- [ ] Confirm Google Search Console international targeting settings (if any
  geo-targeting is set, confirm it's appropriate — site targets Maharashtra +
  broader India)
- [ ] Confirm district/city pages (`/jobs-in-pune`, `/districts/nashik`, etc.)
  have genuinely unique, location-specific content, not templated boilerplate
  with only the place name swapped (thin/duplicate content risk — cross-ref file 09)
