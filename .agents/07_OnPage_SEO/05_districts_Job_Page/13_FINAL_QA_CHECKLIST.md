# 13 — FINAL QA CHECKLIST

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

## Data Preservation Check

### Critical Check - DO NOT PROCEED IF FAILED

- [ ] Existing header unchanged
- [ ] Existing navbar unchanged
- [ ] Existing main navigation unchanged
- [ ] Existing footer unchanged
- [ ] No header/navbar/footer links added
- [ ] No header/navbar/footer links removed
- [ ] No header/navbar/footer labels renamed
- [ ] No header/navbar/footer menu order changed
- [ ] No header/navbar/footer layout redesigned
- [ ] No existing jobs deleted
- [ ] No existing job IDs changed
- [ ] No existing job URLs/slugs removed
- [ ] No existing indexed URLs removed
- [ ] No existing category URLs removed
- [ ] No existing district URLs removed
- [ ] No existing qualification URLs removed
- [ ] No existing exam URLs removed
- [ ] Existing FAQs preserved
- [ ] Existing internal links preserved or redirected
- [ ] Existing WhatsApp and Telegram channels preserved

**IF ANY OF THE ABOVE FAILED: STOP AND FIX BEFORE PROCEEDING**

---

## Technical SEO Check

### Main Districts Page
- [ ] SEO title: "Maharashtra Government Jobs by District | District Wise Sarkari Naukri"
- [ ] Meta description implemented
- [ ] Canonical: https://www.searchsarkarinaukri.com/districts
- [ ] `/districts` has a self-canonical and is not canonicalized to another URL
- [ ] Robots: index, follow
- [ ] HTTPS enabled
- [ ] HTTP status 200
- [ ] No duplicate canonicals
- [ ] No tracking parameters in canonical
- [ ] Open Graph metadata complete
- [ ] Twitter metadata complete
- [ ] H1 is exactly one
- [ ] H1: "Maharashtra Government Jobs by District – District Wise Sarkari Naukri"
- [ ] H2/H3 hierarchy is logical
- [ ] No H1 duplicates
- [ ] No skipped heading levels

### District Pages
- [ ] SEO title template correct
- [ ] Meta description template correct
- [ ] Canonical URL pattern correct
- [ ] Every district page self-canonicalizes to its own district URL
- [ ] No district page canonicalizes to `/districts`
- [ ] No duplicate URLs
- [ ] Consistent slug usage
- [ ] H1 template correct
- [ ] H1 is exactly one per page
- [ ] Breadcrumb implemented
- [ ] Schema markup implemented

---

## Content Check

### Main Districts Page
- [ ] Introduction section present (2000+ characters with provided content)
- [ ] Data freshness section present (36 districts, active jobs dynamic, 6 regions, last updated dynamic)
- [ ] Top districts section present (8 districts with descriptions and job counts)
- [ ] Search/filter section present (district search, region filter, qualification filter, category filter)
- [ ] All 36 districts listed with crawlable URLs
- [ ] Region-wise sections present (6 regions with 2000+ characters each, H3 headings)
- [ ] Government job categories section present (11 categories with H3 headings)
- [ ] Qualification-wise jobs section present (7 qualification levels with H3 headings)
- [ ] Department-wise recruitment section present (10 departments with H3 headings)
- [ ] Exam-wise opportunities section present (5 exam types with H3 headings)
- [ ] Latest Maharashtra jobs section present (dynamic job cards with real data)
- [ ] "How to Find Government Jobs in Your Maharashtra District" section present (10-step ordered list)
- [ ] "Eligibility for Maharashtra District Government Jobs" section present (9 categories)
- [ ] "Important Information Before Applying for a Government Job" section present (12 information points)
- [ ] "Verify Maharashtra Government Recruitment Information" section present (7 subsections)
- [ ] Internal resource links section present (12+ pages linked)
- [ ] One FAQ/direct-answer section present; duplicate Quick Answers and FAQ blocks are not both present
- [ ] Marathi content present (comprehensive with lang="mr" attribute)
- [ ] "Browse Maharashtra Districts A–Z" section present
- [ ] "Find Government Jobs Near You in Maharashtra" section present (10 major districts)
- [ ] "How SearchSarkariNaukri Organizes District Job Information" section present (9 subsections)
- [ ] FAQ section present with unique, non-repeated questions
- [ ] Generic department and exam content is concise and does not overwhelm district discovery intent
- [ ] Eligibility and age-limit claims are qualified and direct users to official notifications
- [ ] Last updated date reflects real dataset changes, not page-load time

