# 00 — Live Seed Findings (Verified Right Now, 25 Aug 2026)

Pulled directly from `https://www.searchsarkarinaukri.com/` (homepage only — I do
not have unrestricted crawl access to every internal URL, so this is a seed
sample, not the full-site audit). The developer/crawler running the full audit
(`00-master-audit-prompt.md`) should re-verify every line below across **all**
page templates, not just the homepage.

## ✅ What's already correct on the homepage

| Item | Value | Verdict |
|---|---|---|
| `<title>` | "Sarkari Naukri 2026 — Latest Government Jobs in India \| SearchSarkariNaukri" | Good length (~65 chars), keyword-front-loaded, brand at end |
| Meta description | "Sarkari Naukri 2026: Search latest government jobs, MPSC, Police Bharti, SSC, Railway & Banking recruitment with apply online links. महाराष्ट्रातील नवीन सरकारी नोकऱ्या — रोज अपडेट." | Present, bilingual, ~180 chars — check truncation on SERP |
| Canonical | `https://www.searchsarkarinaukri.com/` | Present and self-referencing ✅ |
| Meta robots | `index, follow, max-snippet:-1, max-image-preview:large` | Correctly set to allow full indexing/snippets |
| Open Graph tags | og:title, og:description, og:image (1200x630), og:type, og:locale, og:site_name | Fully implemented ✅ |
| Twitter Card | summary_large_image with title/description/image | Present ✅ |
| hreflang / locale signal | `og:locale = mr_IN`, `og:locale:alternate = en_IN` | ⚠️ og:locale is NOT the same as `<link rel="alternate" hreflang="...">` — must verify true hreflang tags exist (see file 11) |
| Search console verification | Google, Bing (msvalidate.01), Yandex all present | Good — confirms property ownership set up |
| Theme color | `#003366` | Present (PWA/mobile chrome tinting) |
| Viewport | `width=device-width, initial-scale=1.0` | Mobile-responsive meta present ✅ |

## 🚩 Issues spotted already (must be formally verified + logged by developer)

1. **Duplicate/repeated result entries on homepage** — In the "Latest Government
   Exam Results" section, **"SBI CBO Result 2026" is listed 5 times identically**
   (same date, same source link), **"MPSC Rajyaseva Result 2026" 3 times**, and
   **"MPSC Result 2026" 2 times**. Similarly in "Latest Admit Cards", **"UPSC CSE
   Admit Card 2026" appears 5 times** identically.
   → Looks like a templating/loop bug (same record rendered multiple times, or a
   badly de-duplicated query). This is a **content-quality + trust signal** issue
   (looks spammy/broken to users and to Google's helpful-content systems) and
   should be root-caused in the CMS/backend query. Log in `09-content-eeat-audit.md`.
2. **og:locale is `mr_IN` (Marathi) as primary** while the visible homepage copy
   is majority **English** with some Marathi phrases mixed in. Verify this
   matches the actual primary language of `<html lang="...">` — mismatch confuses
   language-detection signals. Check in `11-international-hreflang-audit.md`.
3. **URL structure for jobs uses an ID suffix** e's, e.g.
   `/jobs/job--5015`, `/jobs/rites--5010` — some slugs are auto-generated/near-empty
   (e.g. `job--5015` isn't descriptive) vs. others are well-formed
   (`vishweshwar-sahakari-bank--5006`). Inconsistent slugging is a keyword-in-URL
   opportunity being missed on some listings. Flag every non-descriptive slug in
   `02-onpage-seo-audit.md`.
4. **Category/filter URLs use query strings**: `/jobs?category=mpsc`,
   `/jobs?category=police`, etc. Query-string category pages need to be checked for:
   (a) whether they're canonicalized to themselves or the parent `/jobs`, and
   (b) whether they're in the XML sitemap and indexable, or intentionally
   `noindex`ed as thin/duplicate filter pages. Check in `01-technical-seo-audit.md`
   and `03-sitemap-url-audit.md`.
5. **Two different qualification links point to the same URL**: "Graduate
   government jobs" and "Government jobs for female candidates" both link to
   `/graduate-government-jobs`. This is either a bug (wrong href) or duplicate
   content by design — verify and log.
6. **FAQ content exists on the homepage in plain HTML** (12 Q&As) but it is
   **not confirmed whether `FAQPage` schema (JSON-LD) is implemented** — this is
   a high-value, low-effort win for rich results and for AI/answer-engine
   citation (see files `04`, `07`, `08`).
7. **No visible `JobPosting` structured data confirmed** on the job listing
   items shown on the homepage — for a Sarkari-Naukri (government jobs) site
   this is one of the single highest-impact schema types (Google for Jobs
   eligibility). Must be verified per job detail page, not just homepage.
8. Site brand name is inconsistent across meta fields: `SearchSarkariNaukri`
   (og:site_name) vs "Search Sarkari Naukri" (visible H1/nav text) vs
   "SearchSarkariNaukri.com" in FAQ answers — minor, but brand-consistency
   affects entity recognition by Google/AI systems. Log in `08`.

## Not yet verified (requires full crawler / server access) — hand to developer

- Full sitemap.xml URL list & lastmod values (file `03`)
- robots.txt directives (file `01`)
- Per-page title/meta uniqueness across all ~5,000+ job pages (file `02`)
- Core Web Vitals / PageSpeed scores (file `06`)
- Image alt text coverage site-wide (file `05`)
- SSL/security headers, redirect chains, 404s, orphan pages (file `01`)
- Actual `<html lang>` and hreflang tag presence (file `11`)
- GA4 / GSC / conversion tracking implementation (file `13`)
