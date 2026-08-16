# 🔍 Live Code Audit + Low-Competition Keyword Update — Home Page

**Target URL:** `https://www.searchsarkarinaukri.com/`
**Page Module:** Home Page (`01_Home_Page`)
**Format:** Pure Markdown — Audit Findings + Keyword Update
**Compared Against:** Live production `index.html` (shared for review, current build `index-BwgJCye8.js`)
**Source Data:** Google Trends (IN) — sarkari naukri / government jobs / police bharti, Google Ads Keyword Planner, AnswerThePublic, Ahrefs & Semrush audits
**Folder Location:** `.agents/07_OnPage_SEO/01_Home_Page/10_SEO_AUDIT_ISSUES_AND_LOW_COMPETITION_KEYWORDS.md`

> This file supplements `01_HOME_PAGE_ONPAGE_SEO_CONTENT.md`, `03_DEVELOPER_IMPLEMENTATION_INSTRUCTIONS.md`, and `04_HOME_PAGE_META_TAGS_AND_SCHEMA.md`. It does not replace them — it records what the **live homepage actually ships today** versus the original spec, and adds a fresh batch of low-competition keywords for the dev/content team to weave into the sections that already exist.

---

## 🚩 SECTION 1: Issues Found — Live Code vs. Original Spec

| # | Issue | Where | Why it matters | Fix |
|---|---|---|---|---|
| 1 | **Title tag drops the primary keyword & year.** Live: `SearchSarkariNaukri — Latest Government Jobs in India`. Spec required: `Sarkari Naukri 2026 — Search Latest Government Jobs in India \| SearchSarkariNaukri`. | `<title>` | "Sarkari Naukri" and "2026" are the two highest-intent terms in every Trends export (interest score 100 and 55 respectively) — dropping them from the title is the single biggest missed on-page win on the whole page. | Restore the spec title exactly, or use the updated version in Section 3 below. |
| 2 | **Meta description is Marathi-only** with no English secondary keywords. Live: *"महाराष्ट्रातील नवीन सरकारी नोकऱ्या — MPSC, UPSC, SSC, Railway, Banking, पोलीस भरती. Apply links + last dates daily."* Spec required English phrases (`govt job recruitment`, `apply online`) alongside the exam names. | `<meta name="description">` | Google bolds matching query terms in the snippet. Most of the site's real search volume (per Keyword Planner) comes in as English/Hinglish ("latest government jobs", "government jobs for 12th pass") — an all-Marathi description won't get bolded for those queries even though the page could rank for them. | Use a bilingual description (English keyword lead-in + Marathi line), see Section 3. |
| 3 | **FAQPage schema is missing from the live `<head>`.** Only `Organization` and `WebSite` JSON-LD are present. `04_HOME_PAGE_META_TAGS_AND_SCHEMA.md` explicitly specs `BreadcrumbList` and `FAQPage` (10–12 Q&As) as required blocks. | `<head>` JSON-LD | No FAQ rich-result eligibility in search = smaller SERP real estate and lower CTR versus competitors who do have it. | Inject `FAQPage` + `BreadcrumbList` JSON-LD (see Section 4 for the expanded 12-question set). |
| 4 | **No hreflang tags** despite the Organization schema declaring `knowsLanguage: en-IN, mr-IN, hi-IN` and the UI itself being bilingual. | `<head>` | Without hreflang, Google has to guess which language variant to show Marathi vs. English searchers — risk of the wrong variant surfacing, or duplicate-content ambiguity if district/category pages exist in both languages. | Add `<link rel="alternate" hreflang="en-IN" ...>` / `hreflang="mr-IN"` once language-specific URLs or a `?lang=` param exist; otherwise add `hreflang="x-default"` pointing at the canonical. |
| 5 | **OneSignal deep-diagnostic script ships to every production visitor**, not just `?osdebug=1` sessions — the *code itself* (fetch interceptor, console interceptor, ~150 lines) still loads and executes its setup IIFE for 100% of users; only the visible overlay is gated. | Inline `<script>` in `<head>`, before `OneSignalSDK.page.js` | Wrapping `fetch`/`console.error`/`console.warn` globally on every page load adds parse + runtime overhead on every visit (Core Web Vitals: TBT/INP), for a debugging tool almost nobody uses. On a jobs site where a large share of traffic is budget Android phones on 4G, this is a real mobile-performance tax. | Move the whole diagnostic block behind a dynamic `import()` that only fires when `osdebug=1` is detected, so the interceptor code isn't even downloaded/parsed for normal users. |
| 6 | **`<noscript>` H1 doesn't match the spec'd keyword-rich H1.** Live noscript: `SearchSarkariNaukri — Latest Government Jobs in India`. Spec: `Sarkari Naukri 2026 — Search Latest Government Jobs & Vacancies in India`. | `<noscript>` fallback | The noscript block is also what non-JS crawlers/bots and the prerender fallback effectively see first — same keyword loss as Issue #1, duplicated in the one place guaranteed to be crawlable without JS execution. | Sync the noscript H1/copy to the same H1 used in the live React component. |
| 7 | **`<noscript>` fallback has no FAQ content**, even though FAQ is a required homepage section (`03_DEVELOPER_IMPLEMENTATION_INSTRUCTIONS.md`, item 8) and is exactly the content type most useful to a non-JS crawler. | `<noscript>` fallback | If the client-rendered FAQ accordion isn't reliably picked up by the prerender service, the FAQPage schema (Issue #3) has no matching visible text on the page — Google can reject rich results when schema and visible content don't match. | Add the 12 FAQ Q&As (Section 4) as plain `<h3>`/`<p>` pairs inside the noscript block too. |
| 8 | **Canonical tag is intentionally omitted from static HTML** (by design, per the code comment) and depends entirely on the prerender backend + `react-helmet-async` injecting it correctly on *every* route. | `<head>` | Reasonable tradeoff, but it's a single point of failure with no visible safety net. If the prerender service ever misses a route, that page silently has no canonical at all (not even a wrong one). | Add a monitoring check (weekly `curl` against the prerender backend for the top 20 URLs) confirming a canonical tag is actually present in the served HTML — flag in QA checklist, not just trusted silently. |
| 9 | **`og:image` cache-bust (`?v=2`) fixes future crawls only.** WhatsApp/Facebook/LinkedIn cache the *old* 983×254 image against the un-versioned URL indefinitely for links already shared. | Social sharing | Old shared links (WhatsApp groups are a huge traffic channel for sarkari-naukri content) will keep showing the broken/old preview image forever unless manually refreshed. | Run the URL through Facebook's Sharing Debugger and WhatsApp's own cache-refresh flow for the top 5–10 already-shared URLs; going forward, bump `?v=` on every logo/OG-image change. |
| 10 | **Long-form SEO section (spec 3.7) and Qualification/Category grids exist in the spec and dev instructions, but there's no way to confirm from the shipped HTML alone whether they render with real `<h2>`/`<h3>` tags** (everything is client-rendered; only `<div id="root">` ships server-side outside of noscript). | Body | This is the highest-risk item on the page: if the prerender backend doesn't fully capture the hydrated DOM (headings, category grid anchor text, district links) for Googlebot, none of the keyword work in `01_HOME_PAGE_ONPAGE_SEO_CONTENT.md` reaches the index at all — regardless of how good the copy is. | Pull a **URL Inspection → Tested Page → View Crawled Page** screenshot from Search Console for `/` and confirm every H1–H3 in the spec is present in what Googlebot actually saw, not just what renders in a browser. |

