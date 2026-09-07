# 19 — INDIVIDUAL JOB PAGE SEO + AEO + GEO

**Section:** Individual Job Detail Page Optimization  
**Priority:** P1  
**Type:** Implementation Specification  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides individual job page specification without removing existing functionality.**

---

## Goal

Create a comprehensive, production-ready specification for individual government job detail pages that can rank for long-tail keywords like "MSRTC Solapur Recruitment 2026" and provide excellent AEO/GEO signals.

---

## Required Page Elements

### SEO Metadata

#### Title Tag (Dynamic)
**Template:** `[Organisation] Recruitment 2026 – [Post Name] – [Vacancies] Vacancies`

**Example:** `MSRTC Solapur Recruitment 2026 – Driver/Conductor – 306 Vacancies`

**Character Count:** 60-70 characters optimal

#### Meta Description (Dynamic)
**Template:** `Apply for [Organisation] [Post Name] Recruitment [Year]. [Vacancies] vacancies available. Qualification: [Qualification]. Last Date: [Date]. Location: [Location]. Apply online before deadline.`

**Example:** `Apply for MSRTC Solapur Recruitment 2026. 306 vacancies available. Qualification: 10th/12th Pass. Last Date: 15 September 2026. Location: Solapur, Maharashtra. Apply online before deadline.`

**Character Count:** 150-160 characters optimal

#### Canonical Tag
**Template:** `https://www.searchsarkarinaukri.com/jobs/[job-id]/[slug]`

**Rule:** Self-referencing canonical for each individual job page

---

## HTML Structure

### Breadcrumb Navigation
```html
<nav aria-label="Breadcrumb">
  <a href="/">Home</a> → 
  <a href="/jobs">Government Jobs</a> → 
  <a href="/government-jobs/[department]">[Department]</a> → 
  <span>[Organisation] Recruitment 2026</span>
</nav>
```

### H1 (Dynamic)
**Template:** `[Organisation] Recruitment 2026 – [Post Name] – [Vacancies] Vacancies`

**Example:** `MSRTC Solapur Recruitment 2026 – Driver/Conductor – 306 Vacancies`

---

## Required Content Sections

### 1. Recruitment Overview

#### H2: Recruitment Overview

**Required Fields:**
- **Organisation:** [Organisation Name]
- **Recruitment Name:** [Recruitment Title]
- **Post Name:** [Position/Role]
- **Vacancies:** [Number of posts]
- **Location:** [State, District, City]
- **Qualification:** [Required education]
- **Age Limit:** [Age range with relaxations]
- **Salary:** [Pay scale/level]
- **Application Start Date:** [Start date]
- **Application Last Date:** [Deadline]
- **Selection Process:** [Exam stages]
- **Application Fee:** [Fee amount]
- **Application Mode:** [Online/Offline]

---

### 2. Important Dates

#### H2: Important Dates

**Table Format:**
| Event | Date |
|-------|------|
| Application Start Date | [Date] |
| Application Last Date | [Date] |
| Fee Payment Last Date | [Date] |
| Exam Date (if announced) | [Date] |
| Admit Card Release | [Date] |
| Result Declaration | [Date] |

---

### 3. Vacancy Details

#### H2: Vacancy Details

**Table Format:**
| Post | Vacancies | Qualification | Age Limit | Salary |
|------|-----------|---------------|-----------|--------|
| [Post 1] | [Number] | [Qualification] | [Age] | [Salary] |
| [Post 2] | [Number] | [Qualification] | [Age] | [Salary] |

---

### 4. Eligibility Criteria

#### H2: Eligibility Criteria

#### H3: Educational Qualification
```
[Candidate must have completed education from recognized university/board. Specific qualification requirements for each post are mentioned in the vacancy table.]
```

#### H3: Age Limit
```
[Minimum age: X years, Maximum age: Y years. Age relaxation applicable for reserved categories as per government rules.]
```

#### H3: Nationality
```
[Candidate must be Indian citizen. State domicile requirements where applicable.]
```

---

### 5. Application Fee

#### H2: Application Fee

**Table Format:**
| Category | Fee Amount |
|----------|------------|
| General/OBC | [Amount] |
| SC/ST | [Amount] |
| PWD | [Amount] |
| Female | [Amount] |

**Payment Methods:** [Online payment modes available]

---

### 6. How to Apply

#### H2: How to Apply

**Step-by-Step Instructions:**
1. Visit official website: [URL]
2. Click on recruitment notification link
3. Register with mobile number/email
4. Fill application form with correct details
5. Upload required documents
6. Pay application fee
7. Submit application and take printout