### District Pages
- [ ] Unique introduction present (1000-1500 characters)
- [ ] Major organisations listed
- [ ] Current jobs from district present
- [ ] Qualification links present
- [ ] Category links present
- [ ] FAQ section present
- [ ] Related districts linked
- [ ] Nearby district links present with descriptive crawlable anchors
- [ ] Internal resource links present
- [ ] Content is unique per district
- [ ] No duplicate content across districts

---

## Schema Markup Check

### Main Districts Page
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] ItemList schema implemented
- [ ] FAQ schema implemented (if eligible)
- [ ] No JobPosting schema exists on `/districts`
- [ ] No schema errors
- [ ] No schema warnings
- [ ] Validated with Rich Results Test
- [ ] All URLs in schema are accurate
- [ ] All names in schema are accurate

### District Pages
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] Place schema implemented (optional)
- [ ] FAQ schema implemented (if eligible)
- [ ] No JobPosting schema exists on multi-job district listing pages
- [ ] No schema errors
- [ ] No schema warnings
- [ ] Validated with Rich Results Test
- [ ] District-specific URLs in schema
- [ ] District-specific names in schema

---

## Internal Linking Check

### Main Districts Page
- [ ] All 36 districts linked
- [ ] Top districts have descriptive anchors
- [ ] Qualification pages linked
- [ ] Category pages linked
- [ ] Resource pages linked
- [ ] No broken internal links
- [ ] No orphan pages created
- [ ] Anchor text is descriptive
- [ ] No "click here" links

### District Pages
- [ ] Link back to /districts
- [ ] Link to /jobs
- [ ] Related districts linked
- [ ] Qualification pages linked
- [ ] Category pages linked
- [ ] Resource pages linked
- [ ] No orphan district pages
- [ ] Geographic hierarchy links
- [ ] No broken internal links

---

## GEO/Local SEO Check

- [ ] Maharashtra entity mentioned
- [ ] All 36 districts mentioned
- [ ] Geographic entities mentioned naturally
- [ ] Place schema for Maharashtra (optional)
- [ ] Place schema for districts (optional)
- [ ] Geographic internal links
- [ ] Region relationships established
- [ ] No keyword stuffing with location names
- [ ] Natural geographic language used

---

## AEO Check

- [ ] FAQ section present
- [ ] Questions are clear and direct
- [ ] Answers are factual and concise
- [ ] Direct answers come first
- [ ] Self-contained where possible
- [ ] Natural language used
- [ ] FAQ schema implemented (if eligible)
- [ ] No duplicate questions
- [ ] Questions match user intent

---

## Accessibility Check

- [ ] Semantic HTML used
- [ ] ARIA labels added where needed
- [ ] Form controls have labels
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] Color contrast acceptable
- [ ] Alt text for images
- [ ] Screen reader friendly
- [ ] No clickable divs where links/buttons should be
- [ ] No horizontal overflow
- [ ] WAVE test passed
- [ ] axe DevTools test passed

---

## Performance Check

- [ ] PageSpeed Insights score > 90
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] INP < 200ms
- [ ] Images optimized (WebP/AVIF)
- [ ] Lazy loading implemented
- [ ] No render-blocking resources
- [ ] Minimal JavaScript
- [ ] No unnecessary animations
- [ ] Stable card dimensions
- [ ] WebPageTest performance good

