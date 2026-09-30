# Section 63 - Urgent Alerts & Employment News Strip

**Competitor:** MSN “Urgent Alerts” ticker (Employment News issues + RRB JE 4098, SSC CHSL 2536…)  
**Related existing:** `07_CLOSING_SOON_JOBS/`, `57_JOB_NEWS/`  
**Priority:** P2  

## Purpose

Surface time-sensitive national recruitments + Employment News without duplicating full job list.

## Content mix (max 8–10 items)

1. Latest **Employment News** issue → `/employment-news` (see `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/`)  
2. Top 5–7 jobs by **vacancy count** OR flagged `urgent=true` in CMS  
3. Link “View all urgent jobs →” → `/jobs?sort=closing_soon` only if canonical policy allows; prefer `/jobs` + closing-soon section  

## Display fields

- Title (truncated), last date, optional “Closing Soon” badge  
- Link to job detail — **verify slug matches job ID (P0 technical fix)**

## Do not

- Remove Ending Soon section — this strip sits **above** or **beside** it as additive urgency layer.
