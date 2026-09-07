# 15 — TECHNICAL SEO + GEO + AEO + PERFORMANCE DEVELOPER CHECKLIST

**Section:** Technical Implementation Requirements  
**Priority:** P0  
**Type:** Developer Handoff  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides technical requirements without removing existing functionality.**

---

## Metadata Requirements

### Essential Elements
- [ ] One unique `<title>` tag
- [ ] One meta description
- [ ] Self-referencing canonical for /jobs
- [ ] `index,follow` robots directive
- [ ] Correct `lang` attribute
- [ ] Open Graph metadata
- [ ] Twitter/X metadata
- [ ] Correct 200 status
- [ ] No accidental noindex
- [ ] No duplicate canonical

### Recommended Metadata
**Title:** `Government Jobs 2026 – Latest Sarkari Naukri & Govt Jobs`  
**Description:** `Find the latest Government Jobs 2026 and Sarkari Naukri in India. Browse active govt vacancies by qualification, department, state, district and exam.`  
**Canonical:** `https://www.searchsarkarinaukri.com/jobs`

---

## Structured Data Requirements

### /jobs Page Structure
**Use where appropriate:**
- [ ] WebPage schema
- [ ] BreadcrumbList schema
- [ ] ItemList for visible listings (if implemented correctly)

**Do NOT mark the entire hub as one JobPosting.**

### Individual Recruitment Pages
**Use JobPosting only when:**
- [ ] Page is genuinely a job/recruitment posting
- [ ] All required/appropriate properties are accurate
- [ ] All data is visible to users

**Potential fields:**
- [ ] title
- [ ] description
- [ ] datePosted
- [ ] validThrough
- [ ] employmentType
- [ ] hiringOrganization
- [ ] jobLocation
- [ ] baseSalary (when known)
- [ ] identifier
- [ ] educationRequirements
- [ ] qualifications
- [ ] applicationContact/directApply (where applicable)

**Never fabricate missing values.**

### FAQ Schema
**FAQPage markup should only be used if:**
- [ ] Current Google eligibility rules allow it
- [ ] Content meets Google's requirements at implementation time
- [ ] FAQ content is genuinely helpful and accurate

---

## Faceted Navigation Strategy

### Avoid Indexable URL Explosion
**Potential non-indexable combinations:**
- [ ] Search parameters
- [ ] Arbitrary multi-filter combinations
- [ ] Sort parameters
- [ ] Tracking parameters

**Examples to avoid indexing:**
- `?sort=deadline`
- `?qualification=12th&location=pune`
- `?utm_source=...`

### Promote Only Curated Landing Pages
**Curated pages should have:**
- [ ] Real inventory (minimum 10-20 jobs)
- [ ] Unique useful content
- [ ] Sustained search demand
- [ ] Internal link support

---

## Pagination Requirements

### Crawlable Pagination
- [ ] `/jobs?page=2` is crawlable
- [ ] Every page has unique accessible jobs
- [ ] Pagination links are real `<a>` links
- [ ] No JS-only dependency for discovering jobs
- [ ] Canonical strategy is deliberate (self-referencing per page)

---

## Job Lifecycle Management

### Status System
**Required statuses:**
- [ ] Upcoming
- [ ] Open
- [ ] Closing Soon
- [ ] Closed
- [ ] Result Published
- [ ] Archived

### Expiry Handling
**When validThrough passes:**
- [ ] Status becomes Closed
- [ ] Active inventory count decreases
- [ ] Detail page remains available if useful
- [ ] Page links to related jobs/results/admit card where relevant

---

## Date UX Requirements

### Replace Poor UX
**Replace:**
- [ ] "0 days left" → "Closes Today"
- [ ] "1 day left" → "Closes Tomorrow"

**Use correct India timezone** for deadline calculations when source specifies it.

---

## Data Quality Requirements

### Clean Up Data Issues
- [ ] Remove `[email protected]` artefacts
- [ ] Remove broken HTML fragments
- [ ] Validate organisation names
- [ ] Validate vacancy counts
- [ ] Validate application dates
- [ ] Validate location data
- [ ] Validate qualification data
- [ ] Store official source URL
- [ ] Store last verified/checked date (when actual)

---

## SEO-Friendly Data Model

