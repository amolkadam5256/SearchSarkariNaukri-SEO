# 02 — On-Page SEO Audit Checklist

Output file: `outputs/final-reports/02-onpage-seo-audit-REPORT.md`
Run this across **100% of pages** for title/meta/H1/canonical (script it via
crawler export), and a representative sample (min. 20 per template) for deeper
content checks.

## A. Title Tags
- [ ] Every page has exactly one `<title>` tag
- [ ] Length between 50–60 characters (report exact character count per page, flag >60 or <30)
- [ ] Primary keyword present near the front of the title
- [ ] No duplicate titles across different URLs — export full duplicate list
- [ ] Brand name placement consistent (front for homepage/hub pages, end for content pages — confirm site's chosen convention and check compliance)
- [ ] Job listing titles include: post name + organization + year (pattern check across sample of 50 job pages)
- [ ] No keyword stuffing / no ALL CAPS / no excessive punctuation

## B. Meta Descriptions
- [ ] Every page has a meta description
- [ ] Length 120–158 characters (flag truncation risk)
- [ ] Unique per page — export full duplicate list
- [ ] Includes a call-to-action relevant to context ("Apply Online", "Check Eligibility", "Download Admit Card")
- [ ] Bilingual (English + Marathi) descriptions reviewed for natural phrasing, not machine-translated artifacts

## C. Headings
- [ ] Exactly one `<h1>` per page
- [ ] H1 is unique per page and matches page intent/topic (not identical to title verbatim on every template — check for over-optimization)
- [ ] Logical heading hierarchy (H1 → H2 → H3, no skipped levels)
- [ ] No headings used purely for visual styling (should be semantic)

## D. Content Quality (per template — cross-ref file 09 for deeper E-E-A-T)
- [ ] Word count per template type (homepage, job listing, category, static) — report actual counts
- [ ] Thin-content pages flagged (<150–200 words with no other value-add like structured tables/schema)
- [ ] Keyword usage natural, not stuffed; primary + secondary keyword mapping documented per template
- [ ] Freshness signals: "last updated" date visible and accurate on time-sensitive content (results, admit cards, deadlines)
- [ ] Duplicate content check across job listings (template boilerplate ratio vs unique content ratio per page — flag if boilerplate dominates)

## E. Internal Linking
- [ ] Breadcrumb navigation present and consistent (Home > Jobs > Category > Listing)
- [ ] Anchor text of internal links reviewed for descriptiveness (not "click here")
- [ ] Related/similar job recommendations present on listing pages (internal linking depth)
- [ ] Category/hub pages (MPSC, Police, Railway, SSC, Banking, UPSC, ZP) link out to individual relevant listings and vice versa
- [ ] Max click depth from homepage to any indexable page (target: ≤4 clicks)

## F. URL & Slug (cross-ref file 01 section D)
- [ ] Slug includes primary keyword where feasible
- [ ] Flag every non-descriptive numeric-only or near-empty slug found in the crawl

## G. Keyword Research Alignment
- [ ] Confirm target keyword mapping exists per template type (e.g. "MPSC Rajyaseva Bharti 2026", "Police Bharti Maharashtra 2026", "Talathi Bharti online form")
- [ ] Search Console Performance report pulled: top 50 queries by impressions, current avg. position, CTR — flag high-impression/low-CTR queries (title/meta rewrite opportunity) and high-impression/page-2-3 position queries (content depth opportunity)
- [ ] Cannibalization check: multiple URLs ranking/targeting the same query (e.g. district page vs category page vs individual job page all targeting "Police Bharti 2026")

## H. Rich Snippet Eligibility (cross-ref file 04)
- [ ] Star ratings / FAQ / breadcrumb / job posting rich result eligibility checked per template in Rich Results Test
