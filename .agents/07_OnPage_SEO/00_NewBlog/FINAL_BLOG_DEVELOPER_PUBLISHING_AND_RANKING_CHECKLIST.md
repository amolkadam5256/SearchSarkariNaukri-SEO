# Final: Blog Publishing, Ranking Readiness & Developer Instructions

**Document owner:** Search Sarkari Naukri SEO / Editorial  
**Last updated:** 1 October 2026  
**Audience:** Frontend developer, CMS operator, QA, TR (business sign-off)  
**Scope:** All content under `.agents/07_OnPage_SEO/00_NewBlog/` plus live `/blogs/*` behaviour on production.

---

## 1. Executive summary (ranking reality)

| Question | Answer |
|----------|--------|
| **Are blogs “ready to rank” in repo?** | **Content:** Mostly yes for pillars (01–08, 09–15, 12); **new Oct cluster (18–22)** is publish-ready for SEO *metadata* but **thin vs pillar depth** (except 18). |
| **Are blogs ranking on Google today?** | **Blocked / degraded** for known URLs until **P0 canonical hydration bug** is fixed in production. GSC has reported **Soft 404** when user-declared canonical = homepage. |
| **Single biggest fix** | **Dev P0:** Self-referencing canonical on every `/blogs/{slug}` after React hydration (see §5.1). |
| **Single biggest content fix** | **CMS:** Replace live body for 01, 02, 03, 16 with `00_Blog_Error/**/**-FIXED.md` versions (editorial + schema already corrected). |

**Reference docs (do not skip):**

- Canonical root cause: `00_Blog_Error/00_DEVELOPER_CANONICAL_FIX_INSTRUCTIONS.md`
- Editorial fixes audit: `00_Blog_Error/00_FINAL_SEO_AUDIT_REPORT.md`
- Template rules: `Pr_blog_1/blog-template-instructions.md`
- Cluster map: `00_GSC_AEO_BLOG_CLUSTER_INDEX.md`
- Site-wide non-blog backlog: `../10_Post_Release_Audit_2026-09-30/09_DEVELOPER_PENDING_IMPLEMENTATION_INSTRUCTIONS.md`

---

## 2. Master blog inventory (repo → live URL)

**Live URL pattern:** `https://www.searchsarkarinaukri.com/blogs/{slug}`  
**Exception:** Folder `17_*` targets **`/daily-assessment`** (product page, not `/blogs/`).

