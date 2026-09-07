# 28 — KEYWORD TO SECTION INSERTION MAP

**Section:** Exact Keyword Placement Strategy  
**Priority:** P1  
**Type:** Strategic Documentation  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides keyword placement map without removing existing functionality.**

---

## Goal

Create an exact keyword-to-page-section-element mapping to ensure every important keyword is strategically placed in the most effective location for maximum SEO impact.

---

## Keyword Insertion Matrix

### Primary Keywords

| Keyword | Intent | Target Section | Exact Usage | Placement |
|---------|--------|---------------|-------------|----------|
| government jobs | Commercial/Informational | H1 | Primary | Title, H1, first 100 words |
| sarkari naukri | Informational | Intro | Secondary | Intro paragraph, body |
| latest government jobs | Freshness | Latest section | H2/body | H2 heading, section intro |
| government jobs 2026 | Freshness | H1/title/latest | Controlled | Title, H1, latest section |
| government jobs in India | Broad | Intro/state | Body | Intro paragraph |
| government jobs in Maharashtra | Local | State | H3/anchor | State H3, state link anchor |
| government jobs in Pune | Local | State/district | Anchor | District link anchor |
| government jobs for 10th pass | Qualification | Qualification | H3/anchor | Qualification H3, link anchor |
| government jobs for 12th pass | Qualification | Qualification | H3/anchor | Qualification H3, link anchor |
| government jobs for graduates | Qualification | Qualification | H3/anchor | Qualification H3, link anchor |
| government jobs for freshers | Qualification/user intent | Qualification/FAQ | FAQ | FAQ question/answer |
| government jobs near me | Local intent | FAQ/location | FAQ | FAQ question/answer |
| railway government jobs | Department | Department | Anchor | Department link anchor |
| police government jobs | Department | Department | Anchor | Department link anchor |
| government job vacancies | Transactional | Latest | Body | Latest section body |
| government job notifications | Informational | Latest/resources | Body | Latest/resources section |
| government job closing this week | Urgency | Closing Soon | Body | Closing Soon section |
| how to apply for a government job | AEO | How-to/FAQ | FAQ | FAQ question/answer |
| government job last date | AEO | Closing Soon/FAQ | FAQ | FAQ question/answer |

---

## Section-by-Section Keyword Placement

### H1 Section
**Primary Keyword:** `government jobs`
**Secondary Keywords:** `sarkari naukri`, `government jobs 2026`

**Implementation:**
```html
<h1>Government Jobs 2026 – Latest Active Sarkari Naukri</h1>
```

### Introduction Section
**Keywords:** `government jobs`, `sarkari naukri`, `government jobs in India`, `latest government jobs`

**Implementation:**
```
Find the latest active Government Jobs 2026 and Sarkari Naukri across India. Search and filter government vacancies by qualification, department, state, district, exam and application deadline.
```

### Search Section
**Keywords:** `search government jobs`, `find government jobs`

**Implementation:**
```html
<h2>Search Government Jobs</h2>
<p>Search by job title, organisation, department or keyword.</p>
```

### Closing Soon Section
**Keywords:** `government jobs closing soon`, `government jobs closing today`, `government job last date`

**Implementation:**
```html
<h2>Government Jobs Closing Soon</h2>
<p>Looking for government recruitment with an upcoming deadline? Browse active vacancies that are closing soon.</p>
```

### Latest Jobs Section
**Keywords:** `latest government jobs`, `government job vacancies`, `government recruitment`

**Implementation:**
```html
<h2>Latest Government Jobs 2026</h2>
<p>Browse active government recruitment opportunities currently accepting applications.</p>
```

### Qualification Section
**Keywords:** `government jobs by qualification`, `government jobs for 10th pass`, `government jobs for 12th pass`, `government jobs for graduates`

**Implementation:**
```html
<h2>Government Jobs by Qualification</h2>
<h3>10th Pass Government Jobs</h3>
<h3>12th Pass Government Jobs</h3>
<h3>Graduate Government Jobs</h3>
```

### State Section
**Keywords:** `government jobs by state`, `government jobs in Maharashtra`, `government jobs in Pune`, `government jobs in Mumbai`

**Implementation:**
```html
<h2>Government Jobs by State</h2>
<h3>Maharashtra Government Jobs</h3>
<a href="/government-jobs/maharashtra/pune">Government Jobs in Pune</a>
```

### Department Section
**Keywords:** `government jobs by department`, `railway government jobs`, `police government jobs`, `bank government jobs`

**Implementation:**
```html
<h2>Government Jobs by Department</h2>
<a href="/government-jobs/railway">Railway Government Jobs</a>
<a href="/government-jobs/police">Police Government Jobs</a>
```

### Exam Section
**Keywords:** `government jobs by exam`, `UPSC jobs`, `MPSC jobs`, `SSC jobs`

**Implementation:**
```html
<h2>Government Jobs by Exam</h2>
<a href="/exams/upsc-cse">UPSC Jobs</a>
<a href="/exams/mpsc-rajyaseva">MPSC Jobs</a>
```

### How-To Section
**Keywords:** `how to find government jobs`, `how to apply for government jobs`, `government job eligibility`

**Implementation:**
```html
<h2>How to Find the Right Government Job</h2>
<h3>Check Your Qualification</h3>
<h3>Check the Age Limit</h3>
```

### FAQ Section
**Keywords:** `what are government jobs`, `government jobs for 10th pass`, `government jobs for 12th pass`, `government jobs last date`

**Implementation:**
```html
<h2>Frequently Asked Questions About Government Jobs</h2>
<h3>What are government jobs?</h3>
<h3>Which government jobs are available for 10th pass candidates?</h3>
<h3>How can I check the last date for a government job?</h3>
```

---

## Long-Tail Keyword Integration

