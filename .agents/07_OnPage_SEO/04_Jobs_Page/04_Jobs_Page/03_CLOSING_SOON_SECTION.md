# 03 — GOVERNMENT JOBS CLOSING SOON SECTION

**Section:** Deadline-Focused Job Block  
**Priority:** P0  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Capture deadline intent while helping users avoid missed applications by highlighting jobs with upcoming deadlines.

---

## H2 Heading

```html
<h2>Government Jobs Closing Soon</h2>
```

---

## Introduction Copy

```
Looking for government recruitment with an upcoming deadline? Browse active vacancies that are closing soon and check the official notification before applying.
```

---

## Dynamic Deadline Groups

### Suggested Grouping Logic

**Group 1: Closes Today**
- Jobs with deadline = today
- Display: "Closes Today"

**Group 2: Closes Tomorrow**  
- Jobs with deadline = tomorrow
- Display: "Closes Tomorrow"

**Group 3: Closing Within 3 Days**
- Jobs with deadline in 1-3 days
- Display: "2 days left", "3 days left"

**Group 4: Closing This Week**
- Jobs with deadline in 4-7 days
- Display: "Closing This Week"

### UX Rules

**DO NOT show:**
- "0 days left" → Use "Closes Today" instead
- Negative numbers → Use "Closed" instead

**DO show:**
- Clear, actionable deadline language
- Days remaining (not just date)
- Urgency indicators appropriately

---

## Job Card Fields for Closing Soon Section

Each job card should contain:

```html
<article class="job-card closing-soon">
  <h3>Organisation Recruitment 2026 – Vacancy Title</h3>
  <p>Organisation name</p>
  <dl>
    <dt>Location</dt><dd>...</dd>
    <dt>Qualification</dt><dd>...</dd>
    <dt>Vacancies</dt><dd>...</dd>
    <dt>Last Date</dt><dd>...</dd>
    <dt>Status</dt><dd>Open</dt>
  </dl>
  <a href="/jobs/example">View Job Details</a>
</article>
```

**Required Data:**
- Exact recruitment title
- Organisation
- Location
- Qualification
- Vacancies
- Last date (with urgency indicator)
- Status
- View Details link

---

## Long-Tail Semantic Targets

**Keywords to target naturally:**
- government jobs closing soon
- government jobs last date
- govt jobs closing today
- government job last date
- latest government jobs apply online
- government jobs ending this week

**Implementation:** Use these naturally in copy and meta, don't force keyword stuffing.

---

## UX Recommendations

### Section Placement
- Position after search/filters
- Before main "Latest Government Jobs" section
- Make visually distinct (urgency styling)

### Job Count
- Show 6-10 high-value jobs
- Link to complete filtered inventory: "View All Closing Soon Government Jobs"
- Update dynamically as deadlines change

### Visual Indicators
- Use color coding for urgency (red/orange for closing today/tomorrow)
- Add countdown badges where appropriate
- Make deadline information prominent

### Mobile Optimization
- Show most urgent jobs first on mobile
- Use compact card format
- Ensure "View Details" buttons are thumb-friendly

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after search/filters
2. Add introduction copy
3. Create container for deadline-grouped jobs
4. Style to match existing design

### Step 2: Implement Deadline Logic
1. Create backend logic to group jobs by deadline
2. Implement timezone-aware deadline calculations
3. Handle edge cases (midnight deadlines, timezone differences)
4. Update groups dynamically as deadlines pass

### Step 3: Build Job Cards
1. Create compact job card template for closing soon
2. Include all required data fields
3. Add urgency indicators
4. Ensure proper semantic HTML

### Step 4: Add Dynamic Updates
1. Implement real-time deadline updates
2. Automatically move jobs between groups as deadlines approach
3. Remove jobs that have closed from this section
4. Add new jobs as they enter closing-soon window

### Step 5: Add CTA Link
1. Add "View All Closing Soon Government Jobs" link
2. Link to filtered view: `/jobs?deadline=closing-soon`
3. Ensure proper canonical and noindex strategy
4. Test link functionality

### Step 6: Mobile Optimization
1. Test on various mobile devices
2. Optimize card layout for small screens
3. Ensure touch targets are appropriate size
4. Test horizontal scrolling if needed

---

## Backend Requirements

### Deadline Calculation Logic
```javascript
function getDeadlineGroup(deadlineDate) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  
  const deadline = new Date(deadlineDate);
  deadline.setHours(23, 59, 59, 999);
  
  const diffTime = deadline - today;
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  if (diffDays === 0) return 'Closes Today';
  if (diffDays === 1) return 'Closes Tomorrow';
  if (diffDays <= 3) return `${diffDays} days left`;
  if (diffDays <= 7) return 'Closing This Week';
  return null; // Not in closing-soon window
}
```

### Data Requirements
- Accurate deadline dates for all jobs
- Timezone handling (IST for India-focused site)
- Real-time updates as deadlines pass
- Archive handling for closed jobs

---

## Validation Checklist

- [ ] H2 heading added after search/filters
- [ ] Introduction copy added
- [ ] Deadline grouping logic implemented
- [ ] "0 days left" replaced with "Closes Today"
- [ ] Job cards contain all required fields
- [ ] Urgency indicators working correctly
- [ ] Dynamic updates functioning
- [ ] CTA link to filtered view working
- [ ] Mobile layout tested and optimized
- [ ] Timezone handling correct
- [ ] No broken deadline calculations
- [ ] Closed jobs removed automatically
- [ ] Performance acceptable (dynamic updates)
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Use existing job card components, add deadline-specific styling
2. **Performance:** Use efficient date calculations, avoid expensive operations on every render
3. **Timezones:** Use India Standard Time (IST) consistently for deadline calculations
4. **Caching:** Cache deadline groups, update periodically rather than on every request
5. **Edge Cases:** Handle leap years, month boundaries, DST changes (though IST doesn't observe DST)

---

## Success Metrics

- [ ] Users successfully find closing-soon jobs
- [ ] Reduced missed applications (user feedback)
- [ ] Higher engagement with closing-soon section
- [ ] Improved deadline awareness
- [ ] No performance degradation
- [ ] Positive user feedback on urgency indicators

---

## AEO Enhancement

### Question-Answer Format

**Question:** Which government jobs are closing soon?

**Answer:** Browse the Government Jobs Closing Soon section to view active vacancies with application deadlines approaching within the next week. Check the official notification and apply before the deadline.

**Implementation:** Add this as schema markup or helper text.

---

## SEO Considerations

### Canonical Strategy
- Section is part of `/jobs` page → canonical to `/jobs`
- Filtered view `/jobs?deadline=closing-soon` → self-canonical with noindex,follow

### Internal Linking
- Link from individual job pages back to closing-soon section
- Link from other sections to closing-soon when relevant
- Use descriptive anchor text: "government jobs closing soon"

---

**Last Updated:** 4 September 2026  
**Dependencies:** 01_HERO_SECTION_METADATA.md, 02_SEARCH_FILTERS_SECTION.md  
**Blocks:** None (can be implemented independently)