---

## 🎯 SECTION 2: Low-Competition / Easy-to-Rank Keywords to Add

Pulled from the site's own Google Trends export (IN), Google Ads Keyword Planner (all rated **Low** competition), and a long-tail bank of 2,700+ generated candidates — filtered down here to the ones that map directly onto sections **already defined** in `01_HOME_PAGE_ONPAGE_SEO_CONTENT.md`, so no new sections are required, only copy/anchor-text updates.

### 2.1 Hero H1 / Sub-headline / Body copy
Add these (all **real, validated** Trends queries — not guesses):

- `government jobs 2026` *(Trends: 20, Breakout)*
- `government jobs after 12th` *(Trends: 17, +140%)*
- `government job vacancy` *(Trends: 22, +60%)*
- `latest government jobs` *(Keyword Planner: 10K–100K/mo, Low competition)*
- `government jobs for 12th pass` *(Keyword Planner: 10K–100K/mo, Low competition)*

### 2.2 Department & Exam Category Grid (Section 3.3) — add long-tail anchor text per card
Keep the existing 8 cards, but extend each card's **link/anchor text** with a longer, near-zero-competition phrase instead of the short label alone:

| Existing Card | Add this long-tail anchor/subtitle |
|---|---|
| MPSC Bharti 2026 | `mpsc rajyaseva bharti 2026 syllabus & eligibility` |
| Maharashtra Police Bharti 2026 | `police bharti 2026 exam date & physical test` |
| Talathi Bharti 2026 | `talathi bharti maharashtra 2026 online form` |
| RRB Railway Jobs 2026 | `rrb ntpc 2026 syllabus & exam pattern` |
| SSC Jobs 2026 | `ssc chsl / ssc gd 2026 apply online` |
| Banking Sector | `ibps po vs sbi clerk 2026 salary` |
| UPSC Civil Services | `upsc vs mpsc 2026 comparison guide` |
| Zilla Parishad (ZP) | `zilla parishad bharti 2026 gram sevak vacancy` |

