# 1. JavaScript Rendering / Server-Side Rendering (SSR)

**Priority: 🔴 High — this is the root cause behind several other findings.**

## The problem
- The GEO (Generative Engine Optimization) scan measured a **Rendering
  Percentage of 753%** — the fully rendered HTML is 7.5x larger than what
  the server actually sends on first response. That means most content is
  injected client-side by JavaScript after load.
- Your build output (`assets/index-BMk3bV5m.css`, `assets/index-_mOdqmpp.js`)
  is a Vite-style single-page-app (SPA) bundle — this pattern (React/Vue +
  Vite, served as static files by Nginx) almost always ships an
  effectively-empty `<div id="root"></div>` in the raw HTML, with everything
  else added by JS.
- A simple, non-JS-executing crawler (Rank Math SEO Analyzer) confirmed the
  symptom: it found **no H1, no H2, no internal/external links, and no
  canonical tag** on the page — even though all of these exist once
  JavaScript runs.
- This matters for: (a) any crawler/bot that doesn't fully execute JS
  (many SEO tools, some AI/LLM crawlers, social-media link unfurlers), and
  (b) Google itself, which renders JS in a **second, delayed pass** — so
  indexing of JS-only content is slower than indexing of plain HTML.

## How to confirm it yourself
```bash
# Raw HTML the server sends BEFORE any JavaScript runs:
curl -s https://www.searchsarkarinaukri.com/ | head -c 2000

# Compare to what a browser renders (needs a headless browser):
npx playwright screenshot https://www.searchsarkarinaukri.com/ rendered.png
```
If the `curl` output shows only a `<div id="root"></div>` (or similar) with
no visible job listings, headings, or nav links in plain text, this is
confirmed.

## The fix — three options, in order of preference

### Option A (recommended): Move to a framework with built-in SSR
If you're using React, migrate the app (or at minimum the public-facing
pages: homepage, job listing pages, category/district pages) to
**Next.js** (`getServerSideProps` / App Router server components) or
**Remix**. If you're using Vue, use **Nuxt**. These render full HTML on the
server for every request, so crawlers and users both get complete content
immediately — this is the standard, most robust fix and also improves your
Core Web Vitals (see file 02).

### Option B: Static pre-rendering at build time
If page content doesn't change per-request in real time (or changes only a
few times a day when new jobs are posted), pre-render pages to static HTML
at build/deploy time:
- **Vite + vite-plugin-ssr** or **vite-plugin-prerender**, or
- **react-snap** (crawls your own built SPA with a headless browser and
  writes static HTML snapshots for each route), or
- **Astro** (if a rewrite is on the table) — ships zero JS by default and
  is very well suited to a content/listing site like this one.
This is simpler to bolt onto an existing SPA than full SSR and works well
for a site whose data (job postings) refreshes on a schedule rather than
per-request.

### Option C (stopgap, not a long-term fix): Dynamic rendering at the edge
If A/B aren't feasible immediately, serve a pre-rendered HTML snapshot
**only to bots**, while regular users still get the SPA:
1. Run a headless-Chrome rendering service (e.g. `rendertron` or
   `prerender.io`, self-hosted or hosted).
2. In Nginx, detect known crawler user agents and proxy them to the
   rendering service; pass everything else straight to the SPA:

```nginx
map $http_user_agent $is_bot {
    default 0;
    "~*googlebot|bingbot|yandex|baiduspider|facebookexternalhit|twitterbot|linkedinbot|slackbot|discordbot|whatsapp|telegrambot|gptbot|oai-searchbot|claudebot|perplexitybot|ccbot" 1;
}

server {
    listen 443 ssl;
    server_name www.searchsarkarinaukri.com;

    location / {
        if ($is_bot) {
            proxy_pass http://127.0.0.1:3001;  # your rendertron/prerender service
        }
        try_files $uri /index.html;
    }
}
```
This is explicitly a stopgap — Google treats this as acceptable
("dynamic rendering") but it does nothing for real users' Core Web
Vitals, and it needs constant upkeep of the bot user-agent list. Treat it
as a bridge to Option A or B, not the destination.

## What must be present in the raw (pre-JS) HTML once fixed
- [ ] Exactly one `<h1>` per page
- [ ] `<link rel="canonical" href="...">`
- [ ] Primary navigation links (home, jobs, districts, admit-cards, results)
- [ ] The core textual content of the page (job title, eligibility, last
      date, apply link — not placeholders)
- [ ] `<meta name="description">` unique per page
- [ ] JSON-LD structured data (`<script type="application/ld+json">`)

## Verification after deploying the fix
```bash
curl -s https://www.searchsarkarinaukri.com/ | grep -Eo '<h1[^>]*>.*</h1>'
curl -s https://www.searchsarkarinaukri.com/ | grep 'rel="canonical"'
```
Then re-run the Rank Math SEO Analyzer (or any simple crawler) and confirm
H1/H2/links/canonical are now detected without JS execution.
