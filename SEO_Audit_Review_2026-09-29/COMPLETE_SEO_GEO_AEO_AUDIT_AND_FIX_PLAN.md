# SearchSarkariNaukri.com — Complete SEO, GEO, AEO & Technical Audit

**Audit date:** 29 September 2026  
**Property:** https://www.searchsarkarinaukri.com/  
**GSC snapshot (user-provided):** 12 web-search clicks · 497 indexed · 2,196 not indexed · Breadcrumbs 22 valid · Job Postings 0 valid / 0 invalid · Core Web Vitals: no field data  
**Evidence:** Live URL checks (29 Sep 2026) + August 2026 full crawl (`SEO_Audit_Review_2026-08-25`) + GSC issue packages (`.agents/00_Issues_reports/02_Issue_29_August/`)  
**Production app (not in this repo):** `C:\Users\Administrator\Projects\SakariNaukariN` per remediation notes  

**UI rule:** All fixes must be additive or corrective only — no visual redesign, no deletion of useful content or pages.

**Non-negotiable (your instruction):** Do **not delete** jobs, pages, DB records, images, nav/footer, or sections. Only **update**, **add**, **301 redirect**, **noindex**, or **exclude from sitemap** (XML) where needed.

**Fix handoff (step-by-step):** [`01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md`](01_REGRESSION_FIX_IMPLEMENTATION_NO_DELETE.md)  
**Tracker:** [`FIX_TRACKER_NO_DELETE.csv`](FIX_TRACKER_NO_DELETE.csv)  
**Verify live:** `python SEO_Audit_Review_2026-09-29/live_seo_regression_check.py`

**Implementation status (29 Sep 2026):** Live site still shows **sitemap 500** and **job slug/content mismatch** — fixes must be applied on production app **`SakariNaukariN`** (not present in this SEO docs repo). Re-apply patterns from Aug 25 remediation where regressions occurred.

---

## Current SEO Health

**Overall:** Strong information architecture (jobs, departments, qualifications, districts, exams, news, tools, trust pages) but **organic visibility is critically constrained** by indexation imbalance (~82% of known URLs not indexed), **minimal clicks (12)**, and **new live regressions** (sitemap 500, job slug/content mismatches on sampled URLs).

**Strengths:** HTTPS/HSTS, valid robots.txt with sensible filter blocks, rich homepage AEO/FAQ content, breadcrumb schema historically valid, bilingual intent, official-source messaging, privacy/terms present, multi-size favicon links in HTML templates.

**Weaknesses:** Crawl/index budget spent on low-value programmatic URLs; orphan sitemap URLs; duplicate metadata; expired-job lifecycle; admit-card/numeric job URL backlog; **sitemap currently failing**; **URL slug does not match served job on live samples**.

---

## Critical Problems

| # | Issue | Severity | Live / evidence |
|---|--------|----------|-----------------|
| 1 | **`/sitemap.xml` and child sitemaps return HTTP 500** | 🔴 CRITICAL | Fetched 29 Sep 2026; Aug 25 remediation had verified 200 |
| 2 | **Job detail URLs: slug/title in URL ≠ page H1/content** (e.g. Canara Bank slug serves ESIC/NHSRCL content) | 🔴 CRITICAL | Live fetch `...--5015`, `...--5020` |
| 3 | **2,196 not indexed vs 497 indexed** — do not bulk-force index | 🔴 CRITICAL | GSC; classify per URL type first |
| 4 | **Job Postings enhancement: 0 valid** — no Google Jobs eligibility signal | 🔴 CRITICAL | GSC; likely expired markup removed + no active eligible pages and/or crawl failure |
| 5 | **613+ job 404s, numeric/slug variant chaos** | 🔴 CRITICAL | GSC package `01_Not found (404)` |
| 6 | **2,785 broken internal links → 462 dead targets** (district slug pollution) | 🟠 HIGH | Aug crawl |
| 7 | **3,111 sitemap URLs with zero internal inlinks** | 🟠 HIGH | Aug crawl |

---

## Indexation Analysis

**GSC totals (Sep 2026):** 497 indexed · 2,196 not indexed · 12 clicks.

**August 2026 reason breakdown (1,785 URL-level rows in repo — totals may differ from current GSC aggregate):**

