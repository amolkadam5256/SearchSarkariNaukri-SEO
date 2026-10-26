# 🚀 SearchSarkariNaukri.com — Complete SEO Master Checklist & Implementation Tracker

> **Website:** https://www.searchsarkarinaukri.com/  
> **Tracker Created:** 26 October 2026  
> **SEO Developer:** Amol Kadam / Growthik Media  
> **Last Audit Snapshot:** 29 September 2026 (497 indexed · 2,196 not indexed · 12 clicks)  
> **Production Codebase:** `C:\Users\Administrator\Projects\SakariNaukariN`  
> **Rule:** All fixes are additive/corrective only — NO deletion of pages, jobs, content, DB records, nav/footer links.

---

## 📂 Project Files Index (All Related Files in This Repo)

| File / Folder | What It Contains |
|---|---|
| [`SEO_Audit_Review_2026-08-25/`](SEO_Audit_Review_2026-08-25/) | Full SEO/AEO/GEO audit from Aug 25, 2026 — crawl data, screenshots, reports |
| [`SEO_Audit_Review_2026-08-25/outputs/final-reports/`](SEO_Audit_Review_2026-08-25/outputs/final-reports/) | Executive summary across all 13 audit areas |
| [`SEO_Audit_Review_2026-08-25/outputs/remediation/`](SEO_Audit_Review_2026-08-25/outputs/remediation/) | What developers fixed, deployed and verified in Aug 2026 |
| [`SEO_Audit_Review_2026-09-29/COMPLETE_SEO_GEO_AEO_AUDIT_AND_FIX_PLAN.md`](SEO_Audit_Review_2026-09-29/COMPLETE_SEO_GEO_AEO_AUDIT_AND_FIX_PLAN.md) | Sep 29 full audit — critical problems, fix plan, validation |
| [`SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md`](SEO_Audit_Review_2026-09-29/01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md) | Step-by-step developer fix handoff (P0 regressions) |
| [`SEO_Audit_Review_2026-09-29/FIX_TRACKER_NO_DELETE.csv`](SEO_Audit_Review_2026-09-29/FIX_TRACKER_NO_DELETE.csv) | Finding-by-finding before/after status tracker |
| [`SEO_Audit_Review_2026-09-29/live_seo_regression_check.py`](SEO_Audit_Review_2026-09-29/live_seo_regression_check.py) | Run live validation: `python SEO_Audit_Review_2026-09-29/live_seo_regression_check.py` |
| [`tools/generate_blog_package_audit.py`](tools/generate_blog_package_audit.py) | Blog SEO audit generator script |
| [`SearchSarkariNaukri-Keyword-List-899.xlsx`](SearchSarkariNaukri-Keyword-List-899.xlsx) | 899 keywords — primary target list |
| [`SearchSarkariNaukri_Keyword_Research.xlsx`](SearchSarkariNaukri_Keyword_Research.xlsx) | Full keyword research data |
| [`www.searchsarkarinaukri.com_SearchPerformanceOverview_All_8_7_2026.csv`](www.searchsarkarinaukri.com_SearchPerformanceOverview_All_8_7_2026.csv) | GSC search performance export (July–Aug 2026) |
| [`BLOG_ITI_GOVERNMENT_JOBS_MAHARASHTRA_2026.md`](BLOG_ITI_GOVERNMENT_JOBS_MAHARASHTRA_2026.md) | Sample blog content for ITI govt jobs |
| [`ACCOUNT_SETUP_IMPLEMENTATION_GUIDE.docx`](ACCOUNT_SETUP_IMPLEMENTATION_GUIDE.docx) | GA4 / GSC / analytics account setup guide |
| [`SearchSarkariNaukri_Enterprise_SEO_Master_Documentation.docx`](SearchSarkariNaukri_Enterprise_SEO_Master_Documentation.docx) | Enterprise SEO master documentation |
| [`SEO_Performance_Audit_07_08_26.pptx`](SEO_Performance_Audit_07_08_26.pptx) | SEO performance audit presentation (Aug 2026) |
| [`SearchSarkariNaukri_SEO_Performance_Report_27_Aug2026.pptx`](SearchSarkariNaukri_SEO_Performance_Report_27_Aug2026.pptx) | SEO performance report deck (Aug 27, 2026) |

---

## 🔴 CURRENT LIVE CRITICAL ISSUES (As of Sep 29, 2026)

> These must be fixed BEFORE implementing anything else on the real site.

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| R1 | `/sitemap.xml` returns HTTP 500 — Google cannot discover URLs | 🔴 CRITICAL | ❌ NOT FIXED |
| R2 | Job slug ≠ content (e.g. Canara Bank URL shows ESIC/NHSRCL content) | 🔴 CRITICAL | ❌ NOT FIXED |
| R3 | JobPosting schema: 0 valid in GSC — no Google Jobs eligibility | 🔴 CRITICAL | ❌ NOT FIXED |
| R4 | 613 job URLs returning 404 in GSC | 🔴 CRITICAL | ❌ NOT FIXED |
| R5 | 2,196 URLs not indexed vs 497 indexed (82% not indexed) | 🔴 CRITICAL | ❌ NOT FIXED |
| R6 | 2,785 broken internal links → 462 dead link targets | 🟠 HIGH | ❌ NOT FIXED |
| R7 | 3,111 sitemap URLs with zero internal inlinks (orphan pages) | 🟠 HIGH | ❌ NOT FIXED |

