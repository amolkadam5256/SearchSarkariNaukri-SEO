# Jobs page — State & Department Search (MSN parity)

**Competitor:** MySarkariNaukri homepage State + Department dropdown search  
**Existing:** `04_Jobs_Page/00_MASTER_PROMPT_JOBS_PAGE_UPGRADE.md`, robots blocks raw `?search=`  
**Priority:** P1  
**Card labels:** `07_JOB_CARD_MESSAGING_AND_LABELS.md`

## Goal

Match MSN **discovery** without creating index bloat.

## UX (preserve current layout — add filter bar only if already planned; no redesign)

- **State select:** maps to canonical hub URL when user searches:
  - Example: `Maharashtra` → `/jobs-in-maharashtra` or pre-filter `/jobs?state=maharashtra` with **canonical** to hub if indexable.
- **Department select:** maps to `/department/ssc`, `/category/railway-jobs`, etc.

## Helper copy (above filters)

“Pick a state or department to narrow results. For every state, use our [state wise government jobs](/state-government-jobs) directory. SearchSarkariNaukri does not accept applications — use **Apply on official site** on each card.”

## SEO rules

1. **Indexable:** only predefined landing pages in sitemap.  
2. **Non-indexable:** arbitrary query combos → `noindex,follow` + robots already blocks some params.  
3. On change of filter, update `<title>` only on **dedicated** landing routes, not infinite `/jobs?` variants.  
4. Internal links from homepage trending chips must use **clean URLs**.

## Department dropdown labels (display text)

| Label | Target |
|-------|--------|
| All categories | `/jobs` |
| UPSC | `/department/upsc` |
| SSC | `/department/ssc` |
| Railway (RRB) | `/category/railway-jobs` |
| Banking (IBPS/SBI) | `/category/banking-jobs` |
| Defence & Police | `/category/police-jobs` or defence hub |
| Teaching | `/category/teaching-jobs` |
| Engineering / PSU | `/category/psu-jobs` |
| Medical / Health | `/category/medical-jobs` |

## State dropdown

Use same state list as `05_STATE_JOBS_DIRECTORY/PAGE_COPY.md`. On submit: redirect 302/301 to state hub URL (prefer **301** if permanent mapping).

## Implementation checklist

- [ ] State list matches state directory  
- [ ] Department list matches commission tiles  
- [ ] Redirect GSC error URL `/jobs?district_slug=pune` → `/districts/pune` (P0)  
- [ ] Crawlable `<a href>` pagination unchanged (`03_SECTION_COVERAGE_CHECKLIST.md`)

## Do not delete

Existing qualification/district filters — **add** state/department mapping alongside.
