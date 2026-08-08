# 2. Core Web Vitals & Real-User Performance

**Priority: 🔴 High**

## The problem
| Metric | Field data (real users) | Lab data (Lighthouse) |
|---|---|---|
| LCP | **6.0s — Poor** | 1.9s mobile / 0.6s desktop — Good |
| INP | **275ms — Needs improvement** | not measured in lab |
| CLS | **0.19 — Poor** | 0 — Good |
| Core Web Vitals assessment | **FAILED** | Passed |

A second, independent tool (Catchpoint desktop run) measured **CLS 0.204**
— nearly identical to Google's field CLS of 0.19 — confirming this is a
real, reproducible layout-shift problem, not a fluke of the sample.

The lab test passes because it runs once, on a clean network, with no
ad-blockers, no real user interaction, and often before ads/third-party
scripts finish loading. Real visitors — especially on the slower
Android/mobile-network conditions common in your Indian audience — see
something much worse.

## Root causes to check, in likely order of impact

### 1. Third-party script load
Your Google Tag Manager container fires **20 separate GA4 event tags**
plus Google Analytics, Microsoft Clarity, Ahrefs Analytics, and Google
AdSense on every pageview. Each one adds parse/execution time and network
requests before the page is interactive.
- [ ] In GTM, audit which of the 20 tags actually need to fire on **page
      load** vs. which can fire only on user interaction (scroll, click).
      Convert load-triggered tags to interaction-triggered where possible.
- [ ] Load GTM itself with `async` (it already is) but also consider
      delaying GTM initialization until after the main content is
      interactive, using a "Consent Mode"-style or requestIdleCallback
      pattern.
- [ ] AdSense (`pagead2.googlesyndication.com`) is a common LCP/CLS
      culprit — reserve fixed height/width containers for every ad slot
      so ads don't shift content when they load (this alone likely fixes
      a large share of your 0.19–0.204 CLS).

### 2. Layout shift (CLS 0.19–0.204)
- [ ] Add explicit `width`/`height` (or `aspect-ratio` in CSS) to every
      `<img>` tag so the browser reserves space before the image loads.
- [ ] Reserve a fixed-height container for every ad unit before AdSense
      populates it.
- [ ] Avoid injecting banners, cookie notices, or promo content above
      existing content after load — insert them in a way that doesn't
      push content down (e.g. overlay/fixed position, not inline push).
- [ ] Preload web fonts (`<link rel="preload" as="font">`) or use
      `font-display: swap` consistently so text doesn't reflow when
      custom fonts finish loading.

### 3. Largest Contentful Paint (LCP 6.0s field vs 1.9s lab)
- [ ] Identify the actual LCP element on real page loads (PageSpeed
      Insights → "LCP breakdown" panel, or Chrome DevTools Performance
      panel with a throttled connection) — it's usually the hero
      image/heading or the first job-listing card.
- [ ] If the LCP element is an image, ensure it isn't lazy-loaded (only
      lazy-load images below the fold) and preload it:
      `<link rel="preload" as="image" href="...">`.
- [ ] Reduce Time to First Byte — your server response is currently
      0.74s–1.1s across tests, on the slow side. See "Server response
      time" below.
- [ ] Since content is JS-rendered (see file 01), the LCP element likely
      can't paint until the JS bundle downloads, parses, executes, AND
      fetches data — this is very likely your single biggest LCP
      contributor. Fixing file 01 (SSR/pre-rendering) will materially
      improve this metric on its own.

### 4. JavaScript payload
- [ ] Reduce unused JavaScript — PageSpeed flagged **~155 KiB** of
      estimated savings. Run `npx vite-bundle-visualizer` (or your
      bundler's equivalent) to find unused/oversized dependencies and
      code-split routes so each page only loads the JS it needs.
- [ ] Confirm the production build's JS is minified — one crawl flagged
      `assets/index-_mOdqmpp.js` as not minified; verify your Vite/webpack
      build is running in production mode (`NODE_ENV=production` /
      `vite build`, not `vite dev`) on the deployed server.

### 5. Caching
- [ ] PageSpeed flagged **~16 KiB** savings from inefficient cache
      lifetimes. Add long-lived cache headers for hashed static assets
      (JS/CSS/images with content-hash filenames like
      `index-BMk3bV5m.css` are safe to cache for a year):
```nginx
location ~* \.(?:css|js|woff2?|jpg|jpeg|png|webp|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### 6. Server response time (TTFB 0.74s–1.1s)
- [ ] Profile backend response time under load — 0.74–1.1s TTFB is high
      for a mostly-static content site. Check if the API/data layer
      (job listings) is doing unnecessary work per-request; add
      server-side caching (Redis/in-memory) for job listing data that
      doesn't change every request.
- [ ] Confirm gzip/Brotli compression is enabled for HTML/JSON responses,
      not just static assets (current scan shows 0% compression on
      "Other" resource category).
- [ ] Enable HTTP/2 keep-alive and consider a CDN in front of Nginx
      (Cloudflare, Fastly, or similar) to cut network latency for users
      far from your origin server (157.245.102.177).

### 7. Inline styles
- [ ] Move inline `style="..."` attributes into the external CSS
      stylesheet — inline styles block the browser's ability to
      cache/reuse styling and were flagged as a Best Practices issue.

## Verification
1. After each change, re-test at https://pagespeed.web.dev/ — watch the
   **lab** numbers move first.
2. Field/CrUX data takes **28 days** to refresh with enough real-user
   samples — set a calendar reminder to re-check the Core Web Vitals
   assessment 4 weeks after deploying fixes.
3. Use Chrome DevTools → Performance panel with "Slow 4G" + "4x CPU
   slowdown" throttling to approximate the experience of your actual
   mobile audience while testing locally.
