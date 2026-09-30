# MySarkariNaukri vs SearchSarkariNaukri — Competitive SEO & Visibility Plan

**Date:** 30 September 2026  
**Competitor:** https://www.mysarkarinaukri.com/  
**Our site:** https://www.searchsarkarinaukri.com/  
**Rule:** Do not delete any content, page, or section. **Add + update + link only.** Policy: `../09_Developer_Implementation_Pack/00_NO_DELETE_POLICY.md`

---

## Executive summary

| Dimension | MySarkariNaukri (MSN) | SearchSarkariNaukri (SSN) | Who wins today |
|-----------|----------------------|---------------------------|----------------|
| **National breadth** | Strong — 2,270+ active count, all states, central focus | Strong listings but **Maharashtra-weighted** hero/jobs | MSN for all-India head terms |
| **Trust / freshness copy** | “Updated every 2 minutes”, vacancy count in hero | “Last updated” date, verification copy | Tie — different angles |
| **Nav clarity** | Jobs, Admit Card, Results, **Answer Key**, **Employment News**, **State Jobs**, **Free Alert**, exam shortcuts | Rich homepage hubs; some intents buried in footer/long page | MSN for top-nav discovery |
| **Job cards UX (SEO signals)** | City, vacancy count, **PDF**, “View & Apply”, “Closing Soon” | List-style latest jobs; deep apprentice splits | MSN for snippet-friendly cards |
| **Sector hubs** | 8 commission tiles (UPSC, SSC, RRB, Banking, Police, Teaching, PSU, Medical) | Similar sections (33–38, 12, 14) — **already specced** | SSN if implemented on homepage |
| **Candidate education** | Long “Navigating Government Recruitments 2026” guide | FAQs + How to Apply + Verification — **more AEO** | SSN content depth; MSN simpler funnel |
| **Maharashtra / MPSC** | Generic state list | **Deep** MPSC, Talathi, ZP, districts, Marathi | **SSN advantage** |
| **Tools** | “Candidate Tools” in nav | Eligibility, Quiz, Calendar, Study Material | **SSN advantage** |
| **Technical SEO** | Unknown GSC | 497 indexed / 2196 not indexed, sitemap/job URL issues | **Must fix SSN P0 first** |

**Strategy to beat MSN:** Own **Maharashtra + bilingual + tools + verification**, match MSN on **national hub pages** (state, answer key, employment news, syllabus), and fix **indexation/trust bugs** so Google can rank what you already built.

---

## Feature-by-feature comparison

### 1. Primary navigation

| MSN nav item | SSN equivalent | Folder / action |
|--------------|----------------|-----------------|
| Jobs | `/jobs` | `04_Jobs_Page/` — **update** filter spec (new file below) |
| Admit Card | `/admit-cards` | `01_Home_Page/23_ADMIT_CARDS/` + admit-card templates |
| Results | `/results` | `01_Home_Page/24_RESULTS/` |
| Answer Key | **Missing dedicated hub** | **NEW** `08_Standalone_Pages/02_ANSWER_KEYS_HUB/` |
| Employment News | **Missing hub** | **NEW** `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/` |
| Updates | `/job-updates` or `/news` | `06_job-updates/` |
| Free Alert | WhatsApp/Telegram | `01_Home_Page/05_JOB_ALERTS/`, `60_SHARE_ALERT_CTA/` |
| State Jobs | Partial | **UPDATE** `21_STATE_JOBS/` + **NEW** `08_Standalone_Pages/05_STATE_JOBS_DIRECTORY/` |
| Women Jobs | Partial | `17_WOMEN_JOBS/` |
| SSC CGL / UPSC / Railways / Banking | Category/dept pages | `34_SSC`, `33_UPSC`, `35_RAILWAYS`, `36_BANKING` |
| Exam Syllabus & Patterns | `/exams` partial | **NEW** `08_Standalone_Pages/03_EXAM_SYLLABUS_PATTERNS_HUB/` + `51_EXAM_PREPARATION_HUB/` |

### 2. Homepage above the fold

