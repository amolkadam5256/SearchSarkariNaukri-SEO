# SEO / AEO / GEO Technical Audit Package
### Site: https://www.searchsarkarinaukri.com/
### Package generated: 25 Aug 2026

---

## ⚠️ IMPORTANT — READ FIRST

This package is a **REPORTING framework only**. Every file below is a checklist +
instruction prompt that tells whoever runs it (a developer, an SEO analyst, or an
AI agent with full site-crawl access — e.g. Screaming Frog, Sitebulb, Ahrefs Site
Audit, or a browser/crawler-enabled AI) exactly **what to check, how to check it,
and how to log the result.**

**Nothing in this package should be "fixed" automatically.** Every checklist item
ends in a report row (Pass / Fail / Warning + Evidence + Fix Recommendation). The
actual fixing is a separate, later phase done by the developer after this report
is reviewed and approved.

I (the AI that generated this package) do **not** have unrestricted crawling
access to your live server — I can only fetch pages already surfaced by my
search tool. So the two "seed" files (`00-...`) contain **real, verified data**
I was able to pull directly from your homepage right now. Everything else is
the **complete instruction set** the developer/crawler-agent must execute
against the full site (all pages, sitemap, robots.txt, server logs, etc.) to
produce the 100%-accurate, complete audit you asked for.

---

## 📁 Folder Structure

```
seo-audit-searchsarkarinaukri/
├── README.md                                   ← you are here
├── 00-live-seed-findings.md                    ← REAL data pulled from homepage right now
├── 00-master-audit-prompt.md                   ← ⭐ THE MAIN PROMPT — feed this to the crawler/dev/AI
├── 01-technical-seo-audit.md                   ← crawlability, indexation, robots, canonical, security
├── 02-onpage-seo-audit.md                      ← title/meta/H1/keywords/content per-page
├── 03-sitemap-url-audit.md                     ← sitemap vs live-site URL reconciliation
├── 04-structured-data-schema-audit.md          ← JSON-LD / schema.org audit
├── 05-image-alt-media-audit.md                 ← alt text, image SEO, lazy-load, CDN
├── 06-performance-core-web-vitals-audit.md     ← speed, CWV, mobile usability
├── 07-aeo-answer-engine-audit.md               ← Answer Engine Optimization (SGE/AI Overviews, voice)
├── 08-geo-generative-engine-audit.md           ← Generative Engine Optimization (ChatGPT/Perplexity/Gemini citations)
├── 09-content-eeat-audit.md                    ← E-E-A-T, duplicate content, thin content
├── 10-offpage-authority-audit.md               ← backlinks, brand mentions, citations
├── 11-international-hreflang-audit.md          ← mr_IN / en_IN locale + bilingual SEO
├── 12-accessibility-seo-audit.md               ← a11y items that double as SEO signals
├── 13-analytics-tracking-audit.md              ← GA4/GSC/Bing/Yandex verification & event tracking
├── 14-developer-final-report-template.md       ← the exact template the final deliverable must follow
└── outputs/                                    ← crawler/dev drops raw crawl exports + finished reports here
    ├── raw-crawl-data/
    ├── screenshots/
    └── final-reports/
```

## How to use this package

1. Open **`00-master-audit-prompt.md`** — copy its entire content and give it to
   whoever/whatever is going to actually crawl the live site (a developer using
   Screaming Frog + Google Search Console + PageSpeed Insights, OR an AI agent
   that has full web-crawling / browser tool access).
2. That prompt references files `01` through `13` — each is a detailed
   sub-checklist the executor must complete in full, one file per audit area.
3. Each checklist item must be filled into the **exact report table format**
   defined in `14-developer-final-report-template.md` — every row needs
   Status / Evidence(URL + screenshot or code snippet) / Priority / Fix
   Recommendation. No item may be skipped or marked "N/A" without a reason.
4. All raw crawl exports (CSV/JSON from the crawler, PageSpeed JSON, GSC
   exports) go in `outputs/raw-crawl-data/`.
5. The finished, numbered report files (`01-technical-seo-audit-REPORT.md`,
   etc.) go in `outputs/final-reports/` — one output file per input checklist
   file, same numbering, suffixed `-REPORT`.
6. This is an **audit only** — the developer does NOT fix anything found here
   in this pass. A separate remediation ticket/sprint is created from the
   report afterward.