---

### 7. Required Documents

#### H2: Required Documents

**List:**
- Passport size photograph
- Signature
- Educational certificates
- Mark sheets
- Caste certificate (if applicable)
- PWD certificate (if applicable)
- ID proof (Aadhar/PAN)
- Experience certificate (if required)

---

### 8. Selection Process

#### H2: Selection Process

**Stages:**
1. [Stage 1 - e.g., Written Exam]
2. [Stage 2 - e.g., Physical Test]
3. [Stage 3 - e.g., Document Verification]
4. [Stage 4 - e.g., Medical Examination]

**Exam Pattern:** [Brief description of exam pattern if available]

---

### 9. Salary / Pay Scale

#### H2: Salary and Benefits

**Details:**
- **Pay Scale:** [Level/Grade]
- **Starting Salary:** [Amount]
- **Allowances:** [DA, HRA, TA etc.]
- **Other Benefits:** [PF, Pension, Medical etc.]

---

### 10. Official Links

#### H2: Official Links

**Required Links:**
- **Official Notification:** [PDF/Link]
- **Official Website:** [URL]
- **Apply Online:** [Application URL]
- **Advertisement:** [If separate]

---

### 11. Source Attribution

#### H2: Source Information

```
Source: [Official Organisation Name]
Last Updated: [Date when information was last verified]
Disclaimer: Candidates should verify all details from the official notification before applying.
```

---

### 12. FAQ Section (Job-Specific)

#### H2: Frequently Asked Questions

**Required Questions:**
- What is the last date for [Organisation] recruitment?
- What is the qualification for [Post]?
- How many vacancies in [Organisation] recruitment?
- What is the age limit for [Post]?
- How to apply for [Organisation] recruitment?
- What is the selection process?
- What is the application fee?
- When will the admit card be released?

---

### 13. Related Jobs

#### H2: Related Government Jobs

**Algorithm:** Show jobs matching:
- Same department
- Same qualification
- Same location
- Similar organisation

**Display:** 5-10 related job cards with titles, organisations, deadlines

---

### 14. Cross-Links

#### H2: More Opportunities

**Link to:**
- Government Jobs by [Qualification]
- Government Jobs in [Location]
- [Department] Jobs
- [Exam] Information
- Admit Cards
- Results

---

## AEO-Optimized Content Structure

### Question-Answer Format for Key Information

**Example:**
**Question:** What is the last date for MSRTC Solapur Recruitment 2026?

**Answer:** The last date for MSRTC Solapur Recruitment 2026 is 15 September 2026. Candidates must complete the application process before this deadline.

**Implementation:** Add structured Q&A pairs for critical information.

---

## GEO-Optimized Entity Block

### Standardized Entity Section

```html
<div class="entity-block">
  <h3>Recruitment Details</h3>
  <dl>
    <dt>Organisation:</dt><dd>MSRTC Solapur</dd>
    <dt>Recruitment:</dt><dd>Driver/Conductor Recruitment 2026</dd>
    <dt>Post:</dt><dd>Driver, Conductor</dd>
    <dt>Vacancies:</dt><dd>306</dd>
    <dt>Location:</dt><dd>Solapur, Maharashtra</dd>
    <dt>Qualification:</dt><dd>10th Pass, 12th Pass</dd>
    <dt>Age Limit:</dt><dd>18-30 years</dd>
    <dt>Salary:</dt><dd>Level-2 (₹19,900-63,200)</dd>
    <dt>Application Start:</dt><dd>15 August 2026</dd>
    <dt>Application Last:</dt><dd>15 September 2026</dd>
    <dt>Selection Process:</dt><dd>Written Test, Interview</dd>
    <dt>Application Mode:</dt><dd>Online</dd>
    <dt>Official Notification:</dt><dd>[Link]</dd>
    <dt>Official Website:</dt><dd>[Link]</dd>
    <dt>Status:</dt><dd>Open</dd>
    <dt>Last Updated:</dt><dd>4 September 2026</dd>
  </dl>
</div>
```

---

## Structured Data Implementation

### JobPosting Schema (Required)