| GSC reason | Pages | Intent |
|------------|------:|--------|
| Not found (404) | 613 | Restore valid jobs, 301 to canonical slug, 410 only if truly removed; remove from sitemap |
| Discovered – currently not indexed | 896 | Mostly admit-card/numeric job URLs — needs unique content + internal links + crawl budget |
| Crawled – currently not indexed | 136 | Thin/duplicate/low priority — improve or noindex intentionally |
| Soft 404 | 81 | Add listings, related links, FAQs when 0 active jobs |
| Excluded by noindex | 56 | Page-by-page: index valuable hubs; keep noindex on filters/thin |
| Redirect error | 1 | `/jobs?district_slug=pune` → `/districts/pune` (301) |
| Duplicate, Google chose different canonical | 1 | Align user canonical with Google’s chosen URL |
| Alternative page with proper canonical | 1 | Decide primary URL for numeric vs slug job |

**Classification strategy (required before any mass noindex/index):**

1. **Should index:** Active/evergreen job pages, hub pages (MPSC, Railway, 10th pass, `/jobs-in-pune`), news with substance, results/admit cards with unique facts.
2. **Should not index:** Search/filter params (`?search=`, `?category=` combos), login/dashboard, UTM URLs, duplicate numeric job URLs when slug canonical exists.
3. **Canonicalize:** Trailing slash duplicates, state-wise Canara Bank variants only if thin duplicates of parent notification.
4. **noindex,follow:** Expired jobs with historical value (keep content; remove JobPosting).
5. **410/404:** Permanently removed records with no replacement.

**Do not** target “index all 2,196” — target **high-intent, self-canonical, 200, linked** URLs first (~763 active jobs on 77 listing pages per user note).

---

## Technical SEO

| Item | Status | Fix |
|------|--------|-----|
| robots.txt | ✅ | Keep; blocks `?search=`, `?category=`, admin, API |
| Sitemap | 🔴 500 live | **P0:** Fix generator/API/PM2 error; validate XSD; resubmit GSC |
| HTTPS / www | ✅ | Apex → https www |
| Trailing slash | 🟡 | Enforce 301 one way (fixed Aug 25 — verify still live) |
| CSR vs prerender | 🟡 | Googlebot gets prerender; ensure parity for all bots |
| 404 parity | 🟡 | User vs Googlebot status on unknown routes |
| Internal 404s | 🔴 | Fix district slug generator + link repair |
| Dynamic rendering | 🟠 | Prefer SSR/SSG for critical job facts in initial HTML for all UAs |

---

## On-Page SEO

- **Titles:** 3,813 pages >60 chars; **764 duplicate titles** — shorten, unique intent per URL.
- **Meta descriptions:** **719 duplicates**; 293 length issues.
- **H1:** 789 URLs in duplicate H1 groups.
- **Job template:** Use pattern `[Org] [Post] [Year] – [Vacancies/Eligibility] | Search Sarkari Naukri` without misleading text.
- **Thin pages:** 557 indexable pages <150 words — expand or noindex.

---

## Programmatic SEO

Controlled hubs already exist; risk is **uncontrolled combinations** (district × category × qualification) creating crawl bloat.

**Indexable (examples):** `/jobs-in-pune`, `/10th-pass-government-jobs`, `/department/mpsc`, `/category/police-jobs`.

**Non-indexable:** Arbitrary `/jobs?qualification=&state=` combinations unless built as dedicated landing pages with unique intro + jobs + FAQs.

---

## Content SEO

- Homepage: strong topical coverage, Quick Answers, verification copy — **preserve and extend**, do not remove.
- Job pages: median ~196 words — acceptable if structured facts complete; **must match URL and official source**.
- Near-duplicate bodies: 550 exact + 1,955 >80% pairs — dedupe at DB level for admit/result/job clones.

---

## Semantic SEO & Entity SEO

Map consistent entities: Organization → Recruitment → Post → Qualification → Location → Exam → Deadline → Official URL.

Fix **naming drift** (SearchSarkariNaukri vs LyfJobs in legacy copy). Align title, H1, schema, breadcrumbs.

---

## Topical Authority

Clusters to strengthen via internal links (not new thin pages): MPSC, SSC, UPSC, Railway/RRB, Banking/IBPS, Police, Maharashtra districts, qualification ladders.

---

## Internal Linking

**P1:** Link orphan sitemap jobs from hubs (category, department, district, qualification).  
**P1:** Repair 462 broken targets.  
Use descriptive anchors (already good in crawl — maintain).

---

## AEO (Answer Engine Optimization)

