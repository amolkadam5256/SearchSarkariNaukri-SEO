# MASTER PROMPT — SearchSarkariNaukri Admit Card SEO Recovery
## Phase-wise 50-URL Audit → Fix → Validation → Scale

### ROLE
Act as a senior Technical SEO Engineer, SEO Content Architect, Information Architect, Next.js Engineer, Structured Data Engineer, GEO/AEO strategist, accessibility reviewer and Google Search Console troubleshooting specialist.

Website:
https://www.searchsarkarinaukri.com/

Primary section:
https://www.searchsarkarinaukri.com/admit-cards

Primary route:
`/admit-cards/{id}`

### BUSINESS / SEARCH INTENT
The page exists to help candidates find trustworthy, current admit-card/hall-ticket information and reach the official recruiting authority. The official authority remains the final source.

### CURRENT INDEXING PROBLEM
Google Search Console has reported a large number of `/admit-cards/{id}` URLs under "Discovered – currently not indexed". Do NOT assume every discovered URL deserves indexing. The objective is to make valuable pages crawlable, understandable, unique, useful and technically eligible for indexing.

---

# PHASE 0 — INPUT CONTROL

When I provide a large list of 846 admit-card URLs:

1. Preserve the exact URL order supplied.
2. Extract the first 50 URLs only for the current batch.
3. Do not skip URLs because they appear old.
4. Do not invent missing records.
5. Do not silently replace a supplied URL with another URL.
6. Produce one separate Markdown audit file for each of the first 50 URLs.
7. Produce one batch summary Markdown file.
8. Produce one developer implementation prompt Markdown file.
9. Produce one validation checklist Markdown file.
10. Stop after the first 50 unless explicitly instructed to continue.

Batch formula:
- Batch 01 = URLs 1–50
- Batch 02 = URLs 51–100
- Batch 03 = URLs 101–150
- ...
- Continue in groups of 50.
- The final batch may contain fewer than 50.

Do not assume the URLs are sequential numeric IDs. The user's supplied URL order is authoritative for batch grouping.

---

# PHASE 1 — DISCOVERY AUDIT

For each URL independently inspect:

## A. URL / HTTP
- exact URL
- final URL
- status code
- redirect chain
- HTTPS
- canonical URL
- query parameters
- trailing slash behavior
- duplicate URL variants
- response time
- content type

## B. Indexability
Check:
- robots.txt
- meta robots
- X-Robots-Tag
- canonical
- HTTP status
- sitemap presence
- internal-link discoverability
- orphan status
- soft-404 signals
- duplicate-page signals

Classify:
1. Index
2. Improve then index
3. Consolidate/redirect
4. Noindex
5. 404/410
6. Needs data correction
7. Needs manual verification

Never use noindex as a substitute for fixing a duplicate or broken canonical.

---

# PHASE 2 — FULL ON-PAGE SEO AUDIT

For every URL check:

### Title
- unique
- descriptive
- exam name
- year
- admit card intent
- natural wording
- no duplication
- no keyword stuffing

Recommended:
`{Exam Name} Admit Card {Year}: Download Link, Exam Date`

### Meta description
Unique and useful.
Mention:
- exam
- year
- current status
- official link
- exam date where known

### H1
Exactly ONE.

Recommended:
`{Exam Name} Admit Card {Year}`

Reject:
- duplicate H1
- generic "Admit Card"
- keyword-stuffed H1
- H1 containing repeated year/admit-card wording

### H2
Major sections must have descriptive H2s.

### H3
Use for real subsections and individual FAQs.

### H4–H6
Only use when actual nested information requires them.
Never create H4/H5/H6 just to insert keywords.

---

# PHASE 3 — REQUIRED SEMANTIC HTML

Use semantic HTML based on meaning.

Recommended structure:

```html
<header>
  <nav>...</nav>
</header>

<nav aria-label="Breadcrumb">...</nav>

<main id="main-content">
  <article>
    <header>
      <h1>...</h1>
      <p>...</p>
    </header>

    <section aria-labelledby="status-heading">
      <h2 id="status-heading">...</h2>
    </section>

    <section aria-labelledby="dates-heading">
      <h2 id="dates-heading">Important Dates</h2>
      <table>
        <caption>...</caption>
        <thead>...</thead>
        <tbody>...</tbody>
      </table>
    </section>

    <section aria-labelledby="download-heading">
      <h2 id="download-heading">How to Download ... Admit Card</h2>
      <ol>...</ol>
    </section>

    <section>...</section>

    <aside>...</aside>
  </article>
</main>

<footer>...</footer>
```

