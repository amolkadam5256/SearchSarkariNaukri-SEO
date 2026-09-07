# 20 — JOB POSTING SCHEMA IMPLEMENTATION

**Section:** Structured Data for Job Listings  
**Priority:** P1  
**Type:** Technical Implementation  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides schema implementation without removing existing functionality.**

---

## Critical Distinction

### /jobs Hub Page
**DO NOT USE JobPosting schema for the entire listing page.**

**Use instead:**
- WebPage schema
- BreadcrumbList schema
- ItemList schema (only if implemented correctly)

### Individual Job Detail Pages
**USE JobPosting schema ONLY when:**
- Page represents a genuine job/recruitment posting
- All required/appropriate properties are accurate
- Data is visible to users
- No fabricated information

---

## JobPosting Schema Field Mapping

### Required Fields

#### title
**Source:** Job title  
**Schema Property:** `title`  
**Example:** `"MSRTC Solapur Recruitment 2026 – Driver/Conductor"`

#### description
**Source:** Job description/summary  
**Schema Property:** `description`  
**Example:** `"Apply for MSRTC Solapur Recruitment 2026. 306 vacancies for Driver and Conductor posts. Qualification: 10th/12th Pass. Last Date: 15 September 2026."`

#### datePosted
**Source:** Application start date  
**Schema Property:** `datePosted`  
**Format:** `YYYY-MM-DD`  
**Example:** `"2026-08-15"`

#### validThrough
**Source:** Application last date  
**Schema Property:** `validThrough`  
**Format:** `YYYY-MM-DD`  
**Example:** `"2026-09-15"`

**CRITICAL:** Use actual deadline from official notification, never calculate or invent.

#### hiringOrganization
**Source:** Organisation name  
**Schema Property:** `hiringOrganization`  
**Structure:**
```json
{
  "@type": "Organization",
  "name": "MSRTC Solapur",
  "sameAs": "https://msrtc.gov.in"
}
```

#### jobLocation
**Source:** Job location  
**Schema Property:** `jobLocation`  
**Structure:**
```json
{
  "@type": "Place",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Solapur",
    "addressRegion": "Maharashtra",
    "addressCountry": "IN"
  }
}
```

---

## Optional but Recommended Fields

#### employmentType
**Source:** Job type from notification  
**Schema Property:** `employmentType`  
**Values:** `FULL_TIME`, `PART_TIME`, `CONTRACT`, `TEMPORARY`  
**Example:** `"FULL_TIME"`

**Rule:** Use actual type from notification, omit if not specified. Never default to `FULL_TIME`.

#### baseSalary
**Source:** Salary information  
**Schema Property:** `baseSalary`  
**Structure:**
```json
{
  "@type": "MonetaryAmount",
  "currency": "INR",
  "value": {
    "@type": "QuantitativeValue",
    "value": "19900",
    "unitText": "MONTH"
  }
}
```

**Rule:** Only include if salary is specified in notification. Omit entirely if not known.

#### identifier
**Source:** Job ID/reference number  
**Schema Property:** `identifier`  
**Structure:**
```json
{
  "@type": "PropertyValue",
  "name": "MSRTC Job ID",
  "value": "MSRC-2026-306"
}
```

#### qualifications
**Source:** Required qualification  
**Schema Property:** `qualifications`  
**Example:** `"10th Pass, 12th Pass from recognized board"`

#### applicationContact
**Source:** Contact information  
**Schema Property:** `applicationContact`  
**Structure:**
```json
{
  "@type": "ContactPoint",
  "telephone": "+91-XXX-XXXXXXX",
  "email": "recruitment@msrtc.gov.in"
}
```

**Rule:** Only include if official contact details are available.

#### directApply
**Source:** Application URL  
**Schema Property:** `directApply`  
**Example:** `"https://msrtc.gov.in/apply/2026/driver-conductor"`

---

## Complete JobPosting Schema Example

```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "MSRTC Solapur Recruitment 2026 – Driver/Conductor",
  "description": "Apply for MSRTC Solapur Recruitment 2026. 306 vacancies for Driver and Conductor posts. Qualification: 10th/12th Pass. Last Date: 15 September 2026. Location: Solapur, Maharashtra.",
  "datePosted": "2026-08-15",
  "validThrough": "2026-09-15",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "MSRTC Solapur",
    "sameAs": "https://msrtc.gov.in"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Solapur",
      "addressRegion": "Maharashtra",
      "addressCountry": "IN"
    }
  },
  "baseSalary": {
    "@type": "MonetaryAmount",
    "currency": "INR",
    "value": {
      "@type": "QuantitativeValue",
      "value": "19900",
      "unitText": "MONTH"
    }
  },
  "employmentType": "FULL_TIME",
  "identifier": {
    "@type": "PropertyValue",
    "name": "MSRTC Job ID",
    "value": "MSRC-2026-306"
  },
  "qualifications": "10th Pass, 12th Pass from recognized board",
  "applicationContact": {
    "@type": "ContactPoint",
    "telephone": "+91-217-2330800",
    "email": "recruitment@msrtc.gov.in"
  },
  "directApply": "https://msrtc.gov.in/apply/2026/driver-conductor"
}
```

