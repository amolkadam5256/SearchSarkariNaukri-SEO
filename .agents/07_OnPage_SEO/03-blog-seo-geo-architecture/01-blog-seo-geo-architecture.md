# SearchSarkariNaukri — Universal Blog Page Architecture
### One template. Every post. SEO + AI/GEO + technical implementation spec.

Audited against: `/blogs` index (React SPA, react-helmet-async, prerender backend) and the live PMO/Seva Teerth post.

---

## 0. Current-state audit (what's live today)

| Element | Status on live post | Verdict |
|---|---|---|
| Breadcrumb | Text only, no `BreadcrumbList` schema visible | Fix |
| H1 | Present, keyword-relevant | OK |
| Author | Name only, no bio/author page/`Person` schema | Weak |
| Date | Published date shown, no `dateModified` | Weak |
| Category | Shown ("Government Facts"), not a clickable filtered archive link in-body | Fix |
| Body content | ~750 words, single wall of text, no H2/H3 breaks | **Critical** |
| TOC | Missing | Missing |
| Quick-summary/key-facts box | Missing | Missing |
| FAQ + FAQPage schema | Missing | Missing |
| Internal links (in-body) | ~0 | **Critical** |
| Related articles | Missing | Missing |
| Category archive / tag archive pages | Tags shown as flat hashtags, not linked | Fix |
| Comments | Missing | Missing |
| Share buttons | Missing | Missing |
| Reading time | Missing | Missing |
| Image alt text | Featured image present but no visible alt strategy | Verify |
| Schema (Article/BlogPosting/Person/FAQ) | Only sitewide Organization + WebSite in `<head>`, nothing per-post | **Critical** |
| llms.txt | Not present | Missing |
| Sitemap for blogs | `sitemap-blogs.xml` exists, needs auto-inclusion on publish | Verify automation |

This doc fixes every row above with one reusable template.

---

## 1. The One Blog Template (applies to every post, every category)

```
┌─ Hero
│   Breadcrumb (with BreadcrumbList schema)
│   Category chip (→ links to /blogs?category=slug)
│   H1
│   Meta row: Author (→ author page) · Published date · Updated date · Reading time
│   Share buttons (WhatsApp, Telegram, X, Copy link)
│   Featured image (1200×630, descriptive alt, lazy=false for LCP)
│
├─ Quick Facts / Key Takeaways box   ← answer-first, snippet + AI-Overview bait
├─ Table of Contents (auto-generated from H2/H3, sticky on desktop, collapsible on mobile)
├─ Introduction (150–300 words, answers "what is this about" in first 2 sentences)
├─ Body — H2/H3 sectioned, each section leads with the direct answer, then elaborates
│   (tables, cards, checklists, timelines as content demands — see §2)
├─ FAQ section (8–15 Q&A, FAQPage schema)
├─ Author box (bio, expertise, sources reviewed, Person schema)
├─ Related Articles (4–8 cards, same category or tag overlap)
├─ Latest Posts widget (sidebar/desktop, inline-below on mobile — last 6–10 posts sitewide)
├─ Category browse strip ("More in Government Facts →")
├─ Comment section (moderated, schema-safe — see §7)
├─ WhatsApp/Telegram CTA
└─ Footer (sitewide)
```

This is a **single component**, not a per-post hand-built page. Content differs; the shell, schema, and SEO plumbing do not.

---

## 2. Content-block library (use as needed per post)

Every post doesn't need every block — but every post should draw from this shared library so markup stays consistent for AI extraction:

- **Quick Facts box** — 4–8 label/value pairs, always immediately under H1
- **Key Highlights cards** — 3–6 cards, 2-col mobile / 4-col desktop
- **Comparison/spec table** — `<table>` with real `<th>` headers (never a screenshot, never a div-grid pretending to be a table — Google and LLMs both parse `<table>` for passage extraction)
- **Timeline** — ordered list styled as vertical steps, each step = one `<li>` with a heading, not a flat paragraph
- **Checklist** — `<ul>` with icon, real list markup
- **Accordion (syllabus/FAQ-like sub-lists)** — use `<details>/<summary>` where possible; it's crawlable *and* naturally accessible, unlike JS-only accordions that hide content from non-JS crawlers
- **Pull quote / callout** — for a single stat or definition worth extracting alone

Rule for every block: **content must exist in the DOM on first render** (or be present in the prerendered HTML your backend serves to bots). Accordions/tabs that only populate content via `onClick` and never render it to the DOM are invisible to passage-ranking and to LLM crawlers that don't execute JS.

---

## 3. Content-length targets (per category)

| Category | Word count |
|---|---|
| News | 800–1,200 |
| Results / Admit Cards | 1,200–1,500 |
| Government Facts / Explainers (like the PMO post) | 1,500–2,500 |
| Career Guide / Job notification deep-dive | 2,500–4,000 |
| Pillar guides (e.g. "Complete UPSC Guide") | 4,000–7,000 |

The PMO post is currently ~750 words against a 1,500–2,500 target for its category — expand with the missing H2s in §4 rather than padding.

