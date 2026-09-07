# 04 — LATEST GOVERNMENT JOBS LISTING SECTION

**Section:** Main Dynamic Job Inventory  
**Priority:** P0  
**Type:** Enhancement (Improve existing job listing)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This enhances existing job listing functionality without removing current features.**

---

## Goal

Improve the semantic HTML and data quality of the main job listing while maintaining existing functionality.

---

## H2 Heading

```html
<h2>Latest Government Jobs 2026</h2>
```

---

## Introduction Copy

```
Browse active government recruitment opportunities currently accepting applications. Each listing should clearly show the recruiting organisation, vacancy count, qualification, location and application deadline.
```

---

## Job Card Semantic HTML (ENHANCEMENT)

### Recommended Structure
```html
<article class="job-card">
  <h3>Organisation Recruitment 2026 – Vacancy Title</h3>
  <p class="organisation">Organisation name</p>
  <dl class="job-details">
    <dt>Location</dt><dd>...</dd>
    <dt>Qualification</dt><dd>...</dd>
    <dt>Vacancies</dt><dd>...</dd>
    <dt>Last Date</dt><dd>...</dd>
    <dt>Status</dt><dd>Open</dd>
  </dl>
  <a href="/jobs/example" class="view-details">View Job Details</a>
</article>
```

### Required Card Data
- **Exact recruitment title** (fix artefacts like `[email protected]`)
- **Organisation name**
- **Organisation type** (Central Govt, State Govt, PSU, etc.)
- **Job category**
- **Location** (state, district, city)
- **Qualification** (controlled taxonomy)
- **Vacancies** (number)
- **Application start date**
- **Last date** (with proper formatting)
- **Status** (Open, Closing Soon, Closed)
- **Updated date** (where meaningful)

---

## Data Quality Rules (CRITICAL FIXES)

### Fix Artefacts
**Current Problem:** `[email protected]` appears in job titles  
**Solution:** Clean data at source, implement proper sanitization

**Standardize Titles:**
- Format: `[Organisation] Recruitment 2026 – [Role / Vacancies]`
- Do not mechanically rewrite official titles if it changes meaning
- Remove email obfuscation fragments
- Fix broken HTML fragments

### Classification System
**Store organisation_type with controlled values:**
- Central Government
- State Government
- Public Sector Bank
- PSU
- Government University
- Autonomous Body
- Research Institution
- Other Public Organisation

**Rule:** Do not label everything simply "Government" if the source classification is different.

---

## Pagination Strategy (ENHANCEMENT)

### URL Structure
```
/jobs (page 1)
/jobs?page=2 (page 2)
/jobs?page=3 (page 3)
```

### Implementation Rules
- Use crawlable pagination URLs
- Every page must have unique, accessible jobs
- Pagination links must be real `<a>` links
- No JavaScript-only dependency for discovering jobs
- Proper canonical strategy (self-referencing per page)

### UX Enhancement
- Show 20-30 jobs per page (configurable)
- Add "Load More" as secondary option
- Ensure both pagination and "Load More" work
- Maintain state across page navigation

---

## Content vs SEO Balance

### Ranking/Content Rule
**DO NOT:**
- Insert hundreds of words between every group of cards
- Push job inventory below long-form content
- Make users scroll excessively to find jobs

**DO:**
- Keep job inventory as the main purpose
- Add content sections below the main listing
- Balance SEO needs with user experience
- Use job inventory itself as substantial topical content

---

## Related Jobs Logic (NEW ADDITION)

### Recommendation Algorithm
Match jobs by:
- Department
- Qualification
- State/District
- Job category
- Similar organisation

### Example Implementation
```javascript
function getRelatedJobs(currentJob) {
  return jobs.filter(job => 
    job.department === currentJob.department ||
    job.qualification.some(q => currentJob.qualification.includes(q)) ||
    job.location.state === currentJob.location.state
  ).slice(0, 5);
}
```

### UI Placement
- Show on individual job detail pages
- Add "Related Government Jobs" section
- Use descriptive headings: "More Engineering Government Jobs"
- Link back to `/jobs` for broader search

