# 002 — URL Live HTTP Status Test Results

**Test Date:** August 17, 2026

**Test Time:** 22:43 IST (17:13 UTC)

**Total URLs Tested:** 613

**Source:** `https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-17.xlsx` → Sheet: `Table`

**Test Method:** PowerShell `Invoke-WebRequest` with 5-redirect follow and 15-second timeout

---

# 🚨 CRITICAL FINDING

> **609 out of 613 URLs are NOW returning HTTP 200 (Working)**
>
> These URLs were reported as 404 in Google Search Console — but they are LIVE and returning 200 today.
>
> This means the underlying issue has been PARTIALLY FIXED on the website, BUT Google Search Console still shows them as 404 because **Google has not re-crawled these pages yet.**
>
> **The fix is NOT complete until Google validates and removes these from the GSC 404 report.**

---

# Live Test Summary

| HTTP Status | Count | Percentage | Meaning |
|-------------|-------|------------|---------|
| **200 OK** | **609** | **99.3%** | ✅ Page works now — needs GSC re-crawl to clear |
| **410 Gone** | **4** | **0.7%** | ✅ Correctly marked as permanently removed |
| **404 Not Found** | 0 | 0% | — |
| **301/302 Redirect** | 0 | 0% | — |
| **Connection Error** | 0 | 0% | — |

---

# HTTP 410 URLs (Permanently Gone — Correct)

These 4 URLs are correctly returning **HTTP 410 Gone**, which is the proper response for permanently deleted pages.

| # | URL | HTTP Status | SEO Action |
|---|-----|------------|-----------|
| 274 | `https://www.searchsarkarinaukri.com/jobs-in-new-delhi` | 410 | ✅ Correct — remove from sitemap |
| 338 | `https://www.searchsarkarinaukri.com/districts/new-delhi` | 410 | ✅ Correct — remove from sitemap |
| 375 | `https://www.searchsarkarinaukri.com/districts/kanpur-nagar` | 410 | ✅ Correct — remove from sitemap |
| 376 | `https://www.searchsarkarinaukri.com/jobs-in-kanpur-nagar` | 410 | ✅ Correct — remove from sitemap |

> **Note:** HTTP 410 is better than 404 for permanently gone pages. Google will de-index these faster with 410 than 404. These are correctly handled.

---

# HTTP 200 URLs — Critical Observation

All 609 URLs returning 200 include:

### ✅ All Numeric Job IDs are working:
- `/jobs/1701` → 200
- `/jobs/983` → 200
- `/jobs/14` → 200
- `/jobs/29` → 200
- All `/jobs/{number}` → 200

### ✅ All SEO Slug URLs are working:
- `/jobs/indian-railways-ir-gm-electrical-...-110` → 200
- `/jobs/bhabha-atomic-research-centre-barc-...-854` → 200
- All `/jobs/{slug-id}` → 200

### ✅ Truncated Slug URLs are working:
- `/jobs/institute-of-banking-personnel-selectionibps-research-associate-facult` → 200
- `/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-` → 200
- All truncated slugs → 200

### ✅ City/Location Pages are working:
- `/jobs-in-akola` → 200
- `/jobs-in-mumbai-suburban` → 200
- `/jobs-in-palghar` → 200
- `/jobs-in-mumbai-city` → 200
- `/jobs-in-sangli` → 200
- `/jobs-in-kolhapur` → 200
- `/jobs-in-satara` → 200
- `/jobs-in-solapur` → 200
- `/jobs-in-chandrapur` → 200

### ✅ District Pages are working:
- `/districts/all-districts` → 200
- `/districts/mumbai` → 200

### ✅ Category Pages are working:
- `/category/state-government-jobs` → 200

---

# What This Means for SEO

## The Problem

Even though pages now return 200, Google Search Console still shows them as 404 because:

1. Google crawled these pages **when they were 404**
2. Google's index has **cached the 404 status**
3. Google needs to **re-crawl** each page to discover they are now 200
4. GSC will only clear these from the "Not Found (404)" report after successful re-crawl

## The Risk

Until Google re-crawls and validates these pages:
- **613 pages are excluded from Google's index**
- These pages cannot rank in search results
- Traffic is being lost for all these job URLs

---

# Action Required

## Immediate Actions

### 1. Request Re-indexing via GSC URL Inspection
For the most critical/high-traffic pages, use GSC → URL Inspection → Request Indexing.
(Limit: ~10-15 requests per day manually)

### 2. Submit Updated Sitemap
- Ensure all 609 working URLs are in the XML sitemap
- Remove the 4 URLs returning 410
- Submit the updated sitemap in GSC

### 3. Internal Linking
- Ensure every working URL has internal links pointing to it
- This helps Googlebot discover and crawl them faster

### 4. GSC Validation Button
- In GSC → Coverage → Not Found (404) → Click "Validate Fix"
- This triggers Google to re-crawl affected pages

---

# Soft 404 Risk

> ⚠️ **IMPORTANT:** Even though we get HTTP 200, the pages may be **Soft 404s**.
>
> A Soft 404 occurs when a page returns HTTP 200 but the content says "page not found" or shows empty/no content.
>
> **This must be verified by checking the actual rendered content of each page.**

Suspected Soft 404 candidates:
- Truncated slug URLs (broken slugs may show "Job Not Found" with 200)
- Very low job IDs (e.g., `/jobs/14`, `/jobs/18`, `/jobs/19`) — may be old/empty records
- `/category/state-government-jobs` — may show 200 but with no jobs listed

---

# Summary

| Finding | Count | Action |
|---------|-------|--------|
| Currently working (200) | 609 | Submit sitemap, request GSC validation |
| Correctly gone (410) | 4 | Remove from sitemap, remove internal links |
| Still 404 | 0 | N/A |
| Potential Soft 404 | TBD | Manual content verification needed |

→ See `003_URL_Classification.md` for per-category action plan.

→ See `006_Developer_Action_Items.md` for technical implementation.
