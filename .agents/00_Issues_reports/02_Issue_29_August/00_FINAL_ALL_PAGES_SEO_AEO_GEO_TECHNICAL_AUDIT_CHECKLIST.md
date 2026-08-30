# Final All-Pages SEO AEO GEO Technical Audit Checklist

Date: 2026-08-29
Site: `https://www.searchsarkarinaukri.com/`
Purpose: audit every important URL without changing unrelated pages or layout.

## Use This Before Any Fix

This file is the final cross-project audit checklist for Google Search Console and Bing Webmaster issues. It is for checking every URL before implementation. It must not be used as permission to bulk-edit unrelated templates, navbar, footer, header, global layout, global styles, analytics, or tracking.

## Absolute Guardrail

- Do not change navbar.
- Do not change footer.
- Do not change header.
- Do not change unrelated pages.
- Do not change global layout or global styles unless strictly required for the affected SEO issue.
- Do not delete useful pages only because they appear in an error report.
- Add `index, follow` to public pages that should rank, especially the homepage and valid public jobs pages. Do not add it blindly to backend/private/admin/thin/duplicate/error pages.
- Do not add noindex, redirected, duplicate, 404, 410, thin, or canonicalized-away URLs to sitemap.
- Do not create duplicate FAQ blocks across many pages.

## Audit Order For Every URL

1. URL and crawlability.
2. Indexability and robots.
3. HTTP status and redirects.
4. Canonical and duplicate variants.
5. Sitemap inclusion.
6. Internal links and crawl depth.
7. Title, meta description, H1, and headings.
8. Search intent satisfaction.
9. Content quality and information gain.
10. Structured data and entity consistency.
11. AEO/GEO/LLM answer-readiness.
12. Page speed and mobile rendering.
13. FAQ uniqueness and usefulness.
14. Final action decision.

## URL And Crawlability

- URL returns `200 OK` when indexable.
- No unexpected 3xx redirect.
- No accidental 4xx/5xx.
- URL is crawlable and not blocked by `robots.txt`.
- HTTPS is enforced.
- HTTP redirects to HTTPS.
- www/non-www is consistent.
- Trailing slash and lowercase rules are consistent.
- Query parameters are handled correctly.
- No unnecessary parameter URLs are indexed.
- No staging/dev URLs are discoverable.
- Important pages are internally linked and not orphaned.

## Indexability And Robots

- Important public ranking pages should be eligible for indexing: homepage, valid job pages, useful result pages, useful admit-card pages, useful district/location/category/department pages, and important static pages.
- Public pages that should rank should output `<meta name="robots" content="index, follow">` or an equivalent non-blocking robots directive.
- No accidental `noindex`.
- No accidental `nofollow`.
- No `X-Robots-Tag: noindex` on indexable pages.
- Canonical does not point elsewhere unnecessarily.
- Page has enough unique value to be indexed.
- Google/Bing can render important content.
- Sitemap contains indexable canonical URLs only.


## Pages That Should Use index, follow

Use `<meta name="robots" content="index, follow">` on pages that are public, useful, canonical, and intended to rank:

- Homepage.
- Valid published job detail pages.
- Useful expired job pages if the SEO policy keeps historical job pages indexable.
- Valid job category pages with substantial content.
- Valid district/location job pages with useful content.
- Valid department recruitment pages.
- Valid result pages with real result/source/status information.
- Valid admit-card pages with real exam/source/status information.
- Important static pages meant for search users.

## Pages That Should Not Use index, follow

Do not add `index, follow` to:

- Backend pages.
- Admin pages.
- Login/account/private pages.
- Staging/dev/test URLs.
- Search/filter parameter URLs unless converted into clean canonical landing pages.
- Duplicate numeric URLs when a better slug canonical exists.
- Thin placeholder pages.
- 404/410 pages.
- Redirecting URLs.
- Noindex archive pages intentionally excluded by SEO policy.
## Title, Meta, H1, And Heading Rules

- Title exists and is unique.
- Title is concise, relevant, and not stuffed.
- Title includes job/exam/recruitment/year/location/organization only when relevant.
- Meta description exists, is unique, and accurately summarizes the page.
- H1 exists, is visible, unique, and matches intent.
- H2-H6 sections are logical and describe real content.
- No repeated headings or template residue.

## Content Sections To Add By Page Type

