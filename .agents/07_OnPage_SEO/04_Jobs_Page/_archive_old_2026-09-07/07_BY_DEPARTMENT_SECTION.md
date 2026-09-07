# 07 — GOVERNMENT JOBS BY DEPARTMENT / CATEGORY SECTION

**Section:** Department-Based Discovery  
**Priority:** P1  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Help users discover government jobs based on departments and job categories while creating a strong department-based internal linking structure.

---

## H2 Heading

```html
<h2>Government Jobs by Department</h2>
```

---

## Introduction Copy

```
Explore recruitment opportunities by department and job category, including railway, banking, police, teaching, healthcare, defence, engineering, forest and public-sector organisations.
```

---

## H3 Categories with Landing Pages

### Railway Jobs
**Copy:** Find current railway recruitment opportunities and related examination updates across Indian Railways zones and divisions.

**Suggested URL:** `/government-jobs/railway`

**Keyword Cluster:**
- railway government jobs
- railway recruitment 2026
- railway sarkari naukri
- RRB jobs

### Banking Jobs
**Copy:** Explore government and public-sector banking recruitment opportunities across SBI, IBPS, RBI and other banking organisations.

**Suggested URL:** `/government-jobs/banking`

**Keyword Cluster:**
- bank government jobs
- banking government jobs
- bank sarkari naukri
- SBI recruitment, IBPS jobs

### Police Jobs
**Copy:** Find current police recruitment and Police Bharti opportunities across state police forces, central armed police forces and security organisations.

**Suggested URL:** `/government-jobs/police`

**Keyword Cluster:**
- police government jobs
- police bharti 2026
- police recruitment
- government police jobs

### Teaching Jobs
**Copy:** Explore government teaching recruitment and relevant examination information across schools, colleges, universities and education departments.

**Suggested URL:** `/government-jobs/teaching`

**Keyword Cluster:**
- teaching government jobs
- government teacher recruitment
- teaching jobs 2026
- TET/CTET jobs

### Defence Jobs
**Copy:** Find relevant defence recruitment opportunities and examination updates across army, navy, air force and central armed police forces.

**Suggested URL:** `/government-jobs/defence`

**Keyword Cluster:**
- defence government jobs
- military recruitment
- army/navy/air force jobs
- central armed police forces

### Healthcare Jobs
**Copy:** Find government healthcare and medical recruitment opportunities across hospitals, health departments, medical colleges and public health organisations.

**Suggested URL:** `/government-jobs/healthcare`

**Keyword Cluster:**
- government healthcare jobs
- medical government jobs
- health department recruitment
- hospital jobs

### Engineering Jobs
**Copy:** Explore engineering recruitment across government departments, public-sector undertakings, municipal corporations and technical organisations.

**Suggested URL:** `/government-jobs/engineering`

**Keyword Cluster:**
- government engineering jobs
- engineering government jobs 2026
- PSU engineering jobs
- technical government jobs

### Forest Jobs
**Copy:** Discover forest department recruitment opportunities across wildlife services, forest guards, conservation roles and environmental organisations.

**Suggested URL:** `/government-jobs/forest`

**Keyword Cluster:**
- forest government jobs
- forest department recruitment
- wildlife services jobs
- forest guard jobs

### PSU Jobs
**Copy:** Explore recruitment opportunities across public-sector undertakings and government-owned enterprises in various sectors.

**Suggested URL:** `/government-jobs/psu`

**Keyword Cluster:**
- PSU recruitment
- public sector jobs
- government enterprise jobs
- PSU sarkari naukri

### Municipal Corporation Jobs
**Copy:** Find municipal government recruitment across city corporations, municipal councils, urban local bodies and civic services.

**Suggested URL:** `/government-jobs/municipal`

**Keyword Cluster:**
- municipal government jobs
- corporation recruitment
- civic services jobs
- nagar nigam jobs

### Government University Jobs
**Copy:** Explore recruitment opportunities across government universities, central universities, state universities and educational institutions.

**Suggested URL:** `/government-jobs/university`

**Keyword Cluster:**
- government university jobs
- university recruitment
- government college jobs
- academic government jobs

### Research Institution Jobs
**Copy:** Find research and technical recruitment opportunities across government research institutions, laboratories and scientific organisations.

**Suggested URL:** `/government-jobs/research`