| # | Folder | Source file | Slug | Schema in repo | Content depth | CMS sync priority |
|---|--------|-------------|------|----------------|---------------|-------------------|
| 01 | `01_10th_Pass_Government_Jobs_2026` | `01_10th-pass-government-jobs-2026.md` | `10th-pass-government-jobs-2026` | Article | Medium | **P1:** use `00_Blog_Error/03_.../03_10th-pass-...-FIXED.md` |
| 02 | `02_Government_Jobs_Without_Graduation` | `02_government-jobs-without-graduation.md` | `government-jobs-without-graduation` | Article | Medium | **P1:** use `00_Blog_Error/02_.../*-FIXED.md` |
| 03 | `03_Maharashtra_Government_Jobs_2026` | `03_maharashtra-government-jobs-2026.md` | `maharashtra-government-jobs-2026` | Article | Medium | **P1:** use `00_Blog_Error/01_.../*-FIXED.md` |
| 04 | `04_Electrician_...` | `04_electrician-...md` | `electrician-government-jobs-in-maharashtra-2026` | Article | Pillar (~570+ lines) | P2: normalize schema |
| 05 | `05_Fitter_...` | `05_fitter-...md` | `fitter-government-jobs-in-maharashtra-2026` | Article | **Pillar reference** | P2: Article → BlogPosting |
| 06 | `06_Railway_ITI_...` | `06_railway-iti-...md` | `railway-iti-recruitment-maharashtra-2026` | Article | Pillar | P2 |
| 07 | `07_Pune_ITI_...` | `07_pune-iti-...md` | `pune-iti-government-jobs-2026` | Article | Pillar | P2 |
| 08 | `08_Nagpur_ITI_...` | `08_nagpur-iti-...md` | `nagpur-iti-government-jobs-2026` | Article | Pillar | P2 |
| 09 | `09_Gazetted_Officer_in_India_2026` | `BLOG.md` | `gazetted-officer-in-india-2026` | BlogPosting (footer) | Pillar | P2: add YAML frontmatter block |
| 10 | `10_Gazetted_Officer_Attestation_2026` | `BLOG.md` | `gazetted-officer-attestation-2026` | Check footer JSON-LD | Pillar | P2 |
| 11 | `11_IOCL_Data_Entry_...` | `BLOG.md` | `iocl-data-entry-operator-recruitment-2026` | Check footer | Pillar | P2 |
| 12 | `12_Sarkari_Naukri_2026_...` | `BLOG.md` | `sarkari-naukri-2026-latest-government-jobs-india` | BlogPosting | Pillar | Watch cannibalization vs `/jobs`, hub pages |
| 13 | `13_Government_Jobs_in_Pune_2026` | `BLOG.md` | `government-jobs-in-pune-2026` | BlogPosting | Pillar | Link to `/jobs-in-pune` |
| 14 | `14_Nagpur_Government_Bharti_2026` | `BLOG.md` | `nagpur-government-bharti-2026` | BlogPosting | Pillar | Link to `/jobs-in-nagpur` |
| 15 | `15_ZP_Nashik_Recruitment_2026` | `BLOG.md` | `zp-nashik-recruitment-2026` | BlogPosting | Medium–pillar | Link to `/districts/nashik` |
| 16 | `16_UPI_Charges_October_2026` | `16_upi-charges-october-2026.md` | `upi-charges-october-2026` | Article | Medium | **P1:** compare with `00_Blog_Error/04_UPI_.../*-FIXED.md` |
| 17 | `17_Daily_UPSC_MPSC_Quiz_...` | `BLOG.md` + `SEO_METADATA.md` | *(n/a — use `/daily-assessment`)* | BlogPosting in BLOG | Pillar | **Not a blog route** — same canonical rules apply |
| 18 | `18_SSC_CHSL_2026_...` | `18_ssc-chsl-2026-apply-online-guide.md` | `ssc-chsl-2026-apply-online-guide` | BlogPosting + Breadcrumb + FAQ | Medium (~200 lines) | **P0 publish** after canonical fix |
| 19 | `19_RRB_NTPC_...` | `19_rrb-ntpc-graduate-recruitment-2026.md` | `rrb-ntpc-graduate-recruitment-2026` | BlogPosting + Breadcrumb + FAQ | **Thin** (~150 lines) | P2 expand OR publish as supporting post |
| 20 | `20_12th_Pass_...` | `20_12th-pass-sarkari-naukri-2026.md` | `12th-pass-sarkari-naukri-2026` | BlogPosting + Breadcrumb + FAQ | **Thin** | P2 expand; link `/12th-pass-government-jobs` |
| 21 | `21_Bank_Apprentice_...` | `21_bank-apprentice-jobs-2026.md` | `bank-apprentice-jobs-2026` | BlogPosting + Breadcrumb + FAQ | **Thin** | P2 expand; tie to live Canara job pages |
| 22 | `22_Age_Limit_...` | `22_age-limit-government-jobs-2026.md` | `age-limit-government-jobs-2026` | BlogPosting + Breadcrumb + FAQ | **Thin** | P2 expand; link `/guide/government-jobs-2026` |

**Ranking status column (live, as of 1 Oct 2026 — verify after every deploy):**

| Status | Meaning |
|--------|---------|
| **NOT INDEXING (P0)** | GSC Soft 404 or canonical = homepage — **fix code first** |
| **INDEXABLE BUT WEAK** | Canonical OK but thin content, wrong schema type, or cannibalization |
| **INDEXABLE STRONG** | Self-canonical, 1k+ words (or clear niche intent), FAQ visible, internal links, in sitemap |

