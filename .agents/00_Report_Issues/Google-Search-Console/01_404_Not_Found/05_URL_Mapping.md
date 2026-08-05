# 05 - URL Mapping

**Project:** SearchSarkariNaukri.com

**Module:** URL Mapping for Google Search Console 404 URLs

**Priority:** 🔴 Critical

**Status:** ✅ Mapping Strategy Complete — Implementation Pending

---

# Purpose

This document defines the final mapping strategy for every URL reported under **Google Search Console → Page Indexing → Not Found (404)**.

Based on the completed URL Classification (03) and the Database Verification process (04), every URL group now has an assigned implementation action.

This document is the **master implementation reference** for developers.

---

# Reference File

Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

This file contains all **607 affected URLs**.

Every URL group has been mapped.

---

# Mapping Workflow

```
Google Search Console Report (607 URLs)

↓

URL Classification Complete

↓

Database Verification

↓

Determine Final URL

↓

Determine HTTP Response

↓

Assign Priority

↓

Developer Implementation
```

---

# Mapping Rules

## Action 1 — Redirect to Current Slug URL

Condition

- Job ID exists in the database
- Current slug is different from reported URL

Result

```
HTTP 301 Permanent Redirect
```

---

## Action 2 — Permanently Removed

Condition

- Job ID does not exist in the database
- No replacement exists
- No archive value

Result

```
HTTP 410 Gone
```

---

## Action 3 — Archive (Keep as Accessible Page)

Condition

- Job record exists but recruitment is expired
- Historical government recruitment page
- Has SEO value (org like SSC, UPSC, BARC, Railway, Bank)

Result

```
HTTP 200
```

---

## Action 4 — Redirect to Related Category/District/City Page

Condition

- City, District, or Category page removed
- A related parent page exists

Result

```
HTTP 301 Permanent Redirect
```

---

# Group-by-Group Mapping

## Group 1 — Category B: Legacy Numeric URLs (552 URLs)

**Format:** `/jobs/{id}`

**Implementation Strategy:**

```
For each numeric ID in the list:

  1. Query database: SELECT slug FROM jobs WHERE id = {id}

  2. If record found:
     → HTTP 301 redirect from /jobs/{id} to /jobs/{slug}-{id}

  3. If record NOT found:
     → HTTP 410 Gone

  4. If record exists but is an archived/expired recruitment:
     → HTTP 301 redirect to /jobs/{slug}-{id} which serves the archive page (HTTP 200)
```

**Implementation Method:**

This should be handled via a **catch-all route** in Next.js that:
1. Detects if the slug is purely numeric
2. Looks up the job ID in the database
3. Redirects to the SEO slug URL if found
4. Returns 410 if not found

This handles all 552 URLs with a single route handler instead of 552 individual redirect rules.

**Expected Outcome:**
- Most IDs → HTTP 301 → `/jobs/{current-slug}-{id}`
- Missing IDs → HTTP 410

**Priority:** 🔴 Critical (552 URLs = 90.9% of all 404s)

---

## Group 2 — Category C: Old SEO Slug URLs with ID (30 URLs)

**Format:** `/jobs/{old-slug}-{id}`

**Implementation Strategy:**

```
For each old slug URL:

  1. Extract numeric ID from end of slug

  2. Query database: SELECT slug FROM jobs WHERE id = {id}

  3. If current slug matches reported slug:
     → URL is correct but page is missing — investigate routing

  4. If current slug is DIFFERENT from reported slug:
     → HTTP 301 redirect from /jobs/{old-slug}-{id} to /jobs/{current-slug}-{id}

  5. If job ID not found in database:
     → HTTP 410 Gone
```

**Implementation Method:**

In the Next.js job detail page route handler, when the slug is provided:
1. Extract the ID from the end of the slug
2. Look up the job by ID
3. If the stored slug differs from the requested slug → redirect to canonical URL
4. If job doesn't exist → return 410

**This is standard canonical slug enforcement** and handles both current routing and these 30 old URLs.

**All 30 Affected URLs — Job IDs to verify:**

