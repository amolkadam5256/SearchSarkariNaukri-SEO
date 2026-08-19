# Blog Post Template — Implementation Instructions

This pairs with `blog-post-template.html`. That file is a **static HTML reference implementation** of the architecture in `01-blog-seo-geo-architecture.md` — use it as the source of truth for markup, schema placement, and class names when you build the real template (React component, CMS theme, or static generator).

---

## 1. What to do with this file

- Don't publish `blog-post-template.html` as-is — it's a wired-up example using the PMO/Seva Teerth post as sample data.
- Copy the structure into your actual rendering layer (your React SPA, a CMS template, whatever generates each `/blogs/[slug]` page).
- Every `<!-- REPLACE: ... -->` comment marks a value that must come from your post data (title, dates, images, body sections, FAQs, related posts) — nothing in those spots should stay hardcoded.

---

## 2. Required replacements per post

| Placeholder | Source |
|---|---|
| `<title>`, meta description | Post's `metaTitle` / `metaDescription` fields, not the raw H1 |
| `canonical` URL | `https://www.searchsarkarinaukri.com/blogs/{slug}` |
| `og:image`, `twitter:image` | Post's featured image — 1200×630 |
| Breadcrumb + category link | Post's category + slug |
| JSON-LD (`BlogPosting`, `BreadcrumbList`, `ImageObject`) | Always required — fill from post data |
| JSON-LD (`FAQPage`) | Only include this `<script>` block if the FAQ section actually renders on the page — never ship FAQ schema with no matching visible FAQ |
| Quick Facts list | 4–8 label/value pairs specific to the post |
| Table of Contents | Auto-generate from your H2s at build/render time — don't hand-type it |
| Body sections | Real content, one `<section id="...">` per H2 |
| Author box | Pull from your `/author/{slug}` data, don't leave the generic team bio unless that's genuinely the author |
| Related Articles | Computed: same category first, tag-overlap backfill (see architecture doc §8) |
| Latest Posts | Global most-recent-10, independent of this post's category |

---

## 3. Non-negotiable technical rules

1. **Content must be in the DOM on first render** (or in the HTML your prerender backend serves to bots). Don't hide TOC/FAQ/accordion content behind JS that only populates on click — crawlers and LLMs that don't execute JS will see nothing.
2. **Headings must be sequential**: H1 → H2 → H3, never skip a level. This is a real ranking/citation signal, not cosmetic.
3. **One schema type per concept**: emit `BlogPosting`, not both `BlogPosting` and `Article` for the same page.
4. **Don't duplicate sitewide schema**: `Organization` and `WebSite` JSON-LD already live in your global `<head>` (per your `index.html`) — do not re-emit them on every post.
5. **`alt` text on every image**, written per the pattern in the architecture doc (`[Subject] + [Context] + [Detail]`), never left empty except for genuinely decorative images.
6. **`dateModified` must reflect real edits**, not a bumped timestamp with no content change — this is a trust signal both for Google and for AI systems weighing freshness.
7. **`<table>` for tabular data, `<details>/<summary>` for FAQs/accordions** — never divs styled to look like a table or a JS-only accordion. Both need to be real, crawlable HTML elements.
8. **Internal links**: 8–12 minimum for explainer/news posts, 15–25 for job/pillar guides, placed in-body (not just in a related-articles block at the bottom).

---

## 4. Comments section

The HTML file ships a minimal `<section id="comments">` shell with a form and an empty list container. Wire this to your backend:

- POST endpoint that queues comments for moderation (not auto-publish)
- GET endpoint that returns only approved comments for that post
- Render approved comments server-side / in prerendered HTML if you want them to count as crawlable content — a client-only `fetch()` after mount won't be seen by non-JS bots

---

## 5. Sitemap + llms.txt

These aren't part of the HTML template itself, but are required companions (already delivered separately):

- `generate-blog-sitemap.js` — run on publish/update so new posts land in `sitemap-blogs.xml` automatically
- `llms.txt` — place at `https://www.searchsarkarinaukri.com/llms.txt`

---

## 6. Quick QA checklist before you ship a post through this template

- [ ] Title ≤60 chars, description 150–160 chars, both post-specific
- [ ] Canonical points to this exact post URL
- [ ] All 3–4 JSON-LD blocks present and valid (test in Google's Rich Results Test)
- [ ] H1 exists once; H2s sequential; TOC links match actual section IDs
- [ ] Every image has real `alt` text and explicit width/height
- [ ] FAQ schema only present if FAQ section is visible on the page
- [ ] At least the category-minimum number of internal links, placed in-body
- [ ] Related Articles and Latest Posts both populated (not empty state)
- [ ] Reading time shown and roughly matches actual word count ÷ 200
- [ ] Post added to `sitemap-blogs.xml` (automatic if the generator script is wired to your publish hook)