---

## Mobile UX Check

- [ ] Responsive design works
- [ ] Mobile layout tested
- [ ] Touch targets thumb-friendly
- [ ] No horizontal scrolling
- [ ] Search/filter accessible on mobile
- [ ] CTA buttons easy to tap
- [ ] Text readable on mobile
- [ ] Images load properly
- [ ] No broken layout
- [ ] Mobile-friendly test passed

---

## Data Accuracy Check

- [ ] Job counts dynamic (not hardcoded)
- [ ] District counts accurate
- [ ] Last updated date dynamic
- [ ] Last updated date comes from the latest real job/district dataset update
- [ ] Sitemap lastmod follows real content/data changes only
- [ ] No fake freshness generated with current render time
- [ ] No "1 Jobs" (should be "1 Job")
- [ ] No negative job counts
- [ ] No fake vacancy numbers
- [ ] No fake organization names
- [ ] No fake deadlines
- [ ] No fake eligibility criteria
- [ ] All data from database/API

---

## Zero-Job District Check

- [ ] Empty states handled gracefully
- [ ] Helpful message displayed
- [ ] Alternative links provided
- [ ] CTA buttons functional
- [ ] Not appearing as error
- [ ] Page remains indexed
- [ ] Canonical URL correct
- [ ] Content is useful
- [ ] Not thin or duplicated

---

## Marathi Content Check

- [ ] Marathi H2 present
- [ ] Marathi introduction present
- [ ] Key information in Marathi
- [ ] District names in Marathi
- [ ] Accurate translations
- [ ] Marathi copy is natural, professionally rewritten, and not literal machine translation
- [ ] lang="mr" attribute added
- [ ] UTF-8 encoding ensured
- [ ] Font support for Devanagari
- [ ] Language switch functional (if applicable)
- [ ] hreflang tags correct (if separate URL)

---

## Final Acceptance Criteria

The implementation is accepted only when ALL of the following are met:

### Data Preservation (CRITICAL - MUST PASS)
- ✅ Existing header unchanged
- ✅ Existing navbar unchanged
- ✅ Existing main navigation unchanged
- ✅ Existing footer unchanged
- ✅ No header/navbar/footer links added
- ✅ No header/navbar/footer links removed
- ✅ No header/navbar/footer labels renamed
- ✅ No header/navbar/footer menu order changed
- ✅ No header/navbar/footer layout redesigned
- ✅ No existing jobs deleted
- ✅ No existing job IDs changed
- ✅ No existing job URLs/slugs removed
- ✅ No existing indexed URLs removed
- ✅ No existing category URLs removed
- ✅ No existing district URLs removed
- ✅ No existing qualification URLs removed
- ✅ No existing exam URLs removed
- ✅ Existing FAQs preserved
- ✅ Existing internal links preserved or redirected
- ✅ Existing WhatsApp and Telegram channels preserved

### Technical SEO
- ✅ SEO title: "Maharashtra Government Jobs by District | District Wise Sarkari Naukri"
- ✅ Meta description matches specification
- ✅ Canonical: https://www.searchsarkarinaukri.com/districts
- ✅ Robots: index, follow
- ✅ HTTPS enabled
- ✅ HTTP status 200
- ✅ No duplicate canonicals
- ✅ No tracking parameters in canonical
- ✅ Open Graph metadata complete
- ✅ Twitter metadata complete
- ✅ H1 is exactly one
- ✅ H1: "Maharashtra Government Jobs by District – District Wise Sarkari Naukri"
- ✅ H2/H3 hierarchy is logical
- ✅ No H1 duplicates
- ✅ No skipped heading levels
- ✅ Proper heading hierarchy (H1 → H2 → H3 → H4)

