# 21 — ENTITY / GEO ARCHITECTURE

**Section:** Entity Relationships for AI Search Optimization  
**Priority:** P1  
**Type:** Technical Architecture  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides entity architecture without removing existing functionality.**

---

## Goal

Establish clear, machine-readable entity relationships that help search engines, AI systems, and answer engines understand the connections between government jobs, organisations, locations, qualifications, and exams.

---

## Core Entity Hierarchy

### Primary Entity Structure

```
Search Sarkari Naukri (Platform)
        ↓
Government Jobs (Topic Hub)
        ↓
    [Multiple Entity Relationships]
```

---

## Detailed Entity Relationship Model

### Level 1: Platform Entity

**Search Sarkari Naukri**
```
Entity Type: Organization/WebSite
Properties:
- name: "Search Sarkari Naukri"
- url: "https://www.searchsarkarinaukri.com"
- description: "Government job information platform"
- publisher: "Search Sarkari Naukri"
- dateFounded: [Actual founding date]
- sameAs: [Social media profiles]
```

---

### Level 2: Topic Hub Entity

**Government Jobs**
```
Entity Type: WebPage/Topic
Properties:
- name: "Government Jobs"
- url: "https://www.searchsarkarinaukri.com/jobs"
- description: "Latest government job listings and recruitment information"
- about: "Government employment, Sarkari Naukri"
- keywords: ["government jobs", "sarkari naukri", "govt jobs"]
- dateModified: [Dynamic update date]
```

---

### Level 3: Organisation Entity

**Example: MSRTC**
```
Entity Type: GovernmentOrganization
Properties:
- name: "Maharashtra State Road Transport Corporation"
- alternateName: "MSRTC"
- url: "https://msrtc.gov.in"
- description: "State transport corporation for Maharashtra"
- address:
  - addressLocality: "Mumbai"
  - addressRegion: "Maharashtra"
  - addressCountry: "IN"
- foundingDate: [Actual founding date]
- sameAs: [Official website, Wikipedia]
```

---

### Level 4: Recruitment Entity

**Example: MSRTC Driver Recruitment 2026**
```
Entity Type: JobPosting
Properties:
- title: "MSRTC Solapur Recruitment 2026 – Driver/Conductor"
- description: "306 vacancies for Driver and Conductor posts"
- datePosted: "2026-08-15"
- validThrough: "2026-09-15"
- hiringOrganization: [Reference to MSRTC entity]
- jobLocation: [Reference to Solapur entity]
- qualifications: [Reference to qualification entities]
- employmentType: "FULL_TIME"
- baseSalary: [Salary information]
```

---

### Level 5: Job Role Entity

**Example: Driver Post**
```
Entity Type: Occupation
Properties:
- name: "Bus Driver"
- description: "Professional bus driver for public transport"
- skills: ["Driving", "License", "Transport"]
- qualifications: [Reference to 10th/12th pass entities]
- industry: "Transportation"
```

---

### Level 6: Qualification Entity

**Example: 10th Pass**
```
Entity Type: EducationalCredential
Properties:
- name: "10th Pass"
- description: "Secondary School Certificate (SSC) - Class 10"
- educationalLevel: "Secondary School"
- awardedBy: "State/Central Education Boards"
- typicalAge: "15-16 years"
```

---

### Level 7: Location Entity

**Example: Solapur, Maharashtra**
```
Entity Type: Place/City
Properties:
- name: "Solapur"
- description: "City in Maharashtra, India"
- address:
  - addressRegion: "Maharashtra"
  - addressCountry: "IN"
- containedInPlace: [Reference to Maharashtra entity]
- population: [Approximate population]
```

---

### Level 8: Department Entity

**Example: Transport Department**
```
Entity Type: GovernmentOrganization
Properties:
- name: "Transport Department"
- description: "Government department handling transport services"
- parentOrganization: [Reference to Maharashtra Government]
- jurisdiction: "Maharashtra State"
```

---

### Level 9: Exam Entity

**Example: MPSC Rajyaseva**
```
Entity Type: EducationalEvent
Properties:
- name: "MPSC Rajyaseva Examination"
- description: "Maharashtra State Civil Services Examination"
- organizer: [Reference to MPSC entity]
- startDate: [Exam date]
- endDate: [Exam end date]
- location: [Exam centers]
```

---

### Level 10: Official Notification Entity

**Example: MSRTC Recruitment PDF**
```
Entity Type: DigitalDocument
Properties:
- name: "MSRTC Recruitment Notification 2026"
- description: "Official recruitment notification PDF"
- url: [Official PDF URL]
- datePublished: [Notification release date]
- publisher: [Reference to MSRTC entity]
- fileFormat: "application/pdf"
```

---

## Complete Entity Relationship Example

### MSRTC Solapur Recruitment Full Entity Chain

