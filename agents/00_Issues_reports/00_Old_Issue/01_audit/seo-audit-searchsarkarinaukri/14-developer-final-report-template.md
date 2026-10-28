# 14 — Developer Final Report Template
### Every output report file (`outputs/final-reports/XX-topic-REPORT.md`) MUST follow this exact structure.

---

## File header (top of every report file)

```
# [Number] — [Topic Name] — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: [date executed]
Auditor: [name/tool]
Checklist source: [XX-topic-name.md]
Total items checked: [n]
Total Pass: [n] | Total Warning: [n] | Total Fail: [n] | Total N/A: [n]
```

## Finding table (one row per checklist item — mandatory columns)

| # | Checklist Item | Status | Evidence | Affected URL(s) | Severity | Recommended Fix | Effort (S/M/L) |
|---|---|---|---|---|---|---|---|
| 1 | (copy exact item text from checklist file) | ✅ Pass / ⚠️ Warning / ❌ Fail / N/A | (screenshot filename, tool output, or exact code snippet) | (specific URL, "site-wide", or "N/A") | Critical / High / Medium / Low / Info | (specific, actionable instruction — not vague) | S / M / L |

### Status definitions
- **✅ Pass** — meets best practice, no action needed
- **⚠️ Warning** — works but suboptimal, should be improved
- **❌ Fail** — broken, missing, or actively harming SEO/AEO/GEO performance
- **N/A** — not applicable, MUST include a one-line reason

### Severity definitions
- **Critical** — actively blocking indexing/rankings or causing ranking loss (e.g. noindex on money pages, broken canonical, site-wide duplicate titles)
- **High** — significant lost opportunity or trust issue (e.g. missing JobPosting schema, expired dates left live, duplicate homepage content bug)
- **Medium** — meaningful but contained improvement (e.g. single-template thin content, missing alt text on a subset of images)
- **Low** — minor polish (e.g. title 2 characters over ideal length)
- **Info** — observation, no fix required, useful context

## End-of-file summary block (bottom of every report file)

```
## Summary
- Critical issues: [n] — [one-line list of the item numbers]
- High issues: [n]
- Medium issues: [n]
- Low issues: [n]
- Top 3 priority fixes for this audit area:
  1. ...
  2. ...
  3. ...
```

## Executive Summary file (`00-EXECUTIVE-SUMMARY-REPORT.md`) additional required sections

1. **Overall site health score** — simple weighted score out of 100 based on
   Critical=-10, High=-5, Medium=-2, Low=-0.5 per issue, capped at 0.
2. **Sitemap Reconciliation Headline** (pulled straight from file 03 report):
   total sitemap URLs / total indexed / total missing from sitemap / total
   broken in sitemap.
3. **Top 10 Fixes Ranked by Impact-vs-Effort** — a single prioritized table
   across ALL audit areas (technical, on-page, AEO, GEO, etc.) combined,
   sorted by (Severity × ease of fix), for the developer's next sprint.
4. **AEO vs GEO current-state one-liner** — is the site currently winning any
   featured snippets/AI Overviews (file 07)? Is it currently cited by any
   major AI chat tool (file 08)? Two direct yes/no + evidence answers.
5. **Explicit statement**: "This report identifies issues only. No fixes have
   been applied. Remediation requires separate developer sign-off per item."
