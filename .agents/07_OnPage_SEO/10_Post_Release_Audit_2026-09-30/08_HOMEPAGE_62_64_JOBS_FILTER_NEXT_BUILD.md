# Next build (no new external data) — §62, §64, `/jobs` filter

**Source:** Release PDF §6 “next round” + `09_Developer_Implementation_Pack/00_MASTER_DEVELOPER_HANDOFF.md`

---

## 1. Featured high-vacancy block (§64)

**Spec:** `01_Home_Page/64_FEATURED_HIGH_VACANCY_OPENINGS/SECTION_SPEC.md`

**Logic:** Top N published jobs by `vacancy_count` (or posts field), exclude expired.

**UI:** 3–6 cards with org, post, vacancies, last date → job detail URL.

**SEO:** Internal links only; optional ItemList snippet on homepage (coordinate with existing homepage schema).

---

## 2. Trending exam chips (§62)

**Spec:** `01_Home_Page/62_TRENDING_EXAM_CHIPS/SECTION_SPEC.md`

**Examples:** SSC CGL, IBPS PO, RRB NTPC, MPSC Rajyaseva, UPSC CSE — link to real `/exams/...` pages.

**Wire:** `52_POPULAR_SEARCHES` mirror or replace per `03_EXISTING_SECTIONS_WIRE_AND_COPY_UPDATES.md`.

**Blocker from PDF:** “Decisions 1 and 5 from morning report” — confirm chip list with SEO before build.

---

## 3. State / department dropdown on `/jobs` (doc 06)

**Spec:** `04_Jobs_Page/06_STATE_DEPARTMENT_SEARCH_FILTER.md`

**Behaviour:**

- Dropdown or facet: state + department  
- SEO-safe: canonical to `/jobs` with controlled query params OR dedicated hub pages (prefer hubs already live: `/state-government-jobs`)

**Do not** index infinite query combinations.

---

## 4. Official PDF button on job cards

**Status:** Decision only — not specified in this folder.

**Suggestion:** Show “Official notification” when `official_pdf_url` validated; else “Official recruitment page” linking to apply/notice URL.

---

## Acceptance

- [ ] §64 visible on homepage with real vacancy counts  
- [ ] §62 chips all 200 to exam/category pages  
- [ ] `/jobs` filter works without breaking prerender  
- [ ] No regression to stats strip (815 active jobs logic)
