# 11 — Master Implementation Sequence & Checklist

> Read `01_ground_rules_do_not_delete.md` before starting anything below. Every phase is additive: new sections, new pages, new schema, new links, new sitemap entries. Nothing existing is deleted, restructured, or visually redesigned.

## Phase 1 — Technical foundation (file 02)
- [ ] SSR/prerender `/jobs` so job content is in raw HTML
- [ ] Add `/jobs`-specific title, meta description, canonical, OG tags
- [ ] Add crawlable pagination links
- [ ] Add `noindex,follow` to non-SEO filter URL variants only
- [ ] Add breadcrumb HTML
- [ ] Re-measure Core Web Vitals

## Phase 2 — Individual job page upgrade (file 04, 06)
- [ ] Add Quick Information table, status badges, original overview text, FAQ, Related Jobs/Exam to job template
- [ ] Add `JobPosting` JSON-LD with real, unique data per job
- [ ] Implement expired-job flow (schema removed, page kept live, "Closed" badge)

## Phase 3 — `/jobs` page new sections (file 03, 05)
- [ ] Add intro paragraph, By Qualification, By Category, By Location, Recruitment Organizations, How-To, FAQ sections below existing job grid
- [ ] Add WebSite, Organization, BreadcrumbList, CollectionPage/ItemList, FAQPage JSON-LD (no JobPosting on this page)

## Phase 4 — New landing pages (file 07)
- [ ] Build Priority 1 pages: 12th/10th/ITI/Diploma/Graduate qualification pages, Maharashtra, Pune, Nagpur, Nashik, Mumbai
- [ ] Build Priority 2 pages: Police Bharti, Talathi, MPSC, Railway, Closing Soon
- [ ] Build remaining category/recruiter pages

## Phase 5 — Internal linking & sitemap (file 08)
- [ ] Add homepage links to new hub pages
- [ ] Add topic-cluster cross-links (MPSC/SSC/Railway/etc.)
- [ ] Add Related Jobs/Exam links on job pages
- [ ] Extend sitemap index with new child sitemaps; keep existing sitemap entries intact

## Phase 6 — Indexing cleanup for existing "Crawled – not indexed" URLs (file 09)
- [ ] Export and classify affected URLs (A/B/C/D)
- [ ] Apply Phase 2/4 content upgrades to Group A/B pages
- [ ] Audit canonical/robots/noindex per URL
- [ ] Clean sitemap submissions (remove non-indexable URLs from sitemap only, not the pages)
- [ ] Request indexing selectively, only after fixes, starting with Group A

## Phase 7 — GEO/AEO layer (file 10)
- [ ] Add `/llms.txt`
- [ ] Rewrite FAQ/intro copy in answer-first format
- [ ] Add/link "How We Verify Jobs" page
- [ ] Ensure disclaimer, freshness fields, and structured tables are consistent site-wide

## Validation, every phase
- [ ] Google Rich Results Test on a sample of changed pages
- [ ] URL Inspection → Test Live URL to confirm rendered HTML includes new content
- [ ] Confirm no existing file, route, section, or UI element was removed or altered beyond the two approved edits in file 01 (title/H1 on `/jobs`)
- [ ] Diff review: changes should read as additions, not replacements

## Reference: priority/impact matrix (from the original audit)

| Issue | Priority | Impact |
|---|---|---|
| Server-render job content | Critical | Very High |
| Individual JobPosting schema | Critical | Very High |
| Job expiration handling | Critical | Very High |
| Canonical architecture | Critical | High |
| Crawlable pagination | Critical | High |
| Qualification/location/category landing pages | High | Very High |
| Internal linking | High | Very High |
| Better job titles/descriptions | High | High |
| Freshness signals | High | High |
| Breadcrumbs, FAQ, OG tags | Medium | Medium |
| Image SEO, social metadata | Low | Low |

Work top-down through Phases 1–7 in order where possible; each phase's SEO value compounds on the previous one (a well-tagged, well-linked page written for GEO still needs the SSR/canonical foundation from Phase 1 to actually get crawled and indexed).
