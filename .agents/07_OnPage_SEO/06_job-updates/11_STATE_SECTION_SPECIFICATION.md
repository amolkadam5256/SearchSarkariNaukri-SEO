# 11 — STATE SECTION SPECIFICATION

**Section:** State-based Job Discovery  
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

## State Section Structure

### Section Heading
**H2:** Government Jobs by State

### Purpose
Provide state-wise job discovery that:
- Links to state-specific job pages
- Provides geographic job navigation
- Supports local SEO for state-specific keywords
- Creates internal-link equity to state pages

---

## State List

### 1. Maharashtra
**Anchor Text:** Maharashtra
**Target URL:** `/districts`
**Reason:** Site has strong Maharashtra district structure

### 2. Uttar Pradesh
**Anchor Text:** Uttar Pradesh
**Target URL:** `/state/up`

### 3. Bihar
**Anchor Text:** Bihar
**Target URL:** `/state/bihar`

### 4. Rajasthan
**Anchor Text:** Rajasthan
**Target URL:** `/state/rajasthan`

### 5. Madhya Pradesh
**Anchor Text:** Madhya Pradesh
**Target URL:** `/state/mp`

### 6. Gujarat
**Anchor Text:** Gujarat
**Target URL:** `/state/gujarat`

### 7. Karnataka
**Anchor Text:** Karnataka
**Target URL:** `/state/karnataka`

### 8. Tamil Nadu
**Anchor Text:** Tamil Nadu
**Target URL:** `/state/tamilnadu`

### 9. Delhi
**Anchor Text:** Delhi
**Target URL:** `/state/delhi`

### 10. West Bengal
**Anchor Text:** West Bengal
**Target URL:** `/state/westbengal`

---

## Link Verification

### Pre-Implementation Checks
Verify all state pages exist before implementation:
- `/districts` (Maharashtra)
- `/state/up`
- `/state/bihar`
- `/state/rajasthan`
- `/state/mp`
- `/state/gujarat`
- `/state/karnataka`
- `/state/tamilnadu`
- `/state/delhi`
- `/state/westbengal`

If URLs are different, update accordingly.

### Handle Missing State Pages
If some state pages do not exist:
- Remove those states from the list
- Or create placeholder state pages
- Or link to a general state job search page

---

## Content Guidelines

### Display Format
Display states as clickable links in a grid format (2-5 columns depending on space).

### State Names
Use full state names, not abbreviations:
- "Maharashtra" (not "MH")
- "Uttar Pradesh" (not "UP")
- "Madhya Pradesh" (not "MP")

### Maharashtra Special Handling
Maharashtra links to `/districts` because the site already has comprehensive district-wise job structure for Maharashtra.

---

## SEO Considerations

### Long-tail Keywords
Target long-tail state keywords:
- "Maharashtra government jobs"
- "Uttar Pradesh government jobs"
- "Bihar government jobs"
- "Rajasthan government jobs"
- "Madhya Pradesh government jobs"
- "Gujarat government jobs"
- "Karnataka government jobs"
- "Tamil Nadu government jobs"
- "Delhi government jobs"
- "West Bengal government jobs"

### Internal Link Equity
Each state link passes link equity to state-specific pages, helping those pages rank for state-specific keywords.

### Maharashtra Emphasis
Maharashtra is listed first because the site has strong Maharashtra content. This is strategic, not accidental.

---

## Visual Design

### Grid Layout
Display state links in a grid format (2-5 columns) for better UX on desktop and mobile.

### Link Design
Each state link should be:
- Clearly clickable
- Descriptive anchor text
- Hover effect for interactivity
- Sufficient touch target size on mobile

### Mobile Optimization
- Stack links vertically on mobile
- Ensure links are touch-friendly
- Maintain readability

---

## Expansion Strategy

### Future State Addition
If implementing more states in the future:
- Add to this list
- Create corresponding state pages
- Add to grid layout
- Update internal linking strategy

### State Page Requirements
Each state page should include:
- State-specific government jobs
- State recruitment boards
- State public service commissions
- State-specific qualification requirements
- District-wise breakdown (if applicable)

---

**Implementation Priority:** P1  
**State Count:** 10  
**Link Type:** Internal (state-specific job pages)
