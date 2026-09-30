# Developer instructions — State government jobs directory

**Route:** `/state-government-jobs`  
**Priority:** P1  

## Links to existing work

- Homepage sections: `21_STATE_JOBS`, `43_ALL_INDIA_STATE_SEO` — add CTA “All states →” pointing here.  
- District work: `05_districts_Job_Page/` — state pages must link down to districts where they exist.

## Build

- Grid of states/UTs with `[DYNAMIC: job_count]` per state if API supports it; else show state name only.  
- Use `PAGE_COPY.md` intro + FAQ.  
- Each state links to existing slug (`/jobs-in-maharashtra`, etc.) — **create new state landing only if missing**, using district page patterns; do not delete old URLs.

## Indexation

Index directory when ≥ 20 state links return 200. Empty states stay linked but target page may be `noindex` until content exists — do not remove state from grid.