---

## 📊 SEO Health Dashboard

| Metric | Sep 2026 Value | Target |
|--------|---------------|--------|
| GSC Clicks | 12 | 500+ |
| Indexed URLs | 497 | 800–1,200 |
| Not Indexed | 2,196 | < 400 |
| Sitemap Status | 500 ERROR | 200 OK |
| JobPosting Valid | 0 | All active jobs |
| Broken Internal Links | 2,785 | 0 |
| Duplicate Titles | 764 | 0 |
| Duplicate Meta Descriptions | 719 | 0 |
| Duplicate H1 Groups | 789 | 0 |
| Thin Pages (<150 words) | 557 | 0 |
| Core Web Vitals (Mobile LCP) | ~8.5s | < 2.5s |
| Breadcrumb Schema Valid | 22 | All pages |

---

---

# ✅ FULL 244-ITEM SEO CHECKLIST

> **How to use this file:**
> - Change `[ ]` to `[x]` when completed
> - Add `Date:` and `Owner:` on the same line when marking done
> - Track blockers with `[~]` = In Progress, `[!]` = Blocked
> - **Do NOT run changes blindly** — use GSC data + live crawl to confirm issue exists first

---

## PHASE 1 — Fix Technical Blockers 🔧
*Do this first. Nothing else matters until the site is crawlable and indexable.*

---

### 1. Technical SEO (18 items)

- [ ] **1.1** Verify HTTPS on every page and redirect HTTP to HTTPS
- [ ] **1.2** Choose one canonical hostname (www or non-www) — www is canonical, enforce 301 from apex
- [ ] **1.3** Ensure HTTP status codes are correct: 200, 301, 404, 410, 500
- [ ] **1.4** Remove redirect chains and redirect loops — check `/jobs?district_slug=pune` → `/districts/pune` single-hop
- [ ] **1.5** 🔴 Fix sitemap index — currently returning 500; restore from Aug 25 baseline; submit all child sitemaps returning 200
- [ ] **1.6** Exclude login, dashboard, internal search (`?search=`, `?category=`), and low-value pages from indexing
- [ ] **1.7** Check robots.txt — ensure important CSS/JS are crawlable — verify no new blocks added
- [ ] **1.8** Set canonical URLs on all indexable pages — self-canonical on all 200 indexable pages
- [ ] **1.9** Find and fix accidental noindex tags on valuable pages — 56 noindex URLs in GSC, review each; index hubs, keep noindex on thin/filter pages
- [ ] **1.10** 🔴 Fix broken internal links — 2,785 broken links, 462 dead targets — fix district slug generator; update link builder
- [ ] **1.11** Ensure important content (job title, org, dates, eligibility) is available in rendered HTML — prerender for Googlebot, verify parity for all bots
- [ ] **1.12** Check pagination crawlability — `/jobs` has 77 pages; ensure `?page=N` in `<a href>` tags
- [ ] **1.13** Verify mobile-first rendering and responsive layouts — viewport OK; fix touch targets and notification overlay
- [ ] **1.14** Check duplicate URLs from query params, filters, trailing slashes — robots blocks search/category params; enforce trailing slash 301
- [ ] **1.15** Use consistent URL naming — lowercase hyphen slugs only; fix 1,312 URLs > 115 chars with 301
- [ ] **1.16** Create a useful custom 404 page with links to popular sections
- [ ] **1.17** 🔴 Check redirect behavior for deleted/renamed jobs — use 301 from old slug to new canonical; 410 only for truly removed; NEVER mass redirect to homepage
- [ ] **1.18** Check server logs for excessive bot crawling and crawl traps — 419 invalid district path patterns in crawl; block with robots or 404

**Progress: ___/18 completed**

---

### 2. Google Indexing & Search Console (14 items)

- [ ] **2.1** Verify the domain property in Google Search Console — domain property preferred over URL prefix
- [ ] **2.2** 🔴 Submit the XML sitemap and monitor processing errors — Fix 500 first, then resubmit
- [ ] **2.3** Inspect homepage and representative page templates with URL Inspection tool
- [ ] **2.4** Review Page Indexing exclusions and errors — 2,196 not indexed; classify each reason before acting
- [ ] **2.5** Fix "Discovered – currently not indexed" pages — 896 admit-card/numeric job URLs; add unique content + internal links
- [ ] **2.6** Investigate "Crawled – currently not indexed" pages individually — 136 URLs; thin/duplicate; improve or noindex intentionally
- [ ] **2.7** Check "Duplicate, Google-selected canonical" vs user-declared canonical differences
- [ ] **2.8** Review manual actions and security issues in GSC — check for any manual penalties
- [ ] **2.9** Monitor search impressions, clicks, CTR, and average position — currently 12 clicks; critically low
- [ ] **2.10** Review Core Web Vitals reports — no field data yet; optimize mobile LCP from ~8.5s
- [ ] **2.11** Check Googlebot access to important pages via URL Inspection — test homepage, 1 active job, 1 hub, 1 admit card
- [ ] **2.12** Monitor sitemap URLs against indexable, canonical URLs — ensure sitemap only includes 200, self-canonical, index,follow URLs
- [ ] **2.13** Remove obsolete sitemap URLs and stale job listings — expired jobs: remove from XML sitemap only; keep page live
- [ ] **2.14** Validate fixes and request recrawling — request validation per issue type, not entire site