| URL | Job ID | Action |
|-----|--------|--------|
| /jobs/institute-of-banking-personnel-selectionibps-...-858 | 858 | Verify slug, redirect |
| /jobs/sports-authority-of-india-sai-assistant-...-863 | 863 | Verify slug, redirect |
| /jobs/sports-authority-of-india-sai-sai-internship-...-862 | 862 | Verify slug, redirect |
| /jobs/united-commercial-bank-uco-bank-scribe-...-253 | 253 | Verify slug, redirect |
| /jobs/edcil-india-limited-hiring-of-ai-advisor-2026-317 | 317 | Verify slug, redirect |
| /jobs/national-career-servicencs-...-839 | 839 | Verify slug, redirect |
| /jobs/united-commercial-bank-uco-bank-recruitment-...-276 | 276 | Verify slug, redirect |
| /jobs/staff-selection-commission-ssc-junior-engineer-...-860 | 860 | Verify slug, redirect |
| /jobs/united-commercial-bank-uco-bank-information-...-252 | 252 | Verify slug, redirect |
| /jobs/-aurangabad-cantonment-board-2026-895 | 895 | Verify slug, redirect |
| /jobs/nielit-delhi-centre-stqc-drivers-...-313 | 313 | Verify slug, redirect |
| /jobs/edcil-india-limited-hiring-of-ai-advisor-2026 | 2026 | ⚠️ Manual check (ID = year) |
| /jobs/bhabha-atomic-research-centre-barc-research-...-857 | 857 | Verify slug, redirect |
| /jobs/-currency-note-press-nashik-...-887 | 887 | Verify slug, redirect |
| /jobs/indian-railways-ir-gm-st-india-2026-18 | 18 | Verify slug, redirect |
| /jobs/unique-identification-authority-of-indiauidai-...-832 | 832 | Verify slug, redirect |
| /jobs/oil-and-natural-gas-corporation-limited-ongc-...-880 | 880 | Verify slug, redirect |
| /jobs/united-commercial-bank-uco-bank-advt-...-226 | 226 | Verify slug, redirect |
| /jobs/bhabha-atomic-research-centre-barc-ocesdgfs-...-854 | 854 | Verify slug, redirect |
| /jobs/indian-railways-ir-deputy-general-manager-...-25 | 25 | Verify slug, redirect |
| /jobs/sports-authority-of-india-sai-inviting-...-304 | 304 | Verify slug, redirect |
| /jobs/-staff-selection-commission-mts-all-india-2026-898 | 898 | Verify slug, redirect |
| /jobs/bhabha-atomic-research-centre-barc-stipendiary-...-855 | 855 | Verify slug, redirect |
| /jobs/maharashtra-public-service-commissionmpsc-...-847 | 847 | Verify slug, redirect |
| /jobs/bhabha-atomic-research-centre-barc-technical-...-856 | 856 | Verify slug, redirect |
| /jobs/unique-identification-authority-of-indiauidai-...-835 | 835 | Verify slug, redirect |
| /jobs/ntpc-limited-gdmo-medical-officer-...-875 | 875 | Verify slug, redirect |
| /jobs/united-commercial-bank-uco-bank-details-...-282 | 282 | Verify slug, redirect |
| /jobs/indian-railways-ir-general-manager-finance-...-16 | 16 | Verify slug, redirect |
| /jobs/indian-railways-ir-gm-te-ggm-te-india-2026-19 | 19 | Verify slug, redirect |

**Priority:** 🔴 Critical

---

## Group 3 — Category C: Truncated Slug URLs (9 URLs)

**Format:** `/jobs/{truncated-slug}` (no numeric ID)

**Implementation Strategy:**

```
For each truncated slug:

  1. Extract the truncated slug text
  2. Query database: SELECT id, slug FROM jobs WHERE slug LIKE '{truncated_slug}%'
  3. If match found → HTTP 301 redirect to /jobs/{full-slug}-{id}
  4. If no match → HTTP 410 Gone
```

**All 9 URLs — Prefix Lookup Required:**

| Truncated URL Slug | Prefix to Search | Action |
|---|---|---|
| `.../institute-of-banking-personnel-selectionibps-research-associate-facult` | `institute-of-banking-personnel-selectionibps` | Prefix search → redirect |
| `.../sports-authority-of-india-sai-sai-internship-program-head-office-regio` | `sports-authority-of-india-sai-sai-internship` | Prefix search → redirect |
| `.../united-commercial-bank-uco-bank-details-for-recruitment-of-1050-probat` | `united-commercial-bank-uco-bank-details-for-recruitment` | Prefix search → redirect |
| `.../united-commercial-bank-uco-bank-this-has-reference-to-our-earlier-recr` | `united-commercial-bank-uco-bank-this-has-reference` | Prefix search → redirect |
| `.../united-commercial-bank-uco-bank-scribe-declaration-for-recruitment-of-` | `united-commercial-bank-uco-bank-scribe-declaration` | Prefix search → redirect |
| `.../sports-authority-of-india-sai-inviting-application-for-appointment-for` | `sports-authority-of-india-sai-inviting-application` | Prefix search → redirect |
| `.../united-commercial-bank-uco-bank-information-handout-for-recruitment-of` | `united-commercial-bank-uco-bank-information-handout` | Prefix search → redirect |
| `.../united-commercial-bank-uco-bank-recruitment-of-probationary-officers-f` | `united-commercial-bank-uco-bank-recruitment-of-probationary` | Prefix search → redirect |
| `.../united-commercial-bank-uco-bank-advt-no-hohrmrecr2025-26com-03-engagem` | `united-commercial-bank-uco-bank-advt-no` | Prefix search → redirect |