---

## 4. Section-by-section rebuild — worked example (PMO/Seva Teerth post)

```
H1: Why Did the PMO Move Out of South Block? The Story Behind India's New Seva Teerth

Quick Facts:
  New PMO Location: Seva Teerth
  Inaugurated: February 2026
  Old Location: South Block, Raisina Hill
  Sister Complex: Kartavya Bhavan
  Institutions Moved: PMO, Cabinet Secretariat, National Security Council Secretariat

TOC:
  1. India's PMO Has a New Address
  2. What Was South Block?
  3. Why Was a New Complex Needed?
  4. What Is Seva Teerth?
  5. What Is Kartavya Bhavan?
  6. Is South Block Gone?
  7. Why Does This Matter to Citizens?
  8. From Colonial Buildings to Modern Administration
  9. FAQs

H2: India's PMO Has a New Address
  [lead sentence answers it directly, then context]

H2: What Was South Block?
H2: Why Was a New Complex Needed?
  → bullet list of infra drivers (digital systems, secure comms, etc.)
H2: What Is Seva Teerth?
  → Info card: "Seva Teerth Houses" checklist
H2: What Is Kartavya Bhavan?
  → Info card: ministries list
H2: Is South Block Gone?
H2: Why Does This Matter to Citizens?
H2: From Colonial Buildings to Modern Administration

FAQ (10):
  What is Seva Teerth?
  Why did the PMO move from South Block?
  Is South Block demolished?
  Which ministries moved to Kartavya Bhavan?
  When was Seva Teerth inaugurated?
  Does South Block still exist today?
  Who inaugurated Seva Teerth?
  What institutions are housed in Seva Teerth?
  Why was new government infrastructure needed?
  How does this affect ordinary citizens?

Internal links to add (8–12 minimum):
  → /blogs?category=government-facts
  → /blogs/[related: "What Does the Cabinet Secretary Actually Do"]
  → /blogs/[related: "How India's District Administration Works"]
  → /blogs/[related: "Why Doesn't India Have a National Language"]
  → /current-affairs
  → /exam-calendar
  → /blogs (main archive)
  → UPSC / civil-services exam page (relevant since PMO relates to civil service structure)
```

Apply the same pattern (Quick Facts → TOC → sectioned H2s → FAQ → internal links) to **every** post regardless of category — only the block mix (table vs timeline vs card grid) changes.

---

## 5. On-page SEO checklist (apply per post, not just per site)