---

## /jobs Hub Page Schema

### WebPage Schema (Recommended)

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Government Jobs 2026 – Latest Sarkari Naukri & Govt Jobs",
  "description": "Find the latest Government Jobs 2026 and Sarkari Naukri in India. Browse active govt vacancies by qualification, department, state, district and exam.",
  "url": "https://www.searchsarkarinaukri.com/jobs",
  "datePublished": "2026-01-01",
  "dateModified": "2026-09-04",
  "publisher": {
    "@type": "Organization",
    "name": "Search Sarkari Naukri",
    "url": "https://www.searchsarkarinaukri.com"
  }
}
```

### BreadcrumbList Schema (Required)

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
    }
  ]
}
```

### ItemList Schema (Optional)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "url": "https://www.searchsarkarinaukri.com/jobs/123/msrtc-solapur-recruitment",
      "name": "MSRTC Solapur Recruitment 2026"
    }
  ]
}
```

**Rule:** Only use ItemList if you can accurately represent the job listings with proper URLs and names.

---

## Implementation Rules

### DO NOT

❌ Put one fake JobPosting representing the entire /jobs listing page  
❌ Fabricate salary information  
❌ Invent employment type (defaulting to FULL_TIME)  
❌ Calculate or invent validThrough dates  
❌ Add fields with "placeholder" or "TBD" values  
❌ Include JobPosting on /jobs hub page  
❌ Use approximate locations without verification

### DO

✅ Use JobPosting only on individual job detail pages  
✅ Use actual data from official notifications  
✅ Omit fields rather than fabricating values  
✅ Use exact dates from official sources  
✅ Include proper organisation information  
✅ Use accurate location data  
✅ Validate schema with Rich Results Test  
✅ Update schema when job information changes

---

## Schema Implementation Steps

### Step 1: Data Source Validation
1. Verify all job data comes from official notifications
2. Ensure data accuracy before schema generation
3. Validate dates, locations, and qualifications
4. Check for any discrepancies or updates

### Step 2: Schema Generation
1. Generate JobPosting schema for individual pages
2. Generate WebPage schema for /jobs hub
3. Generate BreadcrumbList for all pages
4. Implement ItemList where appropriate

### Step 3: Schema Testing
1. Test with Google Rich Results Test
2. Validate with Schema.org validator
3. Check for warnings and errors
4. Ensure no duplicate schema types

### Step 4: Dynamic Updates
1. Update schema when job information changes
2. Update validThrough when deadline passes
3. Remove schema when job is permanently closed
4. Add/update related schema fields

### Step 5: Monitoring
1. Monitor schema performance in Search Console
2. Track rich result appearances
3. Validate schema errors regularly
4. Update based on Google guideline changes

---

## Validation Checklist

### JobPosting Schema
- [ ] Used only on individual job pages
- [ ] Not used on /jobs hub page
- [ ] All required fields present
- [ ] Optional fields only when data available
- [ ] No fabricated information
- [ ] Accurate dates from official sources
- [ ] Correct organisation information
- [ ] Proper location data
- [ ] Valid employment type (or omitted)
- [ ] Accurate salary (or omitted)
- [ ] Tested with Rich Results Test
- [ ] No schema errors or warnings

### Hub Page Schema
- [ ] WebPage schema implemented
- [ ] BreadcrumbList schema implemented
- [ ] ItemList schema (if appropriate)
- [ ] No JobPosting on hub page
- [ ] Accurate page information
- [ ] Proper publisher information
- [ ] Validated with testing tools

---

## Developer Notes

1. **Data Accuracy:** Schema must match visible page content exactly
2. **Dynamic Generation:** Generate schema from database, not hardcoded
3. **Validation:** Test schema before deployment
4. **Monitoring:** Watch for schema errors in Search Console
5. **Updates:** Keep schema in sync with page content changes

---

## Common Schema Errors to Avoid

### Error 1: Fabricated Data
**Problem:** Adding fake salary or dates  
**Solution:** Omit field entirely if data not available

### Error 2: Wrong Page Type
**Problem:** JobPosting on /jobs hub page  
**Solution:** Use WebPage on hub, JobPosting on detail pages only

### Error 3: Incorrect Dates
**Problem:** Using wrong date format or calculated dates  
**Solution:** Use exact dates from official notification in YYYY-MM-DD format

### Error 4: Missing Required Fields
**Problem:** Missing title, description, or datePosted  
**Solution:** Ensure all required fields are present with accurate data

### Error 5: Duplicate Schema
**Problem:** Multiple JobPosting blocks on one page  
**Solution:** Use only one JobPosting per individual job page

---

## Success Metrics

- [ ] Rich results appear for individual job pages
- [ ] No schema errors in Search Console
- [ ] Improved click-through rates from rich results
- [ ] Better visibility in job search features
- [ ] Accurate job information displayed in search
- [ ] Zero schema validation errors

---

**Last Updated:** 4 September 2026  
**Dependencies:** 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md, 19_INDIVIDUAL_JOB_PAGE_SEO_AEO_GEO.md  
**Status:** Implementation Ready