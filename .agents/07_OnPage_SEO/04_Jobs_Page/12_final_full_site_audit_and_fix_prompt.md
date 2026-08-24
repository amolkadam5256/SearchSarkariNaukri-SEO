# 12 — FINAL: Full-Site SEO Audit & Fix Prompt (Developer Instructions)

> **This is the master, final-run document.** Give this file to the developer or AI coding agent doing the actual implementation. It consolidates files 01–11 into one execution prompt, adds a full-site crawlability/indexability audit (not just `/jobs`), and defines the sign-off criteria before calling the work done.
>
> **Hard constraint, repeated because it overrides everything else:** every change must be a pure **addition** — new sections, new pages, new schema, new meta tags, new sitemap entries, new internal links. **Do not delete, rename, move, or restructure any existing file, folder, route, component, or UI element.** Do not redesign anything visually. The one controlled exception is file 01's **Category 2** rule: a *demonstrably incorrect* existing SEO element (a broken canonical, a stray `noindex`, a fabricated `validThrough` date, a wrongly-converted sitemap) may be corrected — but only as an isolated, labeled `fix:` commit, called out explicitly in the PR description, never bundled silently into a `feat:` content update.

---

## Part 1 — Non-negotiable rules for this run

1. No existing file/folder/route is deleted, renamed, or moved.
2. No existing UI section, component, filter, or design element is removed or restyled.
3. No existing indexed URL changes or redirects unless it is currently broken (404/500) — and even then, flag before acting.
4. No existing working meta tag, schema block, or copy is overwritten — only extended or added to, **except** where file 01's Category 2 exception applies (demonstrably incorrect canonical, noindex, structured data, or sitemap entries) — and even then, isolated and labeled per rule 5.
5. Every commit/PR should read as additions in the diff, with any true fix isolated and labeled `fix:` separately from `feat:` additions.
6. Work in a branch. Do not force-push over the main branch. Get the changes reviewed as a diff before merge.
7. Test every change on a staging URL with Google's **URL Inspection → Test Live URL** and **Rich Results Test** before it goes live.
8. Pagination policy is fixed and non-negotiable across this doc set: `/jobs?page=N` pages are independently indexable and **self-canonicalize** (never canonicalize back to `/jobs`), use plain crawlable `<a href>` links with **no `rel="next"`/`rel="prev"`** (see file 02).
9. Before adding any new JSON-LD block, audit the target page for an existing block of the same `@type` first — never ship duplicate/competing schema of the same type on one page (see file 05 Step 0).

---

## Part 2 — Full-site crawlability & indexability audit (run this first, across every template)

This is the piece not fully covered in files 01–11: a systematic bot-access and noindex sweep across the **entire site**, not just `/jobs`. Run this audit on one representative URL from every page type before touching content.

### 2.1 `robots.txt` audit

- [ ] Fetch `https://www.searchsarkarinaukri.com/robots.txt` and list every `Disallow` rule.
- [ ] Confirm none of these are blocked: `/jobs`, `/jobs/*`, `/category/*`, `/qualification/*`, `/districts/*`, `/recruiters/*`, `/exams/*`, `/results/*`, `/admit-cards/*`, `/blogs/*`, `/sitemap*.xml`.
- [ ] Confirm `Googlebot`, `Googlebot-Image`, and (if relevant) `Bingbot` are not singled out with stricter rules than the default `User-agent: *` block.
- [ ] Confirm the `Sitemap:` directive in `robots.txt` points to the current, correct sitemap index URL.
- [ ] Do not add new `Disallow` rules for anything covered in files 03–07 — every new page type created must be crawlable by default.

### 2.2 Meta robots / `X-Robots-Tag` audit (per template, not per URL — check the template source)

For each template — homepage, `/jobs`, job detail, category, qualification, district, recruiter, exam, results, admit card, blog — check:

- [ ] No `<meta name="robots" content="noindex">` present unless the page is a deliberate parameter/filter variant (per file 02 §7).
- [ ] No `X-Robots-Tag: noindex` HTTP header present on any indexable template.
- [ ] No leftover `noindex` from a staging/dev environment accidentally shipped to production (a very common cause of "Crawled – currently not indexed").
- [ ] Confirm `<meta name="googlebot" content="...">` (if present at all) doesn't conflict with the general robots tag.

