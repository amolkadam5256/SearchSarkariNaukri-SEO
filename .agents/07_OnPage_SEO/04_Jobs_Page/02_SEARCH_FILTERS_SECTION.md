# 02 — SEARCH + FILTERS + POPULAR SEARCHES SECTION

**Section:** Search and Filters Enhancement  
**Priority:** P0  
**Type:** Additive (Enhancement of existing functionality)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This enhances existing search/filter functionality without removing current features.**

---

## Goal

Improve the search and filter UX while making it more SEO-friendly and AEO-optimized.

---

## H2 Heading

```html
<h2>Search Government Jobs</h2>
```

---

## Introduction Copy (NEW ADDITION)

```
Search by job title, organisation, department or keyword. Use the filters to narrow Government Jobs by qualification, location, job category and application deadline.
```

---

## Enhanced Filter Architecture

### Main Search Input (EXISTING - ENHANCE)
```html
<input 
  type="search" 
  placeholder="Search government jobs by title, organisation or keyword"
  aria-label="Search government jobs"
>
```

### Qualification Filter (EXISTING - ENHANCE)
**Options:**
- 10th Pass
- 12th Pass  
- ITI
- Diploma
- Graduate
- Post Graduate
- Engineering
- Medical
- PhD

### Location Filter (EXISTING - ENHANCE)
**Hierarchy:**
- All India
  - State
    - District
      - City

**Implementation:** Use dropdown or cascading selects for better UX

### Department Filter (EXISTING - ENHANCE)
**Options:**
- Railway
- Banking
- Police
- Defence
- Education
- Healthcare
- Forest
- PSU
- Municipal Corporation
- Government University
- Research Institution

### Job Type Filter (NEW ADDITION)
**Options:**
- Permanent
- Contract
- Apprenticeship
- Internship
- Temporary

### Application Status Filter (NEW ADDITION)
**Options:**
- Open
- Closing Soon
- Closed

### Deadline Filter (NEW ADDITION)
**Options:**
- Closing Today
- Closing Tomorrow
- Within 3 Days
- Within 7 Days
- Within 15 Days
- Within 30 Days

### Sort Options (EXISTING - ENHANCE)
**Options:**
- Newest
- Last Date
- Most Vacancies
- Closing Soon
- Recently Updated (only if tracking actual updates)

---

## Popular Search Links (NEW ADDITION)

### Recommended Anchors with Links
```html
<div class="popular-searches">
  <h3>Popular Searches</h3>
  <a href="/government-jobs/10th-pass">10th Pass Government Jobs</a>
  <a href="/government-jobs/12th-pass">12th Pass Government Jobs</a>
  <a href="/government-jobs/graduate">Graduate Government Jobs</a>
  <a href="/government-jobs/railway">Railway Jobs</a>
  <a href="/government-jobs/banking">Banking Jobs</a>
  <a href="/government-jobs/police">Police Jobs</a>
  <a href="/exams/mpsc-rajyaseva">MPSC Jobs</a>
  <a href="/exams/ssc-cgl">SSC Jobs</a>
  <a href="/exams/upsc-cse">UPSC Jobs</a>
  <a href="/government-jobs/maharashtra">Maharashtra Government Jobs</a>
  <a href="/jobs?deadline=closing-soon">Government Jobs Closing Soon</a>
</div>
```

---

## SEO/Faceted Navigation Rules

### DO NOT Index Every Combination

**Examples that should NOT become independent indexable pages:**
- `/jobs?qualification=12th&location=pune&sort=deadline`
- `/jobs?department=railway&qualification=graduate&state=maharashtra`
- `/jobs?utm_source=newsletter&campaign=jobs`

### DO Create Curated Landing Pages

**High-value single-intent clusters:**
- `/government-jobs/10th-pass`
- `/government-jobs/12th-pass`
- `/government-jobs/graduate`
- `/government-jobs/maharashtra`
- `/government-jobs/railway`
- `/government-jobs/police`

**Rule:** Only create a landing page when there is:
- Real inventory (minimum 10-20 active jobs)
- Unique useful content (not just filtered results)
- Sustained search demand
- Internal link support

