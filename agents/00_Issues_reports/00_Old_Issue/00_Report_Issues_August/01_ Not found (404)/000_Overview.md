# 000 — Overview

**Project:** SearchSarkariNaukri.com

**Module:** Google Search Console — Page Indexing — Not Found (404)

**Report Date:** August 17, 2026

**Priority:** 🔴 Critical

**Status:** Investigation & Active Fix Required

**Issue Type:** Technical SEO — HTTP 404 Errors

---

# Objective

Investigate and resolve all **613 URLs** reported under **Google Search Console → Page Indexing → Not Found (404)** as of August 17, 2026.

This documentation provides the complete audit, classification, live HTTP status testing, and implementation plan for resolving all affected URLs.

---

# Reference File

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-17.xlsx
```

**Location:**
```
.agents/00_Report_Issues_August/01_ Not found (404)/
```

**Sheet used:** `Table` (613 URLs + Last Crawled dates)

---

# 404 Growth Timeline (From Chart Sheet)

| Date Range | Affected Pages | Growth |
|------------|---------------|--------|
| May 22 – Jun 1, 2026 | 0 | — |
| Jun 2 – Jun 5, 2026 | 25 | +25 |
| Jun 6 – Jun 8, 2026 | 121 | +96 |
| Jun 9 – Jun 12, 2026 | 212 | +91 |
| Jun 13 – Jun 30, 2026 | 513 | +301 |
| Jul 1 – Jul 10, 2026 | 598 | +85 |
| Jul 11 – Jul 24, 2026 | 607 | +9 |
| Jul 25 – Aug 5, 2026 | 612 | +5 |
| Aug 6 – Aug 14, 2026 | **613** | +1 |

> ⚠️ **Critical:** 513 pages became 404 in a single jump between Jun 12–13. This indicates a **mass deletion or routing change** happened on or around June 12–13, 2026.

---

# Current Issue

Google Search Console has identified **613 URLs** returning HTTP 404 (Not Found).

These URLs are currently excluded from Google's index.

---

# URL Type Breakdown

Based on analysis of all 613 URLs:

| URL Type | Count (Est.) | Pattern |
|----------|-------------|---------|
| Numeric Job IDs (`/jobs/{id}`) | ~530 | `/jobs/1701`, `/jobs/983` |
| SEO Slug + ID (`/jobs/{slug-id}`) | ~55 | `/jobs/barc-ocesdgfs-2026-854` |
| Truncated Slugs (broken) | ~8 | `/jobs/united-commercial-bank-uco-bank-info...` |
| City Pages (`/jobs-in-{city}`) | ~10 | `/jobs-in-mumbai`, `/jobs-in-kolhapur` |
| District Pages (`/districts/{name}`) | ~4 | `/districts/new-delhi`, `/districts/mumbai` |
| Category Pages | 1 | `/category/state-government-jobs` |

---

# Expected Outcome

| Condition | Action |
|-----------|--------|
| Page exists (200) | No action needed — GSC to validate |
| URL changed (301) | Implement permanent redirect |
| Valuable historical job | Restore as archive page (200) |
| Permanently removed | Return HTTP 410 Gone |
| Truncated/broken slug | Fix slug generation or redirect to correct URL |
| City/District page missing | Restore route or redirect to category |

---

# Investigation Process

```
Google Search Console Export (613 URLs)
↓
Extract & Test All URLs (HTTP Status Check)
↓
Classify by URL Type & Status
↓
Verify Database Records (job IDs exist?)
↓
Determine Correct Action per URL
↓
Implement Fix (redirect / restore / 410)
↓
Test in Browser
↓
Validate in Google Search Console
```

---

# Related Documents (This Folder)

```
001_GSC_404_Report_Analysis.md     — Full URL list with analysis
002_URL_Live_Status_Test.md        — HTTP status of all 613 URLs (live test)
003_URL_Classification.md          — URLs grouped by type & recommended action
004_URL_Fix_Strategy.md            — Fix plan for each category
005_SEO_Audit_Full_Report.md       — Complete SEO audit per GSC prompt
006_Developer_Action_Items.md      — Dev handoff with code fixes
007_Testing_Checklist.md           — QA verification checklist
008_GSC_Validation_Process.md      — Steps to validate fixes in GSC
```

---

# Success Criteria

This phase is complete when:

- [ ] Every URL has been live HTTP tested
- [ ] Every URL has a documented action (200 / 301 / 410)
- [ ] Valid pages return HTTP 200
- [ ] Redirects return HTTP 301
- [ ] Permanently removed pages return HTTP 410
- [ ] Sitemap no longer references invalid URLs
- [ ] Internal links updated
- [ ] Google Search Console shows 0 URLs in "Not Found (404)"