Use:
- `header`
- `nav`
- `main`
- `article`
- `section`
- `aside`
- `footer`
- `table`
- `caption`
- `thead`
- `tbody`
- `th`
- `scope`
- `ol`
- `ul`
- `time`
- `a`
- `strong`
- `em`
- `figure`
- `figcaption`
- `details`
- `summary` where appropriate

Do NOT force every tag onto every page.

Semantic HTML is about correct meaning, not maximizing tag count.

---

# PHASE 4 — REQUIRED CONTENT ARCHITECTURE

Every indexable page must be substantially useful.

## H1
`{Exam Name} Admit Card {Year}`

## H2 #1 — Admit Card Status
Immediately answer:
- Is it released?
- Expected?
- Available?
- Historical?
- Revised?
- Postponed?

## H2 #2 — Quick Answer / Latest Update
80–150 words.

Must identify:
- exam
- year
- stage
- authority
- status
- exam date
- official source
- candidate next step

## H2 #3 — Important Dates
Use a real HTML table.

Only verified dates.

Potential rows:
- application date
- exam date
- admit card release
- city intimation
- correction window
- result
- last update

Only include fields actually available.

## H2 #4 — How to Download {Exam Name} Admit Card
5–8 numbered steps.

Use `<ol>`.

## H2 #5 — Official Admit Card Link
Clearly identify:
- authority
- official domain
- official admit-card page

Do not disguise third-party links as official.

## H2 #6 — What to Keep Ready
Examples only when supported:
- registration/application number
- password
- date of birth
- other official login credentials

Never state a credential is mandatory unless verified.

## H2 #7 — Details to Check on Your Admit Card
Explain:
- name
- roll/application number
- exam date
- centre
- reporting time
- photograph/signature
- instructions

Use "may include" for generic fields unless verified.

## H2 #8 — Documents and ID Proof
Separate:
- authority-verified requirements
- general candidate preparation advice

Never convert generic advice into an official requirement.

## H2 #9 — Exam Day Instructions
Provide useful preparation guidance.

Authority-specific rules must come from the authority.

## H2 #10 — What to Do If the Admit Card Is Not Downloading
Cover:
- credentials
- forgot registration details
- portal overload
- browser/cache
- PDF
- mobile/desktop
- official helpdesk
- suspicious links

## H2 #11 — Exam Centre / City Intimation
Conditional.
Do not create a fake city-intimation section.

## H2 #12 — Related Exam Information
Contextually link:
- exam page
- recruitment/job notification
- results
- exam calendar
- syllabus where applicable

## H2 #13 — Related Admit Cards
4–8 genuinely related pages.

Prioritize:
1. same exam
2. same authority
3. same recruitment family
4. same exam category
5. closely related candidate intent

Do not randomly link unrelated pages.

## H2 #14 — Frequently Asked Questions
10–15 questions where sufficient facts exist.

## H2 #15 — Official Source and Verification
Clearly state:
- SearchSarkariNaukri is independent
- official authority is final source
- last updated/verified date

---

# PHASE 5 — UNIQUE CONTENT / ANTI-THIN-CONTENT

This is critical.

Never produce:

"Check your admit card here. Download now. Latest admit card update."

repeated across hundreds of pages.

Each page must have unique factual substance.

Unique variables should include:
- exam name
- stage
- year
- authority
- status
- exam date
- release date
- source
- related exam
- recruitment relationship
- specific candidate questions
- source-verification language
- historical context where useful

Do not spin text mechanically.

If a record has insufficient reliable data:
- improve the underlying record
- or classify it as thin
- or noindex/consolidate/remove as appropriate

---

# PHASE 6 — 10–15 FAQ SYSTEM

Generate questions based on the actual record.

Potential question groups:

### Status
1. Is the {exam} admit card released?
2. When will the admit card be released?

### Download
3. Where can I download the admit card?
4. What is the official website?

### Exam date
5. What is the {exam} exam date?

### Credentials
6. What credentials are required?

### Details
7. What should I check after downloading?

### Problems
8. What if the admit card is not downloading?
9. What if I forgot my registration number?
10. What if the details are incorrect?

### Documents
11. Which documents should I carry?

### Centre
12. Is city intimation available?

### Trust
13. Is SearchSarkariNaukri an official government website?

### Updates
14. Can the exam date/status change?
15. How can I verify the latest update?

Only publish questions that can be answered accurately.

---

# PHASE 7 — INTERNAL LINKING / TOPICAL GRAPH

Build:

`Admit Cards Hub`
↓
`Individual Admit Card`
↓
`Exam`
↓
`Recruitment / Jobs`
↓
`Result`
↓
`Exam Calendar`

For each page:
- at least one crawlable hub link
- relevant contextual links
- related admit-card links
- breadcrumb links

