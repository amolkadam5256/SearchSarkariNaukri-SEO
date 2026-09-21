# 15 — FINAL QA CHECKLIST

**Section:** Quality Assurance  
**Priority:** P0  
**Type:** Testing Checklist  
**Status:** Implementation Ready

---

## CONTENT EDITING RULES

**IMPORTANT:** When updating or creating any content based on this specification, follow these human editing guidelines:

### Primary Objective
Transform draft content into natural, original, reader-first writing while preserving factual meaning, important facts, numbers, dates, names, terminology, search intent, primary topic, important keywords, useful supporting information, intended audience, actual purpose of the page, and legitimate claims supported by source material.

### Key Requirements
1. **Remove generic AI-style openings** - Avoid predictable openings like "In today's digital world...", "In this comprehensive guide...", "Let's dive in...". Start with direct, useful information.
2. **Remove repetition** - Check for repeated ideas, keywords, conclusions, explanations, adjectives, sentence structures, headings, and calls to action.
3. **Vary sentence structure** - Mix short, medium, and long sentences. Avoid predictable grammatical patterns.
4. **Improve paragraph flow** - Use transitions only when genuinely helpful. Avoid excessive use of "Furthermore", "Moreover", "Additionally", etc.
5. **Remove formulaic "rule of three" writing** - Avoid unnecessary lists of three similar adjectives unless they provide genuinely different information.
6. **Remove filler** - Delete unnecessary phrases like "It is worth mentioning that", "It should be noted that", "Needless to say", etc.
7. **Use specific language** - Replace vague statements with precise information. Do not add unsupported facts.
8. **Preserve factual accuracy** - Never change dates, statistics, percentages, names, official terminology, URLs, product names, organization names, exam names, job titles, application requirements, eligibility conditions, fees, or deadlines.
9. **Make writing contextual** - Write according to the actual subject (informational, SEO, product, news, educational, job/exam content).
10. **SEO requirements** - Maintain important target keywords naturally. Never stuff keywords or sacrifice readability for SEO.
11. **Heading structure** - Keep logical hierarchy (H1, H2, H3). Use descriptive headings, not generic ones like "Introduction" or "Conclusion".
12. **Lists and tables** - Use bullet points when information is easier to scan as a list. Use tables for structured comparisons.
13. **Remove robotic phrases** - Rewrite templated or generic phrases naturally.
14. **Do not over-humanize** - Do not add random typos, grammar mistakes, excessive slang, fake personal stories, or fake opinions.
15. **Add human-like specificity** - Prefer concrete explanations over generic claims when supported by source material.
16. **Control tone** - Use professional, clear, direct, helpful, natural, confident tone without exaggeration.
17. **Readability** - Make content easy to scan with short paragraphs, clear headings, direct sentences, useful lists, concrete explanations, and logical ordering.
18. **Preserve author's intent** - Do not change the message simply because of personal style preference.
19. **Originality** - Perform genuine rewriting, not superficial synonym replacement. Understand the idea, identify purpose, reorganize wording, rewrite sentence structures, combine repetitive statements, improve clarity, add specificity only when supported, preserve important terminology, and produce genuinely original phrasing.
20. **Final quality check** - Verify content (meaning preserved, no important info removed, no unsupported claims, no changed facts), writing (natural, varied sentences, purposeful paragraphs, no repetition, appropriate formality, no templates), SEO (search intent satisfied, keywords natural, no stuffing, useful headings, crawlable structure), readability (quick understanding, broken long sentences, reasonable paragraph sizes, useful lists), and quality (precise wording, qualified claims, genuinely useful, valuable sections).

### Output Rule
Return ONLY the rewritten content unless explicitly asked for explanation or audit. Do not mention AI detection, humanization, or bypassing detectors. The objective is high-quality human-readable content, not detector manipulation.

---

## Data Preservation Checks

### [ ] No existing job records were deleted
- Verify all job records still exist in database
- Verify no data loss occurred