Until P0 is verified in headless Chrome, treat **all `/blogs/*` as NOT INDEXING (P0)** even if prerender HTML looks correct.

---

## 3. Issue register (complete checklist)

### 3.1 P0 — Must fix before expecting rankings

- [ ] **BLOG-CANONICAL-001:** After hydration, `<link rel="canonical">` must be `https://www.searchsarkarinaukri.com/blogs/{slug}` — never `/`.
- [ ] **BLOG-CANONICAL-002:** Do not remove prerender `[data-ssn-seo]` tags unless replacing with equivalent correct tags in the same paint.
- [ ] **BLOG-CANONICAL-003:** SEO component must receive `url` or `path` synchronously on blog route; no fallback to `"/"` while post loads.
- [ ] **BLOG-GSC-001:** Re-submit affected URLs in GSC after fix; request indexing for 01, 02, 03, 16 first.
- [ ] **BLOG-SITEMAP-001:** Every published slug appears in `sitemap-blogs.xml` (or child sitemap referenced from `sitemap.xml`).

### 3.2 P1 — Content & GSC recovery (CMS)

- [ ] **BLOG-CMS-001:** Publish `01_maharashtra-government-jobs-2026-FIXED.md` → slug `maharashtra-government-jobs-2026`.
- [ ] **BLOG-CMS-002:** Publish `02_government-jobs-without-graduation-FIXED.md`.
- [ ] **BLOG-CMS-003:** Publish `03_10th-pass-government-jobs-2026-FIXED.md`.
- [ ] **BLOG-CMS-004:** Align UPI post with `04_upi-charges-october-2026-FIXED.md` if diffs remain.
- [ ] **BLOG-META-001:** Title ≤60 chars; meta description 150–160 chars; unique per slug (no duplicate titles with job pages).

### 3.3 P2 — Technical SEO normalization

- [ ] **BLOG-SCHEMA-001:** One primary type: **`BlogPosting`** (not `Article`) for all `/blogs/*` — migrate at render time from CMS JSON-LD blocks.
- [ ] **BLOG-SCHEMA-002:** Required JSON-LD: `BlogPosting`, `BreadcrumbList`; add `FAQPage` only if FAQ HTML is visible on page.
- [ ] **BLOG-SCHEMA-003:** `mainEntityOfPage.@id` must match canonical URL exactly.
- [ ] **BLOG-SCHEMA-004:** Do not duplicate global `Organization` / `WebSite` schema on each post.
- [ ] **BLOG-IMG-001:** Featured image 1200×630 WebP; `og:image`, `twitter:image`, `BlogPosting.image` aligned; real `alt` per `blog-template-instructions.md`.
- [ ] **BLOG-LINK-001:** In-body internal links: minimum **8–12** (explainers), **15–25** (job pillars); see cluster list in `00_GSC_AEO_BLOG_CLUSTER_INDEX.md`.
- [ ] **BLOG-HUB-001:** Each qualification/geo blog links to matching hub (`/10th-pass-government-jobs`, `/iti-government-jobs`, `/jobs-in-pune`, etc.).

### 3.4 P3 — Growth, AEO, cannibalization

- [ ] **BLOG-AEO-001:** Opening paragraph answers primary query in plain language (no fake “Direct Answer (AEO)” heading — use natural H2 if needed).
- [ ] **BLOG-AEO-002:** Quick facts table or bullet block where appropriate; official `.gov.in` / `.nic.in` links for recruitment facts.
- [ ] **BLOG-CANNIBAL-001:** `12` (national Sarkari Naukri) must not compete with homepage/`/jobs` for same title; differentiate title/H1 from homepage H1.
- [ ] **BLOG-CANNIBAL-002:** `20` (12th pass blog) vs `02` (without graduation) vs `/12th-pass-government-jobs` — distinct primary keywords (repo FIXED files already adjusted intent for 02).
- [ ] **BLOG-FRESH-001:** Update `dateModified` only when content actually changes.
- [ ] **BLOG-EXPAND-001:** Expand 19–22 to pillar depth (~500+ lines) if TR wants parity with `05_fitter-...` for competitive queries.

