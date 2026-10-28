# Current `/jobs` Page Audit

Audit date: 7 September 2026

Source reviewed:

- Live/public page text dump from `https://www.searchsarkarinaukri.com/jobs`
- Supplied SEO master prompt and audit notes

## Current Page Foundation

The page already has a solid base and should not be rebuilt from zero.

## Header / Navbar / Footer Lock

The existing site header, navbar, main navigation, and footer must not be changed for this `/jobs` page upgrade.

All improvements should be made inside the `/jobs` page body content. Do not add, remove, rename, reorder, or redesign header/navbar/footer links or CTAs.

Current sections found:

- Header/navigation
- WhatsApp and Telegram alert CTA
- Breadcrumb
- H1: `Government Jobs 2026 - Latest Active Sarkari Naukri`
- Intro copy
- Active job count: `736 active government jobs found`
- Search input
- Quick search chips
- Popular searches
- Government Jobs Closing Soon
- Latest Government Jobs 2026
- Job listings/cards
- Pagination pages 1-4
- Government Jobs by Qualification
- Government Jobs by State
- Government Jobs by Department
- Government Jobs by Exam
- How to Find the Right Government Job
- Useful Government Job Resources
- About These Government Job Listings
- FAQ
- Stay Updated CTA
- Footer

## Current Strengths

- `/jobs` is not empty; it already contains jobs, category navigation, resources, and FAQ.
- Existing qualification links include 10th, 12th, ITI, Diploma, Graduate, Engineering, and Post Graduate.
- Existing department/category links include Railway, Banking, Police, Teaching, Defence, Healthcare, Engineering, Forest, PSU, Municipal, University, and Research.
- Existing exam links include UPSC, MPSC, SSC, Banking, Railway, Police, and CTET/TET.
- Existing resources include Eligibility Checker, Age Calculator, Exam Calendar, Admit Cards, Results, Current Affairs, Daily Quiz, and Career Guidance.
- Current job cards expose useful data: organization, status, category, location, qualification, vacancy, and deadline.

## Main Gaps

The page is currently more of a job listing page than a complete Government Jobs hub.

Missing or underdeveloped architecture:

- Government Jobs Closing Today
- New Government Jobs Today
- Recently Updated Government Jobs
- Advanced filters by state, district, city, qualification, department, exam, job type, application mode, experience, and deadline
- District-level mega section
- City-level section
- Organization-level section
- Post/designation section
- Job-type section
- Freshers section
- Application mode section
- Salary section, if verified data exists
- Central vs State Government Jobs explanation and links
- Recruitment lifecycle links from Jobs to Admit Cards, Results, Exam Calendar, Current Affairs, Quiz, and Career Guidance
- Contextual internal links from each job card and job detail page

## Critical Data/Logic Issues

### Expired Jobs Appearing Active

The live page says it contains active jobs, but supplied audit notes found listings with application deadlines before the audit date.

Required fix:

- If `lastDate < today`, do not show the job as active.
- Keep the job record and URL.
- Show status as `Application Closed`.
- Link closed/historical jobs to related active jobs.

### Count Mismatch

The page shows:

- `736 active government jobs found`
- `200 active jobs found`

This can be valid only if 736 is total active jobs and 200 is the current displayed result range.

Required UI:

- `736 Active Government Jobs`
- `Showing 1-200 of 736 Jobs`

Pagination must match the true count.

### Vacancy Formatting Bugs

Examples in the crawl:

- `6 Posts Posts`
- `100 Posts Posts`
- `Not specified in the official advertisement. Posts`

Required normalization:

- `6 Posts`
- `100 Posts`
- `Not specified in the official notification`

## SEO Opportunity

The biggest opportunity is to connect:

`Job -> Qualification -> State -> District -> City -> Department -> Organization -> Exam -> Post -> Job Type -> Deadline -> Related Jobs`

This gives users multiple useful discovery paths and gives search engines a clearer topical graph.

## Recommended Page Balance

The page should remain utility-first:

- 60-70% job data, search, filters, deadline sections, and listings
- 20-30% structured navigation and internal linking
- 10-20% informational content

Avoid turning `/jobs` into a long generic blog page.