### [ ] No existing WhatsApp/Telegram functionality was broken
- Test WhatsApp join link
- Test Telegram join link
- Verify subscription still works

### [ ] No existing working URLs were changed
- Verify `/job-updates` URL still works
- Verify no redirects were added
- Verify no 404 errors

### [ ] No existing data was deleted
- Verify all job data still exists
- Verify all recruitment data still exists
- Verify no data corruption

### [ ] No existing functionality was broken
- Test all existing features
- Test navigation
- Test footer links
- Test header links

---

## Content Checks

### [ ] H1 is correct
- H1: "Daily Sarkari Naukri Updates & Free Government Job Alerts 2026"
- Only one H1 exists
- H1 is not duplicated
- H1 is clearly different from `/jobs`

### [ ] Introduction is search-focused
- Introduction explains job alerts and recruitment updates
- Introduction is not channel-focused only
- Natural keyword usage

### [ ] Latest Government Job Alerts section exists
- Section heading is present
- Introduction text is present
- Dynamic job table is present
- Real job data from database (not hardcoded)
- Active listings exclude expired/closed jobs
- Qualification snippets are short enough for a listing page

### [ ] Government Jobs Closing Soon section exists
- Section heading is present
- Dynamic closing-soon table is present
- Real job data from database (not hardcoded)
- Days remaining calculated dynamically
- Closing-soon content is prominent because it differentiates `/job-updates` from `/jobs`

### [ ] Daily update sections exist
- New Today section present where data exists
- New This Week section present where data exists
- Closing Today section present where data exists
- Closing This Week section present where data exists
- Recently Updated section present where data exists
- All sections use real dynamic data

### [ ] Freshness dashboard exists
- Active Government Jobs count present
- New Today count present
- Updated Today count present
- Closing Today count present
- Closing This Week count present
- Last updated shows date, time and IST where available
- All metrics come from real data

### [ ] New Government Jobs Today section exists
- Shows only jobs first published today
- Job titles link to detail pages
- Posts, qualification, location and last date are scannable
- Useful fallback appears if no jobs were added today

### [ ] Recently Updated / Corrigendum section exists
- Recently updated notifications shown from real update data
- Deadline extended/corrigendum/application reopened/revised vacancy changes are shown where available
- Each item links to relevant detail page
- No fake update examples are displayed

### [ ] Qualification section exists
- 6 qualification cards present
- Descriptions present
- CTA buttons present
- Links to qualification-based job pages

### [ ] Quick Job Finder exists
- Search input present with accessible label
- Qualification chips present as crawlable anchors
- Category chips present as crawlable anchors
- Location/state chips present as crawlable anchors

### [ ] Category section exists
- 9 category cards present
- Descriptions present
- CTA buttons present
- Links to category-specific pages
- CTA text matches destination type
- Exam-guide destinations are not labeled as `View jobs`

### [ ] State section exists
- 10 state links present
- Links to state-specific pages
- Maharashtra links to `/districts`

### [ ] Why Use section exists
- Section heading present
- Benefits listed
- Independent platform disclaimer present

### [ ] How Alerts Work section exists
- 4-step process present
- Clear instructions

### [ ] How to Check section exists
- Verification steps listed
- Practical guidance

### [ ] Verify Recruitment Information section exists
- Verification statement present
- Last updated date present
- Reviewed date present
- Editorial policy link present

### [ ] Internal Resource Links section exists
- 12 resource links present
- All links work

### [ ] Critical inbound links exist
- Homepage links directly to `/job-updates`
- Main navigation or secondary navigation links to `/job-updates` with `Job Alerts` label
- `/jobs` links to `/job-updates` with a crawlable anchor
- Relevant category pages link to `/job-updates`
- Relevant qualification pages link to `/job-updates`
- Homepage does not only send job-alert users directly to WhatsApp/Telegram

### [ ] FAQ section exists
- 8 FAQ items present
- Questions match visible content
- Answers match visible content

