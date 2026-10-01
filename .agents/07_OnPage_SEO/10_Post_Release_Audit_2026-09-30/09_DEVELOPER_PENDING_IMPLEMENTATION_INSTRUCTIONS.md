# Developer instructions — pending work (post 30 Sep release)

**Audience:** Backend + frontend + prerender/sitemap (production repo: `SakariNaukariN` per handoff docs)  
**SEO repo (this folder):** specs and copy only — implement in production codebase  
**Date:** 1 October 2026  
**Status:** Main release **live**; items below are **not done** on production

**Read first:** `.agents/07_OnPage_SEO/09_Developer_Implementation_Pack/00_NO_DELETE_POLICY.md`

---

## Already live — do not rebuild

| Item | Route / area |
|------|----------------|
| Sitemap excludes 410 jobs | `/sitemap-jobs.xml` |
| Homepage stats (active jobs, orgs, closing today) | Homepage stats strip |
| Job `<title>` de-duplication logic | Job detail + prerender |
| Marathi title org/count fix | Job detail |
| State directory | `/state-government-jobs` |
| Apply guide | `/guide/government-jobs-2026` |
| Syllabus hub | `/exam-syllabus-patterns` |
| Nav/footer/homepage links to above | Header, footer, homepage sections |

**Regression check (SEO repo):**  
`py -3 SEO_Audit_Review_2026-09-29/live_seo_regression_check.py` → expect **PASS** after your P0 fix (samples use job IDs `--6681`, `--6682`).

---

## Build order (mandatory sequence)

| Step | Priority | Work | Blocked by |
|------|----------|------|------------|
| **1** | **P0** | Job slug 301 by ID | Nothing — start here |
| **2** | P1 | Duplicate job pairs (CMS/admin) | **Editor** — dev only implements redirect/unpublish UI if missing |
| **3** | P1 | `/jobs` state + department filter | Nothing |
| **4** | P2 | Homepage §64 featured high-vacancy | Nothing |
| **5** | P2 | Homepage §62 trending exam chips | **SEO decision** on chip list |
| **6** | P2 | Job card “Official PDF” button | **SEO decision** + field `official_pdf_url` |
| **7** | P1 | `/answer-keys` hub | **Data owner** for key URLs (can ship empty state + schema shell) |
| **8** | P1 | `/employment-news` hub | **Data owner** |
| **9** | P1 | 5 UT location pages | **TR approval** + location data |
| **10** | P1 | Women jobs page + homepage card href | **TR decision** on route |
| **11** | Content | Guide 830 → 1,200+ words | **SEO copy** in `03_GUIDE_PAGE_COPY_EXPANSION.md` — CMS paste |

---

## STEP 1 — P0: Stale job slug → 301 to canonical (NOT optional)

### Problem

URLs like `/jobs/canara-bank-...--5015` still **200** with **NHSRCL** body because row **5015** is NHSRCL while the slug prefix is an old Canara slug. Correct Canara URLs use IDs **6681**, **6682**.

This is **not** fixed by changing the regression script. Google and users can still open misleading URLs.

### Required behaviour

1. **Parse job ID** from path: regex `--(\d+)$` (use your existing suffix convention).
2. **Load job by primary key ID** — ID is authoritative, not the slug string.
3. **Compute `canonicalSlug`** with the **same helper** used when publishing (org + post + year + `--{id}`; Marathi rules unchanged).
4. If `requestPath !== '/jobs/' + canonicalSlug` → respond **301 Moved Permanently** to  
   `https://www.searchsarkarinaukri.com/jobs/{canonicalSlug}`  
   (preserve query string only if you already use UTM rules; otherwise omit).
5. **Render** (after redirect): H1, `<title>`, meta description, Open Graph, JSON-LD, BreadcrumbList — all from **that ID’s row**.
6. **Sitemap job feed:** emit **only canonical** job URLs (same helper). Stale slug URLs must **not** appear in `/sitemap-jobs.xml`.
7. **Prerender / CDN cache key:** include job id + `updated_at` (e.g. `job:{id}:{updated_at}`). Purge on job update.

### Files to touch (typical — adjust to your repo)

- Job detail route/controller (Express/React SSR entry)
- `generateCanonicalJobSlug(job)` — single shared module used by sitemap + detail route
- Sitemap job query + URL builder
- Prerender cache invalidation hook on job save

### Acceptance tests

```text
GET /jobs/canara-bank-graduate-apprentice-recruitment-2026-apply-online-for-3500-posts--5015
→ 301 Location: .../jobs/{nhsrcl-canonical-slug-for-5015}

GET /jobs/canara-bank-graduate-apprentice-recruitment-2026-apply-online-for-3500-posts--6681
→ 200, body contains "Canara Bank"

GET /jobs/canara-bank-graduate-apprentice-recruitment-2026-west-bengal-apply-online-for-150-posts--6682
→ 200, body contains "Canara Bank"
```

