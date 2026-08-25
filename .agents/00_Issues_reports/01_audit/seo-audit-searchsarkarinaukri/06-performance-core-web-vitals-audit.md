# 06 — Performance & Core Web Vitals Audit

Output file: `outputs/final-reports/06-performance-core-web-vitals-audit-REPORT.md`
Run PageSpeed Insights (uses Lighthouse + real-world CrUX data) for
Mobile AND Desktop, on: homepage, 1 job listing page, 1 category page, 1
qualification/static page. Also pull the site-wide CrUX report from Search
Console "Core Web Vitals" report.

## A. Core Web Vitals (field data — CrUX, from Search Console)
| Metric | Mobile (Good/Needs Improvement/Poor) | Desktop | URLs affected |
|---|---|---|---|
| LCP (Largest Contentful Paint) | | | |
| INP (Interaction to Next Paint) | | | |
| CLS (Cumulative Layout Shift) | | | |

## B. Lab Data (PageSpeed Insights per page)
For each of the 4 sample pages × 2 device types, log:
- [ ] Performance score (0–100)
- [ ] LCP element identified (what's the largest content element and why it's slow)
- [ ] Total Blocking Time
- [ ] Speed Index
- [ ] Time to Interactive
- [ ] Top 5 "Opportunities" listed by Lighthouse (e.g. render-blocking resources, unused JS/CSS, image sizing)
- [ ] Top 5 "Diagnostics" listed by Lighthouse

## C. Resource Audit
- [ ] Total page weight (KB) per template
- [ ] Number of HTTP requests per template
- [ ] Render-blocking CSS/JS identified — list files
- [ ] Third-party script audit — list every third-party script (ads, analytics,
  chat widgets, fonts) with its load-time impact
- [ ] Font loading strategy (`font-display`, preload of critical fonts) reviewed
- [ ] Browser caching headers (`Cache-Control`, `Expires`) reviewed for static assets

## D. Server & Hosting
- [ ] TTFB (Time to First Byte) measured, flagged if >600ms
- [ ] CDN in use — confirm which provider and coverage
- [ ] Hosting region vs primary audience region (India) checked for latency

## E. Ad / Monetization Impact (if site runs ads)
- [ ] Layout shift caused by ad units measured (common CLS culprit on jobs/content sites)
- [ ] Ad load timing checked against Core Web Vitals impact