### 3.5 Known non-blog production issues (affects blog CTAs)

- [ ] **JOB-SLUG-5015:** Wrong job body on some stale slugs — see `../10_Post_Release_Audit_2026-09-30/02_STALE_JOB_SLUG_ROUTING.md`.
- [ ] Run `SEO_Audit_Review_2026-09-29/live_seo_regression_check.py` after deploy (`py -3` on Windows if `python` missing).

---

## 4. Multi-perspective test matrix (run for every new/updated blog)

Use this as **QA script** — record Pass/Fail in deploy ticket.

### 4.1 SEO / Googlebot

| # | Test | How | Pass criteria |
|---|------|-----|----------------|
| T1 | HTTP status | GET `/blogs/{slug}` | 200 |
| T2 | Prerender canonical | View page source (disable JS) | `rel="canonical"` = blog URL |
| T3 | **Hydrated canonical** | Chrome DevTools → disable cache → reload; or GSC URL Inspection live test | Canonical still = blog URL |
| T4 | Title & description | Inspect `<head>` | Unique; length limits |
| T5 | Robots | meta robots | `index, follow` unless deliberately noindex |
| T6 | Sitemap | Fetch `sitemap.xml` → blog child | Slug present |
| T7 | Rich Results | Google Rich Results Test | BlogPosting valid; FAQ only if on-page FAQ exists |

### 4.2 Content / E-E-A-T

| # | Test | Pass criteria |
|---|------|----------------|
| T8 | Disclaimer | States independent portal; not official government |
| T9 | Editorial policy link | `/editorial-policy` linked where frontmatter specifies |
| T10 | Official sources | Recruitment dates/fees/links trace to official domains |
| T11 | No unsupported claims | No “thousands of vacancies” without notification reference |

### 4.3 AEO / GEO (AI citation)

| # | Test | Pass criteria |
|---|------|----------------|
| T12 | Answer-first intro | First 2–3 sentences answer primary keyword |
| T13 | FAQ parity | Every FAQPage schema question visible in HTML (`<details>` or headings) |
| T14 | Maharashtra/geo posts | State-specific sections where folder implies GEO intent |

### 4.4 UX / accessibility

| # | Test | Pass criteria |
|---|------|----------------|
| T15 | Heading order | Single H1; H2 → H3 no skips |
| T16 | TOC | Anchor IDs match H2 `id` attributes |
| T17 | Tables | Real `<table>` for tabular data |
| T18 | Images | `alt` present; width/height set if template requires |

### 4.5 Analytics / business

| # | Test | Pass criteria |
|---|------|----------------|
| T19 | Primary CTA | Links to `/jobs`, relevant hub, or official apply URL |
| T20 | Internal cluster | Links to 2+ related blogs from inventory §2 |

---

## 5. Developer instructions (implementation format)

### 5.1 P0 — Fix blog canonical after hydration

**Objective:** Google must see self-referencing canonical on all `/blogs/{slug}` pages after full JS execution.

**Steps:**

1. Open production SEO component (referenced in `00_DEVELOPER_CANONICAL_FIX_INSTRUCTIONS.md` as `$0` / hook `K0()` pattern).
2. **Stop** removing prerender SEO tags unless the React SEO layer sets replacements **in the same commit** with correct `canonical`.
3. Set canonical from route:
   - `const canonical = `${SITE_URL}${pathname}`;`
   - For blog detail: `pathname` = `/blogs/${slug}` from router or CMS payload **before** first paint of `<Head>`.
4. **Guard:** If slug is loading, either delay SEO tag update until slug is known, or keep SSR/prerender tag (do not fall back to `/`).
5. Add automated test: fetch blog HTML with headless browser; assert canonical href ends with slug.

**Acceptance criteria:**

