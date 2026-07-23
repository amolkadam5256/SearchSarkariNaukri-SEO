# 07 — Technical SEO

## 7.1 Production `robots.txt` Specification

```
# robots.txt for searchsarkarinaukri.com

User-agent: *
Allow: /

# Block internal search result pages & API endpoints
Disallow: /search?
Disallow: /api/

# Block administrative directories
Disallow: /admin/
Disallow: /dashboard/
Disallow: /login

# Block low-value parameter sort routes
Disallow: /*?sort=
Disallow: /*?page=*&sort=

# Master Sitemap Index Reference
Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml

# Crawl Delay Directives for non-Google crawlers
User-agent: Bingbot
Crawl-delay: 1
```

---

## 7.2 12-Sitemap Architecture Matrix

Master Index URL: `https://www.searchsarkarinaukri.com/sitemap.xml`

| Sitemap File | Contents / Scope | Update Frequency | Google News Protocol? |
|--------------|------------------|------------------|-----------------------|
| `sitemap.xml` | Master Sitemap Index File | Real-time | Index File |
| `sitemap-static.xml` | Homepage, About, Contact, Policies | Monthly | No |
| `sitemap-jobs.xml` | All individual job notification URLs | Real-time | No |
| `sitemap-news.xml` | News articles (Last 48 hours only) | Real-time | **YES** (Google News) |
| `sitemap-results.xml` | Exam results landing pages | Daily | No |
| `sitemap-admit-cards.xml` | Hall ticket / Admit card pages | Daily | No |
| `sitemap-locations.xml` | 36 State and Union Territory pages | Weekly | No |
| `sitemap-districts.xml` | 700+ District landing pages | Weekly | No |
| `sitemap-qualifications.xml` | Qualification hubs | Weekly | No |
| `sitemap-departments.xml` | Department hubs | Weekly | No |
| `sitemap-cross-filter.xml` | High-value programmatic combinations | Weekly | No |
| `sitemap-blogs.xml` | Career guides and blog articles | Weekly | No |

### Google News Sitemap Syntax Example (`sitemap-news.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url>
    <loc>https://www.searchsarkarinaukri.com/news/upsc-2026-calendar-released</loc>
    <news:news>
      <news:publication>
        <news:name>SearchSarkariNaukri</news:name>
        <news:language>en</news:language>
      </news:publication>
      <news:publication_date>2026-07-23T10:00:00+05:30</news:publication_date>
      <news:title>UPSC Annual Exam Calendar 2026 Released — Check Dates</news:title>
    </news:news>
  </url>
</urlset>
```

---

## 7.3 Indexing & Directive Rules

- **Canonical Rule:** Every indexable page MUST serve a single, self-referencing canonical tag:
  `<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/ssc-cgl-2026" />`
- **Default Meta Robots Directive:**
  `<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />`
- **Redirect Management:** 301 permanent redirects enforced sitewide (zero 302 temporary redirects for permanent moves; zero redirect chains permitted).

---

## 7.4 Log File Analysis Protocol (5 Steps)

1. **Log Collection:** Export raw server access logs monthly for Googlebot (`Googlebot-Desktop`, `Googlebot-Mobile`, `Mediapartners-Google`).
2. **Bot Identification:** Verify reverse DNS lookup (`.googlebot.com` / `.google.com`) to filter out fake crawler user-agents.
3. **Crawl Frequency Analysis:** Identify which URL patterns receive > 80% of crawl volume.
4. **Status Code Audit:** Ensure > 98% of Googlebot requests return `HTTP 200` or `HTTP 304`.
5. **Crawl Waste Elimination:** Block bot requests to parameter search pages via robots.txt.

---

## 7.5 Indexability Checklist (10 Items)

- [ ] Page returns HTTP status code 200 OK.
- [ ] Has self-referencing canonical tag.
- [ ] Does NOT contain `noindex` meta tag (unless intentionally zero-job route).
- [ ] Listed in corresponding XML sitemap file.
- [ ] Internal click depth <= 3 clicks from homepage.
- [ ] Unique `<title>` tag (≤ 60 chars) and `<meta description>`.
- [ ] Passes Mobile-Friendly rendering test in URL Inspection tool.
- [ ] Page load speed passes LCP < 2.0s threshold.
- [ ] JavaScript renders full text content in initial HTML DOM.
- [ ] Included in internal link graph (no orphan pages).