Job pages: recruitment overview, important dates, vacancy details, eligibility, qualification, age limit, fee, salary, selection process, how to apply, documents, important links, official notification, related jobs, last updated, verification note, FAQs.

Admit-card pages: admit card status, exam date, release date, authority, official download/source, how to download, required login details, documents, exam-day instructions, download failure guidance, related admit cards/results/jobs, last updated, FAQs.

Result pages: result status, result date, authority, exam date, how to check, roll/registration requirements, merit list/cutoff note, next steps, official source, related pages, last updated, FAQs.

District/category/location pages: active job count, latest jobs, recent closed jobs, departments hiring, qualification/category links, nearby locations, application guidance, eligibility guidance, last updated, FAQs.

Department pages: department overview, latest jobs, closed recruitments, common posts, eligibility patterns, selection process patterns, official source, related departments/categories, last updated, FAQs.

## FAQ Rules

- Add 10-15 FAQs only where the page is indexable and useful.
- FAQs must be specific to the actual page/entity/location/job/exam/result/admit card.
- Do not repeat the same FAQ set across all pages.
- Do not fabricate salary, dates, eligibility, result status, or official links.
- If data is missing, use a verification note and tell users to check the official source.

## AEO GEO LLM Readiness

- Put the direct answer near the top.
- Use factual tables for dates/status/authority/location.
- Identify official source clearly.
- Use consistent entity names.
- Keep location, department, category, and year clear where relevant.
- Ensure structured data matches visible content.
- Avoid filler written only for word count.

## Technical And Speed Checks

- Run Lighthouse/PageSpeed on representative templates.
- Check LCP, CLS, INP, image sizes, caching, render-blocking scripts, and server response time.
- Ensure important SEO content is in crawlable/rendered HTML.
- Ensure schema JSON-LD is present and valid.
- Avoid layout shifts from images/cards/ads.

## Final URL Decision

Each URL must receive one decision: `INDEX`, `IMPROVE_FIRST`, `REDIRECT`, `CANONICALIZE`, `NOINDEX`, `404`, `410`, or `MANUAL_REVIEW`.

## Developer Scope Guardrail

Do not change unrelated pages, footer, navbar, header, menu, global layout, global styles, analytics, tracking, or shared site-wide components unless the change is strictly required to fix a specific SEO/indexing issue. Keep changes limited to the affected URL type, routing, status handling, canonical logic, metadata, structured data, sitemap/robots/indexability, internal links, page content quality, redirects, performance, and QA.

---

## Source Checklist Notes From User Attachment

Complete SEO Audit Checklist for Every URL
1. URL & Crawlability

For every page check:

 URL returns 200 OK
 No unexpected 3xx redirect
 No 4xx/5xx
 URL is crawlable
 Not blocked by robots.txt
 Correct canonical URL
 Canonical is self-referencing where appropriate
 No conflicting canonical signals
 URL appears in XML sitemap where appropriate
 Sitemap URL matches canonical URL
 No duplicate URL variants
 HTTPS enforced
 HTTP redirects to HTTPS
 www / non-www consistency
 Trailing-slash consistency
 Lowercase URL consistency
 Query parameters handled correctly
 No unnecessary URL parameters indexed
 No accidental staging/dev URLs
 No orphan page
 Important page is discoverable through internal links
 Crawl depth is reasonable
2. Google Indexability

Check separately from crawlability.

 Page is eligible for indexing
 No noindex
 No accidental nofollow
 No X-Robots-Tag: noindex
 Canonical does not point somewhere else unnecessarily
 Page is not considered duplicate
 Page has enough unique value
 Google can render the page
 Important content exists in rendered HTML
 Page is not effectively empty before JavaScript execution
 Internal links point to the indexable URL
 Sitemap contains indexable canonical URLs only
 Google Search Console indexing status checked
 "Crawled - currently not indexed" investigated
 "Discovered - currently not indexed" investigated
 Duplicate without user-selected canonical investigated
 Alternate page with proper canonical investigated
Critical distinction

Do not treat:

"URL is crawlable"

as equivalent to:

"Google will index and rank this URL."

Both must be audited independently.

3. Page Title

Audit the <title> specifically for search intent.

Check:

 Title exists
 One unique title per URL
 Primary search intent represented
 Main keyword/topic represented naturally
 Job/exam/recruitment name included where relevant
 Important year included when genuinely relevant
 Location included when relevant
 Organization/department included when relevant
 Title accurately represents page content
 No keyword stuffing
 No unnecessary repeated words
 No boilerplate dominating the title
 Strong differentiator
 Compelling SERP wording
 No duplicate titles across similar pages

