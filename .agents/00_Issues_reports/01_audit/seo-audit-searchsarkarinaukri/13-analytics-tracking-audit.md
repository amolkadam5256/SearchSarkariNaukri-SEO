# 13 — Analytics, Search Console & Tracking Verification Audit

Output file: `outputs/final-reports/13-analytics-tracking-audit-REPORT.md`

## A. Search Engine Verification (site owns/controls these — already partially confirmed)
- [ ] Google Search Console property verified — confirm both `https://www.searchsarkarinaukri.com` (URL-prefix or Domain property) is set up and verified (meta tag already present: `mvXXirem11CN1PlsDJUZHe3ULEZZ89fJYxzVntCwEU4`)
- [ ] Bing Webmaster Tools verified (meta tag present: `048D50336F4A7B374493EA0719557EAD`) — confirm active and sitemap submitted
- [ ] Yandex Webmaster verified (meta tag present: `09463710b0a1a1f7`) — confirm relevance (low priority for India-focused audience — flag if unmaintained)
- [ ] IndexNow protocol implemented (recommended for a site publishing frequent time-sensitive job updates — instantly notifies Bing/Yandex of new/updated pages)

## B. Analytics Implementation
- [ ] Google Analytics 4 (or equivalent) installed and firing correctly (verify via GA4 DebugView or browser network tab)
- [ ] Key events tracked: "Apply Now" click, "Save Job", search usage, filter usage, outbound clicks to official recruiter sites
- [ ] Google Tag Manager in use (if applicable) — audit container for unused/duplicate tags
- [ ] Cross-domain tracking configured correctly if any subdomains exist

## C. Search Console Data Health
- [ ] Confirm no manual actions present (Security & Manual Actions report)
- [ ] Confirm no security issues flagged (malware, hacked content)
- [ ] Core Web Vitals report reviewed (cross-ref file 06)
- [ ] Mobile Usability report reviewed — export any errors
- [ ] Links report reviewed (top linking sites, top linked pages)

## D. Conversion / Goal Tracking
- [ ] Define and confirm tracked "conversions" for this business model (e.g.
  outbound click to official application link, WhatsApp/Telegram channel join,
  saved job/account creation) are actually measured