### Qualification + Location Keywords

**Target in Landing Pages:**
- `government jobs for 12th pass in Maharashtra`
- `government jobs for graduates in Pune`
- `government jobs for 10th pass in Mumbai`

**Implementation:** Use in respective qualification/location landing pages, not on /jobs hub.

### Department + Location Keywords

**Target in Landing Pages:**
- `railway jobs in Maharashtra`
- `police jobs in Maharashtra`
- `government teaching jobs in Maharashtra`

**Implementation:** Use in department landing pages with location sections.

### Deadline Intent Keywords

**Target in Closing Soon Section:**
- `government jobs closing today`
- `government jobs closing this week`
- `government job vacancies closing this month`

**Implementation:** Use naturally in closing soon section body copy.

---

## Keyword Density Guidelines

### Primary Keyword Density

**Government Jobs:**
- Title: 1-2 times
- H1: 1 time
- First 100 words: 1-2 times
- H2 sections: 1-2 times total
- Overall page: 4-6 times naturally

### Secondary Keyword Density

**Sarkari Naukri:**
- Title: 1 time
- H1: 1 time
- Body: 2-3 times naturally
- Overall page: 4-5 times naturally

### Specific Keywords

**Qualification/Location/Department keywords:**
- Relevant sections only
- H3 headings
- Link anchor text
- Body copy where natural
- FAQ where relevant

---

## Keyword Cannibalisation Prevention

### Page Ownership Matrix

| Page | Primary Keyword | Secondary Keywords | Avoid |
|------|----------------|-------------------|-------|
| /jobs | government jobs | sarkari naukri, latest government jobs | MPSC jobs, railway jobs, police jobs |
| /government-jobs/12th-pass | government jobs for 12th pass | 12th pass sarkari naukri, 12th pass govt jobs | government jobs, sarkari naukri |
| /government-jobs/maharashtra | government jobs in Maharashtra | Maharashtra sarkari naukri, Maharashtra govt jobs | government jobs, 12th pass jobs |
| /government-jobs/railway | railway government jobs | railway recruitment, railway jobs | government jobs, sarkari naukri |
| /exams/mpsc-rajyaseva | MPSC jobs | MPSC recruitment, MPSC Rajyaseva | government jobs, railway jobs |

---

## Exact Implementation Examples

### Title Tag Implementation
```html
<title>Government Jobs 2026 – Latest Sarkari Naukri & Govt Jobs</title>
```

### H1 Implementation
```html
<h1>Government Jobs 2026 – Latest Active Sarkari Naukri</h1>
```

### Section H2 Examples
```html
<h2>Government Jobs Closing Soon</h2>
<h2>Latest Government Jobs 2026</h2>
<h2>Government Jobs by Qualification</h2>
<h2>Government Jobs by State</h2>
<h2>Government Jobs by Department</h2>
```

### Section H3 Examples
```html
<h3>10th Pass Government Jobs</h3>
<h3>12th Pass Government Jobs</h3>
<h3>Maharashtra Government Jobs</h3>
<h3>Railway Government Jobs</h3>
```

### Anchor Text Examples
```html
<a href="/government-jobs/12th-pass">12th Pass Government Jobs</a>
<a href="/government-jobs/maharashtra">Maharashtra Government Jobs</a>
<a href="/government-jobs/railway">Railway Government Jobs</a>
```

---

## FAQ Keyword Integration

### Question Keywords
- `what are government jobs`
- `where can I find latest government jobs`
- `which government jobs are available for 10th pass`
- `which government jobs are available for 12th pass`
- `can graduates apply for government jobs`
- `how do I apply for a government job`
- `where can I check the official notification`
- `how can I check the last date`

### Answer Keywords
- `government job eligibility`
- `government job qualifications`
- `government job application process`
- `government job last date`
- `government job notification`

---

## Implementation Steps

### Step 1: Keyword Mapping
1. Create master keyword list
2. Map keywords to primary pages
3. Map keywords to sections
4. Map keywords to elements
5. Validate against cannibalisation rules

### Step 2: Content Optimization
1. Optimize title tags per mapping
2. Optimize H1 per mapping
3. Optimize section headings per mapping
4. Optimize anchor text per mapping
5. Optimize FAQ content per mapping

### Step 3: Validation
1. Check keyword density
2. Validate no cannibalisation
3. Check natural language flow
4. Validate against keyword stuffing
5. Test with SEO tools

---

## Validation Checklist

### Keyword Placement
- [ ] Primary keyword in title
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Secondary keywords in intro
- [ ] Section keywords in H2/H3
- [ ] FAQ keywords in questions
- [ ] Anchor keywords descriptive

### Cannibalisation Prevention
- [ ] Page ownership matrix followed
- [ ] No duplicate primary keywords
- [ ] Secondary keywords distributed
- [ ] Internal links follow strategy
- [ ] Landing pages have unique focus

### Natural Language
- [ ] Keywords used naturally
- [ ] No keyword stuffing
- [ ] Good content flow
- [ ] Readable and user-focused
- [ ] No forced keyword insertion

---

## Developer Notes

1. **Natural Language:** Prioritize user value over keyword density
2. **Cannibalisation:** Strictly follow page ownership matrix
3. **Variation:** Use keyword variations naturally
4. **Monitoring:** Track keyword performance after implementation
5. **Iteration:** Adjust based on Search Console data

---

## Success Metrics

- [ ] Primary keywords ranking in top 10
- [ ] Secondary keywords showing impressions
- [ ] Long-tail keywords gaining traction
- [ ] Improved keyword coverage
- [ ] Better search intent matching
- [ ] Higher click-through rates

---

**Last Updated:** 4 September 2026  
**Dependencies:** 14_KEYWORD_MAP.md  
**Status:** Implementation Ready