### [ ] Trust content is consistent
- Independent platform status mentioned
- Official source verification emphasized
- Editorial policy referenced
- Overlapping trust/verification sections are merged or de-duplicated
- Before You Apply checklist is concise

### [ ] Latest Alerts by Type exists
- New Jobs destination present
- Admit Cards destination present
- Results destination present
- Exam Dates destination present
- Recruitment News destination present
- All destinations already exist

---

## SEO Checks

### [ ] Title tag is correct
- Title: "Daily Sarkari Naukri Updates 2026 - Free Government Job Alerts"
- Title includes primary keyword
- Title is descriptive
- Title is clearly different from `/jobs`

### [ ] Meta description is correct
- Description: "Get daily Sarkari Naukri updates and free government job alerts for UPSC, SSC, Railway, Banking, MPSC, Police Bharti and more. Track new vacancies, closing dates, WhatsApp and Telegram alerts."
- Description includes secondary keywords
- Description is readable and not keyword-stuffed

### [ ] Canonical URL is correct
- Canonical: https://www.searchsarkarinaukri.com/job-updates
- Canonical is self-referencing
- Canonical is absolute URL
- Canonical is not `/job-updates/`
- Canonical is not `/jobs`
- Canonical is not `/`

### [ ] Breadcrumb is correct
- Breadcrumb: Home → Job Updates
- BreadcrumbList schema implemented
- Semantic markup improved

### [ ] Heading hierarchy is correct
- H1: 1 instance
- H2: Section headings
- H3: Subsection headings
- No skipped levels
- No duplicate H1s

### [ ] Keywords are natural
- Primary keyword (Sarkari Naukri) used naturally
- Secondary keywords used naturally
- No keyword stuffing
- No repetition

### [ ] Internal links are present
- 30-50 internal links total
- Descriptive anchor text
- All links work
- No broken links
- All important internal links render as real crawlable anchors

### [ ] URL structure is correct
- URL: /job-updates
- URL is lowercase
- URL is hyphen-separated
- No trailing slash (unless required)

---

## Schema Checks

### [ ] WebPage schema implemented
- WebPage schema present
- Required fields filled
- Dynamic fields (lastReviewed, dateModified) work

### [ ] BreadcrumbList schema implemented
- BreadcrumbList schema present
- Matches visible breadcrumb
- Validated with Rich Results Test

### [ ] Organization schema implemented
- Organization schema present
- Required fields filled
- SameAs links correct

### [ ] WebSite schema implemented
- WebSite schema present
- SearchAction implemented (if applicable)

### [ ] FAQPage schema implemented
- FAQPage schema present
- Questions match visible FAQ
- Answers match visible FAQ
- No hidden FAQ content
- Validated with Rich Results Test

### [ ] ItemList schema implemented
- ItemList schema present (if job listings)
- Links to actual job pages
- Validated with Rich Results Test

### [ ] No JobPosting schema on landing page
- JobPosting schema NOT used on this page
- JobPosting only on individual job pages
- Job detail pages keep `datePosted` and `validThrough` accurate

---

## AEO/GEO Checks

### [ ] Direct-answer content exists
- Platform overview fact block present
- FAQ first sentences are direct answers
- Answers are self-contained

### [ ] Question-based headings exist
- Some headings are question-based
- Headings match user intent

### [ ] GEO content exists
- India context in introduction
- State section with state links
- Maharashtra emphasis where relevant
- Link to /districts

---

## Accessibility Checks

### [ ] Semantic HTML used
- Semantic elements (nav, section, article, aside, footer)
- ARIA labels where needed
- Alt text for images

### [ ] Keyboard navigation works
- Tab navigation works
- Focus states visible
- No keyboard traps

### [ ] Color contrast is sufficient
- Text contrast meets WCAG AA
- Link contrast meets WCAG AA
- Button contrast meets WCAG AA

### [ ] Screen reader compatibility
- Screen reader can read content
- Alt text descriptive
- Form labels present

---

## Performance Checks

