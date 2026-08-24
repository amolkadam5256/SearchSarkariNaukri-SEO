# 02 — `/jobs` Page: Technical SEO Fixes (Additive)

> Follow the ground rules in `01_ground_rules_do_not_delete.md`. Nothing here removes existing filters, cards, or components — it makes the same page crawlable and correctly tagged.

## 1. Server-render (or prerender) job content — CRITICAL

Right now `/jobs` ships an empty `<div id="root"></div>" and loads jobs client-side via API. Add a rendering layer so the **initial HTML response already contains** the current job list, without removing the existing React app or its interactivity.

- Add SSR/SSG/prerendering for the `/jobs` route only (leave every other route as-is for now).
- The React app should still hydrate and power search/filter/sort exactly as it does today — this is additive middleware, not a rewrite.
- Verify with Google's **URL Inspection → Test Live URL → View Crawled Page → HTML** that job titles, organizations, and dates appear in the raw HTML.

## 2. Add a page-specific `<title>` (edit, not addition — approved in file 01)

Current title is homepage-oriented. Update only the `/jobs` route's title:

```
Latest Government Jobs 2026 – Sarkari Naukri & Govt Jobs
```

## 3. Add a page-specific meta description (edit, approved)

```html
<meta name="description" content="Find the latest government jobs 2026 in India. Search active Sarkari Naukri, MPSC, SSC, Railway, Banking, Police Bharti, 10th, 12th, ITI and graduate jobs with last dates and apply links.">
```

## 4. Add a self-referencing canonical tag (new addition)

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">
```

### Pagination canonical policy — fixed, single policy (no longer optional)

`/jobs` pagination is treated as **independently indexable**. Every paginated URL gets a **self-referencing canonical**, not a canonical back to `/jobs`. This is the one consistent policy across this entire file set — file 12 mirrors it exactly, so there is no ambiguity for the developer to resolve.

```html
<!-- on /jobs -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">

<!-- on /jobs?page=2 -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs?page=2">

<!-- on /jobs?page=3 -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs?page=3">
```

Reasoning: each page shows a different, unique set of active jobs, so each is genuinely distinct content and deserves its own canonical rather than being folded into page 1.

## 5. Add route-specific Open Graph tags (new addition, don't remove homepage OG)

```html
<meta property="og:url" content="https://www.searchsarkarinaukri.com/jobs">
<meta property="og:title" content="Latest Government Jobs 2026 – Sarkari Naukri">
<meta property="og:description" content="Find the latest government jobs 2026 in India across MPSC, SSC, Railway, Banking, Police Bharti and more.">
```

## 6. Add crawlable pagination (new addition)

Keep any existing "Load More" button for UX, but **add** real paginated URLs alongside it:

```html
<a href="/jobs?page=2">Next</a>
```

Do **not** add `rel="next"`/`rel="prev"` — Google retired support for these pagination hints years ago, and shipping them adds dead markup without benefit. A plain, normal, crawlable `<a href>` link is all that's needed; combined with the self-referencing canonical per page (see #4), Google will discover and index each page correctly on its own.

Each paginated URL should return unique server-rendered HTML for that page's jobs.

## 7. Add `noindex,follow` only to non-canonical filter/search URL variants (new addition)

Do **not** touch the base `/jobs` URL. For combinations like `/jobs?district=pune&sort=latest` that aren't deliberate SEO landing pages, add:

```html
<meta name="robots" content="noindex, follow">
```

This is additive — it doesn't remove the filter functionality, it just tells Google not to index the infinite parameter combinations while still following links from them.

## 8. Add breadcrumb markup to the page (new addition)

```html
<nav aria-label="breadcrumb">
  <a href="/">Home</a> &gt; <span>Government Jobs</span>
</nav>
```

(JSON-LD BreadcrumbList goes in file 05.)

## 9. Core Web Vitals — measurement only, no rewrite

Measure LCP, INP, CLS, TTFB on `/jobs` after adding SSR. If the API call still blocks rendering, that's the thing to fix in the SSR layer from #1 — don't restructure the front-end bundle to do it.

## Checklist for this file

- [ ] SSR/prerender returns full job list in raw HTML
- [ ] Title updated for `/jobs` only
- [ ] Meta description updated for `/jobs` only
- [ ] Canonical tag added
- [ ] OG tags added
- [ ] Crawlable pagination links added alongside existing UI
- [ ] `noindex,follow` added to non-SEO filter URL variants only
- [ ] Breadcrumb HTML added
- [ ] Core Web Vitals measured post-change