### Required Fields
```javascript
job: {
  job_id: "unique_id",
  title: "Organisation Recruitment 2026 – Role",
  organisation: "Organisation Name",
  organisation_type: "State Government",
  department: "Railway",
  category: "Engineering",
  qualification: ["Diploma", "Engineering"],
  country: "India",
  state: "Maharashtra",
  district: "Pune",
  city: "Pune",
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

---

## GEO / AI-Answer Readiness

### Explicit Entity Labels
**Expose facts in explicit labels:**
- [ ] Organisation:
- [ ] Recruitment:
- [ ] Post:
- [ ] Location:
- [ ] Qualification:
- [ ] Age Limit:
- [ ] Vacancies:
- [ ] Salary:
- [ ] Application Start:
- [ ] Last Date:
- [ ] Application Mode:
- [ ] Official Notification:
- [ ] Official Website:
- [ ] Status:
- [ ] Updated:

**Benefit:** Creates clean entity relationships for search engines and AI systems.

---

## AEO Requirements

### Question-Answer Format
**For FAQs and explainer sections:**
- [ ] Question → answer in first sentence → optional detail
- [ ] Do not make answers dependent on clicking filters
- [ ] Keep answers short and direct
- [ ] Make content self-contained where possible

---

## Core Web Vitals Requirements

### LCP (Largest Contentful Paint)
- [ ] Server-render H1, intro and first job cards
- [ ] Optimize hero assets
- [ ] Avoid oversized above-fold imagery
- [ ] Target: < 2.5 seconds

### CLS (Cumulative Layout Shift)
- [ ] Set image dimensions
- [ ] Reserve ad/banner space
- [ ] Reserve filter/card layout space
- [ ] Target: < 0.1

### INP (Interaction to Next Paint)
- [ ] Debounce search input
- [ ] Avoid expensive filter recomputation on every keystroke
- [ ] Use efficient state management
- [ ] Do not block the main thread
- [ ] Target: < 200 milliseconds

---

## Image Requirements

### Format and Performance
- [ ] Use WebP/AVIF format
- [ ] Lazy load below fold
- [ ] Explicit width/height attributes
- [ ] Avoid decorative image per job card

### Image SEO
**Filename example:** `government-jobs-2026-search-sarkari-naukri.webp`  
**ALT example:** `Government Jobs 2026 on Search Sarkari Naukri`

**Do not keyword-stuff ALT attributes.**

---

## Accessibility Requirements

### Semantic HTML
- [ ] Use semantic `<main>`
- [ ] Use semantic `<section>`
- [ ] Use semantic `<article>` for jobs
- [ ] Use real headings (H1-H6)
- [ ] Use visible labels
- [ ] Ensure keyboard support
- [ ] Ensure visible focus states
- [ ] Use sufficient contrast
- [ ] Use real anchors (not clickable divs)
- [ ] Announce status changes

---

## Indexing QA Requirements

### After Deployment
- [ ] Submit sitemap to Google Search Console
- [ ] Inspect /jobs in Search Console
- [ ] Inspect representative category URLs
- [ ] Inspect representative job URLs
- [ ] Check canonical tags
- [ ] Check rendered HTML
- [ ] Check structured-data validation
- [ ] Check 404/redirect chains
- [ ] Check crawl stats
- [ ] Check index coverage
- [ ] Monitor for 4-6 weeks

---

## Security / Quality Requirements

### Data Safety
- [ ] Sanitize user search input
- [ ] Escape dynamic job text
- [ ] Protect external links from unsafe injection
- [ ] Validate source URLs
- [ ] Avoid exposing internal IDs unnecessarily
- [ ] Avoid exposing sensitive source data

---

## Implementation Steps

### Phase 1: Metadata and Structure
1. Implement title, meta description, canonical
2. Add Open Graph and Twitter metadata
3. Implement breadcrumb navigation
4. Add semantic HTML structure
5. Test with SEO tools

### Phase 2: Structured Data
1. Add WebPage schema
2. Add BreadcrumbList schema
3. Add ItemList schema (if appropriate)
4. Add JobPosting schema on individual pages
5. Validate with Rich Results Test

### Phase 3: Technical Foundation
1. Implement crawlable pagination
2. Add job lifecycle management
3. Fix data quality issues
4. Implement date UX improvements
5. Add faceted navigation strategy

### Phase 4: Performance and Accessibility
1. Optimize Core Web Vitals
2. Implement image optimization
3. Add accessibility features
4. Test with PageSpeed Insights
5. Test with accessibility tools

### Phase 5: GEO/AEO Implementation
1. Add explicit entity labels
2. Implement question-answer format
3. Add AEO-optimized content
4. Test with answer engine validation
5. Monitor AI search performance

---

## Validation Checklist

### Metadata
- [ ] Title tag optimized
- [ ] Meta description optimized
- [ ] Canonical tag correct
- [ ] Open Graph metadata complete
- [ ] Twitter metadata complete
- [ ] Language attribute correct
- [ ] Robots meta tag correct

### Structured Data
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] JobPosting schema on individual pages
- [ ] FAQ schema (if eligible)
- [ ] Schema validation passed
- [ ] No duplicate schema types

### Technical
- [ ] Pagination crawlable
- [ ] Job lifecycle working
- [ ] Data quality issues fixed
- [ ] Date UX improved
- [ ] Faceted navigation strategy implemented

### Performance
- [ ] LCP under 2.5s
- [ ] CLS under 0.1
- [ ] INP under 200ms
- [ ] Images optimized
- [ ] No render-blocking resources

### Accessibility
- [ ] Semantic HTML used
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] Contrast sufficient
- [ ] Screen reader friendly

### Security
- [ ] Input sanitization implemented
- [ ] XSS protection in place
- [ ] External links safe
- [ ] Sensitive data protected

---

## Developer Notes

1. **React Implementation:** Use framework-specific SEO solutions (Next.js metadata, React Helmet, etc.)
2. **Performance:** Monitor Core Web Vitals continuously, optimize iteratively
3. **Accessibility:** Test with screen readers and keyboard navigation
4. **Security:** Validate all user inputs and external data
5. **Monitoring:** Set up ongoing performance and SEO monitoring

---

## Success Metrics

- [ ] Improved Core Web Vitals scores
- [ ] Better Google Search Console coverage
- [ ] Enhanced structured data visibility
- [ ] Improved accessibility scores
- [ ] Better security posture
- [ ] Faster page load times

---

**Last Updated:** 4 September 2026  
**Dependencies:** All section files  
**Blocks:** None (developer handoff)