---

## AEO Opportunity

### Question-Answer Format for Search

**Question:** How can I find government jobs for 12th pass candidates?

**Answer:** Use the qualification filter or open the dedicated 12th Pass Government Jobs page to view current vacancies and their eligibility requirements.

**Implementation:** Add this as helper text or tooltip near the qualification filter.

---

## Accessibility Requirements

### Every Filter Must Have:
- [ ] Visible label
- [ ] Keyboard accessibility
- [ ] Visible focus state
- [ ] Screen-reader status announces result count
- [ ] Filter state understandable without color alone

### Form Best Practices:
- Use proper `<label>` elements
- Group related filters with `<fieldset>`
- Use ARIA attributes where needed
- Provide clear feedback on filter changes

---

## Implementation Steps

### Step 1: Enhance Search Input
1. Update placeholder text to be more descriptive
2. Add aria-label for accessibility
3. Ensure search works with keyboard (Enter key)
4. Add search suggestions if possible

### Step 2: Enhance Qualification Filter
1. Add all recommended qualification options
2. Ensure controlled taxonomy in backend
3. Add qualification-specific landing page links
4. Test filter combinations

### Step 3: Enhance Location Filter
1. Implement state/district/city hierarchy
2. Add location-specific landing page links
3. Ensure location data is structured
4. Test location-based filtering

### Step 4: Add New Filters
1. Add Job Type filter
2. Add Application Status filter
3. Add Deadline filter
4. Add "Recently Updated" sort option (if data available)

### Step 5: Add Popular Searches
1. Create popular searches section below main search
2. Link to relevant landing pages
3. Use descriptive anchor text
4. Update popular searches based on actual user behavior

### Step 6: Implement Faceted Navigation Strategy
1. Add `noindex` to non-SEO filter combinations
2. Create canonical tags for curated landing pages
3. Ensure proper pagination for filtered results
4. Test with Google Search Console

### Step 7: Add AEO Elements
1. Add question-answer helper text
2. Implement direct answers for common queries
3. Add schema markup for Q&A where appropriate
4. Test with answer engine validation tools

---

## Backend Requirements

### Data Model Enhancements
```javascript
job: {
  qualification: ['10th', '12th', 'Graduate'], // Array, not free text
  location: {
    country: 'India',
    state: 'Maharashtra',
    district: 'Pune',
    city: 'Pune'
  },
  department: 'Railway',
  job_type: 'Permanent',
  status: 'Open',
  application_deadline: '2026-09-15',
  last_updated: '2026-09-04'
}
```

### Filter Logic
- Support multiple qualification selection
- Support location hierarchy filtering
- Support combined filters with AND/OR logic
- Return result counts for each filter option

---

## Validation Checklist

- [ ] Search input enhanced with better placeholder
- [ ] All qualification options available
- [ ] Location hierarchy implemented
- [ ] Department filter comprehensive
- [ ] New filters (job type, status, deadline) added
- [ ] Sort options enhanced
- [ ] Popular searches section added
- [ ] Faceted navigation strategy implemented
- [ ] Non-SEO combinations have noindex
- [ ] Curated landing pages have proper canonicals
- [ ] AEO question-answer elements added
- [ ] Accessibility requirements met
- [ ] Mobile layout tested
- [ ] Filter performance acceptable
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Use existing filter components as base, enhance rather than replace
2. **Performance:** Debounce search input, avoid expensive re-renders
3. **URL Structure:** Use clean URLs for curated pages, query params for filters
4. **Analytics:** Track filter usage to optimize popular searches
5. **Testing:** Test filter combinations thoroughly, especially edge cases

---

## Success Metrics

- [ ] Filter usage increases (analytics)
- [ ] Search success rate improves
- [ ] Time-to-find-job decreases
- [ ] Mobile filter engagement increases
- [ ] Popular search clicks increase
- [ ] Zero filter-related errors reported

---

**Last Updated:** 4 September 2026  
**Dependencies:** 01_HERO_SECTION_METADATA.md (should be implemented first)  
**Blocks:** None (can be implemented independently but enhances search UX)