# 23 — PROGRAMMATIC SEO GUARDRAILS

**Section:** Automated Page Generation Rules  
**Priority:** P1  
**Type:** Technical SEO  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides programmatic SEO rules without removing existing functionality.**

---

## Goal

Prevent creation of low-quality or duplicate pages through automated generation, ensuring only valuable, intent-driven pages become indexable.

---

## Core Principle

**Do not automatically create an indexable page for every possible combination.**

---

## Page Generation Guardrails

### Requirement 1: Real Inventory Threshold

**Minimum Requirements for Indexable Page:**

| Page Type | Minimum Active Jobs | Minimum Content |
|-----------|-------------------|------------------|
| Qualification landing page | 10+ active jobs | 500+ unique words |
| State landing page | 20+ active jobs | 500+ unique words |
| City/District landing page | 5+ active jobs | 300+ unique words |
| Department landing page | 10+ active jobs | 500+ unique words |
| Exam landing page | N/A (if exam exists) | 800+ unique words |
| Combined filter page | 15+ active jobs | 800+ unique words |

**Rule:** Below these thresholds, keep page non-indexable or don't create at all.

---

### Requirement 2: Unique Intent Validation

**Each Page Must Have:**
- [ ] Distinct search intent
- [ ] Unique value proposition
- [ ] Different target audience
- [ ] Different keyword focus
- [ ] Different user journey

**Examples of Valid Intent:**
- "government jobs for 12th pass" → Qualification-focused
- "government jobs in Maharashtra" → Location-focused
- "railway government jobs" → Department-focused

**Examples of Invalid Intent:**
- "government jobs in Pune for 12th pass in railway" → Too specific, low demand
- "government jobs with salary 20000" → Not a primary user intent
- "government jobs for married females" → Too narrow

---

### Requirement 3: Unique Content Mandate

**Each Indexable Page Must Have:**
- [ ] Unique title (not duplicate of other pages)
- [ ] Unique H1 (not duplicate of other pages)
- [ ] Unique meta description
- [ ] Unique introductory content
- [ ] Unique section content
- [ ] Unique FAQ where applicable

**Content Similarity Check:**
- Title similarity < 70%
- H1 similarity < 60%
- Content similarity < 50%
- No duplicate content blocks > 200 words

---

### Requirement 4: Sufficient Job Listings

**Job Count Validation:**
```javascript
function validateJobCount(pageType, jobCount) {
  const thresholds = {
    qualification: 10,
    state: 20,
    city: 5,
    department: 10,
    combined: 15
  };
  
  return jobCount >= (thresholds[pageType] || 10);
}
```

**Job Quality Check:**
- [ ] Jobs must be currently active (not expired)
- [ ] Jobs must be from valid organisations
- [ ] Jobs must have complete information
- [ ] Jobs must be from legitimate sources

---

### Requirement 5: Unique Metadata

**Automated Metadata Generation:**
```javascript
function generateMetadata(pageData) {
  return {
    title: generateUniqueTitle(pageData),
    description: generateUniqueDescription(pageData),
    h1: generateUniqueH1(pageData),
    canonical: generateCanonical(pageData)
  };
}
```

**Duplicate Prevention:**
- Check database for similar titles
- Check database for similar H1s
- Auto-append year or modifier if duplicate detected
- Manually review potential duplicates

---

### Requirement 6: Internal Linking Validation

**Each Indexable Page Must Have:**
- [ ] Internal link from /jobs or hub page
- [ ] Internal link to related category pages
- [ ] Internal link to relevant tool pages
- [ ] Internal link to related resources
- [ ] Minimum 3 internal links total

**Orphan Page Prevention:**
- Automatically add internal links during page creation
- Link from parent category pages
- Link from related qualification/location pages
- Link from job cards when relevant

---

### Requirement 7: Meaningful User Demand