Run from SEO repo after deploy:

```bash
py -3 SEO_Audit_Review_2026-09-29/live_seo_regression_check.py
```

Optional one-off audit script: fetch all published job IDs; if any internal link or sitemap loc slug ≠ canonicalSlug, log for cleanup.

### Reference docs

- `10_Post_Release_Audit_2026-09-30/02_STALE_JOB_SLUG_ROUTING.md`
- `SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md` (section R2)

---

## STEP 2 — Duplicate job records (editor + dev support)

**Not a title-template bug.** Six pages share titles because **two DB rows** are the same recruitment.

| Keep one / mark duplicate | Job IDs |
|---------------------------|---------|
| SBI (pair 1) | **6147** vs **6142** |
| SBI (pair 2) | **6146** vs **6144** |
| NMU Jalgaon | **6687** vs **6280** |

### Editor (data)

1. Compare official notification + apply URL for each pair.
2. Mark one row: `duplicate_of: <surviving_id>` or unpublish duplicate per your CMS policy.
3. Reconcile NMU last dates from official PDF.

### Developer (if not already supported)

- Admin action: “Mark as duplicate of …” → surviving job gets traffic; duplicate URL **301** to surviving canonical slug **or** 200 with noindex + banner (prefer **301**).
- Remove duplicate from active `/jobs` list and from sitemap.
- **Do not hard-delete** rows unless policy explicitly allows — prefer unpublish + 301.

**Spec:** `06_DUPLICATE_JOB_RECORDS_EDITOR_TASK.md`

---

## STEP 3 — `/jobs` state + department filter (P1)

**Spec:** `.agents/07_OnPage_SEO/04_Jobs_Page/06_STATE_DEPARTMENT_SEARCH_FILTER.md`

### Implement

- UI: state dropdown + department/category dropdown (reuse existing filter components if any).
- Filter against same query rules as homepage stats (**published, open jobs only**).
- **SEO:**  
  - Prefer linking to `/state-government-jobs` and department hubs for indexable landing pages.  
  - For query URLs (`/jobs?state=...`): `canonical` → `/jobs` unless you have dedicated indexable filter landing pages.  
  - Do not generate infinite indexable parameter combinations.

### Acceptance

- Selecting Maharashtra shows only MH-tagged published open jobs.
- Counts consistent with `/state-government-jobs` for that state (within same publish rules).
- No regression to homepage stats strip logic.

---

## STEP 4 — Homepage §64 Featured high-vacancy (P2)

**Spec:**  
- `01_Home_Page/64_FEATURED_HIGH_VACANCY_OPENINGS/SECTION_SPEC.md`  
- `01_Home_Page/64_FEATURED_HIGH_VACANCY_OPENINGS/DEVELOPER_FULL_SPEC.md`

### Implement

- New homepage section **below** latest jobs (or per spec placement).
- Query: top **N** (e.g. 6) **published, open** jobs ordered by `vacancy_count` DESC (nulls last).
- Card: org, post title, vacancies, last date, link to job detail **canonical URL**.
- Reuse existing job card component — no new design system.
- **Do not remove** existing latest-jobs block.

### Acceptance

- Section visible on homepage with real counts.
- All links 200 and slug matches ID (after P0).
- Empty state: hide section or show “No high-vacancy listings today” — do not show fake numbers.

---

## STEP 5 — Homepage §62 Trending exam chips (P2)

**Spec:** `01_Home_Page/62_TRENDING_EXAM_CHIPS/SECTION_SPEC.md`

### Implement

- Chip row linking to **existing** `/exams/...` routes (200 only).
- Wire per `09_Developer_Implementation_Pack/03_EXISTING_SECTIONS_WIRE_AND_COPY_UPDATES.md` (mirror or extend `52_POPULAR_SEARCHES`).

### Blocker

SEO must confirm chip list (SSC CGL, IBPS PO, RRB NTPC, MPSC Rajyaseva, etc.) — **do not link to 404**.

---

## STEP 6 — Job card “Official PDF” button (P2)

### Implement (after SEO confirms)

- Show button when `official_notification_pdf_url` (or your field) is validated HTTPS and host matches allowlist (`.gov.in`, `.nic.in`, bank/PSC domains from editorial rules).
- Label: **“Official notification (PDF)”** — not “Download from Search Sarkari Naukri”.
- If only HTML recruitment page exists: **“Official recruitment page”** → external apply/notice URL.
- `target="_blank"` + `rel="noopener noreferrer"`.

### Do not

- Host PDFs on SSN domain unless licensed — link out only.

---

## STEP 7 — `/answer-keys` hub (P1)

**Spec folder:** `08_Standalone_Pages/02_ANSWER_KEYS_HUB/`  
(`DEVELOPER_INSTRUCTIONS.md`, `PAGE_COPY.md`, `SEMANTIC_HTML_AND_SCHEMA.md`)

### Implement

