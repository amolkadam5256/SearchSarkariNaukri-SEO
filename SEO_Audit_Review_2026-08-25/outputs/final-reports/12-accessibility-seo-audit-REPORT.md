# 12 — Accessibility Items with SEO Impact — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: 25 August 2026
Auditor: Codex + custom Googlebot crawler + Lighthouse 13.4.1 + read-only source/server/database review
Checklist source: 12-accessibility-seo-audit.md
Total items checked: 8
Total Pass: 3 | Total Warning: 1 | Total Fail: 4 | Total N/A: 0

| # | Checklist Item | Status | Evidence | Affected URL(s) | Severity | Recommended Fix | Effort (S/M/L) |
|---:|---|---|---|---|---|---|:---:|
| 1 | Color contrast checked on key text (WCAG AA minimum) — poor contrast correlates with poor UX signals | ❌ Fail | All eight Lighthouse reports fail color contrast; accessibility scores range 79–85. | site-wide | Medium | Update failing color pairs to WCAG AA and rerun Lighthouse/axe on all four templates. | M |
| 2 | All interactive elements (Save Job, Apply, filters) keyboard-navigable | ⚠️ Warning | Native buttons/links exist for core actions, but no complete keyboard-only journey was automated; rendered mobile overlay and unnamed links require manual keyboard validation. | site-wide | Medium | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 3 | Form fields (search, filters) have associated `<label>` elements | ✅ Pass | Lighthouse label audit passes applicable forms on home/job/category; qualification sample has no applicable form. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 4 | Semantic HTML used for navigation, lists, tables (not div-soup) — this also directly affects how crawlers/LLMs parse content structure (cross-ref file 08 section B) | ✅ Pass | Source and prerender HTML use nav/main/sections/lists/tables and semantic headings; Breadcrumb/ItemList schemas support structure. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 5 | Skip-to-content link present | ❌ Fail | Source search found no skip-to-content link in MainLayout/App/Navbar. | site-wide | Medium | Add a first-focusable skip link targeting the main landmark on every public template. | S |
| 6 | Sufficient tap-target sizing on mobile (cross-ref file 01 section H) | ❌ Fail | All four mobile Lighthouse runs fail target-size. | site-wide | Medium | Increase interactive targets to at least 44×44 CSS px with adequate spacing and rerun mobile Lighthouse. | M |
| 7 | Alt text audit results referenced here too (cross-ref file 05 — alt text is both an accessibility and SEO requirement) | ✅ Pass | Image audit: 0 missing/empty alt among 67 Googlebot-visible images; Navbar logo alt is SearchSarkariNaukri. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 8 | Run Lighthouse Accessibility score (0–100) per template, list top issues | ❌ Fail | Accessibility mobile/desktop: home 85/81, job 85/80, category 83/79, qualification 84/79. Repeated failures: contrast, unnamed links, touch targets. | site-wide | Medium | Fix the recorded contrast, unnamed-link and touch-target failures per template and require Lighthouse accessibility ≥90 before release. | M |

## Summary
- Critical issues: 0 — none
- High issues: 0 — none
- Medium issues: 5 — 1, 2, 5, 6, 8
- Low issues: 0 — none
- Top 3 priority fixes for this audit area:
  1. Item 5: Add a first-focusable skip link targeting the main landmark on every public template.
  2. Item 1: Update failing color pairs to WCAG AA and rerun Lighthouse/axe on all four templates.
  3. Item 2: Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles.
