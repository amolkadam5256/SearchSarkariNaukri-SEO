# State Government Jobs Directory

**Competitor reference:** MSN “State Jobs” + “All 36 States & UTs” + state filter  
**Existing specs:** `01_Home_Page/21_STATE_JOBS/`, `43_ALL_INDIA_STATE_SEO/`  
**Priority:** P1  

## Route

- **Canonical:** `https://www.searchsarkarinaukri.com/state-government-jobs`

## Purpose

National visibility page listing **all states/UTs** with active job counts and links to `/jobs-in-[state]` or `/state/[slug]` (use whichever routes already exist — **no new slug scheme if current works**).

## Sections

1. H1: State Wise Sarkari Naukri 2026 — Government Jobs by State  
2. Intro paragraph (all-India + Maharashtra highlight without neglecting other states)  
3. **Grid:** 28 states + 8 UTs — name, optional live count, link to state hub  
4. Featured states row: UP, Bihar, MP, Maharashtra, Rajasthan, WB, TN, Karnataka, Gujarat, Punjab, Haryana, Kerala, Odisha, Assam, Jharkhand, CG, Telangana, AP, Delhi  
5. Central vs state explanation (UPSC/SSC vs PSC) — link `/department/mpsc`, `/department/upsc`  
6. FAQ: How to find state PSC jobs?  
7. BreadcrumbList + CollectionPage schema  

## Homepage integration

- **UPDATE** `21_STATE_JOBS/SECTION_SPEC.md` — add prominent link “View all states →” to this directory.  
- **UPDATE** `43_ALL_INDIA_STATE_SEO/` — same target URL for consistency.

## Indexation

- Index when each linked state hub returns 200 with ≥1 job or ≥150 words unique intro.  
- `noindex,follow` state rows that are empty until content added — **do not delete** state URLs.
