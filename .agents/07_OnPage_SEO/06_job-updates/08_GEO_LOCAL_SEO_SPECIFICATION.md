# 08 — GEO LOCAL SEO SPECIFICATION

**Section:** Geographic Entity Optimization  
**Priority:** P1  
**Type:** Strategic Documentation  
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

## Geographic Entity Architecture

### Primary Geographic Entity
**India** - National scope for Sarkari Naukri and government jobs

### Secondary Geographic Entities
**States** - State-wise job discovery
- Maharashtra
- Uttar Pradesh
- Bihar
- Rajasthan
- Madhya Pradesh
- Gujarat
- Karnataka
- Tamil Nadu
- Delhi
- West Bengal

### Tertiary Geographic Entities
**Districts** - District-wise job discovery (link to /districts page)

---

## Maharashtra GEO Strategy

### Maharashtra Emphasis
This is particularly important because the site already has strong Maharashtra-oriented content.

### Natural Keyword Combinations
Use natural combinations instead of generic terms:
- Maharashtra government jobs
- Maharashtra Sarkari Naukri
- Maharashtra government job alerts
- MPSC jobs
- Maharashtra Police Bharti
- Talathi recruitment
- ZP recruitment
- Maharashtra state government vacancies

### Current Navigation Integration
The current navigation already exposes Pune, Mumbai, Nagpur and other districts. Build this into a proper state/district architecture rather than repeating city names in the copy.

### Maharashtra Section Content
#### Heading: Maharashtra Government Jobs
**Content:**
MPSC, Police Bharti, Talathi, ZP and other Maharashtra government recruitment.

**Link:** `/districts`

**Purpose:** Direct Maharashtra job seekers to district-wise job discovery

---

## State Section Implementation

### State Link Structure
Each state should link to its respective state page:
- Maharashtra → `/districts` (already has strong district structure)
- Uttar Pradesh → `/state/up`
- Bihar → `/state/bihar`
- Rajasthan → `/state/rajasthan`
- Madhya Pradesh → `/state/mp`
- Gujarat → `/state/gujarat`
- Karnataka → `/state/karnataka`
- Tamil Nadu → `/state/tamilnadu`
- Delhi → `/state/delhi`
- West Bengal → `/state/westbengal`

### State Section Heading
**H2:** Government Jobs by State

### State Section Content
Display states as clickable links in a grid format.

---

## Local SEO Content Requirements

### Introduction Content
Include India-specific context in introduction:
"Find the latest Sarkari Naukri and government job updates in India, including new recruitment notifications, vacancies, application deadlines, exam updates and other important recruitment information."

### Category Content
Include state-specific categories:
- Maharashtra Government Jobs → emphasize MPSC, Police Bharti, Talathi, ZP
- Other state jobs → mention respective state commissions

### Qualification Content
National qualification framework:
- 10th Pass (India-wide)
- 12th Pass (India-wide)
- Graduate (India-wide)
- ITI (India-wide)
- Diploma (India-wide)
- Postgraduate (India-wide)

---

## Geographic Internal Linking

### Link to Districts Page
**Anchor Text:** Government Jobs by District
**Target URL:** `/districts`
**Context:** Why Use section, Related Resources section
**Purpose:** Connect job seekers to district-wise job discovery

### Link to State Pages
**Anchor Text:** [State Name]
**Target URL:** `/state/[state-slug]`
**Context:** State section
**Purpose:** Connect job seekers to state-specific job discovery

### Link to Maharashtra Districts
**Anchor Text:** Maharashtra
**Target URL:** `/districts`
**Context:** State section, Category section
**Purpose:** Direct Maharashtra job seekers to district-wise information

---

## Geographic Schema (Optional)

### Place Schema (Optional)
If implementing geographic schema, use for India entity:

```json
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "India",
  "description": "Sarkari Naukri and government job updates across India"
}
```

### Place Schema for States (Optional)
For Maharashtra:

```json
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Maharashtra",
  "description": "Maharashtra government jobs including MPSC, Police Bharti, Talathi, ZP recruitment"
}
```

**Note:** Place schema is optional. Only implement if it adds genuine value and aligns with content.

---

## GEO Content Guidelines

### Do
- Use natural geographic keyword combinations
- Link to state and district pages
- Emphasize Maharashtra where relevant
- Include India-specific context
- Build proper state/district architecture
- Connect to existing navigation structure

### Do Not
- Stuff geographic keywords
- Repeat city names in copy
- Create fake state pages
- Link to non-existent state pages
- Over-emphasize one state over others
- Break existing navigation structure

---

## Maharashtra-Specific Content

### Category Section - Maharashtra Government Jobs
**H3:** Maharashtra Government Jobs
**Content:** MPSC, Police Bharti, Talathi, ZP and other Maharashtra government recruitment.
**Link:** `/districts`

### Why Use Section - Maharashtra Context
Include Maharashtra-specific benefits:
"Explore government recruitment by state and district" → link to `/districts`

### FAQ - Maharashtra Questions
Consider adding Maharashtra-specific FAQ:
"How can I find Maharashtra government jobs?"
"Answer: You can browse Maharashtra government jobs through the Districts section, which covers all 36 Maharashtra districts including Pune, Mumbai, Nagpur, Nashik and others."

---

**Implementation Priority:** P1  
**Primary GEO Entity:** India  
**Secondary GEO Entities:** States (Maharashtra emphasis)  
**Tertiary GEO Entities:** Districts (link to /districts)