```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "[Organisation] Recruitment 2026 – [Post]",
  "description": "[Job description]",
  "datePosted": "[Application Start Date]",
  "validThrough": "[Application Last Date]",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "[Organisation Name]",
    "sameAs": "[Official Website URL]"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "[City]",
      "addressRegion": "[State]",
      "addressCountry": "IN"
    }
  },
  "baseSalary": {
    "@type": "MonetaryAmount",
    "currency": "INR",
    "value": {
      "@type": "QuantitativeValue",
      "value": "[Salary Amount]",
      "unitText": "MONTH"
    }
  },
  "employmentType": "[FULL_TIME/PART_TIME/CONTRACT]",
  "identifier": {
    "@type": "PropertyValue",
    "name": "[Organisation] Job ID",
    "value": "[Job ID]"
  },
  "qualifications": "[Required qualification]",
  "applicationContact": {
    "@type": "ContactPoint",
    "telephone": "[Contact number if available]",
    "email": "[Email if available]"
  },
  "directApply": "[Application URL]"
}
```

**Critical Rules:**
- Only include fields where you have accurate data
- Never fabricate salary, dates, or qualifications
- Use real `validThrough` from official notification
- Use actual `employmentType` from notification
- If salary is not specified, omit the field entirely

---

## BreadcrumbList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.searchsarkarinaukri.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Government Jobs",
      "item": "https://www.searchsarkarinaukri.com/jobs"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Department]",
      "item": "https://www.searchsarkarinaukri.com/government-jobs/[department]"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "[Organisation] Recruitment 2026",
      "item": "https://www.searchsarkarinaukri.com/jobs/[job-id]/[slug]"
    }
  ]
}
```

---

## Expiry Handling

### When Application Deadline Passes

**Status Change:**
- Change status from "Open" to "Closed"
- Keep page live (don't 404)
- Add "Application Closed" badge
- Update `validThrough` in schema

**Content Updates:**
- Add "Result Published" section when results available
- Link to admit card page if available
- Link to result page if available
- Keep all original information for reference

**Canonical Strategy:**
- Keep same URL
- Update schema to reflect closed status
- Maintain page for historical reference

---

## Long-Tail Keyword Targeting

### Primary Long-Tail Keywords for Individual Pages

**Organisation-Specific:**
- [Organisation] recruitment 2026
- [Organisation] vacancy 2026
- [Organisation] jobs
- [Organisation] recruitment last date
- [Organisation] recruitment eligibility
- [Organisation] apply online

**Post-Specific:**
- [Post] government job
- [Post] vacancy [state]
- [Post] salary [state]
- [Post] qualification required

**Location-Specific:**
- government jobs in [city]
- [organisation] recruitment [city]
- [post] jobs [district]

**Qualification-Specific:**
- [qualification] government jobs [location]
- [organisation] recruitment for [qualification]

---

## Implementation Steps

### Step 1: Template Creation
1. Create individual job page template
2. Implement dynamic metadata generation
3. Add breadcrumb navigation
4. Create structured entity block

### Step 2: Content Sections
1. Add all required content sections
2. Implement AEO Q&A format
3. Add GEO entity structure
4. Create FAQ section

### Step 3: Structured Data
1. Implement JobPosting schema
2. Add BreadcrumbList schema
3. Validate with Rich Results Test
4. Ensure data accuracy

### Step 4: Cross-Linking
1. Add related jobs section
2. Link to qualification/state/department pages
3. Link to exam resources
4. Link to admit cards/results

### Step 5: Expiry Handling
1. Implement status change logic
2. Add result/admit card links
3. Update schema on expiry
4. Keep historical pages accessible

---

## Validation Checklist

- [ ] Dynamic title generation working
- [ ] Dynamic meta description working
- [ ] Self-referencing canonical tag
- [ ] Breadcrumb navigation implemented
- [ ] All required content sections present
- [ ] Entity block standardized
- [ ] JobPosting schema accurate
- [ ] BreadcrumbList schema implemented
- [ ] FAQ section job-specific
- [ ] Related jobs working
- [ ] Cross-links functional
- [ ] Expiry handling implemented
- [ ] No fabricated data in schema
- [ ] Mobile layout tested
- [ ] Accessibility verified

---

## Developer Notes

1. **Dynamic Data:** Ensure all job data comes from reliable source
2. **Schema Accuracy:** Never fabricate missing schema values
3. **URL Structure:** Maintain clean, descriptive URLs
4. **Performance:** Optimize page load for individual job pages
5. **Monitoring:** Track individual job page performance

---

## Success Metrics

- [ ] Individual job pages rank for long-tail keywords
- [ ] Users find specific recruitment information easily
- [ ] Reduced support queries about specific jobs
- [ ] Higher engagement with official source links
- [ ] Improved conversion to official applications
- [ ] Better schema visibility in search results

---

**Last Updated:** 4 September 2026  
**Dependencies:** 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md  
**Status:** Implementation Ready