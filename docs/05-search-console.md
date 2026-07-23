# 05 — Google Search Console Operations

## 5.1 Monitoring Areas & Thresholds

| Area | Frequency | Key Metrics Monitored | Action Threshold Trigger |
|------|-----------|------------------------|---------------------------|
| **Performance** | Daily | Clicks, Impressions, CTR, Avg Position | > 10% WoW click drop -> Immediate investigation |
| **Page Indexing** | Daily | Valid vs Excluded vs Error URLs | Any new 5xx/404 error -> Fix within 24 hours |
| **Crawl Stats** | Monthly | Total bot requests, average response time | TTFB > 500ms or 5xx spike -> Dev Ops alert |
| **Sitemaps** | Weekly | Sitemap process status across all 12 files | Any sitemap status != "Success" -> Fix XML |
| **Security & Manual Actions** | Weekly | Security alerts & manual action status | Any manual action -> Immediate P0 response |
| **Core Web Vitals** | Weekly | % URLs passing CrUX field data | < 90% pass rate -> Speed engineering |
| **Rich Results** | Weekly | JobPosting, FAQPage, Breadcrumb errors | Any schema error -> Fix template code |

---

## 5.2 Search Console Message Glossary & Triage Protocols

### 1. Indexing Messages Glossary

| GSC Message | Technical Meaning | Recommended Fix Protocol | Priority |
|-------------|-------------------|--------------------------|----------|
| **URL is Indexed** | Page is successfully indexed in Google Search | No action required. | Informational |
| **Crawled – currently not indexed** | Google visited but chose not to index (often thin content, duplicate, or weak internal links) | Improve content depth, add 3–5 internal links from high-authority hub pages, re-request indexing. | High |
| **Discovered – currently not indexed** | Google discovered the URL but hasn't crawled it yet (crawl budget or server bottleneck) | Improve TTFB response time, submit URL in XML sitemap index, strengthen internal link flow. | High |
| **Page with redirect** | URL redirects to another destination and is not indexed | Confirm redirect target is canonical and correct. | Medium |
| **Duplicate without user-selected canonical** | Google found duplicates and chose its own canonical | Add explicit self-referencing canonical tag matching internal links. | Medium |
| **Blocked by robots.txt** | Crawl disallowed by robots.txt directive | Update robots.txt if page should be indexed. | High |
| **Excluded by noindex tag** | Page has `noindex` tag present | Remove `noindex` tag if indexation is intended. | High |

### 2. Sitemap, Security & Server Messages Glossary

| GSC Message | Technical Meaning | Recommended Fix Protocol | Priority |
|-------------|-------------------|--------------------------|----------|
| **Sitemap could not be read** | XML syntax error or server timeout | Validate XML schema, verify server accessibility, resubmit. | High |
| **Security issues detected** | Malware, hacked injection, or deceptive content | Isolate compromised code, restore clean backup, request review. | Critical (P0) |
| **Manual action** | Human reviewer penalty for policy violation | Resolve violation, submit detailed reconsideration request. | Critical (P0) |
| **Server error (5xx)** | Origin server failed during bot crawl | Check server error logs, fix backend bottleneck, request validation. | Critical (P0) |

---

## 5.3 Priority Matrix & Fix SLAs

```
CRITICAL (Fix < 24 Hours):  Manual Actions | Security Issues | Server 5xx Errors
HIGH (Fix < 48 Hours):      Sitemap Errors | Crawled Not Indexed | robots.txt Blocks
MEDIUM (Fix < 7 Days):      Core Web Vitals | Mobile Usability | Schema Errors
LOW (Continuous):           Snippet Enhancements | CTR Optimization
```

---

## 5.4 Issue Tracking Template

| Date Found | Issue Type | Affected URLs Count | Root Cause | Fix Implemented | Date Fixed | GSC Validated? |
|------------|-----------|----------------------|------------|-----------------|------------|----------------|
| _(Date)_ | _(e.g., Soft 404)_ | _(e.g., 25 URLs)_ | _(Empty job filter)_ | _(Added dynamic noindex)_ | _(Date)_ | ☐ Yes |

---

## 5.5 Weekly Search Console Checklist

- [ ] Check Notifications panel for manual actions or security alerts.
- [ ] Review Page Indexing report for new coverage errors.
- [ ] Verify all 12 XML sitemaps show "Success" status.
- [ ] Identify high-impression, low-CTR keywords in positions 3–10 for title tag optimization.
- [ ] Inspect new URLs published in the last 7 days using URL Inspection tool.
