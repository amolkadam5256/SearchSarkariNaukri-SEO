# Fix: "Crawled – Currently Not Indexed" — searchsarkarinaukri.com

**Site:** https://www.searchsarkarinaukri.com/
**GSC Status:** Crawled – currently not indexed
**Validation:** Started 14 Jun 2026 → Failed 01 Jul 2026
**Affected URLs:** 116 (from Coverage Drilldown export, 08 Aug 2026)

Suggested repo location for this file:

```
.agents/00_Report_Issues/Google-Search-Console/03_Crawled_Currently_Not_Indexed/README.md
```

---

## 1. What This Status Actually Means

This is **not** a crawl error. Google:

- ✅ Found the URL
- ✅ Crawled it
- ✅ Read the content
- ❌ Chose not to add it to the index

This is almost always a **quality, duplication, or weak-signal** problem — not a technical/availability problem. Do not treat it as "fix the server" — treat it as "make each page worth indexing and easy to trust."

---

## 2. Affected URL Types

The 116 affected URLs fall into three buckets. Each needs a different fix.

| Type                      | Pattern                                          | Example                                                                                 |
| ------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Job detail pages          | `/jobs/{id}`                                     | `/jobs/2220`, `/jobs/1775`                                                              |
| Location/category pages   | `/jobs-in-*`, `*-jobs-in-*`, `*-government-jobs` | `/jobs-in-vadodara`, `/engineer-jobs-in-chandigarh`, `/mbbs-medical-jobs-in-tamil-nadu` |
| District/department pages | `/districts/*`, `/department/*`                  | `/districts/mumbai-suburban/central`, `/department/upsssc`                              |
| News pages                | `/news/{id}`                                     | `/news/58153`                                                                           |

---

## 3. Developer Checklist (Track Per URL)

- [ ] HTTP 200 (no 3xx/4xx/5xx)
- [ ] Self-referencing canonical tag
- [ ] `index,follow` meta robots (no `noindex`, no `X-Robots-Tag: noindex`)
- [ ] Included in sitemap, not duplicated, not redirected
- [ ] No duplicate/near-duplicate content vs. other pages on the site
- [ ] 500+ words of substantive content where appropriate
- [ ] Breadcrumb schema present
- [ ] `JobPosting` schema (job pages) / `CollectionPage` schema (category pages) / `NewsArticle` schema (news pages)
- [ ] Strong internal linking (not an orphan page)
- [ ] Related jobs / related articles section
- [ ] FAQs section
- [ ] Images have alt text
- [ ] Core Web Vitals pass

---

## 4. Step-by-Step Fix Plan

### Step 1 — Verify HTTP Status

Every affected URL must return **200 OK**. Audit for 302 / 307 / 404 / 500 responses and fix routing/redirect issues first — this is the cheapest thing to rule out.

### Step 2 — Verify Robots Directives

Confirm every page has:

```html
<meta name="robots" content="index,follow" />
```

And does **not** have:

```html
<meta name="robots" content="noindex" />
```

or the header:

```
X-Robots-Tag: noindex
```

### Step 3 — Fix Canonical Tags

