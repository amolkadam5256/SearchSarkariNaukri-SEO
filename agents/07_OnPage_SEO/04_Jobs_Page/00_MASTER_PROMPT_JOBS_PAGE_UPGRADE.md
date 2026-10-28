# Master Prompt - Upgrade `/jobs` Page

Target URL: `https://www.searchsarkarinaukri.com/jobs`

Upgrade the existing `/jobs` page into the central Government Jobs / Sarkari Naukri master hub.

## Non-Negotiable Rule

This is an upgrade, not a rebuild.

## Header / Navbar / Footer Lock

Do not change the existing site header, navbar, main navigation, or footer for this `/jobs` page upgrade.

Keep them exactly as they are. Do not add links, remove links, rename labels, reorder menus, redesign layout, alter CTA buttons, or change footer columns as part of this page task.

All new `/jobs` SEO sections, internal links, resource links, CTAs, and discovery blocks must be added inside the `/jobs` page body content only.

Do not delete or replace:

- Existing jobs, job records, job IDs, job slugs, or indexed job URLs
- Existing category, district, qualification, exam, and landing-page URLs
- Existing content, FAQs, internal links, search, pagination, filters, alerts, header links, navbar links, or footer links
- Existing SEO equity

Do not add dummy jobs, fake deadlines, fake salary, fake vacancy numbers, fake organizations, or broken internal URLs.

The correct approach is: add, improve, connect.

## Main Objective

Transform `/jobs` from a basic listing page into the central discovery flow:

`Government Jobs -> Search -> Filter -> Discover -> Compare -> Apply -> Related Jobs`

The page must help users browse by:

- Qualification
- State
- District
- City
- Department
- Organization
- Exam
- Job type
- Post/designation
- Freshers
- Application mode
- Salary, only where verified data exists
- Deadline/status

Every section must use real existing URLs where available. If a destination does not exist, use an existing page/filter or create the destination only when the project architecture and data support it.

## Required Page Title And Meta

SEO title:

`Latest Government Jobs 2026 - Sarkari Naukri & Govt Vacancies | SearchSarkariNaukri`

Meta description:

`Find the latest Government Jobs 2026 and Sarkari Naukri across India. Search vacancies by qualification, state, district, department, exam and deadline. Check eligibility and official notifications before applying.`

Canonical:

`https://www.searchsarkarinaukri.com/jobs`

## Required H1

Use exactly one primary H1:

`Latest Government Jobs 2026 - Sarkari Naukri & Government Vacancies`

Intro copy:

`Find the latest active Government Jobs 2026 and Sarkari Naukri across India. Search government vacancies by qualification, state, district, department, exam, organization, job type and application deadline. Check eligibility, vacancy details and the official notification before applying.`

## Existing Sections To Keep

The current page already contains:

- Header/navigation
- WhatsApp and Telegram alert CTA
- Breadcrumb: `Home -> Government Jobs`
- Government Jobs H1 and intro
- Active job count
- Search
- Quick searches
- Popular searches
- Closing Soon
- Latest Government Jobs
- Job cards
- Pagination
- Qualification links
- State links
- Department links
- Exam links
- How to Find the Right Government Job
- Useful Government Job Resources
- About Government Job Listings
- FAQ
- Job Alerts CTA
- Footer

Keep header/navigation/footer unchanged. Improve only the `/jobs` page body sections, internal page content, job cards, search, filters, listings, SEO metadata, structured data, and contextual links inside the page body.

## Required Above-The-Fold Order

1. Existing header unchanged
2. Breadcrumb with `nav aria-label="Breadcrumb"`
3. H1
4. Short useful intro
5. Dynamic statistics row
6. Main job search
7. Advanced filters or filter entry point
8. Quick search chips

## Required Core Job Sections

Add or improve:

- Government Jobs Closing Today
- Government Jobs Closing Soon with Today, Tomorrow, Next 3 Days, This Week
- New Government Jobs Today
- Latest Government Jobs 2026
- Crawlable pagination

## Required SEO/Internal-Link Hub Sections

Add or improve:

- Government Jobs by Qualification
- Government Jobs by State
- Government Jobs by District
- Government Jobs by City
- Government Jobs by Department
- Government Jobs by Exam
- Government Jobs by Organization
- Government Jobs by Type
- Government Jobs by Post / Designation
- Government Jobs for Freshers
- Government Jobs by Application Mode
- Government Jobs by Salary, only if salary data exists
- Central Government Jobs
- State Government Jobs
- Popular Government Job Categories
- Find Government Jobs by Deadline

## Required Informational Sections

Add or improve:

- How to Find the Right Government Job
- How to Apply for Government Jobs
- Common Documents Required for Government Jobs
- Recruitment lifecycle links: Jobs, Admit Cards, Results, Exam Calendar, Current Affairs, Quiz, Career Guidance
- Useful Government Job Resources
- About These Government Job Listings
- Trust/disclaimer/editorial links
- FAQ
- Never Miss a Government Job Update CTA

## Critical Status Logic

Implement accurate job status:

- `UPCOMING`
- `ACTIVE`
- `CLOSING_SOON`
- `CLOSED`
- `EXPIRED`

If `lastDate < today`, the job must not appear as active. Do not delete expired jobs. Keep URL and record, show `Application Closed`, and link to related active jobs.

## Critical Count Logic

If total active jobs are 736 and only 200 are shown on the current page, display:

- `736 Active Government Jobs`
- `Showing 1-200 of 736 Jobs`

Do not show contradictory counts.

## Job Card Requirements

Each card should show only real known data:

- Job title
- Organization
- Status badge: Active, Closing Soon, New, Closed
- Location
- Qualification
- Vacancies
- Job type/category
- Department
- Application mode
- Posted date, where available
- Updated date, where available
- Last date
- Primary CTA: `View Job Details`
- Optional secondary CTA: `Official Notification`
- Contextual internal links: state, district, qualification, category, exam, organization, job type

Normalize display bugs:

- `6 Posts Posts` -> `6 Posts`
- `Not specified Posts` -> `Not Specified`
- Unknown vacancy -> `Vacancies: Not specified in the official notification`

## Advanced Filter Requirements

Filters must work with existing backend functionality and efficient queries:

- Qualification: 10th, 12th, ITI, Diploma, Graduate, Engineering, Post Graduate, PhD, Medical, Nursing, Pharmacy, Other
- State: all available states
- District: dynamic based on selected state
- Department: Railway, Banking, Police, Defence, Education, Healthcare, Forest, Agriculture, Revenue, Engineering, PSU, Municipal, University, Research, Insurance, Transport, Court, Electricity, Rural Development, Other
- Job type: Permanent, Contract, Apprentice, Temporary, Internship, Trainee, Walk-in, Direct Recruitment
- Application mode: Online, Offline, Walk-in, Email, Other
- Exam: UPSC, MPSC, SSC, RRB, IBPS, SBI, RBI, CTET, TET, Police Recruitment, Other
- Deadline: Closing Today, Tomorrow, 3 Days, This Week, This Month
- Experience: Fresher, No Experience Required, 1+ Year, 2+ Years, Experienced

Do not load all jobs into the browser.

## Structured Data

Use only accurate structured data:

- `/jobs`: BreadcrumbList and ItemList where valid
- Individual jobs: JobPosting with factual fields only
- FAQ structured data only when visible FAQ content qualifies

Do not add fake schema data.

## Accessibility And UX

Requirements:

- Semantic HTML
- One H1, proper H2/H3 hierarchy
- Keyboard-accessible filters and search
- Labels for controls
- Visible focus states
- Good color contrast
- Mobile filter drawer/modal
- Thumb-friendly CTAs
- No horizontal overflow
- No huge text blocks before job listings
- Information-dense but readable cards

## Final Acceptance Criteria

The work is complete only when `/jobs` functions as a complete Government Jobs discovery hub with accurate jobs, search, filters, deadline sections, latest jobs, pagination, body-content internal linking, SEO metadata, structured data, mobile UI, accessibility, no deletion of existing data or URLs, and no changes to the existing header, navbar, main navigation, or footer.