| MSN | SSN | Action |
|-----|-----|--------|
| Hero + **2,270 active** vacancies | Hero + last updated | **NEW** `61_HERO_ACTIVE_VACANCY_COUNT/` — dynamic count (no fake numbers) |
| State + Department search modal | Qualification/district links | **NEW** `04_Jobs_Page/06_STATE_DEPARTMENT_SEARCH_FILTER.md` |
| **Trending Now** chips (SSC CGL, IBPS PO, RRB NTPC…) | Popular searches section | **NEW** `62_TRENDING_EXAM_CHIPS/` + link `52_POPULAR_SEARCHES/` |
| Quick tiles: Latest / Admit / Results / Syllabus | Exam calendar + tools lower | **UPDATE** `11_CAREER_COMMAND_CENTER/` — add Syllabus + Answer Key links |
| **Urgent Alerts** strip (Employment News + mega jobs) | Ending soon section | **NEW** `63_URGENT_ALERTS_EMPLOYMENT_NEWS/` + keep `07_CLOSING_SOON_JOBS/` |

### 3. Job listing presentation

| MSN | SSN | Action |
|-----|-----|--------|
| Featured high-vacancy (RRB JE 4098, SSC CHSL 2536…) | Latest jobs flat list | **NEW** `64_FEATURED_HIGH_VACANCY_OPENINGS/` |
| 40 recent with countdown + PDF | 30+ text list | **UPDATE** `04_Jobs_Page/02_IMPLEMENTATION_PLAN.md` — card fields: city, posts, last date, **official PDF link**, closing-soon badge |
| Browse State Portals | State SEO sections | `43_ALL_INDIA_STATE_SEO/` |

### 4. Content / AEO / GEO

| MSN | SSN | Action |
|-----|-----|--------|
| Single long candidate guide | 12+ homepage FAQs | **NEW** `08_Standalone_Pages/04_CANDIDATE_GUIDANCE_2026/` — merge MSN-style guide **without removing** FAQs |
| Quick Facts in job teasers | Job detail structured fields | **UPDATE** `04_Jobs_Page/_archive.../19_INDIVIDUAL_JOB_PAGE` patterns + `05_districts_Job_Page/` |
| Verify via Employment News | Verification sections | **UPDATE** `29_VERIFICATION/`, `49_RECRUITMENT_VERIFICATION_PROCESS/` — cite employmentnews.gov.in |

### 5. Where SSN must not copy MSN blindly

- Do not claim “updated every 2 minutes” unless true operationally.
- Do not index 36×department infinite filter URLs — use **clean routes** (`/jobs-in-up`, `/department/ssc`).
- Keep **Marathi/English** differentiation — MSN is English-first national.

---

## Priority roadmap to improve visibility

### P0 — Before content expansion (blocking rankings)

1. Fix job ID/slug/content mismatch (see `SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md`).
2. Fix sitemap HTTP 500 / resubmit GSC.
3. Active JobPosting on valid active jobs only.

### P1 — Beat MSN on discoverability (4–6 weeks)

1. Launch **Employment News** + **Answer Keys** hubs (linked from nav/footer, not replacing anything).
2. Homepage: **trending chips**, **urgent alerts**, **featured high-vacancy** (additive sections).
3. `/jobs` state + department filters → canonical landing pages (already in robots policy).
4. Job cards: PDF + Apply CTAs (metadata/schema only if UI already has buttons — **same visual**, add links/labels).

### P2 — Moat (ongoing)

1. Maharashtra district + MPSC cluster internal links.
2. Tools (eligibility, calendar, quiz) linked from hero command center.
3. Admit-card 896 URL quality pass (existing GSC package).

---

## Implementation index

See **`IMPLEMENTATION_INDEX.md`** in this folder for every file path.

---

## Success metrics

- Impressions/clicks: `Sarkari Naukri 2026`, `government jobs`, state names, `SSC CGL 2026`, `RRB NTPC 2026`, `MPSC recruitment 2026`.
- Indexed quality URLs up; **not** total URL count.
- Nav hubs: Employment News, Answer Keys, State Jobs in sitemap + internal links from homepage.
