# 15 — EXAM WISE OPPORTUNITIES SPECIFICATION

**Section:** Exam-wise Opportunities Content  
**Priority:** P1  
**Type:** Content Specification  
**Status:** Implementation Ready

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