- [ ] Title tag: keyword near the front, ≤60 characters
- [ ] Meta description: benefit-led, 150–160 characters, includes primary keyword
- [ ] URL: short, slug = keyword phrase (already true on this site)
- [ ] H1: one per page, contains primary keyword, matches title intent
- [ ] H2/H3: sequential, no skipped levels (H2 → H3, never H2 → H4) — sequenced headings correlate strongly with LLM citation likelihood
- [ ] Primary keyword present naturally in first 100 words
- [ ] Every image: descriptive `alt` (see §6), compressed, explicit `width`/`height` to avoid layout shift
- [ ] Internal links: 15–25 for pillar/job posts, 8–12 minimum for explainer/news posts
- [ ] Outbound citation links for factual/statistical claims (PIB, ministry notification, official gazette) — this is an E-E-A-T and AI-trust signal
- [ ] `canonical` injected per-route via Helmet (already your pattern — keep it, don't hardcode)
- [ ] `og:` + `twitter:` tags per post (title/description/image specific to the post, not the site default)
- [ ] `dateModified` shown and in schema whenever a post is updated
- [ ] Reading time computed from word count (≈200 wpm) and shown in the meta row

---

## 6. Image alt-text standard

Bad: `alt="image"`, `alt="blog photo"`, `alt=""`
Good pattern: **[Subject] + [Context] + [Specific detail]**

| Image | Alt text |
|---|---|
| Featured image, PMO post | `Seva Teerth building complex in New Delhi, India's new Prime Minister's Office inaugurated February 2026` |
| Info card icon | `Icon representing Cabinet Secretariat relocation to Seva Teerth` |
| Timeline graphic | `Timeline of India's PMO relocation from South Block to Seva Teerth, 2024–2026` |

Rules:
- Never leave `alt` empty unless the image is purely decorative (then use `alt=""` intentionally, not by omission)
- Don't keyword-stuff — describe what's actually in the image
- File names should be descriptive before upload: `seva-teerth-pmo-new-delhi.jpg`, not `IMG_4021.jpg`
- Featured image dimensions: 1200×630 (matches your existing OG image standard)

---

## 7. Comment section — implementation notes

- Server-side moderation queue (admin-approve before publish) — protects against spam/injected links hurting your domain trust
- Do **not** wire comments into schema as `Comment`/`UserComments` unless you're prepared to keep them permanently — Google treats structured comment counts as a freshness/engagement signal and removing them later looks like a negative signal
- Render approved comments in the initial server/prerendered HTML (not client-fetch-only) if you want them to contribute to on-page content depth for crawlers
- Basic anti-spam: honeypot field + rate limit by IP/session, no need for CAPTCHA friction on a first pass

---

## 8. Related Articles / Latest Posts / Category logic (single reusable rule)

**Related Articles (4–8 cards):**
1. Same category, most recent, excluding current post
2. If category has <4 posts, backfill with tag-overlap posts from other categories
3. Never show the same related-set sitewide — it must be computed per post

**Latest Posts widget (sidebar or below-content on mobile):**
- Global "last 10 published" across all categories, independent of the current post's category
- This is the block that keeps deep/old posts internally linked from new posts automatically — critical for crawl budget on a large site

**Category strip:**
- "More in [Category] →" linking to `/blogs?category=slug`
- Category itself should be a real indexable archive page with its own `<title>`, meta description, and `CollectionPage` schema — not just a filtered client-side view invisible to bots

---

## 9. Schema (JSON-LD) required per post

See `schema-examples.json` for filled-in copies. Required types per blog post:

1. `BlogPosting` (or `Article` — pick one consistently, don't emit both)
2. `BreadcrumbList`
3. `FAQPage` (only if the FAQ block is present — don't emit empty/mismatched FAQ schema, Google actively penalizes FAQ rich-result spam where the visible FAQ doesn't match markup)
4. `Person` (author) — link `author.url` to a real `/author/[slug]` page
5. Reuse sitewide `Organization` + `WebSite` (already present in your `<head>`) — no need to duplicate per post
6. `ImageObject` for the featured image, referenced from `BlogPosting.image`

Inject schema **inside the same Helmet call that sets the per-post canonical/meta**, so bots and the prerender backend always see it alongside the rest of the head — not as a separate late-mounting effect.

---

## 10. llms.txt (AI/GEO layer)

Add `https://www.searchsarkarinaukri.com/llms.txt` at the domain root — see `llms.txt` file provided. This is the emerging convention (not yet universally adopted by all AI crawlers, but low-cost and increasingly checked) that gives LLMs a curated map of your most important, canonical pages instead of forcing them to infer structure from HTML. Keep it manually curated and short — it's a map, not a full sitemap dump.

---

## 11. Sitemap — blog inclusion workflow

Your `sitemap-blogs.xml` needs to be **auto-regenerated on publish**, not hand-maintained. See `generate-blog-sitemap.js` for the reference implementation:

- Runs on your publish webhook / CMS save hook / cron
- Pulls all published posts from the DB (slug, `updatedAt`)
- Writes `<lastmod>` from `updatedAt`, not `createdAt` — this is what tells Google a post was refreshed
- Excludes draft/unpublished/noindex posts
- Keeps `sitemap-blogs.xml` under 50,000 URLs / 50MB (split by year if you exceed it — you won't for a while at current volume)
- `sitemap.xml` index (already correct per your setup) doesn't need to change — it references `sitemap-blogs.xml` by filename, so regenerating that file's contents is enough

After regenerating, ping Search Console isn't necessary (deprecated) — Google recrawls `sitemap.xml` on its own schedule once submitted, but you can force a refetch of `sitemap-blogs.xml` specifically in GSC's Sitemaps report if you want faster pickup after a bulk publish.

---

## 12. AI/GEO-specific notes (beyond standard SEO)

- **Answer-first writing**: first sentence of every H2 must stand alone as a complete, quotable answer. This is what both Google's passage ranking and LLM extraction key off.
- **Self-contained sections**: don't write "as mentioned above" or "see the next section" — each H2 block should make sense pulled out of context, since that's exactly what gets pulled out of context.
- **One clear answer per question, not hedged**: LLMs preferentially cite content with a direct claim over content that lists five possibilities without a lead answer.
- **Structured data over prose density**: tables, FAQ blocks, and definition-style callouts are disproportionately more likely to be lifted into AI Overviews / ChatGPT / Perplexity answers than paragraph text saying the same thing.
- **Freshness signals**: `dateModified`, visible "Updated on" text, and genuinely revised content (not just a date bump) all matter — LLM-backed search tools weight recency for anything time-sensitive (which is most of this site's content: notifications, cutoffs, vacancies).
- **Citations build trust both ways**: linking out to PIB/official notifications isn't just an SEO nicety — it's what lets an LLM verify your claim against a primary source, which is part of why AI Overviews cite well-sourced pages over unsourced ones.

---

## Files in this delivery

| File | Purpose |
|---|---|
| `01-blog-seo-geo-architecture.md` | This spec |
| `BlogPostTemplate.jsx` | Reusable React component implementing §1–§9 (Helmet meta, schema injection, TOC, FAQ, related posts, comments shell) |
| `schema-examples.json` | Filled JSON-LD for BlogPosting, BreadcrumbList, FAQPage, Person, ImageObject |
| `llms.txt` | Domain-root AI-crawler map |
| `generate-blog-sitemap.js` | Node script: regenerate `sitemap-blogs.xml` from your post DB on publish |
