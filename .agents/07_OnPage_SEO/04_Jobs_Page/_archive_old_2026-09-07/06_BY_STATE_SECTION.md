# 06 — GOVERNMENT JOBS BY STATE / DISTRICT SECTION

**Section:** Location-Based Discovery  
**Priority:** P1  
**Type:** Additive (New content section)  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This adds a new section without removing existing functionality.**

---

## Goal

Help users discover government jobs based on their preferred location with a focus on Maharashtra, while building a strong location-based internal linking structure.

---

## H2 Heading

```html
<h2>Government Jobs by State</h2>
```

---

## Introduction Copy

```
Find government recruitment opportunities by state, district and location. Choose a region to discover vacancies relevant to your preferred work location and eligibility.
```

---

## Priority Maharashtra Cluster

### Maharashtra Government Jobs
**Copy:** Explore current Maharashtra government recruitment across state departments, district offices, municipal organisations, universities, health services, police recruitment and other public organisations.

**Suggested URL:** `/government-jobs/maharashtra`

**Keyword Cluster:**
- Maharashtra government jobs
- government jobs in Maharashtra 2026
- Maharashtra sarkari naukri
- Maharashtra govt jobs

### Key District Pages (Create Only with Real Inventory)

#### Pune Government Jobs
**URL:** `/government-jobs/maharashtra/pune`
**Keywords:** government jobs in Pune, Pune government jobs, Pune sarkari naukri

#### Mumbai Government Jobs
**URL:** `/government-jobs/maharashtra/mumbai`
**Keywords:** government jobs in Mumbai, Mumbai government jobs, Mumbai sarkari naukri

#### Nagpur Government Jobs
**URL:** `/government-jobs/maharashtra/nagpur`
**Keywords:** government jobs in Nagpur, Nagpur government jobs

#### Nashik Government Jobs
**URL:** `/government-jobs/maharashtra/nashik`
**Keywords:** government jobs in Nashik, Nashik government jobs

#### Thane Government Jobs
**URL:** `/government-jobs/maharashtra/thane`
**Keywords:** government jobs in Thane, Thane government jobs

#### Solapur Government Jobs
**URL:** `/government-jobs/maharashtra/solapur`
**Keywords:** government jobs in Solapur, Solapur government jobs

**Rule:** Only publish/index a city/district landing page when it contains meaningful current inventory and unique information.

---

## Other State Examples

### Major States (Create Based on Demand and Inventory)
- Uttar Pradesh Government Jobs
- Rajasthan Government Jobs
- Madhya Pradesh Government Jobs
- Gujarat Government Jobs
- Karnataka Government Jobs
- Bihar Government Jobs
- Delhi Government Jobs
- Telangana Government Jobs
- Tamil Nadu Government Jobs
- Kerala Government Jobs

### All India Government Jobs
**Copy:** Find government recruitment opportunities open to eligible candidates across India.

**URL:** `/government-jobs/all-india`

---

## Existing Site Integration

### Link to Existing Districts Page
**Anchor:** Government Jobs by District  
**Destination:** `/districts`

**Implementation:** Keep the existing `/districts` page as the broad district discovery hub. Link to it from this section for comprehensive district coverage.

---

## Backend Location Model

### Required Data Structure
```javascript
location: {
  country: "India",
  state: "Maharashtra",
  district: "Pune",
  city: "Pune",
  controlled: true
}
```

### Implementation Rules
- Do not infer location from free text when structured source data exists
- Use hierarchical location data (country → state → district → city)
- Validate location data against official sources
- Handle cases where location is "All India" vs specific

---

## Long-Tail Location Keywords

### Target Keywords (Use on Landing Pages, Not on /jobs)
- government jobs in Maharashtra 2026
- government jobs in Pune this month
- government jobs in Mumbai for freshers
- latest government jobs in Nagpur
- government jobs near Pune
- government vacancies in Maharashtra
- district wise government jobs

