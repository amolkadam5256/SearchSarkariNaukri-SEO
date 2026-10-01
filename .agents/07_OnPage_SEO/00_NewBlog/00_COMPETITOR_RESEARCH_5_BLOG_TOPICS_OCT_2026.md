# Competitor blog research + 5 new topics (Oct 2026)

**Purpose:** Gap analysis for SearchSarkariNaukri blog cluster — high-intent keywords, AEO/GEO/SEO, no cannibalization with existing posts in `00_NewBlog/`.

---

## What competitors publish (patterns, not copy)

| Source type | Typical blog formats | Intent they capture |
|-------------|---------------------|---------------------|
| Aggregators (FreeJobAlert-style, DailyGKUpdate) | Daily/weekly “active jobs” tables, last-date roundups | `latest government jobs`, deadline urgency |
| Exam niche sites (EducationIdol, SarkariJobs.com) | “Top 5 jobs this week”, single-exam apply guides | SSC CHSL, RRB NTPC, bank apprentice |
| Employment News / PIB-driven sites | Notification explainers + official links | Trust + freshness |
| Qualification hubs | 10th/12th/graduate long pages | Long-tail qualification SEO |

**SSN already has:** 10th pass, ITI trade (Fitter, Electrician), Maharashtra/Pune/Nagpur, gazetted officer, IOCL, ZP Nashik, UPI news, daily quiz, “latest sarkari naukri 2026” pillar.

**Gaps (Oct 2026):** Timely **apply guides** for open forms (SSC CHSL, RRB NTPC Graduate), **12th pass** pillar (only 10th exists), **bank apprentice** cluster, **age limit / relaxation** evergreen (supports `/age-calculator`).

---

## Five recommended topics (one primary keyword each)

| # | Folder | Primary keyword | Why now |
|---|--------|-----------------|---------|
| 18 | `18_SSC_CHSL_2026_Apply_Online_Guide/` | SSC CHSL 2026 apply online | High volume; application window active Oct 2026 |
| 19 | `19_RRB_NTPC_Graduate_Recruitment_2026/` | RRB NTPC graduate recruitment 2026 | CEN-style railway graduate hiring; strong search + Maharashtra interest |
| 20 | `20_12th_Pass_Sarkari_Naukri_2026/` | 12th pass Sarkari Naukri 2026 | Qualification pillar; complements existing 10th pass blog |
| 21 | `21_Bank_Apprentice_Jobs_2026/` | bank apprentice jobs 2026 | Canara-scale apprentice drives; links banking hub |
| 22 | `22_Age_Limit_Government_Jobs_2026/` | age limit for government jobs | Evergreen; supports eligibility + age calculator |

**Do not target on these posts:** full “Sarkari Result” pages (use `/results`), admit card downloads as primary (`/admit-cards`).

---

## Publishing checklist (every blog)

- [ ] Title ≤60 chars (site cap); meta 150–160 chars  
- [ ] Single H1; H2/H3 sequential  
- [ ] Direct answer in first 100 words (AEO)  
- [ ] Quick Facts table (GEO entity block)  
- [ ] No invented vacancies/dates — “check official notification” where live data not in CMS  
- [ ] 12–18 internal links (jobs, job-updates, exams, guide, state directory, related blogs)  
- [ ] FAQ 10+ with visible FAQPage JSON-LD  
- [ ] BlogPosting + BreadcrumbList + WebPage  
- [ ] Featured image 1200×630, descriptive alt  
- [ ] Disclaimer: independent portal, not government  
- [ ] Add slug to `sitemap-blogs.xml` on publish  

---

## Internal link map (reuse across cluster)

| Page | Use when |
|------|----------|
| `/jobs` | Browse vacancies |
| `/job-updates` | Alerts + closing soon |
| `/guide/government-jobs-2026` | Full apply steps |
| `/state-government-jobs` | State-wise |
| `/exam-syllabus-patterns` | Pattern/syllabus |
| `/exams/ssc-cgl`, `/exams/ssc-chsl` (or SSC exam routes) | Exam hubs |
| `/exams/rrb-ntpc` | Railway |
| `/exams/sbi-po-clerk` | Banking |
| `/eligibility-checker`, `/age-calculator` | Tools |
| `/admit-cards`, `/results`, `/exam-calendar` | Post-apply |
| `/districts`, `/blogs` | GEO + cluster |

---

## Files created

1. `18_SSC_CHSL_2026_Apply_Online_Guide/18_ssc-chsl-2026-apply-online-guide.md`
2. `19_RRB_NTPC_Graduate_Recruitment_2026/19_rrb-ntpc-graduate-recruitment-2026.md`
3. `20_12th_Pass_Sarkari_Naukri_2026/20_12th-pass-sarkari-naukri-2026.md`
4. `21_Bank_Apprentice_Jobs_2026/21_bank-apprentice-jobs-2026.md`
5. `22_Age_Limit_Government_Jobs_2026/22_age-limit-government-jobs-2026.md`

Update `00_GSC_AEO_BLOG_CLUSTER_INDEX.md` after CMS publish.
