# 10. On-Page Technical Metadata (Title, Meta Description, H1)

**Priority: 🟠 Medium**

## The problem

### Title tag — too long
```html
<title>Sarkari Naukri 2026 — Latest Government Jobs, MPSC, UPSC, SSC, Railway</title>
```
Currently 75 characters on the primary crawl (a separate crawl showed a
53-character version — you have two different titles live at different
times/crawls, which itself needs to be resolved to one consistent
version). Google typically displays ~50–60 characters before truncating
with "…" in search results.

**Fix** — settle on one canonical title around 55 characters:
```html
<title>Sarkari Naukri 2026 — Latest Government Jobs in India</title>
```
(56 characters — leads with the highest-intent keyword phrase, drops
the long department list which doesn't fit anyway.)

### Meta description — too long, and two different versions live
Version A (205 characters):
```
India's trusted Sarkari Naukri portal. Daily-updated government jobs across all states — MPSC, UPSC, SSC CGL/CHSL, RRB Railway, IBPS, SBI, State PSC, Police Bharti. Eligibility, last date and apply online.
```
Version B (115 characters, Marathi):
```
महाराष्ट्रातील नवीन सरकारी नोकऱ्या — MPSC, UPSC, SSC, Railway, Banking, पोलीस भरती. Apply links + last dates daily.
```
Two different meta descriptions being served on different crawls of the
same URL means the tag is likely being set dynamically/inconsistently
(possibly A/B tested, possibly a caching or rendering timing issue tied to
file 01). **Pick one, make it static and server-rendered, and keep it in
the 120–160 character range:**
```html
<meta name="description" content="India's trusted Sarkari Naukri portal. Daily government job updates — MPSC, UPSC, SSC, Railway, Banking, Police Bharti. Eligibility, last date & apply link." />
```
(157 characters.)

If you want to serve a Marathi meta description to Marathi-language
searchers specifically, that should be tied to a genuine language-specific
URL (see file 05's hreflang guidance on splitting language versions), not
randomly alternating on the same URL.

### H1 — inconsistent between crawls
One audit found **more than one H1 tag**; a different, simpler crawler
found **zero H1 tags**. Combined with the JS-rendering findings in file
01, the most likely explanation: the server-rendered shell has 0 H1s,
and after JavaScript runs, more than one H1 gets added to the DOM
(e.g. one in a page header component and another in a hero/banner
component that were built independently).

**Fix:**
- [ ] Audit every page template for duplicate H1 elements — grep your
      component source for `<h1` and confirm only one component per page
      type renders it.
- [ ] Make sure the single H1 is present in the server-rendered HTML
      (ties directly to file 01).
- [ ] The H1 should closely match (but doesn't need to be identical to)
      the page's title tag and primary target keyword — e.g. for the
      homepage: `<h1>Sarkari Naukri 2026 — Latest Government Jobs</h1>`.

### Keyword consistency across title / meta / headings
The audit found your most page-frequent terms ("jobs", "भरती", "करा",
"posts", "last date", "aug 2026") aren't well represented together across
Title + Meta Description + Heading tags. Once the H1/title/meta are fixed
above, cross-check that the words used in your on-page content headings
match the words used in the title and meta description — consistency
across these three elements is one of the more reliable, low-effort
relevance signals available.

## Implementation checklist
- [ ] Standardize on ONE title tag and ONE meta description per page —
      remove whatever logic is generating two different versions.
- [ ] Ensure title (50–60 chars) and meta description (120–160 chars) are
      within Google's display limits.
- [ ] Fix duplicate/missing H1 per file 01's SSR guidance.
- [ ] Extend this pattern (unique, keyword-aligned title/meta/H1, each
      within length limits) to every job-posting and category page
      template, not just the homepage — this is likely a template-level
      fix that will apply site-wide once corrected in one place.
- [ ] Re-crawl with Screaming Frog (or similar) after deployment and
      filter for "Title Too Long," "Meta Description Too Long," "Missing
      H1," and "Multiple H1" — confirm 0 pages flagged.

## Verification
```bash
curl -s https://www.searchsarkarinaukri.com/ | grep -Eo '<title>.*</title>'
curl -s https://www.searchsarkarinaukri.com/ | grep -Eo '<meta name="description"[^>]*>'
curl -s https://www.searchsarkarinaukri.com/ | grep -Eo '<h1[^>]*>.*?</h1>'
```
Run this against the homepage and a sample of 5–10 job-posting/category
pages to confirm consistency across templates, not just the homepage.