**Rule:** Do not put all these phrases on /jobs. Use dedicated pages where useful.

---

## Landing Page Requirements

### Each Location Page Must Have:
1. **Real inventory** for that location
2. **Unique content** about that location
3. **Specific departments** active in that location
4. **Internal links** to related locations
5. **Proper metadata** (title, description, canonical)

### Page Structure Template:
```html
<h1>Maharashtra Government Jobs 2026</h1>
<p>Introduction about Maharashtra opportunities...</p>
<section>
  <h2>Latest Maharashtra Government Jobs</h2>
  [Job listings]
</section>
<section>
  <h2>Government Jobs by District in Maharashtra</h2>
  [District links]
</section>
<section>
  <h2>Major Recruiters in Maharashtra</h2>
  [Department information]
</section>
```

---

## Implementation Steps

### Step 1: Create Section Structure
1. Add H2 heading after qualification section
2. Add introduction copy
3. Create container for state/district blocks
4. Style to match existing design

### Step 2: Implement Location Taxonomy
1. Add hierarchical location data structure
2. Map existing location data to controlled values
3. Add validation for location data
4. Handle "All India" vs specific locations

### Step 3: Create Maharashtra Cluster
1. Create Maharashtra government jobs page
2. Create key district pages (Pune, Mumbai, etc.)
3. Add specific content for each location
4. Ensure proper internal linking

### Step 4: Add Other State Links
1. Add links to other major states
2. Create state pages based on demand/inventory
3. Add "All India" option
4. Link to existing `/districts` page

### Step 5: Implement Location-Based Internal Links
1. Link from /jobs to location pages
2. Link from location pages back to /jobs
3. Add cross-links between related locations
4. Use descriptive anchor text

### Step 6: Mobile Optimization
1. Test location blocks on mobile
2. Ensure location selection is intuitive
3. Optimize layout for small screens
4. Test location-based filtering

---

## Validation Checklist

- [ ] H2 heading added after qualification section
- [ ] Introduction copy added
- [ ] Maharashtra cluster created
- [ ] Key district pages created with real inventory
- [ ] Location taxonomy implemented
- [ ] Location data cleaned and standardized
- [ ] Link to existing /districts page maintained
- [ ] Internal linking structure implemented
- [ ] Proper metadata on location pages
- [ ] Mobile layout tested
- [ ] Location-based filtering working
- [ ] No existing functionality broken

---

## Developer Notes

1. **React Implementation:** Create reusable location block component
2. **Data Hierarchy:** Implement cascading location selection (state → district → city)
3. **Landing Pages:** Use template system for consistency across location pages
4. **Inventory Logic:** Only show locations with actual job inventory
5. **Performance:** Cache location counts, update periodically

---

## Success Metrics

- [ ] Location section engagement increases
- [ ] Traffic to location pages grows
- [ ] Users find relevant jobs by location
- [ ] Maharashtra cluster performs well
- [ ] Improved internal linking graph
- [ ] Positive user feedback on location discovery

---

## SEO Considerations

### Local SEO Strategy
- Target location-specific long-tail keywords
- Use descriptive anchor text for internal links
- Include location-specific information in content
- Add location-based FAQ sections

### Content Strategy
- Each location page should include local context
- Mention major employers in that location
- Include location-specific eligibility information
- Link to local resources and exam centers

---

## AEO Enhancement

### Question-Answer Format

**Question:** How can I find government jobs in Maharashtra?

**Answer:** Use the location filter to select Maharashtra or browse the Maharashtra Government Jobs page to view current state-level recruitment, district vacancies, and location-specific opportunities across state departments, municipal organisations, and public-sector employers.

**Implementation:** Add to location pages and FAQ section.

---

**Last Updated:** 4 September 2026  
**Dependencies:** 05_BY_QUALIFICATION_SECTION.md  
**Blocks:** None (can be implemented independently)