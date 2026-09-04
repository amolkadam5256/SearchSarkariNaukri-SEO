# Private Platform Data Limitations

Audit date: 25 August 2026

The following data could not be truthfully exported because no authenticated account access was supplied:

- Google Search Console Pages, Performance, Enhancements, Core Web Vitals, Manual Actions, Security Issues, Mobile Usability, and Links reports.
- Bing and Yandex Webmaster dashboards and sitemap submission status.
- GA4 DebugView, Realtime, event/conversion configuration, and GTM container contents.
- Ahrefs/Semrush/Moz paid backlink indexes and exact DR/DA/referring-domain/lost-link exports.
- Logged-in India Google SERP AI Overview/PAA checks.
- Independent Perplexity, Gemini, Copilot, and Claude web-search sessions.
- WhatsApp/Telegram administrator-only subscriber and engagement metrics.

`gsc-indexed-urls-full-list.csv` and `bing-indexed-urls-full-list.csv` contain headers only. This is intentional: fabricating URL-level index data would invalidate the reconciliation. All related report rows are `N/A` and include this reason.

Public search-engine results and public live pages were checked as a limited baseline, but they are not substitutes for private account exports.
