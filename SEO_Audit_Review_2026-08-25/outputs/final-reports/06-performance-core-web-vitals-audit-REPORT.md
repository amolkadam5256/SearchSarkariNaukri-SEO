# 06 — Performance & Core Web Vitals Audit — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: 25 August 2026
Auditor: Codex + custom Googlebot crawler + Lighthouse 13.4.1 + read-only source/server/database review
Checklist source: 06-performance-core-web-vitals-audit.md
Total items checked: 18
Total Pass: 7 | Total Warning: 4 | Total Fail: 7 | Total N/A: 0

| # | Checklist Item | Status | Evidence | Affected URL(s) | Severity | Recommended Fix | Effort (S/M/L) |
|---:|---|---|---|---|---|---|:---:|
| 1 | Performance score (0–100) | ❌ Fail | `lighthouse-detailed-summary.csv`: performance mobile/desktop — home 42/82; job 56/73; category 71/88; qualification 62/74. | site-wide | High | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 2 | LCP element identified (what's the largest content element and why it's slow) | ⚠️ Warning | Lighthouse trace retained; final viewport screenshots show the homepage notification/onboarding layer and hero/banner content. The LCP-node audit did not expose a stable selector in Lighthouse 13.4.1. | site-wide | Medium | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 3 | Total Blocking Time | ⚠️ Warning | TBT: home mobile 714 ms; job 287 ms; category 206 ms; qualification 141 ms; desktop 0–1 ms. | site-wide | Medium | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 4 | Speed Index | ❌ Fail | Mobile Speed Index: 6.30 s home, 5.43 s job, 3.44 s category, 4.92 s qualification. | site-wide | Medium | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 5 | Time to Interactive | ❌ Fail | Mobile interactive: 8.54 s home, 7.53 s job, 5.65 s category, 7.39 s qualification. | site-wide | Medium | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 6 | Top 5 "Opportunities" listed by Lighthouse (e.g. render-blocking resources, unused JS/CSS, image sizing) | ✅ Pass | Per-run top opportunities/diagnostics are in `lighthouse-detailed-summary.csv`; full audit details in eight Lighthouse JSON/HTML files. Repeated issue: unused JavaScript; several templates also unused CSS, contrast, unnamed links, source maps/third-party cookies. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 7 | Top 5 "Diagnostics" listed by Lighthouse | ✅ Pass | Per-run top opportunities/diagnostics are in `lighthouse-detailed-summary.csv`; full audit details in eight Lighthouse JSON/HTML files. Repeated issue: unused JavaScript; several templates also unused CSS, contrast, unnamed links, source maps/third-party cookies. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 8 | Total page weight (KB) per template | ❌ Fail | Transfer bytes: home 2.91 MB; job 0.92 MB; category 1.03 MB; qualification 0.85–0.89 MB. | site-wide | Medium | Set template byte budgets, code-split the JS bundle, optimize images, and fail CI when mobile transfer size exceeds the agreed threshold. | M |
| 9 | Number of HTTP requests per template | ✅ Pass | Requests: home 37–38; job 29; category 24–25; qualification 24–25. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 10 | Render-blocking CSS/JS identified — list files | ⚠️ Warning | Lighthouse flags unused JS on every sample and unused CSS on job/category/qualification; exact files are in each report JSON. | site-wide | Medium | Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles. | M |
| 11 | Third-party script audit — list every third-party script (ads, analytics, chat widgets, fonts) with its load-time impact | ❌ Fail | Normal browser trace loads OneSignal and Google Fonts; bot prerender additionally injects GTM, direct GA4, Clarity, Ahrefs, and AdSense. This bot/user discrepancy is documented in raw HTML. | site-wide | Medium | Load ads consistently for real users only after consent/critical render, reserve slot dimensions, and measure CLS/revenue impact in browser traces. | M |
| 12 | Font loading strategy (`font-display`, preload of critical fonts) reviewed | ✅ Pass | Google Fonts Poppins stylesheet is used with preconnect; no local critical-font preload observed. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 13 | Browser caching headers (`Cache-Control`, `Expires`) reviewed for static assets | ✅ Pass | Static image response uses `max-age=2592000, public, immutable`; Nginx config applies 30-day caching to static extensions. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 14 | TTFB (Time to First Byte) measured, flagged if >600ms | ✅ Pass | `representative-http-evidence.csv`: all representative ordinary and Googlebot TTFB values under 123 ms, below 600 ms threshold. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 15 | CDN in use — confirm which provider and coverage | ⚠️ Warning | No first-party CDN hostname or CDN response signature observed; assets served from origin. | site-wide | Medium | Add an image/static CDN or edge cache with transforms while preserving canonical asset URLs and cache headers. | L |
| 16 | Hosting region vs primary audience region (India) checked for latency | ✅ Pass | Public IP record places DigitalOcean server in Karnataka, India, aligned with primary audience. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 17 | Layout shift caused by ad units measured (common CLS culprit on jobs/content sites) | ❌ Fail | Desktop CLS is 0.516 job, 0.455 qualification, 0.196 category (poor/needs improvement); normal-browser run did not load AdSense, so shift is not attributable solely to ads. | site-wide | Medium | Load ads consistently for real users only after consent/critical render, reserve slot dimensions, and measure CLS/revenue impact in browser traces. | M |
| 18 | Ad load timing checked against Core Web Vitals impact | ❌ Fail | AdSense is present only in bot-prerender HTML and absent from normal Lighthouse network requests; user ad timing/CLS cannot be measured consistently. | site-wide | Medium | Load ads consistently for real users only after consent/critical render, reserve slot dimensions, and measure CLS/revenue impact in browser traces. | M |

## Lighthouse matrix

| Template | Device | Performance | Accessibility | LCP | TBT | Speed Index | CLS | Bytes | Requests |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| / | desktop | 82 | 81 | 3.22 s | 0 ms | 0.87 s | 0.036 | 2.77 MB | 37 |
| / | mobile | 42 | 85 | 8.54 s | 714 ms | 6.30 s | 0.000 | 2.77 MB | 38 |
| /10th-pass-government-jobs | desktop | 74 | 79 | 1.60 s | 0 ms | 0.80 s | 0.455 | 0.85 MB | 25 |
| /10th-pass-government-jobs | mobile | 62 | 84 | 7.39 s | 141 ms | 4.92 s | 0.000 | 0.81 MB | 24 |
| /jobs?category=mpsc | desktop | 88 | 79 | 1.01 s | 1 ms | 0.85 s | 0.196 | 1.02 MB | 25 |
| /jobs?category=mpsc | mobile | 71 | 83 | 4.92 s | 206 ms | 3.44 s | 0.007 | 0.99 MB | 24 |
| /jobs/job-2026--5015 | desktop | 73 | 80 | 1.57 s | 0 ms | 0.81 s | 0.516 | 0.88 MB | 29 |
| /jobs/job-2026--5015 | mobile | 56 | 85 | 7.53 s | 287 ms | 5.43 s | 0.000 | 0.88 MB | 29 |

Field/CrUX data is N/A because GSC access was not supplied and the PageSpeed API returned quota 429; raw response is retained.

## Summary
- Critical issues: 0 — none
- High issues: 1 — 1
- Medium issues: 10 — 2, 3, 4, 5, 8, 10, 11, 15, 17, 18
- Low issues: 0 — none
- Top 3 priority fixes for this audit area:
  1. Item 1: Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles.
  2. Item 2: Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles.
  3. Item 3: Prioritize mobile: code-split unused JS/CSS, optimize the LCP/cover assets, defer noncritical SDKs, and rerun all eight Lighthouse profiles.