```
Platform: Search Sarkari Naukri
    ↓
Topic: Government Jobs
    ↓
Organisation: MSRTC (Maharashtra State Road Transport Corporation)
    ↓
Department: Transport Department
    ↓
Recruitment: MSRTC Solapur Recruitment 2026
    ↓
Role: Driver, Conductor
    ↓
Location: Solapur → Maharashtra → India
    ↓
Qualification: 10th Pass, 12th Pass
    ↓
Salary: Level-2 (₹19,900-63,200)
    ↓
Important Dates: Application, Exam, Result
    ↓
Official Sources: Notification PDF, Official Website
    ↓
Related Entities: MPSC, Other Transport Jobs, Government Jobs in Solapur
```

---

## Structured Data Implementation

### Organization Schema for Platform

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Search Sarkari Naukri",
  "url": "https://www.searchsarkarinaukri.com",
  "description": "Government job information platform for India",
  "sameAs": [
    "https://www.facebook.com/searchsarkarinaukri",
    "https://twitter.com/searchsarkarinaukri"
  ]
}
```

### GovernmentOrganization Schema for Departments

```json
{
  "@context": "https://schema.org",
  "@type": "GovernmentOrganization",
  "name": "Maharashtra Public Service Commission",
  "alternateName": "MPSC",
  "url": "https://mpsc.gov.in",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Mumbai",
    "addressRegion": "Maharashtra",
    "addressCountry": "IN"
  }
}
```

### Place Schema for Locations

```json
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Solapur",
  "description": "City in Maharashtra, India",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "17.6766",
    "longitude": "75.8926"
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Solapur",
    "addressRegion": "Maharashtra",
    "addressCountry": "IN"
  }
}
```

---

## Knowledge Graph Optimization

### SameAs Links

**Every entity should have sameAs links to:**
- Official website
- Wikipedia page (if available)
- Social media profiles
- Official government portals

**Example:**
```json
"sameAs": [
  "https://msrtc.gov.in",
  "https://en.wikipedia.org/wiki/MSRTC",
  "https://www.facebook.com/msrtc.official"
]
```

---

## Entity Consistency Rules

### Naming Conventions
- Use official organisation names
- Use standard location names
- Use official exam names
- Use recognized qualification names
- Maintain consistency across all pages

### ID System
- Create unique IDs for each entity
- Use consistent ID format
- Reference entities by ID across schema
- Maintain entity database

---

## Implementation Steps

### Step 1: Entity Database Creation
1. Create entity database for organisations
2. Add location entities (state, district, city)
3. Add qualification entities
4. Add department entities
5. Add exam entities

### Step 2: Entity Relationship Mapping
1. Map jobs to organisations
2. Map jobs to locations
3. Map jobs to qualifications
4. Map jobs to departments
5. Map jobs to exams

### Step 3: Schema Implementation
1. Implement Organization schema for platform
2. Implement GovernmentOrganization for departments
3. Implement Place schema for locations
4. Implement EducationalCredential for qualifications
5. Link entities across all pages

### Step 4: Knowledge Graph Enhancement
1. Add sameAs links for all entities
2. Implement official source references
3. Add social media profiles
4. Link to Wikipedia where available
5. Maintain entity consistency

### Step 5: Ongoing Maintenance
1. Update entity information regularly
2. Add new entities as needed
3. Remove obsolete entities
4. Validate entity relationships
5. Monitor knowledge graph performance

---

## Validation Checklist

### Entity Database
- [ ] Organisation entities created
- [ ] Location entities created
- [ ] Qualification entities created
- [ ] Department entities created
- [ ] Exam entities created
- [ ] Unique ID system implemented
- [ ] Entity relationships mapped

### Schema Implementation
- [ ] Organization schema implemented
- [ ] GovernmentOrganization schema used
- [ ] Place schema implemented
- [ ] EducationalCredential schema used
- [ ] Entity references working
- [ ] sameAs links added

### Knowledge Graph
- [ ] Official source references
- [ ] Social media profiles linked
- [ ] Wikipedia connections where available
- [ ] Consistent naming conventions
- [ ] Entity relationships validated

---

## Developer Notes

1. **Entity Database:** Maintain a central entity database for consistency
2. **Dynamic Generation:** Generate schema from entity database
3. **ID System:** Use consistent, unique IDs for entity references
4. **Validation:** Regularly validate entity relationships
5. **Performance:** Optimize entity database queries

---

## Success Metrics

- [ ] Improved knowledge graph understanding
- [ ] Better entity recognition in search
- [ ] Enhanced AI search performance
- [ ] Accurate entity disambiguation
- [ ] Stronger topical authority signals
- [ ] Better rich result quality

---

## GEO/AEO Benefits

### Search Engine Benefits
- Clear entity relationships improve understanding
- Knowledge graph integration enhances authority
- Consistent entity naming reduces confusion
- Official source references build trust

### AI/Answer Engine Benefits
- Structured entities enable better extraction
- Clear relationships support question answering
- Consistent data improves accuracy
- Official references validate information

---

**Last Updated:** 4 September 2026  
**Dependencies:** 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md, 19_INDIVIDUAL_JOB_PAGE_SEO_AEO_GEO.md  
**Status:** Implementation Ready