**Progress: ___/14 completed**

---

## PHASE 2 — Optimize Important Pages 📄
*Start with homepage, quiz, major exam guides, latest jobs, current-affairs hub.*

---

### 3. On-Page SEO (15 items)

- [ ] **3.1** Assign unique, descriptive title tag to each important page — 764 duplicate titles; fix with pattern: `[Org] [Post] [Year] – [Eligibility] | Search Sarkari Naukri`
- [ ] **3.2** Write compelling meta description for key pages — 719 duplicate descriptions; regenerate from job record fields
- [ ] **3.3** Use one clear, visible H1 matching search intent — 789 URLs in duplicate H1 groups; fix at template level
- [ ] **3.4** Organize content using logical H2 and H3 headings — job pages: use H2 for Eligibility, Vacancy, Dates, Apply
- [ ] **3.5** Place main topic naturally in title, H1, and introduction
- [ ] **3.6** Use descriptive URLs without unnecessary parameters — fix 1,312 URLs > 115 chars; slug must match H1 and content
- [ ] **3.7** Add useful alt text to meaningful images — not keyword-stuffed; descriptive only
- [ ] **3.8** Compress images and use WebP or AVIF formats — blog covers > 1.1 MB median; compress and convert
- [ ] **3.9** Use descriptive anchor text for internal links — already good per crawl; maintain standard
- [ ] **3.10** Add breadcrumbs on deep pages — BreadcrumbList: 22 valid in GSC; roll consistently to all pages
- [ ] **3.11** Avoid duplicate titles, descriptions, and boilerplate introductions
- [ ] **3.12** Answer visitor's main question early on the page — job pages: show eligibility/vacancy/dates above fold
- [ ] **3.13** Add last-updated dates only when content is genuinely reviewed — no fake date updates
- [ ] **3.14** Ensure buttons, forms, and quiz entry points work correctly — test on mobile
- [ ] **3.15** Make primary calls to action clear without obstructing content — fix notification overlay; delay/dismiss control

**Progress: ___/15 completed**

---

### 4. Keyword Research & Search Intent (12 items)

- [ ] **4.1** Build a keyword map for every main URL — use 899 keyword list + GSC Performance queries
- [ ] **4.2** Identify informational, navigational, commercial, and transactional intent per page
- [ ] **4.3** Research queries using GSC, keyword tools, and SERP analysis — use GSC export CSV
- [ ] **4.4** Map primary and secondary keywords to relevant pages — use `SearchSarkariNaukri_Keyword_Research.xlsx`
- [ ] **4.5** Identify long-tail queries and question-based searches — quiz, exam eligibility, admit card, result queries
- [ ] **4.6** Separate overlapping pages targeting the same intent — avoid cannibalization between job category pages
- [ ] **4.7** Research Hindi, Marathi, and English query variations — sarkari naukri, सरकारी नोकरी, Maharashtra jobs, etc.
- [ ] **4.8** Identify seasonal demand: MPSC exam cycle, UPSC calendar, admit cards, results — publish timely pages before exam events
- [ ] **4.9** Study competitor page structures and content gaps — see `SEO_Audit_Review_2026-09-29/02_COMPETITOR_MYSARKARINAUKRI_SUMMARY.md`
- [ ] **4.10** Prioritize topics by relevance, opportunity, traffic potential, business value
- [ ] **4.11** Create dedicated landing pages only when serving distinct user need — MPSC, Railway, 10th pass jobs, Banking hubs already exist; strengthen them
- [ ] **4.12** Avoid creating pages solely for minor keyword variations — no thin programmatic variants

**Progress: ___/12 completed**

---

### 5. Content SEO & E-E-A-T (17 items)

- [ ] **5.1** Homepage: preserve Quick Answers, FAQ block, official-source messaging — extend, do not remove
- [ ] **5.2** Job pages: median ~196 words — acceptable if structured facts complete; ensure match between URL and official source
- [ ] **5.3** Fix near-duplicate content — 550 exact + 1,955 > 80% body pairs — dedupe at DB level for admit/result/job clones
- [ ] **5.4** Fix 557 thin pages (< 150 words) — expand or noindex intentionally
- [ ] **5.5** Fix naming drift: "SearchSarkariNaukri" vs "LyfJobs" in legacy copy — align title, H1, schema, breadcrumbs
- [ ] **5.6** Map consistent entities: Organization → Recruitment → Post → Qualification → Location → Exam → Deadline → Official URL
- [ ] **5.7** Add explicit "Source / Last Updated / Application Status" block on every job — visible, crawlable
- [ ] **5.8** Add/maintain editorial policy, corrections policy, disclaimer pages — ensure linked from footer
- [ ] **5.9** No fake authors — real editorial accountability only
- [ ] **5.10** Privacy, terms, contact pages present — keep and strengthen with specific policy details
- [ ] **5.11** Soft 404 landing pages (81 with "0 jobs") — add copy, historical links, related hubs, FAQs (150+ words unique copy)
- [ ] **5.12** Hub pages (MPSC, Railway, Banking, Police, Maharashtra Districts) — unique introductions per hub; add topic cluster links
- [ ] **5.13** Blog content: ensure unique headlines, dates, publisher, canonical; avoid numeric-only news slugs
- [ ] **5.14** Current affairs pages: publish timely, verifiable information with official source citations
- [ ] **5.15** No hidden accordions for critical eligibility/dates — ensure facts in static HTML
- [ ] **5.16** Avoid template FAQ repetition across programmatic pages — only add FAQs with verified facts
- [ ] **5.17** Exam guide pages: ensure syllabus, pattern, eligibility are complete and up to date

