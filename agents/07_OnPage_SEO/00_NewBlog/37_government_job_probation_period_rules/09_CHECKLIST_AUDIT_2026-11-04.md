# Probation Article — Full SEO Checklist Audit

**Audit date:** 4 November 2026  
**Target:** Existing live page: [What Happens During Probation in a Government Job? Can You Lose the Job?](https://www.searchsarkarinaukri.com/blogs/what-happens-during-probation-in-a-government-job-can-you-lose-the-job)  
**Decision:** Update this existing URL. Do not create `/blogs/government-job-probation-period-rules` or another probation URL. Preserve the existing route and published date to retain its history.

## Executive summary

The page is live and clearly about probation, but it is not ready to call fully audited or technically verified. The most important content problems are confirmed from the current rendered page: the FAQ repeats the body almost verbatim; procedural lists and subsequent section headings run together in the extracted content; the body has no visible citations to the primary government sources; and the main related-resource block sends readers to several unrelated exam tools and results pages. The article also omits useful detail on prescribed durations, training/exams, extension conditions, and confirmation procedure.

The browser-readable live page shows one H1, a four-minute reading time, a quick summary, a table of contents, an author label, and a published/updated date of 16 October 2026. It does not expose HTTP status, source HTML, current canonical, robots directives, JSON-LD, sitemap response, image file properties, PageSpeed data, or Search Console results. Those checks remain pending.

**Critical project-level finding:** the earlier local package proposed a new probation URL. That conflicts with this checklist and the already-published page. The package metadata and developer handoff have now been aligned to the existing URL; the live site has not been changed.

## Evidence and limits

- Opened the current live article and blog archive in the browser on 4 November 2026. The archive lists the existing probation page as published 16 October 2026.
- The current browser text shows the article's visible content, title, category, four-minute estimate, author label, FAQs, and related links. It does not provide an HTTP status or complete source markup.
- The repository contains a **25 August 2026** crawl snapshot. For this URL it recorded HTTP 200, one H1, self-canonical, `index, follow`, sitemap inclusion, `en-IN`, one image, 1,395 words, and 43 internal links. These are historical measurements, not a current technical pass.
- The same crawl counted 459 incoming links, but 453 were archive/search/category links; after excluding those, the page itself, and filters, there were no contextual article-to-article incoming links in that snapshot.
- Search Console, GA4, PageSpeed Insights, Lighthouse, and a direct HTTP client were not available for this audit. A local `curl` attempt could not resolve the public host, so it is not evidence of a website outage. No GSC or performance numbers have been invented.

## Findings requiring action

| Priority | Finding | Evidence / required work |
|---|---|---|
| P0 | Preserve the existing URL | Current live URL is already published. Do not create the former proposed `/government-job-probation-period-rules` route. Keep the existing canonical and publication date. |
| P1 | Add official evidence | Current article body shows no linked DoPT or Lok Sabha sources. Cite claims next to the relevant text and add a short official-source list. The revision package's source list contains the verified reference links. |
| P1 | Repair section and list structure | The live extraction runs several list items together and appends headings such as “Can You Lose a Government Job During Probation?” to preceding content. Separate these into real HTML lists and semantic headings, then regenerate/check TOC anchors. |
| P1 | Remove duplicate FAQ answers | Seven visible FAQ answers repeat the main sections substantially verbatim. Keep only distinct reader questions with concise answers that add something beyond the body. |
| P1 | Expand the search-intent coverage | Add clear, sourced sections for duration, assessment, prescribed training/exams, extension, confirmation, consequences, and differences by employer. The live page currently offers mainly a short overview. |
| P1 | Correct overbroad legal phrasing | The statement that probationers have “not the same level” of protection as permanent employees is broad and uncited. Explain only what the cited rules support and direct individual disputes to qualified advice. |
| P1 | Replace irrelevant links | The current “Continue your preparation” block includes current affairs, exam calendar, digital library, results, admit cards, and daily assessment. Replace/supplement with contextual verification, dismissal, application, career, and probation/career links. |
| P2 | Add contextual internal links | Current archive/template links do not equal in-body topic-cluster links. Add suitable links to the verification, dismissal, Income Tax Inspector, and application guides; add reciprocal links from those pages only where natural. |
| P2 | Verify metadata and schema in source | Historical metadata looked complete, but current `<head>`, canonical after hydration, robots, JSON-LD, and duplicates were not inspected. |
| P2 | Verify image implementation and performance | A featured image is visible, but file format, dimensions, compression, `srcset`, width/height, current alt text, LCP treatment, and mobile layout were not verified. |
| P2 | Complete GSC baseline and follow-up | Record the current URL Inspection state, selected canonical, prior 28/90-day queries and performance before a substantive update; repeat after deployment. GSC is unavailable in this audit. |

## Checklist results by section

Status meanings: **Pass** = directly verified; **Partial** = some evidence, but not all criteria; **Fail** = a visible issue; **Pending** = requires a tool, source markup, credentials, or deployment.

### 1. Current-page audit

| Checklist item | Status | Result |
|---|---|---|
| Topic relevance | Pass | The live page directly covers government-job probation. |
| Content depth | Fail | Live page says 4 min; 25 Aug crawl measured 1,395 words. The current checklist's 1,800–2,500 words is an editorial target, not a Google rule. Expand only to answer missing questions, not to hit a count. |
| Heading structure | Fail | Some list content and following section titles appear merged in extracted body text; TOC does not cover all visible section topics. Verify and correct source HTML. |
| FAQ repetition | Fail | FAQ answers repeat body paragraphs nearly verbatim. |
| Official evidence | Fail | No primary source links are visible in the article body. |
| Internal links | Fail | Generic related-resource navigation includes unrelated exam/result pages; no focused body links were found in the extraction. |
| Search intent | Partial | It answers what probation is and whether a job can be lost, but leaves duration, training, exams, extensions, and confirmation procedures underdeveloped. |
| Metadata | Partial | Aug 25 crawl recorded one title (59 chars) and one description (158 chars); inspect current rendered `<head>` and uniqueness before deciding. |
| Canonical | Pending | Historical crawl recorded one self-canonical; current raw source/hydrated head not available. |
| Indexing | Pending | Search Console URL Inspection and selected canonical unavailable. |
| Page speed | Pending | No lab or field performance data collected. |
| Structured data | Pending | JSON-LD and validation output unavailable. |

### 2. Keyword research and mapping

| Checklist item | Status | Result |
|---|---|---|
| One primary intent | Pass | Informational, post-selection probation rules is focused and matches the current page. |
| Primary term in SEO title | Partial | Historical crawl title begins “Government Job Probation Period”; verify current tag. |
| Primary term in H1 | Partial | Current H1 includes “probation” and “government job” but not the exact phrase “government job probation period.” The requested alternative H1 in the brief fixes this naturally. |
| Primary term in first 100 words | Pass | Probation and government-job selection are introduced immediately. |
| Secondary terms in relevant sections | Fail | Extension and detailed training/exam sections are missing; confirmation and termination coverage are brief. |
| Natural distribution / no stuffing | Pass | No obvious repeated exact-match phrase stuffing in the rendered text. |
| Meta description uses topic | Partial | Historical description includes probation, confirmation, performance and extension; current tag not verified. |
| Descriptive image alt | Partial | An image with article-title alt text is exposed in the current page extraction; check the actual alt value and improve it if it repeats only the headline. |
| Search-volume validation | Pending | GSC and keyword-tool query data unavailable. Terms in the checklist are hypotheses, not measured search demand. |
| Cannibalization / existing URL | Fail (corrected in local handoff) | The draft package previously created a second URL for the same intent. The package now targets this existing URL; do not publish a second URL. |

### 3. On-page SEO

| Checklist item | Status | Result |
|---|---|---|
| One intended, unique SEO title | Partial | Prior crawl saw one title, 59 chars; current title and sitewide uniqueness need HTML/archive comparison. |
| Title accurately matches article | Pass | Visible H1 and article content align with the probation topic. |
| Evergreen title without needless year | Pass | Visible H1 has no year. |
| Meta description unique and accurate | Partial | Historical crawl saw a 158-character description; current page-wide uniqueness is unverified. |
| Preserve existing URL and preferred HTTPS host | Pass | Existing public URL is HTTPS and has not been changed. Preserve it in the CMS. |
| Current HTTP 200 / no redirect chain | Pending | Browser rendering confirms the page is reachable, not the status/redirect chain. The Aug 25 crawl measured 200. |
| One H1 | Pass | Current rendered content presents one H1. Historical crawl also found one. |
| Logical H2/H3 structure | Fail | The extracted lists/headings run together; content uses H2 only and major subsections need semantic structure. |
| Empty or styling-only headings | Partial | No empty heading is visible; source DOM was not inspected. |
| TOC and anchor alignment | Partial | TOC exists and its listed links are clickable in the extracted page, but it omits topics that appear later and must be rechecked after editing. |
| Every table has heading | N/A | No comparison table currently appears in the live article. Add one under an explanatory heading if retained in the revision. |
| Author and published/updated date | Pass | Live page shows “Search Sarkari Naukri Team,” published and updated 16 Oct 2026. Preserve the original publication date; change updated date only after a substantive update. |

### 4. Content quality and factual accuracy

| Checklist item | Status | Result |
|---|---|---|
| Plain-language definition | Pass | Article defines probation in plain language. |
| No universal two-year claim | Pass | It says duration varies and rejects a universal two-year rule. |
| Central vs State distinction | Partial | It says rules differ, but does not explain scope with official evidence. Do not imply the DoPT circular governs Maharashtra or other employers. |
| Distinguish government departments, PSUs, autonomous bodies, contracts | Partial | Some organization types are named, but the practical differences are not explained. |
| Appointment, probation, confirmation distinguished | Partial | Main point is present, but confirmation process and terminology need sourced detail. |
| Training/exams only where prescribed | Partial | Mentioned generally; no detailed treatment or sources. |
| Extension conditions with cited rules | Fail | Not explained in the live article. |
| Termination explained without universal legal claims | Fail | The current discussion is brief and contains broad uncited protection language. Rework conservatively. |
| Appointment order and applicable rules emphasized | Pass | The article tells readers to check these. |
| Document dates/issuing authorities | Fail | No official documents are cited in the live article. |
| Unsupported statistics/examples | Pass | No major statistics are visible; retain the no-fabrication rule. |
| Correction/contact route | Fail | No article-level correction route is visible. Add a real Contact or editorial-policy route if approved and verified. |
| Practical example, quick answer, comparison | Partial | Quick summary exists; no procedural example or probation-vs-confirmation table. |
| Word-count target | Partial | The checklist's 1,800–2,500 is editorial only; historical crawl measured 1,395. Improve completeness, not length for its own sake. |

### 5. Internal and external links

| Checklist item | Status | Result |
|---|---|---|
| Verification-guide link | Fail | No contextual body link visible. Relevant live page exists: `/blogs/government-job-verification-process-explained-what-happens-after-you-get-selected`. |
| Dismissal-guide link | Partial | A related “Can a Government Employee Be Fired?” article appears in related links, but add a contextual link in the termination section. |
| Income Tax Inspector career article | Fail | Relevant live page exists at `/blogs/from-probation-to-promotion-the-career-growth-of-an-income-tax-inspector`; not visible as a contextual link. |
| Government application guide | Fail | No contextual body link visible. Current article: `/blogs/how-to-apply-government-jobs-india`. |
| Jobs and career destinations | Partial | `/jobs` appears in the generic resource block; `/career-guidance` is a relevant live page. Replace unrelated recommendations with a concise relevant set. |
| All blogs/archive | Pass | The page links to the blog archive. Keep only as secondary navigation. |
| Inbound contextual links | Fail | Aug 25 crawl showed 459 incoming links, predominantly archive/search/category links; no contextual article-to-article incoming link after excluding those page types. Add reciprocal contextual links where useful. |
| Crawlable links / anchor text | Partial | TOC and navigation links are exposed in rendered content; raw anchor markup and all destinations were not tested. |
| Official source links | Fail | No DoPT/Lok Sabha source link visible in body. |
| External link health | Pending | No article citations to test; technical HTTP link testing unavailable. |
| GA4 internal-click events | Pending | Analytics access/configuration unavailable. |

### 6. Images and page experience

| Checklist item | Status | Result |
|---|---|---|
| Featured image exists | Pass | One image is exposed in current page extraction. |
| Descriptive alt/file name | Partial | Alt is surfaced as article-title text; actual attribute and filename need inspection. |
| WebP, compression, responsive sizes, dimensions | Pending | Image source code/properties unavailable. |
| Process infographic / comparison visual | Fail | No supporting explanatory visual appears in the live article. Useful but not a publication blocker if article text explains the process. |
| Mobile tables and layout | Pending | No mobile viewport test performed. |
| Typography/spacing, TOC, ads/pop-ups, sharing | Pending | Browser extraction cannot verify visual layout or interaction. |
| Unrelated related-article cards | Fail | Current related-card block includes CAG/Election Commission and other broad topics; replace with probation, employment security, and post-selection career resources. |
| Page-experience/Core Web Vitals | Pending | No PSI, Lighthouse, or field data available. Targets in the checklist are thresholds, not measured results. |

### 7. Technical SEO and structured data

| Checklist item | Status | Result |
|---|---|---|
| HTTP 200, HTTPS, host preference, redirect chain | Partial | HTTPS page opens in browser; actual response and redirect chain not inspected. Aug 25 snapshot: 200. |
| Self canonical | Partial | Aug 25 snapshot: one self-canonical. Current initial and hydrated `<head>` pending. |
| Robots/indexability / robots.txt / X-Robots-Tag | Partial | Aug 25 snapshot: `index, follow`, no X-Robots-Tag, indexable. Current headers/directives and robots.txt not inspected. |
| Sitemap inclusion | Partial | Aug 25 snapshot says included once. Current sitemap endpoint could not be fetched in this environment. |
| Semantic `<article>`, `<main>`, language, initial HTML | Pending | Source HTML not available. Historical crawl recorded `en-IN` and prerendered page. |
| Main content and crawlable links in HTML | Partial | Browser-readable content is available, but raw/prerender HTML and JS hydration parity were not tested. |
| Current title, description, canonical in source | Pending | Must inspect initial HTML and post-hydration DOM in browser/devtools. |
| Schema types/validity/duplicates | Pending | No JSON-LD dump or validator report. Preserve existing valid BlogPosting/Article and BreadcrumbList where appropriate; don't add duplicates. |
| FAQPage schema | Pending | Schema unseen. Do not add FAQPage for a Google FAQ rich result: Google removed the FAQ rich-result documentation in June 2026 and announced the result no longer appears starting May 7, 2026. Visible FAQs may remain for readers. |
| Publication / modified dates in schema | Pending | Current page shows both dates as 2026-10-16. Verify schema; keep actual publication date and update modified date only after substantive publication. |
| Image/schema/OG alignment | Pending | Current OG/image metadata not inspected. |
| Mobile crawl/render and pagination | Pending | Not tested. |

### 8. Indexing, analytics, off-page and follow-up

| Checklist item | Status | Result |
|---|---|---|
| Search Console current status, last crawl, selected canonical | Pending | No GSC connection in the available tools. |
| Prior 28/90-day impressions, clicks, queries, CTR, position | Pending | No GSC export supplied or accessible. Record before editing. |
| Manual actions/security issues | Pending | GSC access required. |
| Post-update live inspection and request indexing | Pending | No update has been published. Request once only after substantive deployment; it does not guarantee indexing. |
| 7/14/28-day monitoring | Pending | Start after deployment; no baseline/updated data currently available. |
| GA4 sessions, engagement, conversions, link-click events | Pending | GA4 access/configuration unavailable. |
| Off-page sharing/backlinks/authority | Pending | No campaign or backlink data supplied. Avoid spam tactics; do not claim outreach occurred. |
| Social sharing controls | Partial | WhatsApp and Telegram controls are visible; functionality was not clicked/tested. |

## Official references for the revision

- [DoPT Master Circular on Probation/Confirmation in Central Services, 11 March 2019](https://agwb.cag.gov.in/files/ersa/Master_Circular_on_probation_confirmation.pdf) — Central Services scope only.
- [Lok Sabha Unstarred Question 2870, 15 December 2021](https://sansad.in/getFile/loksabhaquestions/annex/177/AU2870.pdf?source=pqals) — describes Central Government confirmation considerations and extension conditions.
- [DoPT Mode of Recruitment and Appointment chapter](https://dopt.gov.in/sites/default/files/ch-03.pdf) — historical/model provisions; do not treat examples as universal/current rules for all employers.
- Google: [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article), [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals), [June 2026 documentation update on FAQ rich results](https://developers.google.com/search/updates), and [people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

## Readiness decision

**Content:** Not ready as currently live; P1 evidence, structure, FAQ, and link work remains.  
**Technical:** Not verified; do not mark pass based on the August crawl snapshot.  
**URL strategy:** Preserve and update the existing URL only. The local revision package now uses that target and is not a new blog.  
**Indexing/ranking:** Unknown. No current GSC evidence; neither indexing nor rankings are guaranteed.

