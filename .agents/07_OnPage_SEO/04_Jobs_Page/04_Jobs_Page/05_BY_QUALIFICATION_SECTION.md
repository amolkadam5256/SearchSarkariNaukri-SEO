# 05 — GOVERNMENT JOBS BY QUALIFICATION SECTION

**Section:** Qualification-Based Discovery  
**Priority:** P1  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Help users discover government jobs based on their educational qualification while creating a strong internal linking structure.

---

## H2 Heading

```html
<h2>Government Jobs by Qualification</h2>
```

---

## Introduction Copy

```
Government recruitment is available for different education levels, from 10th and 12th pass candidates to ITI and diploma holders, graduates, engineers and postgraduates. Explore current vacancies based on your qualification.
```

---

## H3 Blocks with Landing Pages

### 10th Pass Government Jobs
**Copy:** Find current government recruitment opportunities for candidates who have completed Class 10.

**Suggested URL:** `/government-jobs/10th-pass`

**Keyword Cluster:**
- government jobs for 10th pass
- 10th pass govt jobs
- 10th pass government jobs 2026
- government jobs after 10th

### 12th Pass Government Jobs
**Copy:** Explore current government vacancies for candidates who have completed Class 12, subject to the eligibility conditions in each notification.

**Suggested URL:** `/government-jobs/12th-pass`

**Keyword Cluster:**
- government jobs for 12th pass
- 12th pass government jobs 2026
- govt jobs after 12th
- 12th pass sarkari naukri

### ITI Government Jobs
**Copy:** Discover government recruitment opportunities for ITI certificate holders across technical trades and vocational courses.

**Suggested URL:** `/government-jobs/iti`

**Keyword Cluster:**
- ITI government jobs
- govt jobs after ITI
- ITI sarkari naukri
- ITI pass government jobs

### Diploma Government Jobs
**Copy:** Find government recruitment opportunities for diploma holders in engineering, technology and other diploma programs.

**Suggested URL:** `/government-jobs/diploma`

**Keyword Cluster:**
- government jobs for diploma holders
- diploma government jobs 2026
- govt jobs after diploma
- diploma holder government jobs

### Graduate Government Jobs
**Copy:** Explore government jobs available for graduates across central, state and other public-sector organisations.

**Suggested URL:** `/government-jobs/graduate`

**Keyword Cluster:**
- government jobs for graduates
- graduate government jobs 2026
- graduate sarkari naukri
- govt jobs for freshers

### Engineering Government Jobs
**Copy:** Find government recruitment opportunities for candidates with engineering degrees and diplomas across various technical departments.

**Suggested URL:** `/government-jobs/engineering`

**Keyword Cluster:**
- government jobs for engineers
- engineering government jobs 2026
- government jobs after engineering
- govt engineering jobs

### Post Graduate Government Jobs
**Copy:** Explore recruitment opportunities for candidates with postgraduate qualifications across administration, research and specialised roles.

**Suggested URL:** `/government-jobs/post-graduate`

**Keyword Cluster:**
- postgraduate government jobs
- government jobs after post graduation
- PG government jobs
- post graduate sarkari naukri

---

## Backend Requirement

### Controlled Qualification Taxonomy
**Required Data Structure:**
```javascript
qualification: {
  values: ["10th", "12th", "ITI", "Diploma", "Graduate", "Postgraduate", "Engineering", "Medical", "PhD"],
  allowMultiple: true,
  controlled: true
}
```

**Implementation Rules:**
- Qualification must be controlled data, not only free text
- A job may have multiple qualification tags
- Use standard values, not variations (e.g., "10th" not "10th pass", "SSC")
- Map existing free-text to controlled values during migration

---

## Landing Page Requirements

### Each Qualification Page Must Have:
1. **Real inventory** (minimum 10-20 active jobs)
2. **Unique content** (not just filtered results)
3. **Specific information** about that qualification
4. **Internal links** to related qualifications
5. **Proper metadata** (title, description, canonical)