Use descriptive anchors.

Bad:
`Click Here`

Good:
`MPSC Rajyaseva Admit Card 2026`

Do not overlink.

---

# PHASE 8 — GEO

Optimize for geographic search intent only where the record supports it.

Examples:
- Maharashtra
- Pune
- Mumbai
- Nagpur
- state-specific recruitment
- regional examination centre

Do not insert city/state names merely for SEO.

Where geographically relevant, clearly identify:
- state
- authority jurisdiction
- exam centres/regions if officially available

Create useful local-intent relationships:
`Exam → State → Authority → Admit Card → Centre`

Never fabricate centre locations.

---

# PHASE 9 — AEO

Write answer-first blocks.

For each page, make the following facts easy to extract:

**Status:** ...
**Exam date:** ...
**Admit card release:** ...
**Official authority:** ...
**Official website:** ...
**Download:** ...
**Last updated:** ...

Then provide deeper explanations.

Keep direct answers 1–3 sentences.

Do not hide all answer content behind JavaScript.

---

# PHASE 10 — ENTITY / KNOWLEDGE GRAPH

Explicitly identify:
- Exam
- Exam stage
- Year
- Conducting authority
- Recruitment
- Admit Card
- Result
- Official source

Create consistent relationships.

Avoid ambiguous titles such as:
"MPSC Admit Card 2026"

when the record is actually:
"MPSC Rajyaseva Prelims 2026 Admit Card".

---

# PHASE 11 — STRUCTURED DATA

Use JSON-LD.

Recommended:
- BreadcrumbList
- WebPage
- Organization
- Person only if a real displayed author/editor exists

FAQPage:
Only if the visible FAQ content exactly matches the JSON-LD and implementation is appropriate.

Do NOT add:
- JobPosting
- QAPage
- fake Review
- fake AggregateRating
- fake Event
- fake author
- fake publication date
- fake update date

Do not mark up content that is not visible.

Use `@graph` where appropriate to keep entities coherent.

---

# PHASE 12 — METADATA / SOCIAL

Implement:
- title
- description
- canonical
- robots
- Open Graph
- Twitter/X card
- og:title
- og:description
- og:url
- og:type
- og:image only when a real relevant image exists

Do not create irrelevant social metadata.

---

# PHASE 13 — IMAGE SEO

If images are genuinely useful:
- descriptive filename
- accurate alt text
- width/height
- lazy-load below fold
- no keyword stuffing

Decorative images:
`alt=""`

Informative images:
meaningful alt text.

Do not add stock images just to increase content length.

---

# PHASE 14 — CRAWLABILITY

Verify:
- robots.txt
- sitemap.xml
- internal links
- no JS-only navigation
- no orphan URLs
- no infinite URL parameters
- no duplicate routes
- no redirect chains
- no accidental canonicalization

All important links must use normal crawlable `<a href>`.

---

# PHASE 15 — SITEMAP

Include only:
- canonical
- indexable
- valid
- useful URLs

Do not put 896 low-quality records into sitemap merely because they exist in database.

`lastmod` must represent meaningful content changes.

---

# PHASE 16 — CANONICAL

For a unique indexable page:

`/admit-cards/{id}` → self canonical.

Do not:
- canonicalize all to `/admit-cards`
- canonicalize duplicates to arbitrary pages
- canonicalize to a non-equivalent exam
- use canonical to hide bad content

For true duplicates, choose one canonical and redirect/consolidate when appropriate.

---

# PHASE 17 — HISTORICAL / EXPIRED PAGES

An old admit card is not automatically worthless.

Keep historical pages indexable when:
- the exam identity is clear
- information is useful
- page is unique
- content has search value
- no better canonical exists

Do not keep pages solely because an ID exists.

Invalid or meaningless records:
- 404/410 as appropriate.

Thin but potentially useful:
- improve first.

---

# PHASE 18 — ACCESSIBILITY

Check:
- language
- landmarks
- keyboard navigation
- focus
- contrast
- headings
- table headers
- link purpose
- alt text
- status not communicated by color alone
- accessible buttons
- skip navigation

Do not use icons/SVGs as the only representation of meaning.

---

# PHASE 19 — NEXT.JS ENGINEERING

Inspect:
- route implementation
- dynamic route
- metadata generation
- server component/client component boundary
- data fetching
- caching
- revalidation
- loading/error states
- notFound handling
- redirects
- sitemap generation
- robots generation
- JSON-LD generation
- duplicate fetches
- hydration
- rendering

Critical SEO content should be present in server-rendered HTML.

Do not put H1, summary, dates, status or FAQs exclusively inside client-side effects.

---