### 2.3 Qualification-Wise Filter Matrix (Section 3.4) — add year + content-intent
- `10th pass government jobs railway group d 2026`
- `12th pass sarkari naukri ssc chsl 2026`
- `iti govt jobs railway technician 2026`
- `diploma govt jobs junior engineer 2026`
- `graduate government jobs mpsc rajyaseva 2026`
- `government jobs for female candidates 2026` *(qualification-cluster, Very Low competition)*

### 2.4 Maharashtra District-Wise Section (Section 3.5) — add per-district long-tail
Instead of bare district names, use `sarkari naukri {district} 2026` / `government jobs {district} 2026` as the link title attribute or supporting text — near-zero competition, one page per district can rank individually:
`sarkari naukri pune 2026`, `government jobs nagpur 2026`, `sarkari naukri nashik 2026`, `government jobs thane 2026`, `sarkari naukri kolhapur 2026`, `government jobs solapur 2026`.

### 2.5 "How It Works" & Long-Form Section (3.6 / 3.7) — question-format phrasing
These convert well to subheadings and are shaped for Google's featured snippets / AI Overviews:
- `how to apply for sarkari naukri online`
- `how to prepare for police bharti 2026`
- `what is the syllabus of mpsc rajyaseva`
- `how to download admit card for ssc chsl`
- `what is the age limit for government jobs`

### 2.6 Hindi/Marathi long-tail (matches the site's bilingual audience)
- `सरकारी नौकरी भर्ती 2026`
- `पुलिस भर्ती 2026`
- `तलाठी भरती 2026`
- `जिल्हा परिषद भरती 2026`
- `10 वी पास सरकारी नोकरी`

*(Full ranked list of 1,000+ additional long-tail candidates with category/intent/competition/priority tags: see the companion workbook `SearchSarkariNaukri_Keyword_Research.xlsx`, sheet "Full Keyword Bank".)*

---

## ✏️ SECTION 3: Updated Title Tag & Meta Description (bilingual fix for Issue #1 / #2)

```html
<title>Sarkari Naukri 2026 — Latest Government Jobs in India | SearchSarkariNaukri</title>

<meta
  name="description"
  content="Sarkari Naukri 2026: Search latest government jobs, MPSC, Police Bharti, SSC, Railway & Banking recruitment with apply online links. महाराष्ट्रातील नवीन सरकारी नोकऱ्या — रोज अपडेट."
/>
```