### Content (ALL 24 SECTIONS MUST BE PRESENT)
- ✅ Introduction section (2,000+ characters)
- ✅ Data freshness section (dynamic values)
- ✅ Top districts section (8 districts with descriptions)
- ✅ Search/filter section (accessible HTML)
- ✅ All 36 districts section (complete directory)
- ✅ Region-wise sections (6 regions with 2000+ characters each)
- ✅ Government job categories (11 categories with H3 headings)
- ✅ Qualification-wise jobs (7 qualification levels with H3 headings)
- ✅ Department-wise recruitment (10 departments with H3 headings)
- ✅ Exam-wise opportunities (5 exam types with H3 headings)
- ✅ Latest Maharashtra jobs (dynamic job cards)
- ✅ "How to Find Government Jobs" (10-step ordered list)
- ✅ "Eligibility for Maharashtra District Government Jobs" (9 categories)
- ✅ "Important Information Before Applying" (12 information points)
- ✅ "Verify Maharashtra Government Recruitment Information" (7 subsections)
- ✅ Internal resource links (12+ pages)
- ✅ One FAQ/direct-answer section with no duplicate question block
- ✅ Marathi content (comprehensive with lang="mr")
- ✅ "Browse Maharashtra Districts A–Z"
- ✅ "Find Government Jobs Near You" (10 major districts)
- ✅ "How SearchSarkariNaukri Organizes District Job Information" (9 subsections)
- ✅ FAQ section (12 questions with H3 headings)
- ✅ Content is genuinely useful (no filler)
- ✅ No keyword stuffing
- ✅ No duplicate content

### Schema Markup
- ✅ WebPage schema implemented with all required fields
- ✅ BreadcrumbList schema implemented
- ✅ ItemList schema implemented for 36 districts
- ✅ FAQPage schema implemented (if eligible)
- ✅ No schema errors
- ✅ No schema warnings
- ✅ Validated with Rich Results Test
- ✅ Validated with Schema Validator
- ✅ All URLs in schema are accurate
- ✅ All names in schema are accurate

### Internal Linking
- ✅ All 36 districts linked from main page
- ✅ Top districts have descriptive anchors (not "click here")
- ✅ Qualification pages linked (/government-jobs/10th-pass, etc.)
- ✅ Category pages linked (/government-jobs/police, etc.)
- ✅ Resource pages linked (/jobs, /job-updates, /exams, /admit-cards, /results, /news, /blogs, /current-affairs, /exam-calendar, /digital-library, /eligibility-checker, /age-calculator, /quiz, /career-guidance)
- ✅ No broken internal links
- ✅ No orphan pages created
- ✅ Anchor text is descriptive
- ✅ Crawlable links (not just onClick JavaScript)

### GEO/Local SEO
- ✅ Maharashtra entity mentioned naturally
- ✅ All 36 districts mentioned naturally
- ✅ Geographic entities mentioned naturally (not keyword stuffing)
- ✅ Region relationships established
- ✅ District names consistent everywhere (Chhatrapati Sambhajinagar, Ahilyanagar, Dharashiv)
- ✅ Geographic internal links present
- ✅ Natural geographic language used

### AEO
- ✅ One FAQ/direct-answer section present
- ✅ Questions are clear and direct
- ✅ Answers are factual and concise
- ✅ Direct answers come first
- ✅ Self-contained where possible
- ✅ Natural language used
- ✅ FAQ section present (12 questions with H3 headings)
- ✅ FAQ schema implemented (if eligible)
- ✅ No duplicate questions
- ✅ No duplicate FAQ block repeats the same intent
- ✅ Questions match user intent

### Accessibility
- ✅ Semantic HTML used throughout
- ✅ ARIA labels added where needed (but not when native HTML provides same functionality)
- ✅ Form controls have labels
- ✅ Keyboard navigation works
- ✅ Focus states visible
- ✅ Color contrast acceptable
- ✅ Alt text for images is descriptive
- ✅ Screen reader friendly
- ✅ No clickable divs where links/buttons should be
- ✅ No horizontal overflow
- ✅ WAVE test passed
- ✅ axe DevTools test passed

