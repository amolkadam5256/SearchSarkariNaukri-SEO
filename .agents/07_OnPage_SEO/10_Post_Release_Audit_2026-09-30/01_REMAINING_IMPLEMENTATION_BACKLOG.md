# Remaining implementation backlog (post 30 Sep release)

**Priority key:** P0 = trust/indexing · P1 = spec promised · P2 = growth · DECISION = needs product/SEO call

---

## P0 — Trust / indexing

| ID | Item | Owner | Spec / file |
|----|------|-------|-------------|
| R-SLUG-01 | Legacy job URLs where **slug text ≠ job ID content** (e.g. Canara slug + `--5015` serves NHSRCL). Enforce: load by ID, **301** to `canonicalSlug` when path wrong. | Dev | `02_STALE_JOB_SLUG_ROUTING.md`, `SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md` R2 |
| R-EDIT-01 | **3 duplicate job pairs** — mark one duplicate each: SBI 6147/6142, 6146/6144, NMU Jalgaon 6687/6280 | Editor | `06_DUPLICATE_JOB_RECORDS_EDITOR_TASK.md` |

---

## P1 — Spec / competitor gap (not in 30 Sep release)

| ID | Item | Owner | Spec / file |
|----|------|-------|-------------|
| N-EN-01 | `/employment-news` hub + homepage urgent strip data | Dev + **data owner** | `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/` |
| N-AK-01 | `/answer-keys` hub | Dev + **data owner** | `08_Standalone_Pages/02_ANSWER_KEYS_HUB/` |
| N-GUIDE-01 | Guide **1,200+ words** (live ~830) | SEO copy → Dev paste | `03_GUIDE_PAGE_COPY_EXPANSION.md` |
| N-WOMEN-01 | “Jobs for Female Candidates” card target | **DECISION** then Dev | `04_WOMEN_JOBS_DECISION_AND_SPEC.md` |
| N-UT-01 | 5 UT location pages | **APPROVAL** then Dev/data | `05_UT_LOCATION_PAGES_APPROVAL_BRIEF.md` |
| N-PDF-01 | Official PDF button on job cards | **DECISION** | Morning report item 4 — not spec’d in repo yet |
| N-62-01 | Homepage trending exam chips (§62) | Dev | `01_Home_Page/62_TRENDING_EXAM_CHIPS/` |
| N-64-01 | Featured high-vacancy block (§64) | Dev | `01_Home_Page/64_FEATURED_HIGH_VACANCY_OPENINGS/` |
| N-JOBS-06 | State/department dropdown on `/jobs` | Dev | `04_Jobs_Page/06_STATE_DEPARTMENT_SEARCH_FILTER.md` |

---

## Done (30 Sep release — do not re-build)

- Sitemap: withdrawn/410 jobs excluded from job sitemap  
- Homepage stats strip + closing-today pill logic  
- Job page title de-duplication (except 6 duplicate records)  
- Marathi title organisation/count fix  
- `/state-government-jobs`, `/guide/government-jobs-2026`, `/exam-syllabus-patterns`  
- Internal links from header, footer, homepage, `/jobs`, `/job-updates`

---

## SEO repo hygiene (done in this audit)

- [x] `IMPLEMENTATION_INDEX.md` route for guide  
- [x] `live_seo_regression_check.py` JOB_SAMPLES  
- [ ] Optional: copy PDF evidence into repo `10_Post_Release_Audit_2026-09-30/evidence/` (manual)

---

## Suggested next sprint order

1. R-SLUG-01 (301 by job ID)  
2. R-EDIT-01 (duplicate records)  
3. N-WOMEN-01 + N-UT-01 (decisions — quick)  
4. N-64-01 + N-JOBS-06 (no new external data)  
5. N-62-01 + N-PDF-01 (after decisions)  
6. N-GUIDE-01 (copy)  
7. N-EN-01 + N-AK-01 (blocked on data owners)