Don't blindly optimize toward a character count. Pixel width and intent clarity matter more than arbitrary character limits.

4. Meta Description

Check:

 Exists
 Unique
 Accurately describes page
 Contains primary topic naturally
 Communicates page benefit
 Includes relevant details
 Strong click-through proposition
 No keyword stuffing
 No generic boilerplate
 No duplicate descriptions
 No misleading claims
 Suitable for SERP truncation

Meta descriptions are primarily a CTR/presentation signal, not a direct ranking factor.

5. H1

Every important page should have a strong primary heading.

Check:

 H1 exists
 H1 is visible to users
 H1 accurately describes page
 H1 matches search intent
 H1 is unique
 H1 contains the primary topic naturally
 H1 is not generic
 H1 isn't just "Latest Updates"
 H1 isn't stuffed with keywords
 H1 isn't hidden
 H1 isn't generated incorrectly by JavaScript
 H1 matches title/content intent

Example:

Weak:

Central Govt Jobs

Better:

Central Vigilance Commission Recruitment 2026 – Apply Online, Vacancy, Eligibility & Last Date

6. H2–H6 Content Architecture

Audit the entire heading hierarchy.

Check:

 H2 sections logically cover the topic
 H3 sections support H2 sections
 No random heading jumps
 Headings are descriptive
 Headings represent actual content
 Headings contain relevant subtopics naturally
 No keyword stuffing
 No repetitive headings
 Important search questions are represented
 Heading hierarchy reflects information architecture

For a recruitment page, potential sections might include:

Recruitment Overview
Important Dates
Vacancy Details
Eligibility Criteria
Educational Qualification
Age Limit
Application Fee
Selection Process
Salary / Pay Scale
How to Apply
Required Documents
Important Links
Frequently Asked Questions
Official Notification
7. Search Intent

This is one of the most important audits.

Determine:

Primary intent

Is the user looking for:

Information?
Latest notification?
Eligibility?
Application?
Admit card?
Result?
Answer key?
Syllabus?
Exam date?
Cut-off?
Previous papers?
Direct application link?

Then check:

 Page satisfies primary intent immediately
 Main answer appears above the fold
 No unnecessary introduction before the answer
 Page doesn't target a different intent
 Content format matches SERP expectations
 User doesn't need to hunt for critical information
8. Content Quality

For every URL check:

 Content is genuinely useful
 Content is original
 Content is factually accurate
 Content is current
 Content has sufficient depth
 Content answers obvious follow-up questions
 Content isn't thin
 No unnecessary filler
 No AI-generated repetitive sections
 No copied text
 No spun content
 No template residue
 No contradictory information
 Dates are correct
 Vacancy numbers are correct
 Eligibility information is correct
 Application fee is correct
 Links are correct
 Official source is clearly identified

Do not use word count as the definition of quality.

A 900-word page can be better than a 3,000-word page if it satisfies the query more completely.

9. Information Gain

This is especially important for competitive queries.

Ask:

What does this page provide that competing pages don't?

Check whether the page adds:

Original explanation
Official-source verification
Important dates
Vacancy breakdown
Eligibility interpretation
Step-by-step application guidance
Document checklist
Useful tables
Important links
FAQs based on actual user questions
Status updates
Clear explanations
Historical context when useful
Relevant related resources

Avoid simply expanding pages with generic paragraphs.

10. Keyword / Topic Coverage

Don't only check one keyword.

Build a topic/entity map.

For example:

Central Vigilance Commission Recruitment

Possible related entities:

CVC
Central Vigilance Commission
Government of India
recruitment
vacancy
notification
application form
eligibility
qualification
age limit
salary
selection process
important dates
official website
PDF notification

Check:

 Main topic covered
 Important related entities covered
 Relevant synonyms covered
 User terminology covered
 Long-tail questions covered
 No unnatural keyword repetition
 No semantic gaps
11. Content Freshness

For time-sensitive pages:

 Published date
 Updated date
 Update date is genuine
 Old information removed/updated
 Deadlines updated
 Status updated
 Links updated
 Recruitment status updated
 Old year references checked
 Expired information clearly labelled

Never change the updated date simply to make an old page appear fresh.

12. E-E-A-T / Trust Signals

