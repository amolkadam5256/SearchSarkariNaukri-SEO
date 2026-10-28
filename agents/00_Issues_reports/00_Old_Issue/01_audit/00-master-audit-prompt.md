# 00 — MASTER AUDIT PROMPT
## Give this entire file, as-is, to the developer / SEO analyst / crawler-enabled AI agent who will execute the full audit.

---

## ROLE

You are acting as a **Senior Technical SEO, AEO (Answer Engine Optimization) and
GEO (Generative Engine Optimization) Auditor** with 10+ years of experience
auditing large content publishers, news/jobs portals, and programmatic-SEO
sites. You have full crawling access to the target site, Google Search
Console, Bing Webmaster Tools, PageSpeed Insights / CrUX, and standard SEO
tooling (Screaming Frog, Sitebulb, Ahrefs/Semrush, or equivalent).

## OBJECTIVE

Produce a **100% verified, evidence-based, zero-guesswork technical + on-page +
off-page + AEO + GEO audit report** of the entire website
**https://www.searchsarkarinaukri.com/**.

This is a **REPORT-ONLY engagement**. You must **NOT fix, edit, deploy, or
change anything** on the live site or in the codebase during this audit. Every
finding must be logged with evidence and a recommended fix — remediation is a
separate, later phase.

## SCOPE — Audit the entire site, not just the homepage

- Crawl **every discoverable URL**: via XML sitemap(s), robots.txt, internal
  links, pagination, and (if available) server access logs.
- Cover **every page template** on the site, at minimum:
  1. Homepage (`/`)
  2. Job listing pages (`/jobs/{slug}--{id}`)
  3. Category/filter pages (`/jobs?category=...`)
  4. Qualification pages (`/10th-pass-government-jobs`, `/12th-pass-government-jobs`, `/iti-government-jobs`, `/diploma-government-jobs`, `/graduate-government-jobs`, etc.)
  5. District/location pages (`/districts`, `/districts/{district}`, `/jobs-in-{city}`)
  6. Department/recruiter pages (`/department/{dept}`)
  7. Results pages (`/results`, individual result pages if they exist)
  8. Admit card pages (`/admit-cards`, individual admit card pages)
  9. Any static pages: About, Contact, Privacy Policy, Terms, Disclaimer
  10. Search/404/error pages

## HOW TO EXECUTE THIS AUDIT — Step by step

1. **Discovery phase**
   - Fetch `robots.txt` and list every directive.
   - Fetch `sitemap.xml` (and any `sitemap_index.xml`, sub-sitemaps) — extract
     every `<loc>` URL, its `<lastmod>`, and total count per sitemap.
   - Run a full crawler (Screaming Frog / Sitebulb, unlimited depth) starting
     from the homepage to discover every URL actually linked/reachable on the
     site.
   - Pull the complete **indexed URL list from Google Search Console**
     (Coverage/Indexing report) and **Bing Webmaster Tools**.

2. **Reconciliation phase** (this is critical — the user explicitly wants this)
   - Build a 4-way comparison table: **Sitemap URLs vs Crawled/Linked URLs vs
     Google-Indexed URLs vs Bing-Indexed URLs.**
   - Flag every URL that is:
     - In the sitemap but NOT crawlable/linked anywhere on the site (orphaned
       sitemap entry)
     - Crawlable/linked but NOT in the sitemap (missing from sitemap — lost
       indexing opportunity)
     - In the sitemap but returns non-200 status (404/301/302/500/etc.)
     - In the sitemap but `noindex`ed or blocked by robots.txt (contradiction)
     - Indexed by Google but not in the sitemap, or vice versa
   - Output the **exact count**: total sitemap URLs, total live/crawlable URLs,
     total indexed URLs, total mismatched/problem URLs, with the full URL list
     for every mismatch category (not just a summary number).
   - Full detail goes in `03-sitemap-url-audit.md` — follow that file's exact
     table format.

3. **Per-page technical + on-page audit**
   - For **every unique page template** (not necessarily every single one of
     5,000+ job pages — sample at minimum 20 pages per template type, plus 100%
     of static/category/hub pages), check every item in files `01`, `02`, `04`,
     `05`, `09`, `11`, `12`.
   - For **title tags, meta descriptions, H1s, and canonical tags**, check
     ALL pages (this can be scripted/crawled at scale — do not sample) for:
     duplicates across pages, missing values, length violations, keyword
     stuffing, truncation risk.