### 2.3 JavaScript-rendering / bot-access parity check

- [ ] For each template, fetch the page with `curl -A "Googlebot"` (or equivalent) and compare the raw HTML against what a normal browser renders. They should match on core content (title, H1, main text, key links) after the SSR/prerender work in file 02.
- [ ] Confirm no environment-based bot-blocking (Cloudflare, WAF, rate limiting) is challenging or blocking Googlebot/Bingbot user agents. Check hosting/CDN firewall rules for anything that would serve a CAPTCHA or 403 to a legitimate crawler.
- [ ] Confirm the site is not accidentally gated behind a login, cookie consent wall, or interstitial that a crawler can't pass.

### 2.4 Canonical audit

- [ ] Every indexable page has a self-referencing canonical, unless it's a deliberate near-duplicate pointing to a stronger version (file 09 Group D).
- [ ] No canonical points to the homepage from a deep content page by mistake.
- [ ] No canonical loop (A → B → A) or chain (A → B → C).
- [ ] Paginated `/jobs?page=2`, `?page=3`, etc. each **self-canonicalize** — this is the fixed policy (file 02), not a choice to be made per-page. No pagination URL canonicalizes back to `/jobs`.
- [ ] No `rel="next"`/`rel="prev"` present on pagination links — plain `<a href>` only.

### 2.5 Sitemap audit

- [ ] `sitemap.xml` fetched and inspected **before any change**: determine whether it's already a `<sitemapindex>` or a flat `<urlset>` (see file 08 Part B, Step 1). Do not convert a flat sitemap into an index as part of this rollout — that's a separate, explicitly approved change if it's ever done.
- [ ] `sitemap.xml` (or index) is reachable, valid XML, and lists only 200-status, canonical, non-`noindex` URLs.
- [ ] No 404s, redirects, or `noindex` URLs are present in any sitemap.
- [ ] Every new page type from file 07 has (or will have) a corresponding sitemap entry, submitted either as a new child of an existing index, or as a standalone additional sitemap file if the existing one is flat.
- [ ] Sitemap(s) are submitted in Google Search Console and Bing Webmaster Tools.

### 2.6 HTTP status & redirect audit

- [ ] Spot-check a sample of job, category, qualification, and district URLs for unexpected 404, 500, or redirect chains.
- [ ] Confirm no redirect chains longer than one hop anywhere in the new or existing architecture.
- [ ] Confirm HTTPS is enforced and there's no duplicate HTTP/HTTPS or www/non-www version competing for the same content without a canonical/redirect resolving it.

### 2.7 Mobile-friendliness & Core Web Vitals (per template)

- [ ] Run each template through Google's mobile-friendly test / PageSpeed Insights.
- [ ] Confirm LCP, INP, and CLS are in "Good" range after the SSR changes from file 02 — if not, note as a follow-up performance task, don't let it block the content/schema rollout.

### 2.8 Structured data validation (site-wide pass)

- [ ] Run Rich Results Test on: homepage, `/jobs`, one job detail page, one category page, one qualification page, one district page.
- [ ] Confirm zero errors and note any warnings.
- [ ] For each page checked, list existing `@type` values present **before** adding anything (file 05 Step 0) — confirm no duplicate/competing schema of the same type ends up on one page (e.g. two `BreadcrumbList` or two `Organization` blocks).
- [ ] Confirm `JobPosting` schema appears **only** on individual job pages, never on `/jobs`, category, qualification, or district pages (file 05/06 rule).
- [ ] Spot-check a sample of `JobPosting` blocks for field accuracy: `validThrough` matches the actual notification deadline (never calculated/invented), and `employmentType` matches the notification's stated type or is omitted entirely — never defaulted to `FULL_TIME`.
- [ ] Spot-check a sample of recently-closed jobs: `JobPosting` schema removed, page still returns 200 and remains indexable (Case A in file 06 §2) unless it was a deliberate, separately-reviewed Case B removal.

