# 15 — EXAM WISE OPPORTUNITIES SPECIFICATION

**Section:** Exam-wise Opportunities Content  
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

## Section Overview

Add a comprehensive section explaining Maharashtra government exams and recruitment opportunities. This helps candidates understand major exams and how they connect to government job opportunities.

---

## H2 Heading

```
Maharashtra Government Exams and Recruitment
```

---

## Section Content

### Introduction Paragraph

```
Maharashtra government recruitment is conducted through various competitive examinations and direct recruitment processes. Major exams include MPSC Rajyaseva, Maharashtra Police Bharti, teacher recruitment, health department recruitment, and administrative position exams. These examinations are conducted by different recruiting bodies and lead to government job opportunities across Maharashtra districts.
```

---

## Exam Categories (H3 Headings)

### H3: MPSC Recruitment

```
Maharashtra Public Service Commission (MPSC) conducts Rajyaseva, State Services, and other examinations for administrative positions including Deputy Collector, DSP, Tahsildar, and other state government officer positions. MPSC recruitment is a major pathway for graduates seeking government administrative careers across Maharashtra districts. MPSC exams include preliminary, mains, and interview stages.
```

**Link to:** `/exams/mpsc-rajyaseva` (if exists)

---

### H3: Maharashtra Police Recruitment

```
Maharashtra Police Bharti is conducted for constable, driver, sub-inspector, and other police department positions across all districts. Police recruitment includes physical tests, written examinations, and medical fitness assessments. Maharashtra Police jobs are available district-wise and through statewide recruitment notifications depending on vacancy requirements.
```

**Link to:** `/exams/maharashtra-police-bharti` (if exists)

---

### H3: Teacher Recruitment

```
Teacher recruitment in Maharashtra is conducted by the Education Department, Zilla Parishad, and municipal corporations for positions in government schools, colleges, and educational institutions. Recruitment includes TET exams, direct recruitment for teacher positions, and examinations for principal, lecturer, and professor roles in government educational institutions across Maharashtra districts.
```

**Link to:** `/exams/teacher-recruitment` (if exists)

---

### H3: Health and Medical Recruitment

```
Health department recruitment includes examinations and direct recruitment for medical positions in government hospitals, health centers, and medical colleges. Positions include medical officers, staff nurses, pharmacists, lab technicians, and other healthcare positions. Recruitment is conducted by the Health Department, medical education department, and individual government hospitals across Maharashtra districts.
```

**Link to:** `/exams/health-recruitment` (if exists)

---

### H3: Clerk, Typist and Administrative Recruitment

```
Clerk, typist, and administrative position recruitment is conducted by various government departments, district collector offices, municipal corporations, and other government organisations across Maharashtra. These positions require specific typing skills, computer knowledge, and educational qualifications. Recruitment includes written examinations, typing tests, and skill assessments for clerical and administrative roles.
```

**Link to:** `/exams/clerk-recruitment` (if exists)

---

## Implementation Notes

### HTML Structure

```html
<section aria-labelledby="exam-opportunities">
  <h2 id="exam-opportunities">Maharashtra Government Exams and Recruitment</h2>
  <p>Introduction paragraph about government exams and recruitment.</p>
  
  <h3>MPSC Recruitment</h3>
  <p>Content about MPSC recruitment.</p>
  <a href="/exams/mpsc-rajyaseva" class="exam-link">View MPSC Exams →</a>
  
  <h3>Maharashtra Police Recruitment</h3>
  <p>Content about police recruitment.</p>
  <a href="/exams/maharashtra-police-bharti" class="exam-link">View Police Recruitment →</a>
  
  <!-- Continue for all exam types -->
</section>
```

### Linking Strategy

- Link to existing exam pages where they exist
- Use descriptive anchor text: "View MPSC Exams", "View Police Recruitment", etc.
- Do not create broken links
- If exam page doesn't exist, link to /exams or /jobs

### Content Guidelines

- Each exam section should be 200-400 characters
- Focus on actual exam information
- Do not fabricate exam details
- Mention district relevance where applicable
- Use natural language, not keyword stuffing

---

## Validation Checklist

### Content
- [ ] All 5 exam types are covered
- [ ] Each exam type has H3 heading
- [ ] Content is exam-specific
- [ ] Links point to existing pages where available
- [ ] No broken links created
- [ ] Content is accurate and realistic

### Structure
- [ ] H2 heading is present
- [ ] H3 headings for each exam type
- [ ] Proper semantic HTML used
- [ ] ARIA labels added
- [ ] Accessible navigation

### SEO
- [ ] Exam names mentioned naturally
- [ ] Geographic context included where relevant
- [ ] Internal links with descriptive anchors
- [ ] No keyword stuffing
- [ ] Content is genuinely useful

---

**Last Updated:** 8 September 2026  
**Status:** Implementation Ready
