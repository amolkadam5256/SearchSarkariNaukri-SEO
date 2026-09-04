# 08 — GOVERNMENT JOBS BY EXAM SECTION

**Section:** Exam-Based Discovery  
**Priority:** P1  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Leverage existing exam pages to create strong internal linking while helping users discover government jobs through major competitive exams.

---

## H2 Heading

```html
<h2>Government Jobs by Exam</h2>
```

---

## Introduction Copy

```
Explore government recruitment and examination information for major competitive exams, including UPSC, MPSC, SSC, banking, railway, police and teaching exams.
```

---

## Internal Links to Existing Exam Pages

### UPSC Jobs
**Anchor:** UPSC Jobs  
**Destination:** `/exams/upsc-cse`

**Copy:** Union Public Service Commission conducts civil services, engineering services, medical services and other central government recruitments.

**Keyword Targets:**
- UPSC jobs
- UPSC recruitment
- civil services jobs
- central government jobs through UPSC

### MPSC Jobs
**Anchor:** MPSC Jobs  
**Destination:** `/exams/mpsc-rajyaseva`

**Copy:** Maharashtra Public Service Commission conducts state civil services, group B, group C and other Maharashtra government recruitments.

**Keyword Targets:**
- MPSC jobs
- MPSC recruitment
- Maharashtra civil services
- state government jobs through MPSC

### SSC Jobs
**Anchor:** SSC Jobs  
**Destination:** `/exams/ssc-cgl`

**Copy:** Staff Selection Commission conducts central government recruitments including CGL, CHSL, MTS, GD and other examinations.

**Keyword Targets:**
- SSC jobs
- SSC government jobs
- SSC recruitment
- central government jobs through SSC

### Banking Exams
**Anchor:** Banking Exams  
**Destination:** `/exams/sbi-po-clerk`

**Copy:** Banking recruitment includes SBI PO, SBI Clerk, IBPS PO, IBPS Clerk, RBI Grade B and other public-sector bank examinations.

**Keyword Targets:**
- banking exams
- bank government jobs
- SBI recruitment
- IBPS jobs

### Railway Exams
**Anchor:** Railway Exams  
**Destination:** `/exams/rrb-ntpc`

**Copy:** Railway Recruitment Board conducts NTPC, Group D, ALP, JE and other technical and non-technical railway examinations.

**Keyword Targets:**
- railway recruitment
- railway exams
- RRB jobs
- railway government jobs

### Police Recruitment
**Anchor:** Police Recruitment  
**Destination:** `/exams/maharashtra-police-bharti`

**Copy:** Police recruitment includes state police constable, driver, sub-inspector and other law enforcement examinations across states.

**Keyword Targets:**
- police recruitment
- police bharti
- government police jobs
- law enforcement jobs

### CTET / TET
**Anchor:** CTET / TET  
**Destination:** `/exams/ctet`

**Copy:** Central Teacher Eligibility Test and state TET examinations for primary and upper primary teaching recruitment.

**Keyword Targets:**
- CTET jobs
- TET recruitment
- teaching eligibility
- government teacher jobs

---

## Cannibalisation Rule

### Keyword Ownership
- **Dedicated exam pages** own exam-specific high-intent queries
- **/jobs** should link to exam pages contextually
- **/jobs** should NOT try to own MPSC Jobs, UPSC Jobs, Railway Recruitment
- **/jobs** shows current matching vacancies where appropriate

### Internal Linking Strategy
```html
<!-- On /jobs page -->
<section>
  <h2>Government Jobs by Exam</h2>
  <a href="/exams/upsc-cse">UPSC Jobs</a>
  <a href="/exams/mpsc-rajyaseva">MPSC Jobs</a>
  <a href="/exams/ssc-cgl">SSC Jobs</a>
  ...
</section>

<!-- On exam page -->
<a href="/jobs">Current Government Jobs</a>
<a href="/government-jobs/maharashtra">Maharashtra Government Jobs</a>
```

---

## Integration with Existing Navigation

### Leverage Current Site Architecture
The site already has strong navigation with:
- Jobs
- Exams
- Updates
- Tools
- Specific exam destinations (UPSC, MPSC, SSC, Banking, Railway, Police, Teacher)

**Implementation:** This section should complement existing navigation by providing contextual exam-focused links from the jobs page.

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after department section
2. Add introduction copy
3. Create container for exam links
4. Style to match existing design

### Step 2: Create Exam Link Blocks
1. Create blocks for each major exam
2. Add descriptive copy for each exam
3. Link to existing exam pages
4. Add current job count for each exam

### Step 3: Add Dynamic Job Integration
1. Show current jobs matching each exam
2. Link exam pages to relevant current jobs
3. Implement bidirectional linking
4. Update job counts dynamically

### Step 4: Enhance Internal Linking
1. Link from /jobs to exam pages
2. Link from exam pages back to /jobs
3. Add cross-links between related exams
4. Use descriptive anchor text

### Step 5: Mobile Optimization
1. Test exam blocks on mobile
2. Ensure links are thumb-friendly
3. Optimize layout for small screens
4. Test exam-based filtering

---

## Validation Checklist

- [ ] H2 heading added after department section
- [ ] Introduction copy added
- [ ] All exam link blocks created
- [ ] Links to existing exam pages working
- [ ] Descriptive copy for each exam
- [ ] Dynamic job integration working
- [ ] Internal linking structure implemented
- [ ] Mobile layout tested
- [ ] No keyword cannibalisation
- [ ] Performance acceptable
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Create reusable exam link component
2. **Integration:** Use existing exam page routes, don't create duplicates
3. **Dynamic Data:** Link exam categories to current job inventory
4. **Internal Links:** Maintain existing navigation structure
5. **Performance:** Cache exam counts, update periodically

---

## Success Metrics

- [ ] Exam section engagement increases
- [ ] Traffic to exam pages grows
- [ ] Users discover relevant jobs through exams
- [ ] Improved internal linking graph
- [ ] Positive user feedback on exam discovery
- [ ] Better cross-navigation between jobs and exams

---

## SEO Considerations

### Keyword Strategy
- Focus on exam-specific intent queries
- Use descriptive anchor text for internal links
- Include exam-specific information in content
- Link exam pages to relevant job categories

### Content Strategy
- Each exam page should already have comprehensive content
- This section provides contextual links from jobs
- Add current job opportunities to exam pages
- Create bidirectional content relationships

---

## AEO Enhancement

### Question-Answer Format

**Question:** How can I find government jobs through MPSC exam?

**Answer:** MPSC conducts Maharashtra state civil services and other government recruitments. Browse the MPSC Jobs page for examination schedules, eligibility criteria, and current vacancies. Use the government jobs page to find MPSC-related recruitments currently accepting applications.

**Implementation:** Add to exam pages and FAQ section.

---

**Last Updated:** 4 September 2026  
**Dependencies:** 07_BY_DEPARTMENT_SECTION.md  
**Blocks:** None (can be implemented independently)