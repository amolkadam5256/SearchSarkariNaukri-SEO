# 13 — TRUST VERIFICATION SPECIFICATION

**Section:** Trust and Verification Content  
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

## Trust Section Structure

### Section Heading
**H2:** Verify Recruitment Information

### Purpose
Build trust by explaining:
- How information is collected
- What users should verify
- Independent platform status
- Editorial policy link
- Last updated dates

---

## Trust Content

### Main Verification Statement
We collect recruitment information from official notifications and recruitment websites. Before applying, candidates should open the official notification and confirm the vacancy, eligibility, age limit, application fee, important dates and application process.

### Verification Information Block
**Last Updated:** [Dynamic date]  
**Reviewed Date:** [Dynamic date]  
**Editorial Policy:** [Link to editorial policy]  
**Official Source:** Always verify with official recruitment notification  
**Recruitment Authority:** Respective government department

---

## Trust Subsections

### 1. How We Verify Job Information
**Content:**
We collect recruitment information from official notifications and recruitment websites. Before applying, candidates should open the official notification and confirm the vacancy, eligibility, age limit, application fee, important dates and application process.

### 2. Independent Platform Status
**Content:**
Search Sarkari Naukri is an independent information platform and is not affiliated with any government department. Before submitting an application, always check the official recruitment notification and official website.

### 3. Editorial Policy Link
**Content:**
View our editorial policy for more information about how we collect, verify, and present recruitment information.

**Link:** `/editorial-policy`

---

## E-E-A-T Improvements

### Experience
Show that the platform has experience with government job information:
- "Search Sarkari Naukri brings job seekers together with current government recruitment information across central and state departments."

### Expertise
Demonstrate expertise in government job recruitment:
- Explain verification process
- Provide accurate eligibility information
- Show understanding of recruitment lifecycle

### Authoritativeness
Build authority through:
- Accurate information
- Official source verification
- Editorial policy
- Regular updates

### Trustworthiness
Build trust through:
- Transparency about independent status
- Clear verification instructions
- Editorial policy link
- Last updated dates
- Official source emphasis

---

## Trust Signals

### Date Information
Display dynamic dates:
- Last Updated: [dynamic date]
- Reviewed Date: [dynamic date]

### Editorial Policy
Link to editorial policy:
- Explain data collection process
- Explain verification process
- Explain correction mechanism

### Official Source Emphasis
Repeatedly emphasize:
- "Always verify with official recruitment notification"
- "Check the official recruitment notification before applying"
- "Apply through the official website"

### Disclaimer
Include disclaimer in multiple places:
- First CTA section
- Why Use section
- Verify Recruitment Information section
- FAQ section

---

## Content Guidelines

### Tone
Use professional, transparent, helpful tone:
- Be clear about independent status
- Be helpful about verification process
- Be transparent about data sources
- Be accurate about information

### Consistency
Keep trust messaging consistent:
- Independent platform status
- Official source verification
- Editorial policy reference
- Last updated dates

### Placement
Place trust content strategically:
- After practical content (How to Check)
- Before FAQ section
- Near final CTA

---

## Technical Implementation

### Dynamic Dates
Implement dynamic date fields:
- Last Updated: Updates when content changes
- Reviewed Date: Updates when content is reviewed

### Editorial Policy Link
Ensure editorial policy page exists:
- Verify `/editorial-policy` exists
- Verify page is accessible
- Verify page loads correctly

### Schema Markup
Consider adding aboutPage schema to link to editorial policy:
```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "mainEntity": {
    "@type": "Organization",
    "name": "Search Sarkari Naukri",
    "publishingPrinciples": "https://www.searchsarkarinaukri.com/editorial-policy"
  }
}
```

---

**Implementation Priority:** P1  
**Trust Signals:** Dates, editorial policy, official source emphasis  
**E-E-A-T Focus:** Transparency, accuracy, verification
