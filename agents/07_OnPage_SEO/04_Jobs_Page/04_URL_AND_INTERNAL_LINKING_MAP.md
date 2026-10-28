# URL And Internal Linking Map

## Preservation Rule

Existing URLs are SEO assets. Before modifying routes or links, collect and preserve:

- Existing job URLs
- Existing category URLs
- Existing district URLs
- Existing city URLs
- Existing qualification URLs
- Existing exam URLs
- Existing indexed landing pages

Do not change URLs unless unavoidable. If a URL must change, add a permanent redirect.

## Header / Navbar / Footer Lock

Do not modify the existing header, navbar, main navigation, or footer for this `/jobs` page upgrade.

All new internal links required by this map must be placed inside the `/jobs` page body sections, job cards, contextual content blocks, related-job blocks, or individual job body content.

Do not add new links to the global header, navbar, or footer as part of this task.

## Recommended Master Hub

Primary hub:

`/jobs`

Every major job discovery path should start here and connect to individual job pages.

## Recommended URL Architecture

Qualification pages:

- `/10th-pass-government-jobs`
- `/12th-pass-government-jobs`
- `/iti-government-jobs`
- `/diploma-government-jobs`
- `/graduate-government-jobs`
- `/engineering-government-jobs`
- `/post-graduate-government-jobs`

State pages:

- `/jobs-in-maharashtra`
- `/jobs-in-gujarat`
- `/jobs-in-karnataka`
- `/jobs-in-delhi`
- Add other states only where architecture/data supports it.

District pages:

- `/districts/pune`
- `/districts/mumbai`
- `/districts/nagpur`
- Use existing district URL patterns where already present.

City pages:

- `/jobs-in-pune`
- `/jobs-in-mumbai`
- `/jobs-in-nagpur`
- Use existing city URL patterns where already present.

Category pages:

- `/category/railway-jobs`
- `/category/banking-jobs`
- `/category/police-jobs`
- `/category/medical-jobs`
- `/category/defence-jobs`
- Use existing category URL patterns where already present.

Exam pages:

- `/exams/upsc-cse`
- `/exams/mpsc-rajyaseva`
- `/exams/ssc-cgl`
- `/exams/rrb-ntpc`
- Use existing exam URL patterns where already present.

Individual jobs:

- `/jobs/[existing-slug]`

Never change existing individual job slugs casually.

## Core Internal-Link Graph

Master flow:

```text
/jobs
  -> qualification pages
  -> state pages
  -> district pages
  -> city pages
  -> department/category pages
  -> exam pages
  -> organization pages
  -> job type pages
  -> post/designation pages
  -> individual jobs
```

Location flow:

```text
/jobs
  -> /jobs-in-maharashtra
  -> /districts/pune
  -> /jobs-in-pune
  -> /jobs/[individual-job]
```

Qualification flow:

```text
/jobs
  -> /12th-pass-government-jobs
  -> individual 12th-pass job
```

Category flow:

```text
/jobs
  -> /category/police-jobs
  -> police recruitment listing
  -> individual police job
```

Exam flow:

```text
/jobs
  -> /exams/mpsc-rajyaseva
  -> MPSC recruitment
  -> individual job
```

Recruitment lifecycle flow:

```text
Government Job
  -> Application
  -> Admit Card
  -> Exam
  -> Answer Key
  -> Result
  -> Cutoff
  -> Merit List
  -> Document Verification
  -> Final Selection
```

Connect `/jobs` to existing:

- Admit Cards
- Results
- Exam Calendar
- Current Affairs
- Daily Quiz
- Career Guidance
- Eligibility Checker
- Age Calculator

## Individual Job Page Internal Links

Every individual job page should link back to relevant pages:

- Government Jobs
- State jobs
- District jobs
- City jobs
- Qualification jobs
- Department/category jobs
- Exam page
- Organization page
- Job type
- Application mode, if supported
- Related active jobs
- Closing Soon jobs

Example for a Latur 12th-pass contract recruitment:

- Government Jobs
- Maharashtra Government Jobs
- Latur Government Jobs
- 12th Pass Government Jobs
- Contract Government Jobs
- District Government Jobs
- Closing Soon Government Jobs

## Related Jobs Logic

For every individual job, generate contextual related jobs based on:

- Same qualification
- Same state
- Same district
- Same city
- Same department
- Same organization
- Same exam
- Same job type
- Similar designation
- Similar deadline/status

Suggested heading:

`Related Government Jobs`

Suggested groups:

- More jobs in this district
- More jobs in this state
- More jobs for this qualification
- More jobs from this department
- More jobs from this organization
- More closing-soon jobs

## Indexing Strategy

Index only important, high-value pages with real search demand and useful content.

Potentially indexable:

- `/jobs`
- `/10th-pass-government-jobs`
- `/12th-pass-government-jobs`
- `/iti-government-jobs`
- `/diploma-government-jobs`
- `/graduate-government-jobs`
- `/engineering-government-jobs`
- `/jobs-in-maharashtra`
- `/jobs-in-pune`
- `/districts/pune`
- `/category/railway-jobs`
- `/category/banking-jobs`
- `/category/police-jobs`
- `/exams/mpsc-rajyaseva`
- `/exams/ssc-cgl`
- `/exams/upsc-cse`

Noindex or canonicalize thin parameter combinations where appropriate.

Do not blindly canonicalize every filter page to `/jobs` if it prevents useful landing pages from ranking.

## Thin Page Guardrail

Do not create pages like:

- `/12th-pass-government-jobs-in-pune-without-exam-2026`
- `/12th-pass-government-jobs-in-pune-without-exam-for-freshers`
- Any automated keyword-combination page without real data and unique value

A page should exist only when it has:

- Real search intent
- Sufficient job data
- Unique useful content
- Legitimate internal relationships
- Accurate metadata and schema

## Anchor Text Rules

Use descriptive anchor text.

Good:

- `Government Jobs in Pune`
- `View Maharashtra Government Jobs`
- `12th Pass Government Jobs`
- `Railway Jobs`

Avoid:

- `Click here`
- `More`
- Random giant link paragraphs

Organize links into cards, grids, tabs, accordions, or compact contextual lists.