**Keyword Cluster:**
- research government jobs
- scientific institution jobs
- government laboratory jobs
- research organisation recruitment

---

## Important Classification Rule

### Separate Organisation Types
**Controlled Values for organisation_type:**
- Central Government
- State Government
- Public Sector Bank
- PSU
- Government University
- Autonomous Body
- Research Institution
- Other Public Organisation

**Implementation:** Avoid misleading users and improve entity accuracy by correctly classifying organisations. Do not label everything simply "Government" if the source classification is different.

---

## Keyword Clusters

### Primary Department Keywords
- central government jobs
- state government jobs
- railway government jobs
- bank government jobs
- police government jobs
- teaching government jobs
- government healthcare jobs
- engineering government jobs
- PSU recruitment
- municipal government jobs

### Secondary Keywords
- railway recruitment 2026
- banking recruitment
- police bharti
- teacher recruitment
- defence jobs
- medical jobs
- technical jobs
- forest department
- public sector jobs

---

## Cannibalisation Rule

### Keyword Ownership
- **Dedicated department pages** own department-specific high-intent queries
- **/jobs** provides discovery links and broad inventory
- **/jobs** should NOT try to own department-specific keywords

### Internal Linking Strategy
```html
<!-- On /jobs page -->
<section>
  <h2>Government Jobs by Department</h2>
  <a href="/government-jobs/railway">Railway Jobs</a>
  <a href="/government-jobs/banking">Banking Jobs</a>
  ...
</section>

<!-- On department page -->
<a href="/jobs">View All Government Jobs</a>
<a href="/government-jobs/police">Police Jobs</a>
<a href="/government-jobs/teaching">Teaching Jobs</a>
```

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after state section
2. Add introduction copy
3. Create container for department blocks
4. Style to match existing design

### Step 2: Implement Department Taxonomy
1. Add controlled department values to backend
2. Map existing department data to controlled values
3. Add organisation classification system
4. Update job data to use controlled values

### Step 3: Create Department Blocks
1. Create H3 blocks for each department
2. Add descriptive copy for each
3. Add links to department landing pages
4. Implement job count per department

### Step 4: Create Landing Pages
1. Create landing page template for departments
2. Implement department-specific pages
3. Add unique content for each page
4. Ensure proper metadata and canonicals

### Step 5: Add Internal Links
1. Link from /jobs to department pages
2. Link from department pages back to /jobs
3. Add cross-links between related departments
4. Use descriptive anchor text

### Step 6: Mobile Optimization
1. Test department blocks on mobile
2. Ensure links are thumb-friendly
3. Optimize layout for small screens
4. Test department-based filtering

---

## Validation Checklist

- [ ] H2 heading added after state section
- [ ] Introduction copy added
- [ ] All department blocks created
- [ ] Controlled taxonomy implemented
- [ ] Organisation classification system working
- [ ] Department data cleaned and standardized
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

1. **React Implementation:** Create reusable department block component
2. **Data Classification:** Implement organisation type classification at data level
3. **Landing Pages:** Use template system for consistency across department pages
4. **Internal Links:** Automate internal linking based on job department data
5. **Performance:** Cache department counts, update periodically

---

## Success Metrics

- [ ] Department section engagement increases
- [ ] Traffic to department pages grows
- [ ] Users find relevant jobs by department
- [ ] Improved internal linking graph
- [ ] Positive user feedback on department discovery
- [ ] Better organisation classification accuracy

---

## SEO Considerations

### Keyword Strategy
- Target department-specific long-tail keywords
- Use descriptive anchor text for internal links
- Include department-specific information in content
- Add department-related FAQ sections

### Content Strategy
- Each department page should include:
  - Overview of that department
  - Major recruiters in that department
  - Typical roles and qualifications
  - Application process specific to department
  - Related departments and cross-links

---

## AEO Enhancement

### Question-Answer Format

**Question:** What government jobs are available in railway department?

**Answer:** Railway recruitment includes positions across Indian Railways zones such as RRB NTPC, RRB Group D, RRB ALP, JE, and other technical and non-technical roles. Eligibility varies by position and includes 10th pass, 12th pass, diploma, and graduate qualifications depending on the recruitment notification.

**Implementation:** Add to department pages and FAQ section.

---

**Last Updated:** 4 September 2026  
**Dependencies:** 06_BY_STATE_SECTION.md  
**Blocks:** None (can be implemented independently)