### Page Structure Template:
```html
<h1>10th Pass Government Jobs 2026</h1>
<p>Introduction about 10th pass opportunities...</p>
<section>
  <h2>Latest 10th Pass Government Jobs</h2>
  [Job listings]
</section>
<section>
  <h2>Departments Recruiting 10th Pass Candidates</h2>
  [Department information]
</section>
<section>
  <h2>Frequently Asked Questions</h2>
  [FAQ specific to 10th pass]
</section>
```

---

## Cannibalisation Rule

### Keyword Ownership
- **/jobs** owns broad "Government Jobs"
- **Qualification pages** own qualification-specific queries
- **/jobs** links to qualification pages
- **/jobs** should NOT repeat full landing-page content

### Internal Linking Strategy
```html
<!-- On /jobs page -->
<section>
  <h2>Government Jobs by Qualification</h2>
  <a href="/government-jobs/10th-pass">10th Pass Government Jobs</a>
  <a href="/government-jobs/12th-pass">12th Pass Government Jobs</a>
  ...
</section>

<!-- On qualification page -->
<a href="/jobs">View All Government Jobs</a>
<a href="/government-jobs/12th-pass">12th Pass Government Jobs</a>
<a href="/government-jobs/diploma">Diploma Government Jobs</a>
```

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after main job listing
2. Add introduction copy
3. Create container for qualification blocks
4. Style to match existing design

### Step 2: Implement Qualification Taxonomy
1. Add controlled qualification values to backend
2. Map existing free-text qualifications to controlled values
3. Update job data to use array of qualifications
4. Add validation for qualification data

### Step 3: Create Qualification Blocks
1. Create H3 blocks for each qualification
2. Add descriptive copy for each
3. Add links to qualification landing pages
4. Implement job count per qualification

### Step 4: Create Landing Pages
1. Create landing page template
2. Implement qualification-specific pages
3. Add unique content for each page
4. Ensure proper metadata and canonicals

### Step 5: Add Internal Links
1. Link from /jobs to qualification pages
2. Link from qualification pages back to /jobs
3. Add cross-links between related qualifications
4. Use descriptive anchor text

### Step 6: Mobile Optimization
1. Test qualification blocks on mobile
2. Ensure links are thumb-friendly
3. Optimize layout for small screens
4. Test horizontal scrolling if needed

---

## Validation Checklist

- [ ] H2 heading added after main listing
- [ ] Introduction copy added
- [ ] All qualification blocks created
- [ ] Controlled taxonomy implemented
- [ ] Qualification data cleaned and standardized
- [ ] Landing pages created with real inventory
- [ ] Each landing page has unique content
- [ ] Internal linking structure implemented
- [ ] Proper metadata on landing pages
- [ ] Mobile layout tested
- [ ] No keyword cannibalisation
- [ ] Performance acceptable
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Create reusable qualification block component
2. **Data Migration:** Plan careful migration from free-text to controlled values
3. **Landing Pages:** Use template system for consistency across qualification pages
4. **Internal Links:** Automate internal linking where possible based on job data
5. **Performance:** Cache qualification counts, update periodically

---

## Success Metrics

- [ ] Qualification section engagement increases
- [ ] Traffic to qualification pages grows
- [ ] Users find relevant jobs by qualification
- [ ] Reduced bounce rate on qualification pages
- [ ] Improved internal linking graph
- [ ] Positive user feedback on qualification discovery

---

## SEO Considerations

### Keyword Strategy
- Target qualification-specific long-tail keywords
- Use descriptive anchor text for internal links
- Avoid keyword stuffing in qualification descriptions
- Focus on user intent and helpful information

### Content Strategy
- Each qualification page should be a comprehensive resource
- Include specific information about that qualification
- Add FAQ sections for qualification-specific questions
- Link to related resources (exam prep, eligibility, etc.)

---

## AEO Enhancement

### Question-Answer Format

**Question:** Which government jobs are available for 10th pass candidates?

**Answer:** 10th pass candidates can find government recruitment opportunities in railways, police, defence, support services, forest departments and other organisations. Eligibility varies by recruitment notification. Use the 10th Pass Government Jobs page to view current vacancies.

**Implementation:** Add to qualification pages and FAQ section.

---

**Last Updated:** 4 September 2026  
**Dependencies:** 04_LATEST_JOBS_SECTION.md  
**Blocks:** None (can be implemented independently)