---

## Part 3 — Apply the additive fixes (execute files 02–10, in this order)

Once Part 2's audit is complete and any blocking bot/noindex/robots.txt issues are fixed, implement the content and schema work already specified in the earlier files, in this sequence:

1. **File 02** — `/jobs` technical SEO (SSR, title, meta, canonical, pagination, breadcrumb HTML)
2. **File 04 + 06** — Individual job page template additions + `JobPosting` schema
3. **File 03 + 05** — `/jobs` new content sections + listing-page schema
4. **File 07** — New qualification/category/recruiter/location landing pages
5. **File 08** — Internal linking additions + sitemap architecture
6. **File 09** — Classification and fix pass for existing "Crawled – currently not indexed" URLs
7. **File 10** — GEO/AEO layer (`llms.txt`, answer-first copy, E-E-A-T signals)

Each step must pass its own checklist (already listed in that file) before moving to the next.

---

## Part 4 — Final sign-off checklist (don't call the run "done" until every box is checked)

### Crawlability
- [ ] `robots.txt` blocks nothing important
- [ ] No unintended `noindex` (meta or header) on any indexable template
- [ ] Googlebot/Bingbot user agents are not blocked by CDN/WAF/firewall rules
- [ ] JS-rendered content matches server-rendered/bot-fetched content

### Indexability
- [ ] Every indexable page has a correct, non-conflicting canonical
- [ ] `/jobs` pagination self-canonicalizes per page, with no `rel="next"`/`rel="prev"` markup
- [ ] Sitemap contains only clean, indexable, 200-status URLs; existing `sitemap.xml` structure was inspected, not blindly converted
- [ ] No redirect chains or orphaned pages in the new architecture
- [ ] "Crawled – currently not indexed" URLs from file 09 have been reclassified and improved, not deleted

### On-page & structured data
- [ ] `/jobs` and all new landing pages have unique titles, meta descriptions, H1s per the keyword map (file 07)
- [ ] `JobPosting` schema is present only on job detail pages, with accurate `validThrough` sourced from the actual notification (never calculated) and `employmentType` sourced from the notification or omitted (never defaulted to `FULL_TIME`)
- [ ] Closed-job pages follow Case A (schema removed, page stays live) by default; Case B (page actually removed/noindexed) only used as a rare, separately reviewed decision
- [ ] `/jobs`, category, and qualification pages carry CollectionPage/ItemList/FAQPage schema, not JobPosting, with no duplicate schema types stacked on the same page
- [ ] FAQ visible text matches FAQ schema text exactly, everywhere it's used

### Content & linking
- [ ] New sections on `/jobs` (file 03) are live and none of the existing sections were removed or reordered
- [ ] Internal links from homepage → hubs → clusters → individual pages are in place (file 08)
- [ ] Anchor text is descriptive everywhere new links were added — no "Click Here"
- [ ] Disclaimer and "Verified" sourcing language are consistent across `/jobs`, category, and job pages

### GEO/AEO
- [ ] `/llms.txt` is live at the site root
- [ ] FAQ/intro copy follows the answer-first pattern
- [ ] Freshness fields (`datePosted`, `validThrough`, "Last Updated") are populated and accurate everywhere

### Process integrity
- [ ] Every change is additive; any true bug fix was isolated and labeled separately
- [ ] No existing file, folder, route, or UI element was deleted, renamed, or restyled
- [ ] Diff reviewed and approved before merge to production
- [ ] Post-deploy: URL Inspection re-run on the changed templates to confirm live rendering matches expectations

---

## Part 5 — What to hand back after this run

A short report covering, per template audited in Part 2:
- Any `robots.txt` / `noindex` / bot-blocking issue found and fixed
- Any canonical issue found and fixed
- Confirmation that files 02–10's additive work has been applied
- The final sign-off checklist above, fully checked
- A list of anything intentionally deferred (e.g. Core Web Vitals follow-up work), with reasoning

This report, plus a clean diff of only additive changes (and any isolated, labeled bug fixes), is what "final run" should produce — not a code rewrite, not a redesign, not a restructure.
