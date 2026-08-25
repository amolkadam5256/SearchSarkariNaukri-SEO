# Methodology and Evidence Register

## Automated live crawl

- Googlebot Smartphone user agent; 4 concurrent internal requests with rate limiting.
- Started `2026-08-25T06:11:57.541Z`; finished `2026-08-25T06:25:15.098Z`.
- 3,871 unique sitemap URLs; 5,540 internal URL records discovered/classified (5,524 fetched and 16 UTM URLs intentionally not fetched because `robots.txt` blocks them); 1,480 unique external targets.
- A separate ordinary crawler/CSR-shell pass is preserved under `csr-shell-first-pass/` to document the non-prerendered response.
- Complete exports: `sitemap-urls-full-list.csv`, `crawled-urls-full-list.csv`, `url-audit-all.csv`, `internal-links.csv`, `structured-data.csv`, `images-all.csv`, and reconciliation/error CSVs.

## Rendering and HTTP

- Ordinary browser, Googlebot Smartphone, and Googlebot Desktop responses were recorded in `representative-http-evidence.csv` with raw HTML bodies.
- Mobile and desktop Googlebot HTML hashes were identical for the homepage, jobs hub, job detail, category query, and qualification templates.
- Ordinary visitors receive a CSR shell; recognized bots receive backend prerendered HTML. A random unknown route returns 200 to ordinary visitors but 404 to Googlebot.
- Eight Lighthouse 13.4.1 runs cover homepage, job, category, and qualification templates on mobile and desktop. JSON, HTML, summary CSV, and rendered screenshots are included.
- Google PageSpeed API returned HTTP 429 / quota unavailable; raw response retained in `pagespeed-home-mobile.json`.

## Production read-only checks

- Nginx server block and process status were inspected over SSH without writes/reloads.
- Nginx serves static assets with 30-day immutable caching, gzip is enabled, and TLS listeners use HTTP/2.
- The default shared access-log format omits `$host`, so bot traffic cannot be reliably attributed to this virtual host across the shared log. No traffic counts were guessed.
- TLS certificate: Let's Encrypt YE1; CN `searchsarkarinaukri.com`; SANs include apex, www, and API; valid 3 July–1 October 2026.
- Server IP is in DigitalOcean's India/Karnataka region according to the public IP record checked during the audit.
- Database queries were SELECT-only. `production-database-readonly-evidence.tsv` documents repeated result/admit-card rows and table counts.

## Source review

- Local application source was reviewed read-only at `C:\Users\Administrator\Projects\SakariNaukariN`.
- Relevant files: `frontend/src/App.jsx`, `frontend/src/components/SEO.jsx`, `frontend/src/pages/Home.jsx`, `frontend/index.html`, `backend/src/controllers/prerender.controller.js`, `backend/src/controllers/sitemap.controller.js`, and analytics/IndexNow helpers.
- No application files were changed.