For important informational pages check:

 Publisher identity
 About information
 Contact information
 Editorial transparency
 Source attribution
 Official source links
 Author information where appropriate
 Review/update information
 Clear corrections process where appropriate
 No misleading claims
 No fake expertise
 No fabricated sources

For government-job content, official notification/source verification is particularly important.

13. External Links

Check:

 Official notification link
 Official application link
 Official department website
 Relevant authoritative sources
 Links actually work
 HTTPS
 No malicious/spam destinations
 No unnecessary external links
 Anchor text describes destination
 Important links are visually obvious
14. Internal Linking

This is a major ranking lever.

Check:

 Page receives internal links
 Important pages receive more contextual links
 Links come from relevant pages
 Anchor text is descriptive
 No excessive exact-match anchors
 Related jobs linked
 Related admit cards linked
 Related results linked
 Related syllabus pages linked
 Category pages linked
 Breadcrumbs link correctly
 No orphan URLs
 No broken internal links
 No links to redirected URLs
 No links to non-canonical URLs

Create a topic cluster, not isolated pages.

15. Breadcrumbs

Check:

 Breadcrumb exists where appropriate
 Logical hierarchy
 Links work
 Breadcrumb URL matches canonical URL
 BreadcrumbList schema implemented correctly
 Breadcrumb reflects actual site architecture

Example:

Home → Government Jobs → Central Government Jobs → CVC Recruitment 2026

16. Structured Data

Audit JSON-LD/schema.

Check:

 Valid JSON-LD
 Schema matches page type
 No misleading structured data
 Required properties present
 Recommended properties where useful
 No duplicate conflicting schema
 BreadcrumbList
 Organization/WebSite where appropriate
 Article/NewsArticle where genuinely applicable
 FAQPage only when eligible and genuinely represented
 JobPosting only for actual individual job postings meeting Google's requirements
 Schema data matches visible page content

Do not add every possible schema type just because it exists.

17. Canonicalization

Check:

Self-canonical where appropriate
Canonical absolute URL
HTTPS canonical
Correct hostname
Correct path
No canonical chain
No canonical to unrelated page
No canonical to category homepage
Canonical page is indexable
Canonical agrees with sitemap
Canonical agrees with internal links
18. Robots.txt

Site-level audit:

 Important pages not blocked
 CSS/JS resources not unnecessarily blocked
 Admin/private areas blocked where appropriate
 Search-result URLs handled
 Parameter URLs handled
 Sitemap declaration correct
 No accidental wildcard rule
 No environment/staging paths exposed
19. XML Sitemap

Check:

 Only canonical URLs
 Only indexable URLs
 Only 200 URLs
 No redirects
 No 404s
 No noindex
 Correct lastmod
 Sitemap segmented if large
 Sitemap index works
 Submitted to GSC
 Important pages included
20. JavaScript / Rendering

Especially important for Next.js.

Check:

 Server-rendered content
 Important text available in rendered HTML
 Metadata available
 H1 available
 Internal links available
 Canonical available
 Structured data available
 Content doesn't depend unnecessarily on client-side JS
 No hydration errors
 No broken dynamic routes
 No content disappearing after hydration
 Googlebot can render page correctly
21. Next.js Technical SEO

For your type of site, specifically audit:

generateMetadata
metadata inheritance
canonical generation
robots.ts
sitemap.ts
dynamic route generation
generateStaticParams
server/client component boundaries
SSR/SSG/ISR strategy
metadata for dynamic pages
Open Graph
Twitter metadata
structured data
redirects
middleware
route handlers
trailing slash configuration
image optimization
next/image
font loading
caching
revalidation
hydration errors
404 handling
410 handling where appropriate
22. Core Web Vitals

Measure real and lab performance.

LCP
 Main content loads quickly
 Hero image optimized
 Fonts optimized
 Server response fast
INP
 Buttons respond quickly
 JavaScript isn't blocking interactions
 Heavy client-side components minimized
CLS
 Images have dimensions
 Ads don't shift layout
 Fonts don't cause major shifts
 Dynamic content reserves space

Also check:

TTFB
FCP
total JS
unused JS
unused CSS
image payload
font payload
third-party scripts
23. Mobile SEO

Test actual mobile rendering.

 Responsive
 No horizontal scrolling
 Text readable
 Buttons usable
 Tables usable
 Forms usable
 Navigation usable
 Important information visible
 No intrusive interstitials
 No mobile/desktop content mismatch