---

## Implementation Steps

### Step 1: Enhance Job Card HTML
1. Update job card template to use semantic HTML
2. Ensure proper heading hierarchy (h3 for job title)
3. Add structured data markup where appropriate
4. Test with accessibility tools

### Step 2: Fix Data Quality Issues
1. Identify and clean `[email protected]` artefacts
2. Standardize job title format
3. Implement organisation classification
4. Add data validation at source

### Step 3: Implement Controlled Taxonomy
1. Add qualification taxonomy (10th, 12th, ITI, etc.)
2. Add location taxonomy (country/state/district/city)
3. Add department taxonomy
4. Update backend to use controlled values

### Step 4: Enhance Pagination
1. Implement crawlable pagination URLs
2. Add proper canonical tags per page
3. Ensure pagination links are accessible
4. Test with Google Search Console

### Step 5: Add Related Jobs
1. Implement recommendation algorithm
2. Add related jobs section to detail pages
3. Use descriptive anchor text
4. Test recommendation quality

### Step 6: Mobile Optimization
1. Optimize job card layout for mobile
2. Ensure touch targets are appropriate
3. Test horizontal scrolling if needed
4. Optimize loading performance

---

## Backend Requirements

### Enhanced Data Model
```javascript
job: {
  id: "unique_id",
  title: "Organisation Recruitment 2026 – Role",
  organisation: "Organisation Name",
  organisation_type: "State Government",
  department: "Railway",
  category: "Engineering",
  qualification: ["Diploma", "Engineering"],
  location: {
    country: "India",
    state: "Maharashtra",
    district: "Pune",
    city: "Pune"
  },
  vacancies: 100,
  salary: "Level-6",
  employment_type: "Permanent",
  application_start: "2026-08-15",
  application_deadline: "2026-09-15",
  status: "Open",
  official_notification_url: "https://...",
  official_application_url: "https://...",
  official_website_url: "https://...",
  date_posted: "2026-08-10",
  date_updated: "2026-09-04"
}
```

### API Enhancements
- Add filtering by taxonomy fields
- Add pagination support
- Add related jobs endpoint
- Add deadline-based sorting
- Add quality validation

---

## Validation Checklist

- [ ] Job cards use semantic HTML
- [ ] H3 headings for job titles
- [ ] All required data fields present
- [ ] Data artefacts cleaned (`[email protected]`)
- [ ] Organisation classification implemented
- [ ] Controlled taxonomy in place
- [ ] Pagination URLs crawlable
- [ ] Canonical tags correct per page
- [ ] Related jobs working
- [ ] Mobile layout optimized
- [ ] Performance acceptable
- [ ] No existing functionality broken
- [ ] Accessibility tested
- [ ] Core Web Vitals monitored

---

## Developer Notes

1. **React Implementation:** Enhance existing job card components, maintain current styling
2. **Performance:** Use virtual scrolling for large job lists, optimize re-renders
3. **Data Quality:** Implement validation at API level, not just UI
4. **Pagination:** Consider server-side rendering for SEO, client-side for UX
5. **Testing:** Test with various job data scenarios, edge cases

---

## Success Metrics

- [ ] Job card click-through rate improves
- [ ] User time-to-find-job decreases
- [ ] Pagination usage increases (indicating better discovery)
- [ ] Related jobs click-through rate acceptable
- [ ] Zero data quality complaints
- [ ] Positive user feedback on job information

---

## SEO Considerations

### Structured Data
- Consider `ItemList` structured data for the listing page
- Individual job pages can use `JobPosting` schema
- Ensure all schema data is accurate and visible to users
- Never fabricate missing schema values

### Internal Linking
- Link from job cards to qualification/state/department pages
- Link from detail pages back to `/jobs`
- Use descriptive anchor text
- Build topical authority through contextual links

---

**Last Updated:** 4 September 2026  
**Dependencies:** 01_HERO_SECTION_METADATA.md, 02_SEARCH_FILTERS_SECTION.md  
**Blocks:** None (enhances existing functionality)