- [ ] URL Inspection (live) for `10th-pass-government-jobs-2026` shows user canonical = blog URL.
- [ ] Same for `maharashtra-government-jobs-2026`, `government-jobs-without-graduation`, `upi-charges-october-2026`.
- [ ] Soft 404 cleared in GSC within 2–4 weeks after recrawl (monitor Coverage report).

**Files in repo (spec only — implement in app repo `SakariNaukariN`):**

- `00_Blog_Error/00_DEVELOPER_CANONICAL_FIX_INSTRUCTIONS.md` (full code examples)

---

### 5.2 P1 — CMS import from FIXED markdown

**Objective:** Replace live CMS HTML/markdown for Soft 404 URLs with audited copies.

**For each row, operator action:**

| Slug | Import from |
|------|-------------|
| `maharashtra-government-jobs-2026` | `00_Blog_Error/01_Maharashtra_Government_Jobs_2026/01_maharashtra-government-jobs-2026-FIXED.md` |
| `government-jobs-without-graduation` | `00_Blog_Error/02_Government_Jobs_Without_Graduation/02_government-jobs-without-graduation-FIXED.md` |
| `10th-pass-government-jobs-2026` | `00_Blog_Error/03_10th_Pass_Government_Jobs_2026/03_10th-pass-government-jobs-2026-FIXED.md` |
| `upi-charges-october-2026` | `00_Blog_Error/04_UPI_Charges_October_2026/04_upi-charges-october-2026-FIXED.md` (if not already identical) |

**Steps:**

1. In CMS, open post by slug.
2. Paste body from FIXED file (preserve H1 once — CMS may map title from YAML `title`).
3. Map YAML frontmatter fields to CMS fields: `title`, `meta_description`, `canonical`, `slug`, `date_published`, `date_updated`, `social_image`, `primary_keyword`.
4. Paste JSON-LD `<script type="application/ld+json">` blocks into “Custom head” or schema plugin **only if** CMS does not auto-generate schema (avoid duplicate BlogPosting).
5. Publish → run tests T1–T7 on that slug.

**Acceptance criteria:**

- [ ] Visible FAQ matches FAQPage JSON-LD (if present).
- [ ] No duplicate H1 in body vs template title.

---

### 5.3 P2 — Publish new Oct 2026 cluster (18–22)

**Objective:** Ship five competitor-intent posts without breaking cluster linking rules (`00_COMPETITOR_RESEARCH_5_BLOG_TOPICS_OCT_2026.md`).

**Build order (recommended):**

1. `ssc-chsl-2026-apply-online-guide` (18) — highest intent, full schema in repo.
2. `rrb-ntpc-graduate-recruitment-2026` (19)
3. `12th-pass-sarkari-naukri-2026` (20)
4. `bank-apprentice-jobs-2026` (21)
5. `age-limit-government-jobs-2026` (22)

**Per post developer checklist:**

1. Create CMS entry; slug must match frontmatter `slug` exactly.
2. Upload WebP to `/images/blogs/{filename}` per frontmatter `image_seo`.
3. Wire canonical + OG tags from frontmatter.
4. Inject or render three JSON-LD blocks from markdown footer (BlogPosting, BreadcrumbList, FAQPage).
5. Add to blog sitemap generator on publish hook.
6. Add 8+ internal links (minimum) to `/jobs`, `/department/ssc`, `/department/railway-rrb`, `/12th-pass-government-jobs`, `/graduate-government-jobs`, related blogs.
7. Run full test matrix §4.

**Acceptance criteria:**

- [ ] All five URLs return 200 and pass T3 (hydrated canonical).
- [ ] Listed in sitemap within 24h of publish.

---

### 5.4 P2 — Schema normalization (Article → BlogPosting)

**Objective:** Align with `Pr_blog_1/blog-template-instructions.md` §3 rule 3.

**Steps:**

