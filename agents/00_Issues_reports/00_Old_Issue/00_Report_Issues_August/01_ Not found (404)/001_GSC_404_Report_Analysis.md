# 001 — GSC 404 Report Analysis

**Source:** Google Search Console → Page Indexing → Not Found (404)

**Export Date:** August 17, 2026

**Total URLs:** 613

**Website:** https://www.searchsarkarinaukri.com

---

# Analysis Summary

## URL Pattern Distribution

### Group A — Numeric Job IDs
Format: `/jobs/{number}`

These are direct numeric database IDs. The URL works if the job record exists in the database and the route `/jobs/[id]` is active.

Examples:
- `https://www.searchsarkarinaukri.com/jobs/1701`
- `https://www.searchsarkarinaukri.com/jobs/983`
- `https://www.searchsarkarinaukri.com/jobs/14`
- `https://www.searchsarkarinaukri.com/jobs/29`

**Root Cause Hypothesis:** These job IDs either:
1. Were deleted from the database
2. Have a status change (unpublished/archived) that returns 404
3. The route `/jobs/[id]` is returning 404 for non-existent IDs instead of a proper response

---

### Group B — SEO-Friendly Slugs with ID
Format: `/jobs/{full-descriptive-slug-{id}}`

These are SEO-optimized URLs that include the full job title as slug + numeric ID at end.

Examples:
- `https://www.searchsarkarinaukri.com/jobs/indian-railways-ir-gm-electrical-at-corporate-office-new-delhi-on-deputation-bas-110`
- `https://www.searchsarkarinaukri.com/jobs/bhabha-atomic-research-centre-barc-ocesdgfs-2026-scientific-officer-c-mumbai-kal-854`
- `https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-assistant-director-deputation-basis-all-india-2026-863`
- `https://www.searchsarkarinaukri.com/jobs/maharashtra-public-service-commissionmpsc-motor-vehicle-prosecutor-regional-tran-847`

**Root Cause Hypothesis:** These SEO slugs worked previously. Possible causes:
1. Slug generation logic changed — new slugs don't match stored slugs
2. Job records deleted
3. Routing not matching slug format

---

### Group C — Truncated / Broken Slugs (No Trailing ID)
Format: `/jobs/{truncated-slug-without-id}`

These slugs are **cut off** — they have no numeric ID at the end and appear to be truncated at a URL length limit.

Examples:
- `https://www.searchsarkarinaukri.com/jobs/institute-of-banking-personnel-selectionibps-research-associate-facult`
- `https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-`
- `https://www.searchsarkarinaukri.com/jobs/sports-authority-of-india-sai-inviting-application-for-appointment-for`
- `https://www.searchsarkarinaukri.com/jobs/edcil-india-limited-hiring-of-ai-advisor-2026`
- `https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-information-handout-for-recruitment-of`
- `https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-recruitment-of-probationary-officers-f`
- `https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-this-has-reference-to-our-earlier-recr`
- `https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagem`
- `https://www.searchsarkarinaukri.com/jobs/united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probat`

**Root Cause:** URL was truncated before the numeric ID. These are **permanently broken slugs** that were likely crawled by Google from sitemap or internal links with truncated hrefs.

**Action Required:** Implement 301 redirect from truncated slug → correct full slug URL.

---

### Group D — City Pages
Format: `/jobs-in-{city-name}`

404 city location pages found:
- `https://www.searchsarkarinaukri.com/jobs-in-new-delhi`
- `https://www.searchsarkarinaukri.com/jobs-in-akola`
- `https://www.searchsarkarinaukri.com/jobs-in-mumbai-suburban`
- `https://www.searchsarkarinaukri.com/jobs-in-palghar`
- `https://www.searchsarkarinaukri.com/jobs-in-kanpur-nagar`
- `https://www.searchsarkarinaukri.com/jobs-in-mumbai-city`
- `https://www.searchsarkarinaukri.com/jobs-in-sangli`
- `https://www.searchsarkarinaukri.com/jobs-in-kolhapur`
- `https://www.searchsarkarinaukri.com/jobs-in-satara`
- `https://www.searchsarkarinaukri.com/jobs-in-solapur`
- `https://www.searchsarkarinaukri.com/jobs-in-chandrapur`

**Root Cause:** City/location pages either:
1. Route `/jobs-in-[city]` was removed from Next.js routing
2. Dynamic route not handling these city slugs

---

### Group E — District Pages
Format: `/districts/{district-name}`

404 district pages found:
- `https://www.searchsarkarinaukri.com/districts/new-delhi`
- `https://www.searchsarkarinaukri.com/districts/all-districts`
- `https://www.searchsarkarinaukri.com/districts/kanpur-nagar`
- `https://www.searchsarkarinaukri.com/districts/mumbai`

**Root Cause:** `/districts/` route removed or not implemented.

---

### Group F — Category Pages
- `https://www.searchsarkarinaukri.com/category/state-government-jobs`

**Root Cause:** `/category/[slug]` route not implemented or category deleted.

---

# Duplicate URL Pairs (Potential Issues)

The export contains **paired URLs** — both the numeric ID and the full SEO slug for the same job:

| Numeric URL | SEO Slug URL |
|-------------|-------------|
| `/jobs/110` | `/jobs/indian-railways-ir-gm-electrical-...-110` |
| `/jobs/858` | `/jobs/institute-of-banking-personnel-...-858` |
| `/jobs/835` | `/jobs/unique-identification-authority-...-835` |
| `/jobs/875` | `/jobs/ntpc-limited-gdmo-medical-officer-...-875` |
| `/jobs/863` | `/jobs/sports-authority-of-india-sai-assistant-...-863` |
| `/jobs/854` | `/jobs/bhabha-atomic-research-centre-barc-ocesdgfs-...-854` |
| `/jobs/855` | `/jobs/bhabha-atomic-research-centre-barc-stipendiary-...-855` |
| `/jobs/856` | `/jobs/bhabha-atomic-research-centre-barc-technical-...-856` |
| `/jobs/857` | `/jobs/bhabha-atomic-research-centre-barc-research-...-857` |
| `/jobs/847` | `/jobs/maharashtra-public-service-commission...-847` |
| `/jobs/832` | `/jobs/unique-identification-authority-...-832` |
| `/jobs/839` | `/jobs/national-career-service...-839` |
| `/jobs/880` | `/jobs/oil-and-natural-gas-corporation-...-880` |
| `/jobs/895` | `/jobs/-aurangabad-cantonment-board-...-895` |
| `/jobs/898` | `/jobs/-staff-selection-commission-mts-...-898` |
| `/jobs/860` | `/jobs/staff-selection-commission-ssc-junior-...-860` |

**Action:** For each pair — decide which URL is canonical. The SEO slug should be canonical, and the numeric URL should 301 redirect to the slug.

---

# Key Findings

1. **Mass 404 spike on June 12–13, 2026** — 301 pages went 404 overnight. A deployment or database change caused this.

2. **Both numeric and slug URLs for same job are 404** — the underlying job records may have been deleted/unpublished.

3. **Truncated slugs** — evidence of a URL generation bug where slugs were truncated before the numeric ID suffix.

4. **City & District pages route missing** — entire route segments (`/jobs-in-*` and `/districts/*`) are returning 404.

5. **Category route missing** — `/category/state-government-jobs` not found.

---

# Next Steps

→ See `002_URL_Live_Status_Test.md` for live HTTP status results for all 613 URLs.

→ See `003_URL_Classification.md` for per-URL action plan.