**Progress: ___/17 completed**

---

## PHASE 3 — Build Topical Authority 🔗
*Connect job, state, district, exam, syllabus, quiz, and current-affairs pages into topic clusters.*

---

### 6. Technical Performance & Core Web Vitals (13 items)

- [ ] **6.1** Fix mobile LCP — currently ~8.5s; target < 2.5s — optimize LCP image + defer noncritical JS
- [ ] **6.2** Do NOT remove homepage SEO sections (Quick Answers, FAQs) to chase performance scores
- [ ] **6.3** Fix notification overlay — delay and add dismiss control — Aug audit finding; do not redesign UI
- [ ] **6.4** Defer noncritical JavaScript; keep critical job data in initial HTML
- [ ] **6.5** Compress and convert images to WebP/AVIF — blog covers > 1.1 MB; high priority
- [ ] **6.6** Add `width` and `height` attributes to images to prevent CLS
- [ ] **6.7** Implement lazy loading for images below the fold
- [ ] **6.8** Increase nginx proxy timeout for `/sitemap*.xml` if DB is slow
- [ ] **6.9** Improve universal SSR for critical job detail routes — currently CSR shell for ordinary user agents
- [ ] **6.10** Fix touch targets on mobile — Aug audit finding
- [ ] **6.11** Run Google PageSpeed Insights on homepage, one job page, one hub page monthly
- [ ] **6.12** Monitor CWV field data in GSC once traffic increases
- [ ] **6.13** Ensure prerender parity between Googlebot and other user agents

**Progress: ___/13 completed**

---

### 7. Internal Linking & Site Architecture (18 items)

- [ ] **7.1** 🔴 Fix district slug link builder — repair 462 broken internal link targets (district slug pollution)
- [ ] **7.2** 🔴 Add inlinks for 3,111 orphan sitemap URLs — link from existing hub categories, departments, qualifications, districts
- [ ] **7.3** Use descriptive anchor text for all internal links — already good per crawl; maintain
- [ ] **7.4** Connect MPSC cluster: /department/mpsc → exam guides → current affairs → quiz → jobs
- [ ] **7.5** Connect Railway/RRB cluster: hub → syllabus → admit card → result → jobs
- [ ] **7.6** Connect Banking/IBPS cluster: hub → bank-wise pages → eligibility → jobs
- [ ] **7.7** Connect Police cluster: Maharashtra Police → state-wise → district-wise → jobs
- [ ] **7.8** Connect qualification ladders: 10th pass → 12th pass → graduate → postgraduate → jobs
- [ ] **7.9** Connect district/location clusters: `/jobs-in-pune`, `/jobs-in-mumbai`, etc. → active job listings
- [ ] **7.10** Link active "Latest Jobs" section on homepage to all individual job pages — verify slug integrity first (R2 fix)
- [ ] **7.11** Add "Related Jobs" section on job detail pages linking to same org/category/location
- [ ] **7.12** Add breadcrumbs on all job, hub, exam, quiz, and blog pages
- [ ] **7.13** Avoid orphan pages — every indexable URL must have at least 2 inlinks from relevant pages
- [ ] **7.14** Ensure pagination links use `<a href>` — do not block via JavaScript
- [ ] **7.15** Add "See all [Category] jobs" links from hub pages to paginated job listings
- [ ] **7.16** Link quiz pages from current affairs, exam guide, and department hub pages
- [ ] **7.17** Link admit card and result pages from their corresponding exam hub pages
- [ ] **7.18** Verify redirect `/jobs?district_slug=pune` → 301 → `/districts/pune` — single hop, no chain

**Progress: ___/18 completed**

---

### 8. Structured Data & Schema Markup (15 items)