**Search Volume Validation:**
- Check Keyword Planner for search volume
- Check Search Console for historical queries
- Validate demand before page creation
- Minimum threshold: 50+ monthly searches (varies by category)

**User Intent Validation:**
- Check if users actually search for this combination
- Analyze Search Console query data
- Review competitor pages for similar intent
- Skip pages with no demonstrated demand

---

## Guardrail Implementation

### Pre-Creation Validation

```javascript
function validatePageCreation(pageData) {
  const validations = [
    validateJobCount(pageData.type, pageData.jobCount),
    validateUniqueIntent(pageData.intent),
    validateUniqueContent(pageData.content),
    validateUserDemand(pageData.keywords),
    validateInternalLinks(pageData.links),
    validateMetadata(pageData.metadata)
  ];
  
  if (validations.every(v => v.passed)) {
    return { approved: true };
  } else {
    return { 
      approved: false, 
      reasons: validations.filter(v => !v.passed).map(v => v.reason)
    };
  }
}
```

---

### Page Quality Scoring

**Quality Score Components:**
```javascript
function calculateQualityScore(pageData) {
  let score = 0;
  
  // Job count (max 25 points)
  score += Math.min(pageData.jobCount * 2, 25);
  
  // Content length (max 20 points)
  score += Math.min(pageData.contentLength / 50, 20);
  
  // Unique content (max 15 points)
  score += pageData.contentUniqueness * 15;
  
  // Internal links (max 10 points)
  score += Math.min(pageData.internalLinks * 2, 10);
  
  // User demand (max 20 points)
  score += pageData.searchVolume * 2;
  
  // Metadata quality (max 10 points)
  score += pageData.metadataQuality * 10;
  
  return score;
}
```

**Minimum Score for Indexing:** 60/100

---

## Automated Page Generation Rules

### ALLOWED Automated Generation

**Qualification Pages:**
- Generate for: 10th, 12th, ITI, Diploma, Graduate, Engineering
- Only if: 10+ active jobs + unique content + user demand
- Example: `/government-jobs/12th-pass`

**State Pages:**
- Generate for: Maharashtra, and other states with 20+ jobs
- Only if: 20+ active jobs + unique content + user demand
- Example: `/government-jobs/maharashtra`

**Department Pages:**
- Generate for: Railway, Banking, Police, Teaching, Defence
- Only if: 10+ active jobs + unique content + user demand
- Example: `/government-jobs/railway`

**City Pages:**
- Generate for: Cities with 5+ jobs (Pune, Mumbai, Nagpur, etc.)
- Only if: 5+ active jobs + unique content + user demand
- Example: `/government-jobs/maharashtra/pune`

---

### PROHIBITED Automated Generation

**Combined Filter Pages:**
- ❌ `/government-jobs/12th-pass-in-pune-in-railway`
- ❌ `/government-jobs/graduate-maharashtra-banking-experience`
- ❌ `/government-jobs/fresher-pune-software-government`

**Low-Volume Combinations:**
- ❌ Pages with < 5 jobs
- ❌ Pages with < 50 monthly searches
- ❌ Pages with overlapping intent

**Over-Specific Pages:**
- ❌ Pages for single job listings
- ❌ Pages for very narrow demographics
- ❌ Pages for rare qualification combinations

---

## Manual Review Requirements

### Require Manual Review For:

**High-Impact Pages:**
- State landing pages (Maharashtra, etc.)
- Major department pages (Railway, Banking)
- New qualification categories
- High-traffic location pages

**Borderline Cases:**
- Pages with quality score 50-60
- Pages with marginal user demand
- Pages with similar intent to existing pages
- Pages with potential cannibalisation

**New Page Types:**
- Any new category of page
- Experimental page structures
- Pages targeting new keyword clusters

---

## Content Quality Standards

### Minimum Content Requirements

**Qualification Page (500+ words):**
- Introduction to qualification
- Types of jobs available
- Typical departments recruiting
- Eligibility requirements
- Application process
- Career progression
- FAQ section

