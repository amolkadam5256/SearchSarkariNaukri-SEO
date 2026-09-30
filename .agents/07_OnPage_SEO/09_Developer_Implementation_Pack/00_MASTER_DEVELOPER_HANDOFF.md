# Master developer handoff — competitor gaps + messaging (no deletes)

**Site:** https://www.searchsarkarinaukri.com/  
**Reference competitor:** https://www.mysarkarinaukri.com/  
**Date:** 30 September 2026  

## Non-negotiable rules

**Read first:** [`00_NO_DELETE_POLICY.md`](00_NO_DELETE_POLICY.md) — no content, page, or section may be removed.

1. **Do not delete** jobs, pages, homepage sections, URLs, footer/nav items, database rows, FAQs, copy blocks, or media. **Add and update only.**  
2. **Do not redesign** UI — reuse existing cards, chips, typography, spacing.  
3. **Add** new routes, nav/footer links, homepage blocks, and copy blocks only where specs say.  
4. **Update** existing pages by **appending** sections or improving metadata — never strip working content.  
5. Copy in this pack is **editorial baseline** — replace placeholders marked `[DYNAMIC]` with real DB fields; do not invent vacancies or dates.  
6. Voice guide: read `01_BRAND_MESSAGING_AND_VOICE.md` before publishing any text.

## Build order

| Step | Work | Folder |
|------|------|--------|
| 0 | Fix job slug + sitemap (blocking SEO) | `SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md` |
| 1 | New hub pages (P1) | `08_Standalone_Pages/*/DEVELOPER_INSTRUCTIONS.md` |
| 2 | Homepage sections (P2) | `01_Home_Page/61_*` … `64_*` → `DEVELOPER_FULL_SPEC.md` |
| 3 | Jobs listing parity | `04_Jobs_Page/06_*` + Phase 11 in `02_IMPLEMENTATION_PLAN.md` |
| 4 | Wire nav/footer | `02_NAV_AND_FOOTER_LINKS.md` (this pack) |
| 5 | QA | Each folder `04_QA_CHECKLIST.md` |

## Folder map (detailed instructions + human copy)

| Route | Folder |
|-------|--------|
| `/employment-news` | `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/` |
| `/answer-keys` | `08_Standalone_Pages/02_ANSWER_KEYS_HUB/` |
| `/exam-syllabus-patterns` | `08_Standalone_Pages/03_EXAM_SYLLABUS_PATTERNS_HUB/` |
| `/guide/government-jobs-2026` | `08_Standalone_Pages/04_CANDIDATE_GUIDANCE_2026/` |
| `/state-government-jobs` | `08_Standalone_Pages/05_STATE_JOBS_DIRECTORY/` |
| Homepage hero count | `01_Home_Page/61_HERO_ACTIVE_VACANCY_COUNT/` |
| Homepage trending | `01_Home_Page/62_TRENDING_EXAM_CHIPS/` |
| Homepage urgent strip | `01_Home_Page/63_URGENT_ALERTS_EMPLOYMENT_NEWS/` |
| Homepage featured jobs | `01_Home_Page/64_FEATURED_HIGH_VACANCY_OPENINGS/` |

## Existing specs to keep using (do not replace)

- Verification: `01_Home_Page/49_RECRUITMENT_VERIFICATION_PROCESS/`  
- How it works: `28_HOW_IT_WORKS/`  
- Job updates page: `06_job-updates/`  
- State chips on homepage: `21_STATE_JOBS/`, `43_ALL_INDIA_STATE_SEO/`  
- AEO FAQs: `58_AEO_DIRECT_ANSWERS/`, `59_EXPANDED_FAQ/`  

New copy must **align** with: *SearchSarkariNaukri is an independent information portal; the official notification is final.*