4. **Performance + Core Web Vitals**
   - Run PageSpeed Insights (Lab + CrUX field data) for: homepage, 1 job
     listing page, 1 category page, 1 static page — mobile AND desktop.
   - Log results per file `06`.

5. **Structured data**
   - Validate every page template with Google's Rich Results Test / Schema
     Markup Validator. Log per file `04`.

6. **AEO (Answer Engine Optimization)** and **GEO (Generative Engine
   Optimization)** — treat these as DISTINCT disciplines, do not merge:
   - AEO = optimizing to be the direct answer in Google featured
     snippets / "People Also Ask" / voice assistants / SGE AI Overviews.
   - GEO = optimizing to be **cited as a source** inside generative AI chat
     answers (ChatGPT, Perplexity, Gemini, Copilot, Claude) when users ask
     job-search-related questions.
   - Execute both `07-aeo-answer-engine-audit.md` and
     `08-geo-generative-engine-audit.md` in full — they test different things.

7. **Off-page / authority, E-E-A-T, accessibility, analytics, international**
   — execute files `10`, `09`, `12`, `13`, `11` in full.

8. **Compile the final report**
   - For every checklist file `01`–`13`, produce a matching output file:
     `outputs/final-reports/{same-number}-{same-name}-REPORT.md`
   - Every report file MUST follow the exact table structure defined in
     `14-developer-final-report-template.md` — no exceptions, no free-form
     prose replacing the table.
   - Produce one master summary: `outputs/final-reports/00-EXECUTIVE-SUMMARY-REPORT.md`
     containing: total issues found by severity (Critical/High/Medium/Low),
     top 10 highest-impact fixes ranked by effort-vs-impact, and the sitemap
     reconciliation headline numbers.

## OUTPUT FILE NAMING CONVENTION (mandatory)

All report output files MUST use this exact format:
```
{two-digit-number}-{kebab-case-topic-name}-REPORT.md
```
Examples: `01-technical-seo-audit-REPORT.md`, `03-sitemap-url-audit-REPORT.md`,
`07-aeo-answer-engine-audit-REPORT.md`

One topic = one file. Do not combine multiple audit areas into a single file.
Do not split one audit area across multiple files.

## RULES

- ❌ Do NOT fix any issue you find. Report only.
- ❌ Do NOT skip a checklist item. If something is genuinely not applicable,
  write `N/A — reason: ...` — never leave a row blank.
- ❌ Do NOT estimate or guess numbers (page counts, load times, word counts).
  Every number must come from an actual tool run and be reproducible.
- ✅ Every finding needs: the exact URL(s) affected, a screenshot or raw
  code/data snippet as evidence, a severity rating, and a specific fix
  recommendation (not a vague "improve this").
- ✅ Cross-check findings — e.g. if `01` says a page is `noindex`, `03` must
  reflect that it should NOT be in the sitemap.
- ✅ Use the exact same URL formatting/casing throughout all files so results
  are diffable/searchable.
- ✅ Re-run this audit quarterly (or after major site changes) using this same
  prompt + file structure, and version each run in a dated subfolder, e.g.
  `outputs/final-reports/2026-08-25/`.

## FILES TO EXECUTE, IN ORDER

1. `01-technical-seo-audit.md`
2. `02-onpage-seo-audit.md`
3. `03-sitemap-url-audit.md`
4. `04-structured-data-schema-audit.md`
5. `05-image-alt-media-audit.md`
6. `06-performance-core-web-vitals-audit.md`
7. `07-aeo-answer-engine-audit.md`
8. `08-geo-generative-engine-audit.md`
9. `09-content-eeat-audit.md`
10. `10-offpage-authority-audit.md`
11. `11-international-hreflang-audit.md`
12. `12-accessibility-seo-audit.md`
13. `13-analytics-tracking-audit.md`
14. Compile `14-developer-final-report-template.md` format into
    `outputs/final-reports/00-EXECUTIVE-SUMMARY-REPORT.md`

Begin with Step 1 (Discovery phase) now.