**State Page (500+ words):**
- State government overview
- Major departments in state
- State-specific qualifications
- Application process
- Important dates
- District-wise opportunities
- FAQ section

**Department Page (500+ words):**
- Department overview
- Types of roles
- Qualification requirements
- Career progression
- Exam information
- Salary structure
- FAQ section

---

## Expiry and Archival Rules

### When Jobs Expire

**Keep Page If:**
- Page has other active jobs
- Page has historical value
- Page receives traffic
- Page serves as hub for related content

**Update Page If:**
- Job count drops below threshold
- Content becomes outdated
- User demand decreases significantly
- Better page exists for same intent

**Archive Page If:**
- Page has zero active jobs
- Page receives no traffic
- Page serves no current purpose
- No historical value

---

## Implementation Steps

### Step 1: Guardrail System Setup
1. Implement validation functions
2. Create quality scoring system
3. Set up pre-creation checks
4. Configure manual review triggers
5. Test guardrail system

### Step 2: Page Generation Logic
1. Define allowed page types
2. Set inventory thresholds
3. Configure content requirements
4. Implement metadata generation
5. Add internal linking logic

### Step 3: Monitoring System
1. Track page quality scores
2. Monitor page performance
3. Identify low-performing pages
4. Flag pages for review/removal
5. Update guardrails based on data

### Step 4: Content Quality System
1. Create content templates
2. Implement uniqueness checks
3. Add content length validation
4. Configure FAQ generation
5. Set up editorial review process

### Step 5: Maintenance Process
1. Regular page audits
2. Remove low-quality pages
3. Update underperforming pages
4. Merge similar pages
5. Refine guardrail rules

---

## Validation Checklist

### Guardrail System
- [ ] Validation functions implemented
- [ ] Quality scoring system working
- [ ] Pre-creation checks active
- [ ] Manual review triggers configured
- [ ] Guardrail system tested

### Page Generation
- [ ] Only allowed page types generated
- [ ] Inventory thresholds enforced
- [ ] Content requirements met
- [ ] Metadata generation working
- [ ] Internal linking automated

### Content Quality
- [ ] Minimum content length enforced
- [ ] Uniqueness checks working
- [ ] Duplicate content prevented
- [ ] Content templates implemented
- [ ] Editorial review process

### Monitoring
- [ ] Quality scores tracked
- [ ] Page performance monitored
- [ ] Low-performing pages identified
- [ ] Review/removal process active
- [ ] Guardrails refined regularly

---

## Developer Notes

1. **Validation Logic:** Implement comprehensive validation before page creation
2. **Quality Scoring:** Use data-driven quality assessment
3. **Manual Review:** Set up efficient manual review workflow
4. **Monitoring:** Automate monitoring and alerting
5. **Iteration:** Continuously refine guardrails based on performance

---

## Success Metrics

- [ ] Zero low-quality programmatic pages indexed
- [ ] Reduced duplicate content issues
- [ ] Better average page quality scores
- [ ] Improved user engagement on generated pages
- [ ] Higher conversion rates
- [ ] Reduced maintenance overhead

---

## Common Guardrail Violations

### Violation 1: Insufficient Inventory
**Problem:** Page created with only 2-3 jobs  
**Solution:** Implement minimum job count threshold

### Violation 2: Duplicate Content
**Problem:** Multiple pages with similar content  
**Solution:** Implement content uniqueness checks

### Violation 3: No User Demand
**Problem:** Page created for keywords nobody searches  
**Solution:** Implement search volume validation

### Violation 4: Poor Internal Linking
**Problem:** Orphan pages with no internal links  
**Solution:** Automate internal linking during creation

### Violation 5: Low Quality Content
**Problem:** Thin or generic content  
**Solution:** Implement minimum content length and quality requirements

---

**Last Updated:** 4 September 2026  
**Dependencies:** 22_INDEXING_CRAWL_CONTROL.md  
**Status:** Implementation Ready