### [ ] PageSpeed score is acceptable
- PageSpeed Insights score > 90
- LCP < 2.5 seconds
- CLS < 0.1
- INP < 200 ms

### [ ] Images optimized
- Images in WebP/AVIF format
- Images lazy loaded
- Images sized correctly

### [ ] JavaScript minimized
- Non-critical JavaScript deferred
- No render-blocking JavaScript
- JavaScript minified

### [ ] CSS optimized
- Critical CSS inline
- Non-critical CSS deferred
- CSS minified

---

## Mobile Checks

### [ ] Responsive design works
- Mobile layout correct
- No horizontal scrolling
- Content readable

### [ ] Touch targets are sufficient
- Buttons are touch-friendly
- Links are touch-friendly
- Touch targets > 44px

### [ ] Font sizes are readable
- Font sizes readable on mobile
- No zooming required
- Text legible

---

## Freshness Checks

### [ ] Latest jobs update dynamically
- Latest jobs table updates daily
- Real data from database
- No hardcoded jobs

### [ ] Closing soon updates dynamically
- Closing soon table updates daily
- Real data from database
- Days remaining calculated dynamically

### [ ] Last updated date works
- Last updated date displays correctly
- Date updates when content changes
- Date comes from real page/job-alert dataset update time
- Date is not generated from current render time on every request

### [ ] Sitemap freshness is accurate
- `/job-updates` exists in XML sitemap
- Sitemap lastmod changes only after meaningful page/data updates

---

## Trust Checks

### [ ] Editorial policy link works
- Editorial policy page exists
- Link works
- Page loads correctly

### [ ] Independent platform status clear
- Independent status mentioned
- Not affiliated with government
- Clear disclaimer

### [ ] Official source verification emphasized
- Official source mentioned multiple times
- Verification instructions clear
- Always verify with official notification

---

## Final Acceptance

### [ ] All P0 items complete
- H1 updated
- Title/meta updated
- Breadcrumb improved
- Introduction rewritten
- First CTA added

### [ ] All P1 items complete
- Latest jobs section added
- Closing soon section added
- Qualification section added
- Category section added
- State section added
- Why Use section added
- How Alerts Work section added
- How to Check section added
- Verify section added
- Internal links added
- FAQ section added
- Schema implemented

### [ ] All P2 items complete
- CTA placement improved
- Author/reviewer added
- Last updated added
- Performance optimized
- Mobile optimized

### [ ] No regressions
- WhatsApp/Telegram still works
- All existing features work
- No broken links
- No 404 errors
- No performance regression

### [ ] Ready for deployment
- All tests passed
- All issues resolved
- Documentation updated
- Stakeholder approval

### [ ] 21 September 2026 Search Console remediation complete
- `/job-updates` treated as discovered/live-indexable, not Soft 404
- Repeated indexing requests stopped
- Homepage, navigation and `/jobs` inbound links added
- `/job-updates` differentiated from `/jobs`
- Exact self-canonical verified
- No JobPosting schema on `/job-updates`
- Active listing count verified against open jobs only
- Duplicate job entries reviewed by authority, notice number, post, deadline and official PDF
- Initial HTML/View Source checked for key SEO content where practical
- API failure fallback leaves useful SEO content visible
- Random nonexistent URLs return real HTTP 404
- Googlebot logs checked for recurring 429, 5xx, WAF or CAPTCHA issues
- Core Web Vitals measured: LCP <= 2.5s, INP < 200ms, CLS < 0.1

### [ ] 21 September 2026 section audit complete
- Freshness dashboard added
- New Government Jobs Today added
- Recently Updated / Corrigendum section added
- Quick Job Finder added near top
- Latest Alerts by Type added
- Listing-table qualification text shortened
- Category CTA labels corrected
- Repetitive trust sections merged
- Reviewer/reviewed date added only if truthful
- Official government links compacted or organized

---

**QA Status:** [ ] Passed / [ ] Failed  
**QA Date:** [Date]  
**QA By:** [Name]  
**Notes:** [Any issues or observations]