- [ ] **8.1** 🔴 JobPosting schema — emit only on active jobs with `validThrough` end-of-day IST; remove on expired jobs — currently 0 valid in GSC
- [ ] **8.2** JobPosting required fields: `title`, `description`, `datePosted`, `validThrough`, `hiringOrganization`, `jobLocation`, `employmentType`, official application URL
- [ ] **8.3** Expired jobs: remove JobPosting JSON-LD; keep page live with "deadline passed" banner
- [ ] **8.4** NEVER emit JobPosting when page content does not match the recruitment — current live bug; fix R2 first
- [ ] **8.5** BreadcrumbList — roll consistently to all pages — 22 valid in GSC sample; extend to all
- [ ] **8.6** FAQPage — homepage only; do NOT mass-deploy fake FAQs on programmatic pages
- [ ] **8.7** Organization schema — add verified `sameAs` social profile URLs — currently empty
- [ ] **8.8** WebSite SearchAction — remove duplicate block on homepage — Aug finding
- [ ] **8.9** 🔴 Remove invalid same-URL hreflang — `en/mr/x-default` on identical URL is invalid; set correct `html lang` attribute instead
- [ ] **8.10** NewsArticle/BlogPosting on news/blog templates — ensure unique headlines, datePublished, publisher, canonical
- [ ] **8.11** No VideoObject unless actual embedded official video content exists
- [ ] **8.12** Test with Rich Results Test after every schema change: https://search.google.com/test/rich-results
- [ ] **8.13** Validate schema vocabulary at https://validator.schema.org/
- [ ] **8.14** Monitor GSC Enhancements tab for JobPosting, Breadcrumbs, FAQ status weekly
- [ ] **8.15** Do not use schema types that Google does not officially support for rich results

**Progress: ___/15 completed**

---

## PHASE 4 — Improve AEO and GEO 🤖
*Make answers concise, verifiable, with source attribution. Structure content for AI search.*

---

### 9. GEO — Generative Engine Optimization (15 items)

- [ ] **9.1** 🔴 Fix wrong job on wrong URL FIRST — mismatched job content destroys AI citation trust — fix R2 before all GEO work
- [ ] **9.2** Add explicit "Source / Last Updated / Application Status" block on every job — visible, in static HTML, crawlable
- [ ] **9.3** Ensure all critical facts (eligibility, dates, vacancy count, official URL) are in static HTML — NOT JavaScript-rendered only
- [ ] **9.4** Add clear site identity block: site name, independence disclaimer, editorial accountability
- [ ] **9.5** Official source links on every job: `Apply Here → [Official Website URL]`
- [ ] **9.6** Labeled entity facts on job templates: Organization, Post Name, Qualification, Last Date, Salary, Location
- [ ] **9.7** No hidden content in accordions for critical facts — AI engines may not expand JS accordions
- [ ] **9.8** Maintain HSTS and HTTPS — trust signals for AI citation eligibility
- [ ] **9.9** Add concise definitional sentence at top of every hub page (what is MPSC, what is Railway recruitment, etc.)
- [ ] **9.10** Publish information with genuine value beyond competitor pages — original analysis, official data, not just copy
- [ ] **9.11** Organization `sameAs` with Wikipedia, Wikidata, official social profiles where available
- [ ] **9.12** Ensure page structure is clear: H1 → structured facts → details → official link → related content
- [ ] **9.13** No keyword stuffing — clean, factual, verifiable language for AI trust
- [ ] **9.14** Update stale content regularly — expired/outdated pages hurt AI citation eligibility
- [ ] **9.15** GEO and AEO are complementary, NOT guaranteed — focus on truth, accuracy, and structure

**Progress: ___/15 completed**

---

### 10. AEO — Answer Engine Optimization (12 items)

- [ ] **10.1** Homepage FAQ block + Quick Answers (12+ questions) — preserve and extend — current win; do not remove
- [ ] **10.2** Per-job FAQs must use verified facts only — no template FAQ repetition across programmatic pages
- [ ] **10.3** Format: Question H2/H3 → direct answer first → details table → official source
- [ ] **10.4** Answer user's main question at the top of each page — eligibility, vacancy, dates above fold
- [ ] **10.5** Quiz pages: add "What is the answer?" block with explanation — structured for featured snippet
- [ ] **10.6** Hub pages: add "How to apply for [Org] recruitment?" FAQ section with step-by-step answer
- [ ] **10.7** Exam guides: add "What is the [Exam] syllabus?" and "What is the eligibility?" FAQ sections
- [ ] **10.8** Current affairs: structure as Question → Answer → Source
- [ ] **10.9** State/district job pages: add "Which government jobs are available in [State/District]?" FAQ
- [ ] **10.10** Use tables for structured data (salary, eligibility, vacancies, important dates) — AI engines extract tables
- [ ] **10.11** Ensure FAQ content is in static HTML — not loaded via JavaScript/AJAX
- [ ] **10.12** Monitor if pages appear in AI Overviews / Perplexity / Gemini — track as new KPI

**Progress: ___/12 completed**

---

### 11. External Links, Backlinks & Authority (12 items)

- [ ] **11.1** Maintain HTTPS — all external links should point to HTTPS versions of official sites
- [ ] **11.2** Link to official government portals on every job page — already present; maintain
- [ ] **11.3** Editorial/disclaimer on homepage — independence from government — already present; keep
- [ ] **11.4** Fill `Organization.sameAs` with verified social profiles — LinkedIn, Twitter/X, Facebook
- [ ] **11.5** Fix any broken outbound links to official government websites — annual check
- [ ] **11.6** Pursue editorial mentions from Maharashtra government job news portals — off-page outreach
- [ ] **11.7** Submit to relevant government job directories — only reputable, relevant directories
- [ ] **11.8** Build links from educational institutions discussing MPSC/UPSC preparation
- [ ] **11.9** Monitor referring domains monthly — use Ahrefs or Semrush
- [ ] **11.10** Monitor toxic/spammy backlinks and disavow if necessary
- [ ] **11.11** No paid link schemes — only editorial, organic links
- [ ] **11.12** Track referring domains as a KPI — not raw link count