24. Images

Every meaningful image:

 Relevant image
 Correct dimensions
 Compressed
 WebP/AVIF where appropriate
 Descriptive filename
 Useful alt text
 No keyword stuffing in alt
 Lazy loading where appropriate
 Above-fold images prioritized
 No unnecessarily huge images
25. Links & HTTP Status

Crawl every page's links.

Identify:

200
301
302
307
308
404
410
500
redirect chains
redirect loops

Fix:

Page → 301 → 301 → 200

to:

Page → 200

or directly to the final URL.

26. Duplicate Content

Check:

 Exact duplicates
 Near duplicates
 Template-heavy duplicates
 Same content across multiple URLs
 Query parameters
 Pagination
 Category/tag duplicates
 Old-year vs new-year pages
 Mobile duplicates
 Printer pages
 Search pages

Then determine whether each should be:

consolidated
canonicalized
redirected
noindex
retained
27. Thin Content

Identify pages with:

Very little unique content
Generic introductions
Mostly tables copied from elsewhere
No meaningful explanation
No unique value
Automatically generated text
Duplicate content
Empty sections
Broken templates

Then decide whether to:

Improve / merge / redirect / noindex / remove.

28. Orphan Pages

For every URL calculate:

inbound internal links
contextual inbound links
breadcrumb links
category links
homepage links

A page with zero meaningful internal links should be investigated.

29. Site Architecture

Check:

Homepage → Category → Subcategory → Detail Page

Make sure the architecture is:

logical
shallow enough
semantically grouped
internally linked
scalable
consistent

For SearchSarkariNaukri, potential clusters could include:

Government Jobs
Central Government Jobs
State Government Jobs
Admit Cards
Results
Answer Keys
Syllabus
Exams
Scholarships
Recruitment Notifications
30. SERP Competition

For each important URL, compare against ranking pages.

Audit:

Search intent
Title
H1
Content depth
Content freshness
Topic coverage
Internal links
External links
Page UX
Original information
Tables
FAQs
Entity coverage
Trust signals
Page speed
SERP features

Then ask:

Why should Google rank this page above the current result?

If the answer isn't obvious, the page needs improvement.

31. CTR Optimization

Use GSC data.

Look at:

impressions
clicks
CTR
average position

Find pages with:

High impressions + low CTR

These are prime title/meta opportunities.

High CTR + poor position

Content/authority/relevance may need improvement.

Good position + low CTR

SERP presentation may be the problem.

32. Search Console Validation

For important URLs inspect:

Indexing status
URL Inspection
Page indexing
Crawled page
Referring page
Last crawl
Google-selected canonical
User-declared canonical
Mobile usability
Core Web Vitals
Enhancements
Performance queries
Performance pages
33. Analytics / User Behaviour

Where data is available:

Organic landing sessions
Engagement
Conversion
Scroll depth
Exit rate
Internal search
CTA clicks
Application-link clicks
Download clicks

For a job portal, don't optimize only for pageviews.

Optimize for successful user completion.

34. Ad / UX Quality

If monetized:

 Ads don't dominate content
 Ads don't obscure primary information
 No aggressive interstitials
 No excessive popups
 Page remains usable
 Important links remain accessible
 CLS controlled
 Mobile experience remains good
35. Accessibility

SEO and accessibility overlap significantly.

Check:

 Semantic HTML
 Proper headings
 Image alt text
 Form labels
 Keyboard navigation
 Link names
 Button names
 Color contrast
 Focus states
 ARIA only where necessary
 Tables properly structured
36. Security

Check:

HTTPS
No mixed content
No malware
No hacked pages
Security headers
Safe third-party scripts
No exposed credentials
No indexable admin/private content
37. International / Language SEO

If multiple languages/regions exist:

 hreflang
 Correct language targeting
 Correct canonical
 No conflicting hreflang
 Language-specific URLs
 Translations genuinely localized
 No auto-translated low-quality pages
38. Pagination / Archives

Audit:

category pages
archive pages
pagination
date archives
tag pages
author pages
search pages

Determine whether each should be:

indexable
canonicalized
noindexed
consolidated
removed
39. Programmatic SEO Quality

This is critical for a site with hundreds of automatically generated pages.