Every page must have a **self-referencing** canonical. Never point a job page's canonical at a different job.

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/2220" />
```

### Step 4 — Eliminate Thin / Duplicate Content

For every URL, confirm it has:

- Unique `<title>`
- Unique `<h1>`
- Original description (not templated boilerplate)
- Job info, department details, eligibility, age limit, salary, selection process, important dates, important links

**Root cause to check specifically:** if two pages differ only by city or qualification (e.g. `/graduate-jobs-in-kerala` vs `/graduate-jobs-in-tamil-nadu`) but share near-identical body text with just the location swapped, Google will treat them as **low-value duplicates** and refuse to index most of them. This is very likely a major driver given how many `*-jobs-in-*` pages are in the affected list.

### Step 5 — Eliminate "Thin Page" Pattern

A category page that renders as just:

```
Jobs in Vadodara
No jobs found
```

will not get indexed. Every category/district page must include:

- Introduction paragraph (unique, location-specific)
- Government recruitment overview for that location/qualification
- Latest jobs list
- Related jobs
- Nearby districts/states
- FAQs
- Useful links

### Step 6 — Fix Internal Linking

Every affected URL should be reachable via links from:

- Homepage
- State pages
- Qualification pages
- District pages
- "Latest Jobs" / "Related Jobs" widgets
- Breadcrumbs

Orphan pages (reachable only via sitemap, not via on-site links) are commonly ignored by Google.

### Step 7 — Sitemap Audit

Confirm every affected URL:

- Exists in the sitemap
- Appears only once (no duplicates)
- Is not itself redirected
- Returns 200 when the sitemap is crawled

### Step 8 — Structured Data

| Page type         | Schema                                          |
| ----------------- | ----------------------------------------------- |
| Job detail        | `JobPosting`                                    |
| Category/district | `CollectionPage` + `BreadcrumbList` + `WebPage` |
| News              | `NewsArticle` (where genuinely applicable)      |

### Step 9 — Dynamic Route Validation (Next.js or equivalent)

For `/jobs/[id]` and similar dynamic routes: if the underlying record does not exist (deleted/expired job), the route must return a real **404**, not an empty/soft-404 page with 200 status.

### Step 10 — Strengthen Job Detail Pages (`/jobs/{id}`)

Each job page should include:

- Recruitment/organization name
- Post name
- Vacancy count
- Salary
- Eligibility
- Age limit
- Selection process
- Application fee
- Important dates
- Official notification link
- Official website link
- FAQs
- Related jobs
- Breadcrumbs

### Step 11 — Strengthen Category/Location Pages (`*-jobs-in-*`)

Each category page should include:

- Introduction (unique per page — do not template-swap only the city name)
- District/location information
- Active vacancies list
- Qualification filters
- Department filters
- FAQs
- Internal links
- **Never publish a version with only a title + empty job list**

### Step 12 — Strengthen News Pages (`/news/{id}`)

For each news URL, confirm:

- The article is original (not scraped/aggregated)
- It's at least several hundred words
- It includes at least one relevant image
- It links to related articles
- It has `Article`/`NewsArticle` schema
- It has a visible author and publication date

---

## 5. Action Plan Summary (What to Hand to the Dev Team)

Instead of "Google isn't indexing these pages," assign these concrete tasks:

1. Audit every URL listed in Search Console's Coverage Drilldown export.
2. Classify each URL as **Job**, **Category**, **District**, or **News** (see §2).
3. Check HTTP status, robots directive, canonical tag, and sitemap inclusion for each.
4. Rewrite/expand thin or near-duplicate content, especially across `*-jobs-in-*` city/qualification variants.
5. Add missing schema (`JobPosting` / `CollectionPage` / `NewsArticle`) and breadcrumbs.
6. Add/strengthen internal links so no affected page is an orphan.
7. Ensure dynamic routes return a real 404 for missing records.
8. After deployment, request **Validate Fix** in Google Search Console for this issue.

---

## 6. Notes on Timeline

- Google already ran one validation pass (14 Jun 2026 → 01 Jul 2026) which **failed**, meaning the underlying content/quality issues were still present at last check.
- Do not request re-validation until Steps 1–12 above have actually been deployed to production and spot-checked on a sample of each page type.
  \_Source: Google Search Console export, searchsarkarinaukri.com, Coverage & Coverage-Drilldown reports, 07 Aug 2026 and C:\Users\computer1\Desktop\Growthik_Media\02_Clients\03_SearchSarkariNaukri\SearchSarkariNaukri\.agents\00_Report_Issues\Google-Search-Console\03_Crawled_Currently_Not_Indexed\https*\_\_www.searchsarkarinaukri.com*-Coverage-Drilldown-2026-08-08 (1).xlsx\_
