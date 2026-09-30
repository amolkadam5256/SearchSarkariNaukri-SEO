# Competitor vs SearchSarkariNaukri — sitemap, pages, visibility audit

**Date:** 30 September 2026  
**Competitor:** https://www.mysarkarinaukri.com/  
**Our site:** https://www.searchsarkarinaukri.com/  
**Policy:** Do not delete any content, page, or section — `09_Developer_Implementation_Pack/00_NO_DELETE_POLICY.md`

---

## 1. Live technical check (today)

| Check | MySarkariNaukri | SearchSarkariNaukri |
|-------|-----------------|---------------------|
| Homepage | 200 | 200 |
| `/sitemap.xml` | **500** | **500** |
| `/sitemap_index.xml` (MSN) | Returns **HTML homepage**, not XML (misconfigured) | n/a |
| `robots.txt` | 200, sitemap declared | 200, sitemap declared |
| GSC (SSN, user data) | n/a | ~497 indexed, ~2,196 not indexed, 12 clicks |

**P0 for both sites:** sitemap must return **200** before any ranking push. SSN Aug 2026 baseline: **12 child sitemaps**, **1,057 unique URLs** verified (`live-sitemap-verification-summary.json`).

---

## 2. Sitemap architecture comparison

### SearchSarkariNaukri (documented structure — Aug 2025/2026)

| Child sitemap | ~URLs (Aug 10 audit) | Role |
|---------------|---------------------:|------|
| sitemap-static.xml | 43 | Home, legal, tools |
| sitemap-jobs.xml | 891 | Job details |
| sitemap-locations.xml | 29 | Location hubs |
| sitemap-qualifications.xml | 10 | 10th/12th/graduate… |
| sitemap-departments.xml | 13 | MPSC, SSC, UPSC… |
| sitemap-cross-filter.xml | 99 | Controlled combos |
| sitemap-results.xml | 38 | Results |
| sitemap-admit-cards.xml | 33 | Admit cards |
| sitemap-districts.xml | 46 | District hubs |
| + news/blogs/images/quiz (post-remediation) | (in 1,057 total) | Content |

**SSN strength:** Split sitemaps, programmatic hubs, Maharashtra depth.  
**SSN risk:** Many URLs not indexed (quality + job slug bugs + crawl budget); orphans per Aug crawl.

### MySarkariNaukri (inferred from site + robots)

- Single sitemap index declared; **live fetch failed 500** — treat as competitor weakness too.  
- robots: blocks `?s=`, paginated `?page=2+`, `/keywords/`, crawl-delay 2.  
- Nav implies page types: Jobs, Admit Card, Results, **Answer Key**, **Employment News**, Updates, **State Jobs**, Women Jobs, exam shortcuts, **Exam Syllabus & Patterns**, Candidate Tools.

**MSN strength:** National nav, Employment News urgency, featured cards (PDF + apply), state/department search, ~2,270 count in hero.  
**MSN gap vs SSN:** Less Maharashtra/MPSC/Marathi depth; fewer tools (eligibility, calendar, quiz).

---

## 3. Page-type matrix (what to beat them on)

| Page / intent | MSN | SSN today | Action | Spec folder |
|---------------|-----|-----------|--------|-------------|
| Employment News hub | Yes (nav + urgent) | Missing top-level | **Add** `/employment-news` | `08_Standalone_Pages/01_EMPLOYMENT_NEWS_HUB/` |
| Answer Keys hub | Yes (nav) | Missing | **Add** `/answer-keys` | `08_Standalone_Pages/02_ANSWER_KEYS_HUB/` |
| Syllabus & pattern hub | Yes (nav + tile) | Partial `/exams` | **Add/enhance** | `08_Standalone_Pages/03_EXAM_SYLLABUS_PATTERNS_HUB/` |
| State jobs directory | Yes (36 states) | Partial sections | **Add** + wire 21, 43 | `05_STATE_JOBS_DIRECTORY/` |
| Candidate guide | Long footer content | FAQs + partial how-to | **Add** | `04_CANDIDATE_GUIDANCE_2026/` |
| Free job alert | Nav | `/job-updates`, alerts | **Update links** | `05_JOB_ALERTS/`, `06_job-updates/` |
| Admit / Results | Nav | Yes | **Quality pass** | `23_ADMIT_CARDS/`, `24_RESULTS/` |
| Featured high-vacancy | Homepage | List only | **Add section** | `64_FEATURED_HIGH_VACANCY_OPENINGS/` |
| Trending exams | Homepage chips | Popular searches | **Add section** | `62_TRENDING_EXAM_CHIPS/` |
| Urgent / EN strip | Homepage | Ending soon only | **Add section** | `63_URGENT_ALERTS_EMPLOYMENT_NEWS/` |
| Hero vacancy count | Yes | Last updated only | **Add line** | `61_HERO_ACTIVE_VACANCY_COUNT/` |
| Job card PDF + apply | Yes | Partial | **Update** | `04_Jobs_Page/07_JOB_CARD_MESSAGING_AND_LABELS.md` |
| State/dept job filter | Yes | Partial | **Update** | `04_Jobs_Page/06_STATE_DEPARTMENT_SEARCH_FILTER.md` |
| MPSC / districts / Marathi | Weak | **Strong** | **Keep + interlink** | `18_MAHARASHTRA_JOBS/`, `05_districts_Job_Page/` |
| Tools (quiz, eligibility) | Light | **Strong** | **Link from hero** | `26_TOOLS/`, `51_EXAM_PREPARATION_HUB/` |

---

## 4. Rankings / visibility (what “beat them” means)

We do **not** have verified Ahrefs/Semrush ranks in repo. Practical targets:

1. **Fix SSN indexation** (sitemap 200, job URL = content, JobPosting on active jobs).  
2. **Own head terms** where MSN wins today: Employment News, answer key, state wise jobs, SSC/RRB featured cards.  
3. **Defend moat:** MPSC, Talathi, district jobs, Marathi queries.  
4. **Measure in GSC:** impressions on new hub URLs 4–8 weeks after deploy.

---

## 5. Implementation pack (all MD — developer reads in order)

1. `09_Developer_Implementation_Pack/00_NO_DELETE_POLICY.md`  
2. `09_Developer_Implementation_Pack/00_MASTER_DEVELOPER_HANDOFF.md`  
3. `00_Competitor_MySarkariNaukri/IMPLEMENTATION_INDEX.md`  
4. Per-page `DEVELOPER_INSTRUCTIONS.md` + `PAGE_COPY.md` in each `08_Standalone_Pages/*/`  
5. P0: `01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md`

---

## 6. Sitemap after new pages (additive)

When new hubs go live, **add** to `sitemap-static.xml` (or appropriate child):

- `/employment-news`  
- `/answer-keys`  
- `/exam-syllabus-patterns` (or canonical `/exams` only — one URL)  
- `/guide/government-jobs-2026`  
- `/state-government-jobs`  

Do **not** remove existing sitemap entries.
