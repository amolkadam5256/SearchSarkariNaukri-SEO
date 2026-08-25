# 00 — EXECUTIVE SUMMARY — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: 25 August 2026
Auditor: Codex + custom Googlebot crawler + Lighthouse 13.4.1 + read-only source/server/database review
Checklist source: .agents/00_Issues_reports/01_audit (files 01–14)
Total items checked: 238
Total Pass: 87 | Total Warning: 49 | Total Fail: 60 | Total N/A: 42

## Overall site health score

**0.0 / 100** using the required formula (Critical −10, High −5, Medium −2, Low −0.5 per Fail/Warning; raw deduction 255.5, score capped at 0). The formula is intentionally issue-count based and becomes severe on a 238-item audit; use the prioritized table below for sprint planning.

## Sitemap Reconciliation Headline

| Metric | Result |
|---|---:|
| Total sitemap URLs | 3,871 |
| Total indexed | N/A — authenticated GSC export unavailable |
| Linked 200 self-canonical URLs missing from sitemap | 482 |
| Parameter variants missing but canonicalized elsewhere | 451 |
| Broken/non-200 URLs in sitemap | 11 |
| Sitemap URLs with no discovered inlinks | 3,111 |

Full URL lists are in **../raw-crawl-data/**; file 03 explains why the broad 933 count is split into actionable self-canonical pages and canonicalized parameter variants.

## Top 10 Fixes Ranked by Impact-vs-Effort

| Rank | Fix | Audit area | Severity | Effort | Evidence / impact |
|---:|---|---|---|:---:|---|
| 1 | Remove expired JobPosting markup and stale sitemap entries | 04/03/01 | High | M | 2,782 live pages have expired validThrough; 11 410 jobs remain in sitemap. |
| 2 | Repair generated district/location links | 01/03 | High | M | 2,785 broken internal occurrences across 462 unique targets; 419 are 404 district paths. |
| 3 | Add missing self-canonical pages to sitemap | 03 | High | M | 482 linked 200 self-canonical URLs missing (418 location combinations, 50 news, 14 query hubs). |
| 4 | Compress and modernize editorial images | 05/06 | High | M | All 67 covers exceed 1.1 MB; median 2.66 MB; no WebP/AVIF/srcset/lazy. |
| 5 | Restore analytics for real users | 13 | High | M | GA4/GTM/Clarity/Ahrefs/AdSense appear in bot HTML, not ordinary browser traces. |
| 6 | Improve mobile LCP/JS execution | 06 | High | M | Homepage mobile score 42, LCP 8.54 s, TBT 714 ms; all mobile samples below 72. |
| 7 | Deduplicate result/admit records and metadata | 09/02 | High | M | Confirmed DB duplicates; 764 duplicate-title and 719 duplicate-description affected URLs. |
| 8 | Build internal paths to sitemap content | 01/02/03 | High | L | 3,111 sitemap URLs have zero discovered internal inlinks. |
| 9 | Normalize trailing slash, query and unknown-route behavior | 01 | Medium | S | /jobs and /jobs/ both 200; ordinary unknown route 200 while Googlebot receives 404. |
| 10 | Correct html lang and same-URL hreflang | 11/01 | Medium | S | Homepage mr-IN despite English dominance; en-IN/mr-IN/x-default point to the same URL. |

## AEO vs GEO current state

- **AEO current win: No verified win.** Logged-in India featured-snippet/AI Overview and GSC data were unavailable; the four exact public query checks did not surface the domain. Evidence: **../raw-crawl-data/public-search-baseline.md**.
- **GEO current citation: No verified major-tool citation.** This search-enabled audit session did not cite/surface the domain for the exact ChatGPT/MPSC prompt; independent Perplexity, Gemini, Copilot and Claude sessions were unavailable and are explicitly N/A.

## Cross-audit issue counts

| Severity | Fail/Warning items |
|---|---:|
| Critical | 0 |
| High | 15 |
| Medium | 89 |
| Low | 5 |

## Evidence scope and limitations

The audit includes a complete sitemap crawl/reconciliation, Googlebot and ordinary-browser raw HTML, official XSD validation, 8 Lighthouse runs, full schema/image/internal/external-link exports, a site-wide normalized-text near-duplicate scan, read-only code/server/database evidence, TLS/header tests and a public search baseline. Account-only GSC/Bing/Yandex/GA4/GTM/backlink/AI-tool data is never fabricated and is documented in **../raw-crawl-data/private-platform-data-limitations.md**.

**This report identifies issues only. No fixes have been applied. Remediation requires separate developer sign-off per item.**

The sentence above describes the original audit snapshot; the post-audit remediation status is recorded below.

## Post-audit developer remediation — 25 August 2026

Developer-controlled findings documented in this audit were subsequently fixed in the local application, deployed to production, and verified live. The original counts above intentionally remain unchanged as before-state evidence. See `../remediation/DEVELOPER-REMEDIATION-REPORT.md`, `../remediation/before-after-findings.csv`, and `../remediation/LIVE-VERIFICATION.md` for the remediation status and evidence.