For every template inspect:

 Unique title generation
 Unique H1
 Unique description
 Unique introduction
 Correct entity data
 Correct dates
 Correct links
 Correct schema
 Correct canonical
 Correct breadcrumbs
 Correct sitemap inclusion
 No empty fields
 No "undefined"
 No "null"
 No placeholder text
 No duplicate paragraphs
 No incorrect organization names
 No incorrect year
 No stale data

Template correctness must be audited before auditing hundreds of individual URLs.

40. Page-Type Specific Audit

Don't use exactly the same checklist for every URL.

Create separate rules for:

Recruitment page
vacancy
eligibility
age
fee
dates
selection
salary
application
notification
Admit Card
exam name
release date
exam date
download link
login instructions
documents
official website
Result
result date
result link
roll number
cutoff where appropriate
merit information
official source
Answer Key
release date
objection dates
answer key PDF
response sheet
objection process
Syllabus
subjects
exam pattern
marks
duration
sections
PDF
official source
41. Entity Consistency

Check the same entity across the site.

For example:

SSC

should not randomly appear as:

Staff Selection Commission
Staff Selection Comm.
SSC Commission
Staff Selection Board

unless context requires it.

Maintain consistent:

Organization
Exam
Department
Job title
State
Year
Recruitment
Qualification

This helps build a coherent topical/entity graph.

42. Semantic Internal Linking

Don't only link based on keywords.

Link related entities.

For example:

SSC CGL Recruitment

→ SSC CGL Admit Card
→ SSC CGL Result
→ SSC CGL Syllabus
→ SSC CGL Answer Key
→ SSC CGL Previous Year Papers

This creates a much stronger topic cluster.

43. Dead / Expired Recruitment Pages

Do not automatically delete old job pages.

Evaluate:

historical search demand
backlinks
impressions
traffic
uniqueness
ongoing usefulness
related current recruitment

Possible actions:

Keep

If useful and still receiving demand.

Update

If a new recruitment cycle exists.

Consolidate

If several pages overlap.

Redirect

If there is a highly relevant replacement.

Remove / 410

If genuinely obsolete and valueless.

44. Technical Log-Level Audit

For serious SEO auditing, inspect server/application logs where available.

Look for:

Googlebot crawl frequency
Googlebot status codes
repeated crawling
crawl traps
parameter crawling
redirect crawling
404 crawling
JS/CSS failures
slow responses
excessive crawl of low-value URLs

This is where you can identify problems that a normal crawler misses.

45. Final Page-Level Scoring

I recommend scoring every URL across these categories:

Category	Weight
Indexability	15
Search Intent	15
Content Quality	15
On-Page SEO	10
Internal Linking	10
Technical SEO	10
Structured Data	5
Performance	5
UX/Mobile	5
Trust/E-E-A-T	5
Images/Media	2.5
External Signals	2.5
Total	100

Then classify:

90–100: Excellent
80–89: Strong
70–79: Needs improvement
60–69: Significant issues
<60: High-priority SEO remediation

The Most Important Part for Your 846/896 URLs

For a large programmatic site, don't manually audit 896 pages independently first.

Use a 4-level audit system:

Level 1 — Site-wide technical audit

Find systemic problems:

robots → sitemap → canonicals → redirects → rendering → status codes → performance → architecture

Level 2 — Template audit

Audit each page type:

Recruitment → Admit Card → Result → Answer Key → Syllabus → etc.

Fix the template before generating/fixing hundreds of pages.

Level 3 — URL-by-URL audit

Then audit every URL for:

intent → title → H1 → H2-H6 → content → entities → freshness → links → schema → canonical → indexability → UX

Level 4 — Google/Search performance validation

Finally combine:

GSC + crawl data + analytics + rankings + backlinks + competitor SERPs

This produces an actual SEO remediation system, rather than just a checklist.

For your site specifically, I would also make every URL audit produce a structured record like:

URL
Page Type
HTTP Status
Indexability
Canonical
Robots
Sitemap
Title
Meta Description
H1
H2-H6
Primary Intent
Primary Topic
Secondary Topics
Entity Coverage
Content Quality
Freshness
Internal Links
Orphan Status
External Links
Schema
Breadcrumbs
Images
CWV
Mobile UX
Duplicate Risk
Thin Content Risk
SERP Competition
GSC Impressions
GSC Clicks
GSC CTR
Average Position
SEO Score
Priority
Recommended Fix
Developer Action
Content Action

That gives you something a developer/Codex agent can actually execute and validate, rather than simply saying "improve SEO."