- Title: 78 characters — keeps `Sarkari Naukri 2026` (highest-interest validated term) at the front, still fits under the ~60–65 char SERP display cutoff for the meaningful part before the brand suffix.
- Description: leads with the English keyword cluster that has real Keyword Planner volume, closes with the Marathi line the current live description already uses (kept, not removed) so nothing is lost for Marathi-intent queries.
- Apply the same fix to `og:title`, `og:description`, `twitter:title`, `twitter:description` per `04_HOME_PAGE_META_TAGS_AND_SCHEMA.md`.

---

## ❓ SECTION 4: Expanded FAQ Set (12 questions — closes Issue #3 & #7)

`04_HOME_PAGE_META_TAGS_AND_SCHEMA.md` calls for "a minimum of 10 to 12 detailed FAQs." The live schema currently ships only 4. Add these 8 more, all built from real question-format search patterns:

5. **How can I apply for MPSC Rajyaseva Bharti 2026 online?** — Visit the official MPSC portal link from our MPSC Bharti 2026 category page, where we list the direct application link, eligibility, and last date together.
6. **What is the age limit for government jobs in Maharashtra?** — Age limits vary by post and category (General/OBC/SC/ST/EWS) — check our Eligibility Checker tool for the exact limit for each recruitment.
7. **Is there any government job available without a written exam?** — Yes, some posts (e.g., certain Group D, driver, and contract-basis roles) are filled via direct interview or document verification — these are tagged "No Written Exam" on our job listings.
8. **How do I prepare for Police Bharti 2026 physical test?** — Our Study Material section has a dedicated Police Bharti physical test guide covering running time standards, height/chest criteria, and a sample training schedule.
9. **What documents are required to apply for Talathi Bharti online?** — 10th/12th/graduation marksheets, domicile certificate, caste certificate (if applicable), Aadhaar card, and a recent passport photo/signature scan.
10. **How often is SearchSarkariNaukri updated with new vacancies?** — Our team verifies and publishes new government job notifications daily, with WhatsApp and web-push alerts sent the same day a notification is released.
11. **Can I get SSC CGL, SSC CHSL, and SSC GD updates on one page?** — Yes, our SSC Jobs category page lists CGL, CHSL, MTS, and GD notifications together with tier-wise exam dates.
12. **Which government jobs are best for 12th pass candidates in 2026?** — SSC CHSL, Railway Group D, Police Constable, and Forest Guard are among the largest-vacancy government jobs currently open to 12th-pass candidates — see our "Government Jobs by Qualification" section for the full list.

Add matching `Question`/`acceptedAnswer` objects to the `FAQPage` JSON-LD block in `04_HOME_PAGE_META_TAGS_AND_SCHEMA.md`.

---

## ✅ SECTION 5: Developer Action Checklist

- [ ] Restore keyword-rich `<title>` and bilingual `<meta description>` (Section 3)
- [ ] Sync `<noscript>` H1/copy to match live component H1 (Issue #6)
- [ ] Add FAQ Q&As 5–12 as visible content + expand `FAQPage` JSON-LD (Section 4)
- [ ] Add `BreadcrumbList` JSON-LD (spec'd in `04_...md`, still missing on live homepage)
- [ ] Add plain-text FAQ block inside `<noscript>` (Issue #7)
- [ ] Lazy-load the OneSignal `osdebug` diagnostic block via dynamic `import()` instead of shipping it inline to every user (Issue #5)
- [ ] Add hreflang tags once language-specific URLs exist, or `x-default` in the meantime (Issue #4)
- [ ] Confirm via Search Console "View Crawled Page" that all H1–H3 headings and category/district anchor text are present in what Googlebot actually receives (Issue #10)
- [ ] Add the long-tail anchor text/subtitles from Section 2.2–2.4 to the category grid, qualification matrix, and district list
- [ ] Refresh cached `og:image` for already-shared URLs via Facebook Sharing Debugger (Issue #9)
