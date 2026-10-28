# 9. Sitemap, robots.txt & Canonical Tags — Ongoing Hygiene

**Priority: 🟢 Low (maintenance) — current state is already valid, this file is about keeping it that way and closing a visibility gap**

## Current state (already good — don't break these)
- **XML Sitemap**: `https://www.searchsarkarinaukri.com/sitemap.xml` —
  valid, UTF-8, sitemap index format, 1,819 discovered pages, submitted
  and read successfully.
- **robots.txt**: `https://www.searchsarkarinaukri.com/robots.txt` — valid,
  correctly disallows private/app areas, allows Googlebot at `/`,
  references the sitemap. Current rules:
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /dashboard
Disallow: /saved-jobs
Disallow: /my-saved-jobs
Disallow: /profile-setup
Disallow: /preferences
Disallow: /reminders
Disallow: /api/
Disallow: /login
Disallow: /register
Disallow: /*?utm_*
Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml
```
  No major search engines or AI crawlers are blocked — good, keep it that
  way (don't add blanket `Disallow: /` rules for AI user-agents unless
  that's a deliberate business decision).
- **Canonical tag**: present and self-referencing in the actual rendered
  HTML (`<link rel="canonical" href="https://www.searchsarkarinaukri.com/" />`).

## The gap
One simple crawler (Rank Math Analyzer) reported **no canonical tag
found** — this is the same JavaScript-rendering issue covered in file 01,
not a problem with the canonical tag itself. The fix is the same: ensure
the canonical `<link>` is present in the server-rendered HTML, not
injected only by client-side JS.

## Ongoing sitemap hygiene checklist
- [ ] **Only list canonical, indexable URLs in the sitemap.** Don't
      include URLs that are `noindex`'d, redirect elsewhere, or return
      404/410 — every mismatch wastes a small amount of Google's trust in
      the sitemap's accuracy. Automate sitemap generation to pull only
      from your database of live, publishable job postings/pages.
- [ ] **Update `lastmod` accurately** — only bump the `lastmod` date on a
      URL when its content genuinely changed, not on every sitemap
      regeneration. Inaccurate `lastmod` timestamps reduce Google's trust
      in the signal over time.
- [ ] **Remove expired job postings from the sitemap** once they're
      handled per file 03's soft-404 guidance (either 301-redirected,
      converted to a "closed" page, or removed).
- [ ] **Keep sitemap file size reasonable** — a single sitemap file
      supports up to 50,000 URLs / 50MB uncompressed; at 1,819 URLs
      you're nowhere near the limit, but if you split into multiple
      sitemap files as the site grows (e.g. by content type:
      jobs-sitemap.xml, districts-sitemap.xml, blog-sitemap.xml), keep
      all of them referenced from the sitemap index.
- [ ] **Re-submit the sitemap in Search Console** any time you make a
      structural change to site sections (new content type added,
      major URL pattern change).

## robots.txt checklist
- [ ] Periodically re-run the [robots.txt
      tester](https://www.google.com/webmasters/tools/robots-testing-tool)
      (or any validator) after deploys that touch routing — a common
      accidental regression is a build/deploy pipeline overwriting
      robots.txt with a stricter default (some frameworks ship a
      `Disallow: /` robots.txt for staging that can leak to production).
- [ ] Confirm the `Disallow: /*?utm_*` rule isn't accidentally blocking
      legitimate paginated or filtered URLs that use query parameters for
      real content (e.g. `/jobs?category=mpsc`) — spot-check that pattern
      against your actual URL structure so you're only blocking marketing
      UTM parameters, not content-bearing query strings.

## Canonical tag checklist (for every template, not just homepage)
- [ ] Every indexable page has exactly one self-referencing canonical
      tag, server-rendered.
- [ ] Paginated job-listing pages (e.g. page 2, 3... of a category) either
      self-canonicalize per page (recommended by current Google guidance)
      or, if you intentionally want only page 1 indexed, canonicalize to
      page 1 — pick one approach and apply it consistently.
- [ ] Filtered/query-parameter URLs (e.g. `/jobs?category=mpsc`) should
      canonicalize to the clean version if the filtered view isn't meant
      to be indexed separately, or self-canonicalize if it is.

## Verification
```bash
curl -s https://www.searchsarkarinaukri.com/sitemap.xml | head -30
curl -s https://www.searchsarkarinaukri.com/robots.txt
curl -s https://www.searchsarkarinaukri.com/some-job-page | grep 'rel="canonical"'
```
Re-run the XML sitemap validator and robots.txt tester after any change
to either file.
