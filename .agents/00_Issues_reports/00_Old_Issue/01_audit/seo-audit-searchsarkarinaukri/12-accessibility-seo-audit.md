# 12 — Accessibility Items with SEO Impact

Output file: `outputs/final-reports/12-accessibility-seo-audit-REPORT.md`
Not a full WCAG audit — scoped to accessibility items that directly overlap
with SEO/crawlability/UX ranking signals.

## Checklist
- [ ] Color contrast checked on key text (WCAG AA minimum) — poor contrast
  correlates with poor UX signals
- [ ] All interactive elements (Save Job, Apply, filters) keyboard-navigable
- [ ] Form fields (search, filters) have associated `<label>` elements
- [ ] Semantic HTML used for navigation, lists, tables (not div-soup) — this
  also directly affects how crawlers/LLMs parse content structure
  (cross-ref file 08 section B)
- [ ] Skip-to-content link present
- [ ] Sufficient tap-target sizing on mobile (cross-ref file 01 section H)
- [ ] Alt text audit results referenced here too (cross-ref file 05 — alt text
  is both an accessibility and SEO requirement)
- [ ] Run Lighthouse Accessibility score (0–100) per template, list top issues