**Progress: ___/12 completed**

---

## PHASE 5 — Measure and Improve 📈
*Track organic clicks, impressions, indexed URLs, quiz completions, referrals. Review monthly.*

---

### 12. Job Portal SEO (13 items)

- [ ] **12.1** 🔴 Active jobs only in XML job sitemap — expired jobs must be excluded from sitemap; page stays live
- [ ] **12.2** 🔴 JobPosting on active jobs only — verify `validThrough` is not in the past
- [ ] **12.3** Expired jobs: show "Deadline Passed" / "Applications Closed" banner; keep page; remove JobPosting
- [ ] **12.4** Job URL slug must always match job H1, organization, and content — critical trust + ranking factor
- [ ] **12.5** Job title format: `[Org] [Post Name] Recruitment [Year] — [Vacancy/Eligibility] | Search Sarkari Naukri`
- [ ] **12.6** Resolve 613 job 404s: restore valid jobs to 200; redirect old numeric URLs to canonical slug; 410 for removed
- [ ] **12.7** Batch-link orphan jobs from category, department, district, qualification hubs
- [ ] **12.8** "Apply Now" button must link directly to official government application portal
- [ ] **12.9** "Application Status" field — Active / Closed / Results Announced / Admit Card Released
- [ ] **12.10** Structured data for active jobs: rich results eligibility test monthly
- [ ] **12.11** Admit card pages (896 discovered-not-indexed) — add unique content, FAQs, hub links, canonical
- [ ] **12.12** Result pages — unique structured content, links to next step (next exam, next recruitment)
- [ ] **12.13** Avoid creating purely numeric job URLs — always use descriptive slug with ID suffix (`--{id}`)

**Progress: ___/13 completed**

---

### 13. Exam, Quiz & Educational SEO (12 items)

- [ ] **13.1** MPSC hub: link to syllabus, previous papers, current vacancies, admit cards, results, news
- [ ] **13.2** UPSC hub: link to all UPSC exam types, eligibility, calendar, preparation resources
- [ ] **13.3** Railway/RRB hub: link to all RRB zones, exam types, admit cards, results
- [ ] **13.4** Daily UPSC & MPSC Quiz: ensure quiz is linked from homepage, MPSC hub, current affairs, exam guides
- [ ] **13.5** Quiz pages: add schema for quiz questions if structured Q&A format is used
- [ ] **13.6** Exam syllabus pages: structured table format for subjects, marks, duration
- [ ] **13.7** Previous year question papers: link from exam hub; ensure PDFs have accessible text
- [ ] **13.8** Current affairs hub: publish weekly/monthly roundups with official source citations
- [ ] **13.9** Admit card release: publish timely before exam date; link from exam hub; include official download link
- [ ] **13.10** Result pages: publish on result date; link from exam hub, admit card page, and current affairs
- [ ] **13.11** Hindi/Marathi exam content: identify top Marathi exam queries; create dedicated content
- [ ] **13.12** Link quiz pages in article content where relevant to exam preparation topics

**Progress: ___/12 completed**

---

### 14. Images, Accessibility & UX (13 items)

- [ ] **14.1** Compress all images — blog covers > 1.1 MB; target < 150 KB per image
- [ ] **14.2** Convert images to WebP or AVIF format
- [ ] **14.3** Add `width` and `height` to all `<img>` tags to prevent layout shift (CLS)
- [ ] **14.4** Add descriptive `alt` text to all meaningful images — not keyword-stuffed
- [ ] **14.5** Empty `alt=""` on purely decorative images
- [ ] **14.6** Lazy load images below the fold with `loading="lazy"`
- [ ] **14.7** Fix notification/push prompt overlay — delay display and provide clear dismiss control on mobile
- [ ] **14.8** Fix touch target sizes on mobile — buttons/links must be at least 48x48px
- [ ] **14.9** Ensure sufficient color contrast on all text elements — accessibility requirement
- [ ] **14.10** Keyboard navigation must work for all forms, buttons, quizzes
- [ ] **14.11** Forms: clear labels, error messages, and validation feedback
- [ ] **14.12** Test with Microsoft Clarity for UX diagnostics — heatmaps, session recordings
- [ ] **14.13** Ensure all interactive elements have descriptive ARIA labels where needed

**Progress: ___/13 completed**

---

### 15. International & Multilingual SEO (9 items)