# PHASE 20 — PERFORMANCE

Audit:
- LCP
- INP
- CLS
- server response
- HTML size
- JS size
- image size
- font loading
- third-party scripts
- unnecessary hydration

Do not sacrifice page usefulness for artificial word count.

---

# PHASE 21 — DATA VALIDATION

Create automated checks for:

- missing exam name
- duplicate exam name
- missing year
- invalid year
- missing authority
- missing official source
- invalid official source
- missing exam date
- invalid date
- missing status
- invalid status
- duplicate record
- duplicate content
- missing last updated
- stale source
- invalid URL
- broken internal URL
- dead official URL
- orphan page
- wrong related links

---

# PHASE 22 — FIRST 50 QUALITY GATE

Do not scale until all 50 have been audited.

Required representative coverage:
- expected
- released
- historical
- duplicate
- missing source
- missing date
- invalid/dead
- long title
- short title
- multiple related exams
- no related exams

For every URL produce:
- current state
- issue
- evidence
- severity
- exact fix
- developer file/component/data field
- acceptance test

---

# PHASE 23 — PRIORITY

### P0
Blocking:
- 404/500 unexpectedly
- redirect loop
- wrong canonical
- noindex conflict
- robots blocking
- wrong route
- duplicate canonical
- critical server-rendering failure

### P1
Major:
- thin page
- duplicate page
- missing official source
- orphan page
- incorrect exam data
- missing internal links

### P2
Important:
- metadata
- heading hierarchy
- content depth
- schema
- AEO/GEO
- accessibility

### P3
Enhancement:
- UX
- visual polish
- performance refinements
- secondary metadata

---

# PHASE 24 — OUTPUT FILES

For Batch 01 create:

`00_BATCH_01_MASTER_AUDIT.md`

`01_URL_001_AUDIT.md`
through
`50_URL_050_AUDIT.md`

Also:
`BATCH_01_DEVELOPER_FIX_PLAN.md`
`BATCH_01_SCHEMA_AUDIT.md`
`BATCH_01_INTERNAL_LINK_AUDIT.md`
`BATCH_01_CONTENT_AUDIT.md`
`BATCH_01_INDEXABILITY_AUDIT.md`
`BATCH_01_VALIDATION_REPORT.md`

Every URL file must be independently actionable.

---

# PHASE 25 — FINAL TABLE

Create:

| # | URL | HTTP | Indexability | Canonical | H1 | Title | Meta | Content | Semantic HTML | Internal Links | Schema | Sitemap | Priority | Exact Fix |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Do not write "OK" without evidence.

---

# PHASE 26 — BEFORE / AFTER

For every issue show:

**Current**
- what exists

**Problem**
- why it is weak

**Required**
- exact target state

**Implementation**
- developer action

**Validation**
- how to test

---

# PHASE 27 — DO NOT DO

Never:
- keyword stuff
- create fake facts
- fake dates
- fake authors
- fake reviews
- fake ratings
- fake exam centres
- copy identical FAQ answers
- create doorway pages
- generate 896 spun pages
- canonicalize all pages to hub
- force every URL into sitemap
- force every URL into index
- use JobPosting schema
- use QAPage incorrectly
- hide critical content from DOM
- rely on JS-only content
- use "click here" everywhere
- create meaningless H4-H6 headings
- add location keywords without geographic relevance

---

# PHASE 28 — DEVELOPER DEFINITION OF DONE

A URL is fixed only when:
- [ ] HTTP correct
- [ ] final URL correct
- [ ] canonical correct
- [ ] robots correct
- [ ] crawlable
- [ ] one H1
- [ ] logical H2/H3
- [ ] H4-H6 only where needed
- [ ] semantic HTML
- [ ] unique title
- [ ] unique meta description
- [ ] unique useful content
- [ ] verified status
- [ ] verified dates
- [ ] official source
- [ ] download steps
- [ ] troubleshooting
- [ ] relevant internal links
- [ ] related pages
- [ ] useful FAQ
- [ ] structured data valid
- [ ] visible schema content matches
- [ ] sitemap decision correct
- [ ] accessible
- [ ] mobile usable
- [ ] performance acceptable
- [ ] no fabricated facts

### FINAL COMMAND
Start with the first 50 URLs I provide. Audit them independently. Do not skip, merge or invent URLs. Produce all requested Markdown files. Do not move to URLs 51+ until I explicitly ask for the next batch.

---

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix this specific Google Search Console indexing issue. Keep all implementation changes limited to admit-card URL routing, canonical logic, page content quality, metadata, structured data, sitemap/robots/indexability, internal links inside the relevant admit-card experience, and QA required for these 896 URLs.