1. At render time, map legacy `@type: Article` in stored JSON-LD to `BlogPosting` **or** regenerate JSON-LD from CMS fields.
2. Ensure `headline` = post title, `dateModified` from CMS.
3. Re-validate in Rich Results Test for samples: `fitter-government-jobs-in-maharashtra-2026`, `10th-pass-government-jobs-2026`.

**Acceptance criteria:**

- [ ] No blog URL emits both Article and BlogPosting for the same page.

---

### 5.5 P2 — BLOG.md-style posts (09–15, 17)

**Issue:** Several `BLOG.md` files lack YAML frontmatter at top; SEO block is at file footer.

**Steps:**

1. When importing, map footer **Canonical URL** and JSON-LD to CMS fields (see e.g. `14_Nagpur_Government_Bharti_2026/BLOG.md`).
2. For folder 17, deploy content to **`/daily-assessment`** per `17_.../SEO_METADATA.md` — not under `/blogs/`.

---

## 6. Editorial / SEO operator instructions

1. **One primary keyword per URL** — see `00_GSC_AEO_BLOG_CLUSTER_INDEX.md` publishing rule.
2. **Official links only** for vacancy counts, dates, fees, eligibility.
3. **Do not publish** FAQ schema without visible FAQ section.
4. After dev deploys P0, **request indexing** in GSC for priority slugs (01, 02, 03, 16, then 18–22).
5. Monitor: GSC Performance filter `Page` contains `/blogs/` — baseline impressions/clicks weekly.
6. Optional content work: expand 19–22 using `05_fitter-government-jobs-maharashtra-2026.md` as structure reference (tables, district links, FAQ depth).

---

## 7. Regression automation (extend recommended)

Current script: `SEO_Audit_Review_2026-09-29/live_seo_regression_check.py` — **does not yet test blog canonicals**.

**Developer task BLOG-QA-001:** Add function `check_blog_canonical(slugs: list[str])`:

1. Fetch each `/blogs/{slug}` with GET.
2. Optionally use headless Chromium in CI to read post-hydration `<link rel="canonical">`.
3. Fail if canonical is `BASE/` or missing.
4. Default slug list: P0 URLs in §3.1 + any newly published from §5.3.

---

## 8. Sign-off checklist (TR / release)

Before marking “blogs ranking-ready”:

- [ ] P0 canonical fix deployed and T3 passed on 4 legacy URLs + 1 new URL (18).
- [ ] P1 FIXED content live for 01, 02, 03 (and 16 if needed).
- [ ] Oct cluster 18–22 published OR consciously scheduled with thin-content note in analytics.
- [ ] Sitemap includes all live blog slugs.
- [ ] GSC ownership verified; Coverage report screenshot saved.
- [ ] Internal links from homepage or `/blogs` index to new cluster (if index exists).

---

## 9. Document change log

| Date | Change |
|------|--------|
| 2026-10-01 | Initial master checklist; JSON-LD completed for blogs 20–22 FAQPage; 21–22 frontmatter aligned with 18–19. |

---

## 10. Quick links for developers (copy-paste)

```
Repo blog root:
.agents/07_OnPage_SEO/00_NewBlog/

P0 canonical spec:
.agents/07_OnPage_SEO/00_NewBlog/00_Blog_Error/00_DEVELOPER_CANONICAL_FIX_INSTRUCTIONS.md

CMS FIXED sources:
.agents/07_OnPage_SEO/00_NewBlog/00_Blog_Error/

Template QA:
.agents/07_OnPage_SEO/00_NewBlog/Pr_blog_1/blog-template-instructions.md
```

**Production verification URLs (canonical must match):**

- https://www.searchsarkarinaukri.com/blogs/10th-pass-government-jobs-2026
- https://www.searchsarkarinaukri.com/blogs/maharashtra-government-jobs-2026
- https://www.searchsarkarinaukri.com/blogs/government-jobs-without-graduation
- https://www.searchsarkarinaukri.com/blogs/upi-charges-october-2026
- https://www.searchsarkarinaukri.com/blogs/ssc-chsl-2026-apply-online-guide *(after publish)*