### Performance
- ✅ PageSpeed Insights score > 90
- ✅ LCP < 2.5s
- ✅ CLS < 0.1
- ✅ INP < 200ms
- ✅ Images optimized (WebP/AVIF)
- ✅ Lazy loading implemented
- ✅ No render-blocking resources
- ✅ Minimal JavaScript
- ✅ No unnecessary animations
- ✅ Stable card dimensions
- ✅ WebPageTest performance good

### Mobile UX
- ✅ Responsive design works
- ✅ Mobile layout tested
- ✅ Touch targets thumb-friendly (minimum 44x44px)
- ✅ No horizontal scrolling
- ✅ Search/filter accessible on mobile
- ✅ CTA buttons easy to tap
- ✅ Text readable on mobile
- ✅ Images load properly on mobile
- ✅ No broken layout
- ✅ Mobile-friendly test passed

### Data Accuracy
- ✅ Job counts dynamic (not hardcoded)
- ✅ District counts accurate
- ✅ Last updated date dynamic
- ✅ Last updated date reflects real data changes
- ✅ Sitemap lastmod reflects real data/content changes
- ✅ Proper pluralization (1 Job, 2 Jobs)
- ✅ No "1 Jobs" errors
- ✅ No negative job counts
- ✅ No fake vacancy numbers
- ✅ No fake organization names
- ✅ No fake deadlines
- ✅ No fake eligibility criteria
- ✅ All data from database/API
- ✅ Job status indicators present (Active, Closing Soon, Application Closed, Exam Scheduled, Admit Card Released, Result Announced, Recruitment Cancelled)

### District Pages
- ✅ 36 district pages exist with unique URLs
- ✅ Each district page has unique H1
- ✅ Each district page has unique introduction (1000-1500 characters)
- ✅ Each district page shows current jobs from that district
- ✅ Each district page lists major organisations
- ✅ Each district page has district-specific FAQ
- ✅ Each district page links back to /districts
- ✅ Each district page links to /jobs
- ✅ Each district page links to related districts
- ✅ Each district page includes nearby district links with crawlable descriptive anchors
- ✅ Each district page links to qualification pages
- ✅ Each district page links to category pages
- ✅ Each district page links to resource pages
- ✅ No orphan district pages
- ✅ Zero-job districts have helpful empty states
- ✅ Metadata correct for each district page
- ✅ Schema markup valid for each district page

### 21 September 2026 Search Console Remediation
- ✅ `/districts` is treated as indexed; ranking-quality work prioritized over repeated indexing requests
- ✅ Duplicate/repetitive content removed
- ✅ Marathi quality fixed
- ✅ Live vacancy counts and visible timestamps synchronized
- ✅ All 36 child district pages strengthened with unique content
- ✅ Nearby-district links added
- ✅ Zero-job district pages remain useful
- ✅ Unknown URLs return real HTTP 404 instead of SPA fallback 200
- ✅ Important SEO routes are SSR/prerendered where practical
- ✅ Core Web Vitals measured against LCP <= 2.5s, INP < 200ms, CLS < 0.1
- ✅ Official-source links and last-verification dates added on job detail pages where available
- ✅ Editorial policy/about/contact pages linked where available

### District Data Check
- ✅ All 36 districts spelled correctly
- ✅ District names consistent (Chhatrapati Sambhajinagar, Ahilyanagar, Dharashiv)
- ✅ Region assignments correct
- ✅ URL slugs consistent
- ✅ Job counts accurate
- ✅ Active status correct
- ✅ Internal links work
- ✅ Page availability verified
- ✅ Metadata correct
- ✅ Schema markup valid

---

## Sign-Off

**Developer:** ____________________  
**Date:** ____________________  
**QA Status:** [ ] Approved / [ ] Needs Revision  
**Notes:** ____________________

---

**Last Updated:** 21 September 2026  
**Status:** Implementation Ready + Quality Addendum Required