- [ ] **15.1** 🔴 Remove invalid same-URL hreflang — `en/mr/x-default` on identical URL is an error
- [ ] **15.2** Set accurate `html lang` attribute per page — use dominant language of content
- [ ] **15.3** For mixed EN/MR pages: use `lang="en"` if majority English, `lang="mr"` if majority Marathi
- [ ] **15.4** Separate hreflang implementation only when truly separate Marathi-language URLs are launched
- [ ] **15.5** Include Marathi search terms naturally in copy where relevant — e.g., सरकारी नोकरी, महाराष्ट्र
- [ ] **15.6** Do NOT create separate language duplicate pages unless separate URLs with unique Marathi content
- [ ] **15.7** Research top Marathi queries in GSC and create targeted content if volume justifies it
- [ ] **15.8** Maintain bilingual intent signaling — English URLs with Marathi/Hindi context in content body
- [ ] **15.9** Document multilingual strategy decision in `.agents/` folder for developer reference

**Progress: ___/9 completed**

---

### 16. Analytics, Conversion & Monitoring (14 items)

- [ ] **16.1** Verify GA4 tracking on all pages — see `ACCOUNT_SETUP_IMPLEMENTATION_GUIDE.docx`
- [ ] **16.2** Set up organic traffic goal in GA4 — track clicks from GSC
- [ ] **16.3** Track quiz completions as GA4 conversion event
- [ ] **16.4** Track "Apply Now" external link clicks as GA4 events
- [ ] **16.5** Track user registrations as GA4 conversion event
- [ ] **16.6** Set up Microsoft Clarity — connect with GA4 for session heatmaps
- [ ] **16.7** Set up GSC Performance report — filter by country (India), device (mobile), and date
- [ ] **16.8** Set up Bing Webmaster Tools — submit sitemap when GSC sitemap is fixed
- [ ] **16.9** Create monthly SEO review dashboard: impressions, clicks, CTR, avg position, indexed URLs
- [ ] **16.10** Track Core Web Vitals field data in GSC — set alert for significant regressions
- [ ] **16.11** Track referring domains monthly — Ahrefs or Semrush; not raw link count
- [ ] **16.12** Set up rank tracking for top 50 priority keywords from the 899-keyword list
- [ ] **16.13** Document success metrics — target: 500+ clicks/month by Q1 2027
- [ ] **16.14** Monthly report: indexed count, impressions, clicks, top 10 queries, top 10 pages

**Progress: ___/14 completed**

---

### 17. Sitemap, Content Maintenance & Governance (12 items)

- [ ] **17.1** 🔴 Sitemap architecture (when fixed): index → static, jobs, locations, qualifications, departments, news, blogs, results, admit-cards, districts
- [ ] **17.2** Include only: 200, self-canonical, index,follow, meaningful lastmod URLs
- [ ] **17.3** Exclude: 404, 410, noindex, redirects, expired jobs, empty news sitemap
- [ ] **17.4** Weekly: publish/refresh active jobs; remove expired from sitemap (keep page); inspect top hubs in GSC
- [ ] **17.5** Monthly: duplicate title report; external official link check; orphan link pass
- [ ] **17.6** Quarterly: programmatic SEO review — add landing pages only when search demand + unique copy justified
- [ ] **17.7** Quarterly: content audit — identify thin pages to expand, outdated pages to update/noindex
- [ ] **17.8** Clamp `lastmod` dates — never future dates in sitemap
- [ ] **17.9** Aim for 800–1,200 strong indexed URLs (jobs + hubs + exams + news) — NOT 4,000+ weak ones
- [ ] **17.10** Govern programmatic URL creation — avoid uncontrolled district x category x qualification combinations
- [ ] **17.11** Non-indexable: arbitrary `/jobs?qualification=&state=` combos unless built as dedicated landing pages with unique intro + jobs + FAQs
- [ ] **17.12** Document content publishing workflow in `.agents/` folder with SEO requirements for each content type

**Progress: ___/12 completed**

---

### 18. Security & Trust (10 items)

- [ ] **18.1** Maintain HTTPS / HSTS — currently good; verify no mixed content
- [ ] **18.2** Privacy Policy — present and linked from footer — already present; keep
- [ ] **18.3** Terms of Service — present and linked from footer — already present; keep
- [ ] **18.4** Contact page — present; verify still accessible and functional
- [ ] **18.5** Editorial/disclaimer — independence from government — present on homepage; maintain
- [ ] **18.6** Corrections policy — document how inaccurate job info is updated — add to footer or editorial page
- [ ] **18.7** No fake authors — real bylines or organizational attribution only
- [ ] **18.8** Secure admin/login pages — confirm not crawlable by Googlebot
- [ ] **18.9** Monitor for content injection, spam links in user-generated sections
- [ ] **18.10** Verify API endpoints are not exposed to public crawlers — robots.txt disallows `/api/`; confirm

**Progress: ___/10 completed**

---

---

## 🛠️ SEO Tools Reference

| Tool | Main Purpose | When to Use |
|------|-------------|-------------|
| Google Search Console | Indexing, queries, clicks, impressions, CTR, errors | Weekly monitoring |
| Google Analytics 4 | Organic traffic, conversions, user behavior | Weekly/monthly reporting |
| Screaming Frog SEO Spider | Technical crawl, status codes, canonicals, links | After every major deployment |
| Google PageSpeed Insights | Core Web Vitals and performance | After performance changes |
| Rich Results Test | Google-supported structured-data eligibility | After every schema change |
| Schema.org Validator | Schema vocabulary validation | After every schema change |
| Ahrefs | Backlinks, keywords, competitor research | Monthly authority check |
| Semrush | Keyword research, content gaps, visibility | Keyword planning |
| Bing Webmaster Tools | Bing indexing and search performance | After sitemap fix |
| Microsoft Clarity | User behaviour and UX diagnostics | Ongoing UX monitoring |