**Current win:** Homepage FAQ block + Quick Answers (12+ questions).  
**Gaps:** Per-job and hub FAQs must use **verified facts only**; avoid template FAQ repetition across programmatic pages.  
**Format:** Question H2/H3 → direct answer first → details table → official source.

---

## GEO (Generative Engine Optimization)

**Good:** Labeled facts on job templates (org, dates, qualification), disclaimer on independence from government.  
**Improve:** Explicit “Source / Last updated / Application status” block on every job (visible, crawlable).  
**Risk:** Wrong job on wrong URL destroys trust for AI citation — fix routing **before** scaling content.

---

## AI Search Optimization

Ensure facts are in **static HTML**, not JS-only. Concise definitional sentences at top of job/hub pages. No hidden accordions for critical eligibility/dates.

---

## Structured Data

| Type | Status | Action |
|------|--------|--------|
| BreadcrumbList | ✅ 22 valid in GSC sample | Roll consistently; fix any broken breadcrumb URLs |
| JobPosting | 🔴 0 valid in GSC | Emit only on **active** jobs with valid `validThrough`; remove when expired |
| FAQPage | ✅ Homepage | Do not mass-deploy fake FAQs |
| Organization | 🟡 | Fill `sameAs` with verified social profiles |
| WebSite SearchAction | ✅ | Remove duplicate block on homepage |
| hreflang on same URL | 🔴 | Remove invalid en/mr/x-default on identical URL; set accurate `html lang` |

---

## JobPosting SEO

1. Active jobs only: title, description, datePosted, validThrough (end of day IST), hiringOrganization, jobLocation, employmentType, applicationContact/directApply when official URL exists.  
2. Expired: remove JobPosting; show closed banner; `noindex,follow` optional for pure archive policy.  
3. **Never** emit JobPosting when page content does not match the recruitment (current live bug).

---

## News SEO

NewsArticle/BlogPosting present on news/blog templates — ensure unique headlines, dates, publisher, canonical; avoid numeric-only news slugs where possible (50 URLs flagged).

---

## Image SEO

Blog covers >1.1 MB median — WebP/AVIF, dimensions, lazy load, descriptive alt (not stuffed).

---

## Video SEO

N/A unless VideoObject added for embedded official content — do not fake.

---

## Google Discover / Google News

Discover: timely recruitment, large images, strong headlines, mobile UX.  
News: original updates with source links; news sitemap only if eligible publisher guidelines met.

---

## E-E-A-T

Privacy, terms, contact, editorial/disclaimer on homepage — **keep**.  
Add/strengthen: editorial policy, corrections policy (pages may exist — ensure linked from footer).  
No fake authors.

---

## Mobile SEO

Viewport OK; **touch targets** and **notification overlay** hurt mobile UX/Lighthouse (Aug audit) — fix without changing visual brand (delay overlay, dismiss control).

---

## Core Web Vitals

GSC: **no field data** yet. Lab (Aug): mobile LCP up to ~8.5s on homepage — optimize LCP image/JS without removing content.

---

## JavaScript / Rendering SEO

Hybrid prerender for Googlebot; ordinary View Source still CSR shell — improve universal SSR for critical routes.

---

## Sitemap

**Architecture (when fixed):** index → static, jobs, locations, qualifications, departments, cross-filter, news, blogs, results, admit-cards, districts.  
**Include only:** 200, self-canonical, index,follow, meaningful lastmod.  
**Exclude:** 404, 410, noindex, redirects, expired jobs (per policy), empty news sitemap.

---

## Robots.txt

Current rules appropriate. Remember: robots disallows crawl of some params; **deindex** requires noindex, not robots alone.

---

## Canonicalization

Self-canonical on indexable pages; strip/merge duplicate job numeric URLs to one slug; fix **slug-ID binding** so canonical URL matches content.

---

## Pagination

`/jobs` 77 pages — ensure `?page=N` in crawlable `<a href>`, self-canonical per page or canonical to page 1 policy (document one approach); avoid infinite filters.

---

## Faceted Navigation

robots blocks `?search=` and `?category=` — good. Align with meta robots on remaining query hubs.

---

## Duplicate Content

764 duplicate titles, 719 duplicate descriptions, 550 exact body duplicates — DB dedupe + unique intros on programmatic landings.

---

## Thin Content

Soft 404 landings with “0 jobs” — add historical links, related hubs, 150+ words unique copy.

