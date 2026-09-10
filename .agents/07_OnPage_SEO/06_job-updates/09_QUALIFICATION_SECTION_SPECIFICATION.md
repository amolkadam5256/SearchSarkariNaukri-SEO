# 09 — QUALIFICATION SECTION SPECIFICATION

**Section:** Qualification-based Job Discovery  
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

## Qualification Section Structure

### Section Heading
**H2:** Government Jobs by Qualification

### Purpose
Create internal-link blocks for each qualification category that:
- Explain what jobs are available for that qualification
- Link to qualification-based job pages
- Provide SEO relevance for qualification keywords
- Create internal-link equity

---

## Qualification Categories

### 1. 10th Pass Government Jobs
**H3:** 10th Pass Government Jobs

**Content:**
Find government job opportunities available for candidates who have completed Class 10. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.

**Link:** `/jobs?qualification=10th`

**CTA Anchor:** View 10th Pass Jobs

**SEO Keywords:** 10th pass government jobs, 10th pass sarkari naukri, 10th pass govt jobs

---

### 2. 12th Pass Government Jobs
**H3:** 12th Pass Government Jobs

**Content:**
Find government job opportunities available for candidates who have completed Class 12. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.

**Link:** `/jobs?qualification=12th`

**CTA Anchor:** View 12th Pass Jobs

**SEO Keywords:** 12th pass government jobs, 12th pass sarkari naukri, 12th pass govt jobs

---

### 3. Graduate Government Jobs
**H3:** Graduate Government Jobs

**Content:**
Find government job opportunities available for graduate candidates. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.

**Link:** `/jobs?qualification=graduate`

**CTA Anchor:** View Graduate Jobs

**SEO Keywords:** graduate government jobs, graduate sarkari naukri, graduate govt jobs

---

### 4. ITI Government Jobs
**H3:** ITI Government Jobs

**Content:**
Find government job opportunities available for ITI certificate holders. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.

**Link:** `/jobs?qualification=iti`

**CTA Anchor:** View ITI Jobs

**SEO Keywords:** ITI government jobs, ITI sarkari naukri, ITI govt jobs

---

### 5. Diploma Government Jobs
**H3:** Diploma Government Jobs

**Content:**
Find government job opportunities available for diploma holders. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.

**Link:** `/jobs?qualification=diploma`

**CTA Anchor:** View Diploma Jobs

**SEO Keywords:** diploma government jobs, diploma sarkari naukri, diploma govt jobs

---

### 6. Postgraduate Government Jobs
**H3:** Postgraduate Government Jobs

**Content:**
Find government job opportunities available for postgraduate candidates. Check current vacancies, eligibility, age requirements, application dates and official notifications before applying.

**Link:** `/jobs?qualification=postgraduate`

**CTA Anchor:** View Postgraduate Jobs

**SEO Keywords:** postgraduate government jobs, postgraduate sarkari naukri, postgraduate govt jobs

---

## Content Guidelines

### Consistent Structure
Each qualification block should follow the same structure:
1. H3 heading with qualification name
2. Brief description (1-2 sentences)
3. Descriptive CTA button
4. Link to qualification-based job page

### Content Similarity
The content is intentionally similar across qualifications because the process is the same. Avoid repetitive phrasing by varying sentence structure slightly.

### Link Verification
Verify all qualification-based job pages exist before implementation:
- `/jobs?qualification=10th`
- `/jobs?qualification=12th`
- `/jobs?qualification=graduate`
- `/jobs?qualification=iti`
- `/jobs?qualification=diploma`
- `/jobs?qualification=postgraduate`

If URLs are different, update accordingly.

---

## SEO Considerations

### Long-tail Keywords
Target long-tail qualification keywords:
- "government jobs by qualification"
- "10th pass government jobs"
- "12th pass government jobs"
- "graduate government jobs"
- "ITI government jobs"
- "diploma government jobs"

### Internal Link Equity
Each qualification block passes link equity to qualification-based job pages, helping those pages rank for qualification-specific keywords.

### Schema Markup
Consider adding ItemList schema for qualification categories if they link to actual job listings.

---

## Visual Design

### Grid Layout
Display qualification blocks in a grid format (2-3 columns) for better UX on desktop and mobile.

### Card Design
Each qualification block should be a card with:
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
**Qualification Categories:** 6  
**Link Type:** Internal (qualification-based job pages)