---

## 📅 Implementation Roadmap Summary

### Phase 1 — Fix Technical Blockers (Week 1–2) 🚨 START HERE
> Do not change any page content until these are fixed.

| Priority | Task | Files to Change | Validation |
|----------|------|----------------|------------|
| P0-R1 | Fix `/sitemap.xml` HTTP 500 | `routes/sitemap*.js`, nginx | `curl -I sitemap.xml` → 200 |
| P0-R2 | Fix job slug does not match content (routing bug) | Job detail route, prerender cache | Slug URL must match H1 + JSON-LD title |
| P0-R3 | Fix JobPosting schema (0 valid) | Job schema template | Rich Results Test on 1 active job |
| P0-R4 | Fix 613 job 404s | Jobs module, redirects table | GSC 404 export decreases |

**Validation script:** `python SEO_Audit_Review_2026-09-29/live_seo_regression_check.py`

---

### Phase 2 — Optimize Important Pages (Week 3–6)
- Homepage → Daily UPSC/MPSC Quiz → Major exam guides (MPSC, Railway, UPSC) → Latest jobs → Current affairs hub
- Fix 764 duplicate titles, 719 duplicate meta descriptions, 789 duplicate H1 groups
- Repair breadcrumbs on all pages, fix broken internal links (462 targets)

---

### Phase 3 — Build Topical Authority (Week 7–12)
- Connect MPSC, Railway, Banking, Police, Maharashtra district clusters
- Link 3,111 orphan sitemap URLs from relevant hubs
- Admit card pages (896): add unique content, FAQs, canonical, hub links
- Expand hub pages with verified unique introductions + topic cluster links

---

### Phase 4 — Improve AEO and GEO (Month 3–4)
- Make job facts in static HTML (not JS-only)
- Source attribution blocks on all job pages
- Verified FAQ sections on hub and exam pages
- Structure quiz content for featured snippets and AI citation

---

### Phase 5 — Measure and Improve (Ongoing — Monthly)
- Track: organic clicks, impressions, indexed URLs, quiz completions, application clicks, referring domains
- Monthly report → quarterly programmatic SEO review → annual full technical audit

---

## 📊 Overall Checklist Progress

| Section | Items | Completed | Progress |
|---------|-------|-----------|----------|
| 1. Technical SEO | 18 | 0 | 0% |
| 2. Google Indexing & GSC | 14 | 0 | 0% |
| 3. On-Page SEO | 15 | 0 | 0% |
| 4. Keyword Research | 12 | 0 | 0% |
| 5. Content SEO & E-E-A-T | 17 | 0 | 0% |
| 6. Technical Performance & CWV | 13 | 0 | 0% |
| 7. Internal Linking & Architecture | 18 | 0 | 0% |
| 8. Structured Data & Schema | 15 | 0 | 0% |
| 9. GEO — Generative Engine Optimization | 15 | 0 | 0% |
| 10. AEO — Answer Engine Optimization | 12 | 0 | 0% |
| 11. External Links & Authority | 12 | 0 | 0% |
| 12. Job Portal SEO | 13 | 0 | 0% |
| 13. Exam, Quiz & Educational SEO | 12 | 0 | 0% |
| 14. Images, Accessibility & UX | 13 | 0 | 0% |
| 15. International & Multilingual SEO | 9 | 0 | 0% |
| 16. Analytics, Conversion & Monitoring | 14 | 0 | 0% |
| 17. Sitemap, Content Maintenance | 12 | 0 | 0% |
| 18. Security & Trust | 10 | 0 | 0% |
| **TOTAL** | **244** | **0** | **0%** |

---

## ⚠️ Important SEO Distinctions

| Term | What It Means for This Project |
|------|-------------------------------|
| SEO | Improve crawling, indexing, relevance, rankings, organic traffic |
| Technical SEO | Ensure Google can access and interpret the site correctly |
| AEO | Structure useful answers for question-based search and answer engines |
| GEO | Improve likelihood that AI engines (ChatGPT, Gemini, Perplexity) can understand, trust, and reference content |
| Internal Linking | Connect related job, exam, quiz, location, and hub pages |
| Off-Page SEO | Earn credible links and mentions from relevant external sources |
| CRO | Convert visitors into quiz participants, registrations, and job applicants |

> GEO and AEO are complementary practices — NOT guaranteed ranking systems.
> No special schema, AI file, or keyword technique guarantees citation by an AI engine.
> Start with a real crawl + GSC data, not blind page changes.
> This checklist is a complete audit framework — not every item is currently broken.
> Prioritize findings based on evidence, impact, and implementation effort.

---

## 🔄 Change Log

| Date | Section | Change | Owner |
|------|---------|--------|-------|
| 2026-10-26 | All | Tracker created with full 244-item checklist | Amol Kadam |
| | | | |
| | | | |

---

*Last updated: 26 October 2026 | SearchSarkariNaukri.com SEO Repository | Growthik Media*