**Priority:** 🟡 High

---

## Group 4 — Category G: District Pages (4 URLs)

**All Affected URLs:**

| URL | Action |
|-----|--------|
| `/districts/new-delhi` | Verify if district routing exists; redirect or 410 |
| `/districts/all-districts` | Likely removed — HTTP 410 |
| `/districts/kanpur-nagar` | Verify if district routing exists; redirect or 410 |
| `/districts/mumbai` | Verify if district routing exists; redirect or 410 |

**Implementation Strategy:**

```
Verify if /districts/{slug} routing exists in the application.

If routing exists → page should load (HTTP 200) — investigate why 404 occurs
If routing does NOT exist → HTTP 410

Note: /districts/all-districts is likely a removed listing page → HTTP 410
```

**Priority:** 🟡 High

---

## Group 5 — Category H: City / Location Pages (11 URLs)

**All Affected URLs:**

| URL | City | Action |
|-----|------|--------|
| `/jobs-in-new-delhi` | New Delhi | Verify routing or 410 |
| `/jobs-in-akola` | Akola | Verify routing or 410 |
| `/jobs-in-mumbai-suburban` | Mumbai Suburban | Verify routing or 410 |
| `/jobs-in-palghar` | Palghar | Verify routing or 410 |
| `/jobs-in-sangli` | Sangli | Verify routing or 410 |
| `/jobs-in-kolhapur` | Kolhapur | Verify routing or 410 |
| `/jobs-in-satara` | Satara | Verify routing or 410 |
| `/jobs-in-mumbai-city` | Mumbai City | Verify routing or 410 |
| `/jobs-in-kanpur-nagar` | Kanpur Nagar | Verify routing or 410 |
| `/jobs-in-solapur` | Solapur | Verify routing or 410 |
| `/jobs-in-chandrapur` | Chandrapur | Verify routing or 410 |

**Implementation Strategy:**

```
Verify if /jobs-in-{city} routing exists in the application.

If exists and city maps to an existing district → redirect to /districts/{slug}
If exists but city has no jobs → HTTP 410
If routing was completely removed → HTTP 410
```

**Priority:** 🟡 High

---

## Group 6 — Category E: Category Pages (1 URL)

| URL | Category | Action |
|-----|----------|--------|
| `/category/state-government-jobs` | State Government Jobs | Verify if category exists under /categories/ or another path |

**Implementation Strategy:**

```
Check if the State Government Jobs category exists.

If exists under /categories/state-government-jobs → HTTP 301 redirect
If category was removed → HTTP 410
```

**Priority:** 🟡 High

---

# Mapping Validation

Before implementation verify

- Target URL exists
- No duplicate mappings
- No redirect loops
- No redirect chains
- Only one final destination
- Correct HTTP status selected

---

# Recommended Implementation Approach

## For 552 Numeric URLs — Dynamic Handler (Most Efficient)

Instead of 552 redirect rules, implement ONE dynamic route handler:

```
Route: /jobs/[slug]

Handler logic:
  if slug is purely numeric (parseInt(slug) > 0):
    look up job by ID in database
    if job found: redirect 301 → /jobs/{job.slug}-{job.id}
    if job not found: return 410
```

## For 30 Old Slug URLs with ID — Canonical Enforcement

In the existing job detail page handler:

```
Extract ID from slug suffix
Look up job by ID
If job.slug !== requested slug: redirect 301 → /jobs/{job.slug}-{job.id}
If job not found: return 410
```

## For 9 Truncated Slug URLs — Prefix Route Handler

```
Route: /jobs/[slug]

Handler logic:
  if slug has no numeric suffix:
    search database WHERE slug LIKE '{slug}%'
    if unique match found: redirect 301 → /jobs/{job.slug}-{job.id}
    if no match: return 410
```

## For City, District, Category — Case-by-Case

Verify each individually and apply 301 or 410 as appropriate.

---

# Success Criteria

The mapping phase is complete when

- All **607 URLs** have been mapped.
- Every URL has one implementation action.
- No duplicate mappings exist.
- No URL is left undecided.
- The document is ready for implementation.

---

# Next Document

```
06_Redirect_Strategy.md
```

Purpose

This document defines how developers should implement:

- HTTP 301 Permanent Redirects
- HTTP 410 Gone responses
- Legacy URL handling
- Redirect priority
- Redirect validation

without changing the application's UI, existing content, business logic, or unrelated functionality.