1. New route `/answer-keys` — indexable, 200.
2. Table columns per `PAGE_COPY.md` (exam, commission, key status, official link, objection window).
3. Data: from exam/result module — add fields if missing:  
   `answer_key_status`, `answer_key_url`, `objection_start`, `objection_end`.
4. Add nav/footer link per `09_Developer_Implementation_Pack/02_NAV_AND_FOOTER_LINKS.md` **when page has content or honest empty state**.
5. FAQ + FAQPage schema only if FAQs visible on page.

### If no data owner yet

Ship **empty state**: explain keys are on official sites; link `/results`, `/exams`, `/exam-syllabus-patterns`; do **not** invent keys.

### Guide page

Live guide already points to commission sites for answer keys until this hub exists — update guide link when `/answer-keys` is live.

---

## STEP 8 — `/employment-news` hub (P1)

**Spec folder:** `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/`

Blocked on **data owner** (feed from https://www.employmentnews.gov.in). Same pattern as answer keys: build page + pipeline or empty state with official link.

Homepage §63 urgent strip depends on this feed — implement after EN data pipeline defined (`07_EMPLOYMENT_NEWS_ANSWER_KEYS_DATA_OWNERS.md`).

---

## STEP 9 — Five UT location pages (P1)

**Approval:** TR must approve before build (`05_UT_LOCATION_PAGES_APPROVAL_BRIEF.md`).

### UTs without dedicated page today

- Andaman and Nicobar Islands  
- Dadra and Nagar Haveli and Daman and Diu  
- Ladakh  
- Lakshadweep  
- Puducherry  

### Implement (after approval)

- Clone existing state location template (e.g. Delhi).
- Routes: follow production pattern (`/state/{slug}` — confirm with existing `/state/delhi`).
- Link from `/state-government-jobs` grid (replace “no dedicated page” text with link).
- Dynamic job count; zero jobs OK.
- Add location tags to jobs in DB so filters work.

---

## STEP 10 — “Jobs for Female Candidates” homepage card (P1)

**Decision:** `04_WOMEN_JOBS_DECISION_AND_SPEC.md`  
**Existing section spec:** `01_Home_Page/17_WOMEN_JOBS/SECTION_SPEC.md`

### Recommended dev work (after TR picks Option A)

- New page `/women-government-jobs` or `/government-jobs-for-women` (confirm slug with SEO).
- Copy from decision brief — no false reservation claims.
- Update homepage card `href` from graduate jobs page to this URL.
- **Do not remove** graduate jobs page.

---

## STEP 11 — Guide word count expansion (content, not backend)

**Live URL:** `/guide/government-jobs-2026` (~830 words)

**Copy to paste:** `10_Post_Release_Audit_2026-09-30/03_GUIDE_PAGE_COPY_EXPANSION.md`

Developer: append new H2 sections via CMS or static content source; update `dateModified`; extend FAQPage schema if new FAQs added.

---

## QA checklist before sign-off

| Check | How |
|-------|-----|
| P0 slug 301 | Manual + regression script |
| Sitemap job URLs all 200, none 410, canonical slugs only | Sample + GSC inspect |
| Homepage stats unchanged logic | Compare strip vs `/jobs` total |
| No deleted nav/footer links | Diff only **additions** |
| New pages in `sitemap-static.xml` (or generator) | `/answer-keys`, UT pages when live |
| Prerender includes new sections in HTML source | View-source / curl |
| `IMPLEMENTATION_INDEX.md` | SEO repo — routes documented |

---

## What is NOT developer work

| Item | Owner |
|------|--------|
| Merge duplicate SBI/NMU rows | Editor |
| Approve 5 UT pages | TR |
| Women jobs card destination | TR / SEO |
| Employment News + Answer Keys data | Data owners |
| §62 chip list + PDF button rules | SEO |
| Guide extra paragraphs | SEO (copy provided) |

---

## Single ticket summary (for Jira / WhatsApp to dev)

**Title:** P0 job canonical 301 + jobs filters + §64 + answer-keys shell  

**Description:**  
1. **P0:** Resolve job by ID; 301 stale slug to canonical; sitemap canonical URLs only.  
2. **P1:** `/jobs` state/department filters; duplicate job admin 301; `/answer-keys` page (spec in SEO repo `08_Standalone_Pages/02_ANSWER_KEYS_HUB/`).  
3. **P2:** Homepage featured high-vacancy block (`64_*` spec).  
4. **After TR/SEO:** UT pages, women jobs page, §62 chips, PDF button, EN hub, guide copy paste.

**Test:** `SEO_Audit_Review_2026-09-29/live_seo_regression_check.py` → PASS.

**Policy:** No deletes — see `00_NO_DELETE_POLICY.md`.

---

**Document owner:** SEO / TR  
**Related:** `00_LIVE_RELEASE_VERIFICATION_AUDIT.md`, `01_REMAINING_IMPLEMENTATION_BACKLOG.md`
