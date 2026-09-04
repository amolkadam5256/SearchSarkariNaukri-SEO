# SearchSarkariNaukri â€” Admit Card SEO Expansion & Indexability Implementation Prompt

## Objective
Upgrade every `/admit-cards/{id}` detail page so it is genuinely useful, search-intent aligned, internally linked, crawlable, and materially different from other admit-card pages.

The site currently has 896 URLs reported in Google Search Console under **Discovered â€“ currently not indexed**. The live category page says admit cards are pulled hourly from official `.gov.in` / `.nic.in` sources, while the supplied page contains only a small amount of detail on each individual admit-card record. Do NOT solve this by adding generic filler to all pages.

## Critical rule
Generate content from the actual database record for each admit card. Never invent exam dates, release dates, application numbers, official links, eligibility, documents, exam pattern, city-intimation dates, download procedures, or authority details.

If a field is unavailable, omit the section or write a short, accurate statement such as:
"Details are not available in the current record. Check the official notification/source for the latest information."

Do not create 896 pages with the same paragraph and swapped keywords. Each page must be substantively useful for its specific exam.

## Required page architecture

1. Breadcrumb
   Home > Admit Cards > {Exam Name}

2. H1
   `{Exam Name} Admit Card {Year}`

3. Above-the-fold status card
   - Status: Expected / Out / Released / Not Released / Updated
   - Exam date
   - Admit-card release date, if known
   - Last updated
   - Conducting authority
   - Official source domain
   - Primary CTA: Download / Check Official Admit Card
   - Secondary CTA: Official notification

4. Short answer / summary
   80â€“140 words explaining what candidates need to know now.

5. Admit Card Status
   Explain the current status using only record-backed facts.

6. Important Dates
   Use a compact table. Only include dates that exist in the record/source.

7. How to Download {Exam Name} Admit Card
   5â€“8 numbered steps. Keep the steps generic unless the official source provides a specific process.

8. Direct Official Link
   Make the authority's official source the primary download/check destination.

9. Details Printed on the Admit Card
   Explain common fields only when appropriate:
   candidate name, roll/application number, exam date, reporting time, centre, instructions, photograph/signature, etc.
   Do not claim a field is present unless supported; phrase common fields as "may include".

10. Documents / Items to Carry
   Use only verified requirements. Otherwise clearly label them as "commonly required; verify the official notice".

11. Exam Day Instructions
   General guidance, clearly separated from authority-specific instructions.

12. What to Do If You Cannot Download the Admit Card
   Troubleshooting:
   - verify credentials
   - try official portal again
   - clear cache/use another browser
   - check notice/helpdesk
   - contact official authority if the issue persists

13. Exam Centre / City Intimation
   Include only when relevant or supported.

14. Related Exam Information
   Link to the corresponding exam page, result page, syllabus/exam pattern page, jobs/recruitment page, and exam calendar where relevant.

15. Related Admit Cards
   4â€“8 genuinely related pages, preferably same authority, same exam family, or similar recruitment.

16. Last Updated / Verification Notice
   State when the page was last checked and that the official authority remains the final source.

17. FAQ â€” 10 to 15 questions
   FAQs must be specific to the exam and current record. Use a mix of:
   - release status
   - download location
   - exam date
   - credentials
   - documents
   - correction/troubleshooting
   - exam centre/city slip where relevant
   - what to do if the link is inactive
   - official-source verification
   - next update / result relationship

18. Editorial / source note
   Short statement that SearchSarkariNaukri is an independent information portal and candidates should verify official notices.

## SEO requirements

- One clear H1 only.
- Unique title tag and meta description per record.
- Avoid keyword stuffing.
- Include the exact exam name naturally plus useful variants such as "hall ticket" only where relevant.
- Use descriptive internal links.
- Canonical URL must point to the preferred `/admit-cards/{id}` URL.
- Do not canonicalize all pages to `/admit-cards`.
- Ensure the page returns HTTP 200.
- Ensure no accidental `noindex`.
- Ensure important page content is server-rendered/available to crawlers.
- Include the detail URLs in the XML sitemap when they are indexable.
- Do not include expired/duplicate/thin URLs in the sitemap simply to increase URL count.
- Use valid `BreadcrumbList` structured data.
- Use `FAQPage` structured data only when the visible page contains the same FAQs and the markup is valid; do not use it as a spam tactic.
- Use appropriate `WebPage`/`Article`-type metadata only if it accurately represents the page.
- Do not fabricate `datePublished`, `dateModified`, ratings, reviews, authorship, or organization claims.
- Every important admit-card page must have at least one strong internal link from an indexable hub.
- Avoid pagination/orphaning that prevents discovery.

## Indexability strategy for the 896 URLs

Before adding content, classify every URL:

A. Active + useful + unique -> indexable.
B. Historical but still useful/searchable -> indexable if content is substantial and accurate.
C. Duplicate record -> consolidate/canonical/redirect according to the actual duplicate relationship.
D. Thin or placeholder record with no reliable information -> improve from source data or keep out of index until useful.
E. Invalid/dead record -> 404/410 as appropriate.
F. Wrong/duplicate year or title -> correct the underlying record and URL strategy.

Do NOT blindly force all 896 URLs into Google's index.

## Technical acceptance checklist

For every indexable `/admit-cards/{id}`:
- 200 response
- self-referencing canonical
- index,follow
- unique title
- unique meta description
- unique H1
- meaningful body content
- official source link
- internal links
- breadcrumb
- valid structured data
- sitemap inclusion
- no accidental robots block
- no duplicate canonical
- no empty/placeholder headings
- no broken links
- mobile-friendly rendering
- fast server response
- content visible without requiring client-side interaction

## Deliverable
Implement the architecture in the actual application. Then generate a validation report containing:
- total admit-card records
- indexable
- noindex
- duplicates
- missing source
- missing exam date
- missing last-updated
- missing canonical
- missing title/meta/H1
- missing internal links
- HTTP status failures
- sitemap coverage
- structured-data validation failures

Do not mark the job complete merely because the UI looks better. The goal is useful pages + clean technical indexability + crawlable architecture.
## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, site-wide layout, global styling, tracking setup, analytics setup, or shared components unless strictly required for admit-card indexing/content architecture. Do not mass-publish thin duplicate content just to make discovered URLs indexable.