---

## URL Architecture

Prefer lowercase hyphen slugs; 1,312 URLs >115 chars — shorten slugs with 301 from old URL.  
**Reject** free-text district paths (419 invalid patterns in crawl).

---

## Multilingual SEO

Mixed EN/MR on same URL — use dominant `lang`; Marathi search terms in copy where natural; separate hreflang only if separate URLs launched.

---

## Security / HTTPS

HTTPS good in GSC sample (22). Maintain HSTS; fix mixed content if any.

---

## Search Console Strategy

1. **Fix sitemap 500** → resubmit → monitor Coverage.  
2. Export full “Not indexed” CSV → map to repo issue folders.  
3. URL Inspection: homepage, 1 active job, 1 hub, 1 admit card after fixes.  
4. Request validation **per issue type**, not whole site.  
5. Track Performance queries once impressions appear (currently negligible clicks).

---

## Exact Fix Plan (developer — production codebase)

### P0 — Critical (week 1)

| Problem | Why | Fix | Files / area | Validation |
|---------|-----|-----|--------------|------------|
| Sitemap 500 | Google cannot refresh discovery | Check API/PM2 logs, sitemap route, DB timeout; restore Aug 25 generator | Backend sitemap service, nginx | `curl -I sitemap.xml` → 200; XSD validate |
| Job ID ≠ slug content | Wrong indexable document, trust/legal risk | Route by primary key; if slug mismatch → 301 to correct slug or 404; regenerate slugs from org+post+year | Job detail route, prerender, CMS | Slug URL must match H1 + JSON-LD title |
| JobPosting 0 valid | No rich results / jobs tab | JobPosting only active jobs; Rich Results Test | Job schema template | GSC Enhancements |
| 404 job URLs | 613 GSC exclusions | DB restore / 301 / 410 + sitemap purge | Jobs module, redirects table | GSC 404 export decreases |

### P1 — High (weeks 2–4)

- Redirect `/jobs?district_slug=pune` → `/districts/pune`.  
- Repair internal district links (462 targets).  
- Admit-card 896 URLs: unique content, canonical, sitemap, hub links.  
- Expired job policy: no JobPosting, sitemap exclusion, visible “closed” state.  
- Remove invalid same-URL hreflang; fix `html lang`.  
- Add orphan job inlinks from hubs (batch by category).

### P2 — Medium

- Title/meta dedupe pipeline.  
- Organization `sameAs`.  
- Image compression.  
- Mobile LCP/overlay.  
- CWV monitoring.

### P3 — Growth

- Keyword map from GSC Performance.  
- Content hub expansion (MPSC, Railway) with **unique** intros only.  
- Discover/News optimization.

---

## Priority Roadmap

| Phase | Focus |
|-------|--------|
| P0 | Sitemap live · job URL integrity · active JobPosting · 404 job recovery |
| P1 | Indexation classification · internal links · soft 404 · noindex alignment |
| P2 | Metadata dedupe · CWV · images · hreflang/lang |
| P3 | Topical hubs · AEO/GEO depth · Discover |

---

## Validation Checklist

- [ ] `sitemap.xml` + all children HTTP 200, XSD valid, URL count matches DB policy  
- [ ] Sample 20 job URLs: slug = content = canonical = JSON-LD  
- [ ] Active job: JobPosting valid in Rich Results Test  
- [ ] Expired job: no JobPosting; closed message visible  
- [ ] robots.txt unchanged intent  
- [ ] Lighthouse SEO ≥90 mobile on homepage + job + hub  
- [ ] GSC: sitemap success, indexed count trend up on **priority** URLs only  
- [ ] Broken internal links → 0 on recrawl  

---

## Long-Term SEO Growth Strategy

1. **Quality indexed URLs over quantity** — aim for 800–1,200 strong URLs (jobs + hubs + exams + news), not 4,000+ weak ones.  
2. **Weekly:** publish/refresh active jobs, remove expired from sitemap, inspect top hubs in GSC.  
3. **Monthly:** duplicate title report, external official link check, orphan link pass.  
4. **Quarterly:** programmatic SEO review — add landing pages only when search demand + unique copy justified.  
5. **Measure success:** impressions and clicks on MPSC, Railway, qualification, and district head terms — not raw indexed count alone.

---

*This document satisfies the master audit output structure for handoff to developers working on the production Next.js/API codebase. No UI redesign required.*
