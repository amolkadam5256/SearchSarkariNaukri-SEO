# 10 — CATEGORY SECTION SPECIFICATION

**Section:** Category-based Job Discovery  
**Priority:** P1  
**Type:** Content Specification  
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

## Category Section Structure

### Section Heading
**H2:** Government Jobs by Category

### Purpose
Transform category mentions into actual navigational entities that:
- Explain what jobs are available in each category
- Link to category-specific exam/job pages
- Provide SEO relevance for category keywords
- Create internal-link equity

---

## Category Definitions

### 1. Railway Government Jobs
**H3:** Railway Government Jobs

**Content:**
RRB/RRC recruitment, Railway vacancies, Group D, NTPC, ALP, Technician and other railway recruitment updates.

**Link:** `/exams/rrb-ntpc`

**CTA Anchor:** View Railway Jobs

**SEO Keywords:** railway government jobs, railway sarkari naukri, RRB recruitment, railway vacancies

---

### 2. Banking Government Jobs
**H3:** Banking Government Jobs

**Content:**
SBI, IBPS, RBI and other banking recruitment notifications.

**Link:** `/exams/sbi-po-clerk`

**CTA Anchor:** View Banking Jobs

**SEO Keywords:** banking government jobs, banking sarkari naukri, SBI recruitment, IBPS recruitment

---

### 3. Police Government Jobs
**H3:** Police Government Jobs

**Content:**
Police Bharti, constable, SI and other police recruitment updates.

**Link:** `/exams/maharashtra-police-bharti`

**CTA Anchor:** View Police Jobs

**SEO Keywords:** police government jobs, police sarkari naukri, police bharti, constable recruitment

---

### 4. SSC Government Jobs
**H3:** SSC Government Jobs

**Content:**
SSC CGL, CHSL, MTS and other Staff Selection Commission recruitment updates.

**Link:** `/exams/ssc-cgl`

**CTA Anchor:** View SSC Jobs

**SEO Keywords:** SSC government jobs, SSC sarkari naukri, SSC CGL, SSC CHSL

---

### 5. UPSC Government Jobs
**H3:** UPSC Government Jobs

**Content:**
Civil Services, IAS, IPS and other UPSC recruitment notifications.

**Link:** `/exams/upsc-civil-services`

**CTA Anchor:** View UPSC Jobs

**SEO Keywords:** UPSC government jobs, UPSC sarkari naukri, civil services, IAS, IPS

---

### 6. Defence Government Jobs
**H3:** Defence Government Jobs

**Content:**
Army, Navy, Air Force and other defence recruitment notifications.

**Link:** `/exams/indian-army`

**CTA Anchor:** View Defence Jobs

**SEO Keywords:** defence government jobs, defence sarkari naukri, army recruitment, navy recruitment, air force recruitment

---

### 7. Teaching Government Jobs
**H3:** Teaching Government Jobs

**Content:**
TET, CTET, UGC NET and other teaching recruitment notifications.

**Link:** `/exams/ctet`

**CTA Anchor:** View Teaching Jobs

**SEO Keywords:** teaching government jobs, teaching sarkari naukri, TET, CTET, UGC NET

---

### 8. Maharashtra Government Jobs
**H3:** Maharashtra Government Jobs

**Content:**
MPSC, Police Bharti, Talathi, ZP and other Maharashtra government recruitment.

**Link:** `/districts`

**CTA Anchor:** View Maharashtra Jobs

**SEO Keywords:** Maharashtra government jobs, Maharashtra sarkari naukri, MPSC, talathi recruitment, ZP recruitment

---

### 9. PSU Government Jobs
**H3:** PSU Government Jobs

**Content:**
Public Sector Undertaking recruitment notifications across various sectors.

**Link:** `/exams/psu`

**CTA Anchor:** View PSU Jobs

**SEO Keywords:** PSU government jobs, PSU sarkari naukri, public sector undertaking recruitment

---

## Content Guidelines

### Consistent Structure
Each category block should follow the same structure:
1. H3 heading with category name
2. Brief description (1-2 sentences)
3. Descriptive CTA button
4. Link to category-specific exam/job page

### Link Verification
Verify all category-specific pages exist before implementation:
- `/exams/rrb-ntpc`
- `/exams/sbi-po-clerk`
- `/exams/maharashtra-police-bharti`
- `/exams/ssc-cgl`
- `/exams/upsc-civil-services`
- `/exams/indian-army`
- `/exams/ctet`
- `/districts`
- `/exams/psu`

If URLs are different, update accordingly.

### Category Descriptions
Keep descriptions concise but informative. Mention key exams or organizations within each category.

---

## SEO Considerations

### Long-tail Keywords
Target long-tail category keywords:
- "railway government jobs"
- "banking government jobs"
- "police government jobs"
- "SSC government jobs"
- "UPSC government jobs"
- "defence government jobs"
- "teaching government jobs"
- "Maharashtra government jobs"
- "PSU government jobs"

### Internal Link Equity
Each category block passes link equity to category-specific pages, helping those pages rank for category-specific keywords.

### Maharashtra Emphasis
Maharashtra category links to `/districts` because the site already has strong Maharashtra district structure.

---

## Visual Design

### Grid Layout
Display category blocks in a grid format (3 columns) for better UX on desktop and mobile.

### Card Design
Each category block should be a card with:
- H3 heading
- Description text
- CTA button
- Hover effect for interactivity

### Mobile Optimization
- Stack cards vertically on mobile
- Ensure buttons are touch-friendly
- Maintain readability

---

**Implementation Priority:** P1  
**Category Count:** 9  
**Link Type:** Internal (category-specific exam/job pages)
