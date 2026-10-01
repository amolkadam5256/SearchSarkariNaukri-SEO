# Live release verification audit — 30 Sep 2026

**Evidence PDF:** `C:\Users\abc\Downloads\SSN_SEO_Fixes_Live_2026-09-30.pdf`  
**Release time (claimed):** 30 Sep 2026, 13:39 IST  
**Re-audit run:** 1 Oct 2026 (SEO repo + live URL checks)  
**Production:** https://www.searchsarkarinaukri.com

---

## Executive summary

| Area | Dev release claim | SEO repo re-check (1 Oct) | Verdict |
|------|-------------------|---------------------------|---------|
| Sitemap excludes 410 jobs | 9 → 0 in job sitemap | Not re-scanned XML locally (TLS limits on agent); PDF + dev evidence accepted | **Done (live)** — re-run `live_seo_regression_check.py` sitemap section periodically |
| Homepage stats (815 / 280 / closing today) | Fixed | Not numerically re-fetched homepage API | **Done (live)** per PDF screenshots |
| Duplicate `<title>` groups | 98 pages → 6 (duplicate DB rows) | Not re-crawled all 806 jobs | **Done (code)** — **6 editor actions remain** |
| Marathi title bug (27 pages) | Fixed | Not spot-checked | **Done (live)** per PDF |
| `/state-government-jobs` | Live, indexable, linked | **200**, content + UT “no page yet” copy visible | **Done** |
| `/guide/government-jobs-2026` | Live, ~830 words | **200**, steps + FAQ present | **Done** — **copy expansion optional** (spec 1,200+) |
| `/exam-syllabus-patterns` | Live, sector hub | **200**, cards + pattern table | **Done** |
| Nav/footer/homepage links to new pages | Added | Spot-check: guide + state pages reachable | **Done** |
| `IMPLEMENTATION_INDEX` guide URL | Wrong slug in index | Repo still had old URL until this audit | **Fixed in repo** (see below) |
| `live_seo_regression_check.py` samples | Use `--6681` / `--6682` not `--5015` | Script still used wrong IDs → **FAIL** | **Fixed in repo** |
| Stale slug `/jobs/canara-bank-...--5015` | PDF: ID 5015 is NHSRCL, not Canara | **Still live:** Canara slug serves NHSRCL body | **Open (P1 routing)** — see `02_STALE_JOB_SLUG_ROUTING.md` |
| Employment News / Answer Keys hubs | Not built | Spec only in `08_Standalone_Pages/` | **Not done** |
| Women jobs card → graduate page | Wrong target | Decision pending | **Not done** |
| 5 UT location pages | Listed without links on directory | As designed until approval | **Not done** |
| Homepage §62 chips, §64 featured, `/jobs` filter (06) | Next round | Specs exist, not built | **Not done** |
| Official PDF button on job cards | Decision pending | Not in this repo | **Not done** |
| Duplicate job records (SBI ×2, NMU) | Editor task | Data, not code | **Not done** |

---

## Verified live (1 Oct 2026)

### `/state-government-jobs`

- H1 and state/UT structure present.
- Five UTs explicitly say “No dedicated page yet” with fallback to all jobs (matches release notes).
- Job counts dated “01 October 2026”.

### `/guide/government-jobs-2026`

- Title ~57 chars (site cap), full step guide, fake-notification section, Maharashtra notes, 3 FAQs.
- “Last reviewed: 30 September 2026”.
- Answer-key step points to official commission sites (not `/answer-keys` — hub not built).

### `/exam-syllabus-patterns`

- Sector blocks (UPSC, SSC, Railway, Banking, Police/Defence, Teaching, PSU, Medical, MPSC).
- Exam pattern table from existing exam-page data.
- FAQs + last reviewed date.

### Job slug integrity spot-check

| URL pattern | Expected | Observed |
|-------------|----------|----------|
| `...--6681` (Canara Uttarakhand) | Canara Bank | **Correct** — org, vacancies, dates match |
| `...--5015` (old Canara slug) | Should 301 to canonical for job ID 5015 OR show NHSRCL under NHSRCL slug only | **Mismatch** — URL says Canara; page is NHSRCL (expired) |

This is **not** fixed by updating the regression script alone. Routing/canonical policy for legacy slugs is still required.

---

## Regression script (repo)

After updating `JOB_SAMPLES` to `--6681` and `--6682`, run:

```bash
py -3 SEO_Audit_Review_2026-09-29/live_seo_regression_check.py
```

Expected: **PASS** for samples + sitemap/robots checks (unless new live regressions appear).

---

## Repo fixes applied in this audit pass

1. `IMPLEMENTATION_INDEX.md` — guide route → `/guide/government-jobs-2026`
2. `live_seo_regression_check.py` — sample job URLs → real Canara IDs
3. New folder `10_Post_Release_Audit_2026-09-30/` — backlog + implementation briefs for open items
4. `04_CANDIDATE_GUIDANCE_2026/PAGE_COPY.md` — optional expansion sections + link corrections aligned with live site

---

## Sign-off checklist

| Role | Action |
|------|--------|
| **Dev** | Implement stale-slug 301 (P1), next build: §64, §62, `/jobs` filter |
| **Editor** | Mark duplicate pairs: SBI 6147/6142, 6146/6144; NMU 6687/6280 |
| **SEO** | Approve UT pages + women jobs destination; assign EN/Answer Keys data owners |
| **SEO** | Publish guide expansion when ready (`03_GUIDE_PAGE_COPY_EXPANSION.md`) |

---

**Status:** Release items **largely complete on live site**; **SEO repo and follow-ups** tracked in `01_REMAINING_IMPLEMENTATION_BACKLOG.md`.
