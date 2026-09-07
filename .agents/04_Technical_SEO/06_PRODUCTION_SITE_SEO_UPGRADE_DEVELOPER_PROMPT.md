# Production Site SEO Upgrade - Developer Prompt

Production domain:

`https://www.searchsarkarinaukri.com/`

## Mission

Perform a complete SEO, content, information architecture, internal linking, technical SEO, and user experience upgrade of the existing SearchSarkariNaukri website.

This is not a rebuild. The objective is:

`ADD + IMPROVE + CONNECT + OPTIMIZE`

## Absolute Rules

Do not delete:

- Existing data
- Existing jobs
- Existing job IDs
- Existing job slugs
- Existing indexed pages
- Existing important URLs
- Existing working sections
- Existing search functionality
- Existing pagination
- Existing filters
- Existing FAQs
- Existing links
- Existing job information

Do not replace the current website with a simplified design.

Do not create:

- Fake jobs
- Fake departments
- Fake vacancies
- Fake dates
- Fake application links
- Fake statistics
- Fake government information
- Fake schema
- Thin SEO spam pages
- Duplicate pages

If a URL must change:

1. Preserve the old URL.
2. Add a permanent 301 redirect to a relevant equivalent page.
3. Update internal links.
4. Update canonical.
5. Update sitemap.
6. Verify redirect.
7. Avoid redirect chains.

## Header / Navbar / Footer Caution

Do not make casual global header, navbar, or footer changes while fixing SEO errors.

For `/jobs` specifically, follow the Jobs Page instruction folder: do not change header, navbar, main navigation, or footer.

For whole-site work, any header/navbar/footer improvement must be deliberate, curated, non-spammy, and separately reviewed because it affects the entire website.

Prefer adding new SEO/internal-link sections inside relevant page bodies, cards, breadcrumbs, related-content blocks, and contextual content areas.

## First Step - Inventory Before Changes

Before modifying code, inspect and document:

- Homepage
- `/jobs`
- Individual job detail pages
- Category pages
- State pages
- District pages
- City pages
- Qualification pages
- Organization/department pages
- Exam pages
- Result pages
- Admit card pages
- Answer key pages
- Syllabus pages
- Admission pages if they exist
- Scholarship pages if they exist
- Scheme pages if they exist
- Blog/news pages
- Search pages
- Pagination
- Filters
- Existing URLs
- Existing metadata
- Canonicals
- Structured data
- Navigation
- Footer
- Breadcrumbs
- Existing internal links
- Database/API structure
- CMS/admin structure
- Routing
- Sitemap generation
- robots.txt
- `llms.txt`
- Deployment configuration
- Caching
- Image handling
- JavaScript/CSS loading
- SSR/SSG behavior where applicable

Create a URL and page-type inventory before implementation.

## Current Audit Issues To Fix

From the 7 September 2026 Semrush audit:

- 6 duplicate title tag issues
- 4 duplicate-content pages
- 4 duplicate meta description issues
- 1 page could not be crawled
- 19 pages with low word count
- 2 pages with low text-to-HTML ratio
- `sitemap.xml` not found warning
- 70 outgoing external links containing nofollow
- 11 pages with only one incoming internal link
- 2 pages requiring content optimization
- 1 subdomain without HSTS

From the SEOptimer audit:

- Homepage title is too long
- Homepage meta description is too long
- Duplicate canonical tags on homepage
- Desktop PageSpeed needs improvement
- Rendered content percentage is high
- SPF record is missing
- Local Business schema is missing, only add if legitimate
- Social profiles are missing, only add if official profiles exist

Do not hide issues from tools. Fix the underlying implementation.

## Metadata System Requirements

Create reusable metadata generation functions/templates:

- `generateHomepageMetadata`
- `generateJobsMetadata`
- `generateJobMetadata(job)`
- `generateStateMetadata(state)`
- `generateDistrictMetadata(district)`
- `generateCityMetadata(city)`
- `generateQualificationMetadata(qualification)`
- `generateDepartmentMetadata(department)`
- `generateOrganizationMetadata(organization)`
- `generateExamMetadata(exam)`
- `generateResultMetadata(result)`
- `generateAdmitCardMetadata(admitCard)`
- `generateAnswerKeyMetadata(answerKey)`
- `generateSyllabusMetadata(syllabus)`
- `generateArticleMetadata(article)`

Every indexable page must have:

- Unique title
- Unique meta description
- One canonical URL
- Correct Open Graph metadata
- Correct Twitter card metadata where supported
- Correct page-level structured data where appropriate

Never generate duplicate titles dynamically.

## Title Examples

Homepage:

`Government Jobs in India 2026 - Latest Sarkari Naukri | SearchSarkariNaukri`

Jobs page:

`Latest Government Jobs 2026 - Sarkari Naukri, Govt Jobs & Vacancies`

State page:

`Government Jobs in Maharashtra 2026 - Maharashtra Sarkari Naukri`

District page:

`Government Jobs in Pune 2026 - Pune District Sarkari Naukri`

Qualification page:

`12th Pass Government Jobs 2026 - Latest Sarkari Naukri`

Individual job:

`[Exact Job Name] 2026 - Vacancy, Eligibility, Salary, Dates & Apply Online`

Rules:

- Keep titles readable.
- Make titles specific.
- Include the main page entity.
- Include year where appropriate.
- Do not keyword-stuff.

## Canonical URL System

Every indexable page must have exactly one canonical URL.

Canonical must be:

- Absolute
- HTTPS
- Correct hostname
- Self-referencing for canonical pages
- Consistent with sitemap URLs

Do not:

- Emit duplicate canonical tags.
- Canonicalize every page to homepage.
- Canonicalize every useful landing page to `/jobs`.
- Index every temporary filter/search parameter combination.

## Sitemap Requirements

Implement or verify:

- `/sitemap.xml`
- Sitemap index if needed
- `/sitemap-jobs.xml`
- `/sitemap-states.xml`
- `/sitemap-districts.xml`
- `/sitemap-categories.xml`
- `/sitemap-pages.xml`
- `/sitemap-blog.xml`

Only include canonical, indexable, valid URLs.

Exclude:

- 404 pages
- Redirected URLs
- Duplicate URLs
- Noindex URLs
- Temporary parameter URLs
- Non-canonical URLs
- Admin/private URLs

Update sitemap automatically when jobs/pages change.

## Robots Requirements

Verify `/robots.txt`.

Required baseline:

```txt
User-agent: *
Allow: /

Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml
```

Do not block important CSS, JavaScript, images, job pages, taxonomy pages, or rendering resources.

## Website Architecture Requirements

The site must support these silos:

- Government Jobs
- State Jobs
- District Jobs
- City Jobs
- Qualification Jobs
- Department Jobs
- Organization Jobs
- Exam Jobs
- Results
- Admit Cards
- Answer Keys
- Syllabus
- Career and recruitment guides

Each silo should connect logically to related silos.

## Jobs Master Hub

The `/jobs` page must become the primary Government Jobs discovery hub.

Keep existing:

- Jobs
- Job cards
- Pagination
- Search
- Filters
- FAQs
- Existing URLs

Add or improve page-body sections:

- Latest Government Jobs
- New Government Jobs Today
- Recently Updated Government Jobs
- Closing Soon
- Popular Government Jobs
- Government Jobs by Qualification
- Government Jobs by State
- Government Jobs by District
- Government Jobs by City
- Government Jobs by Department
- Government Jobs by Organization
- Government Jobs by Exam
- Government Jobs by Post/Designation
- Government Jobs by Job Type
- Government Jobs by Salary, if verified data exists
- Government Jobs for Freshers
- Government Jobs by Application Mode
- Government Jobs by Recruitment Status
- FAQs
- Helpful government-job resources

## Individual Job Pages

Every job detail page should become a complete recruitment information page using real data only.

Recommended sections:

- Breadcrumbs
- H1: `[Exact Job Name] Recruitment 2026`
- Short summary
- Job overview
- Organization
- Department
- Post name
- Vacancy
- Location
- Qualification
- Age limit
- Experience
- Salary
- Application mode
- Application fee
- Important dates
- Eligibility criteria
- Vacancy details
- Selection process
- Exam pattern where officially available
- Application process
- Documents required
- Official notification
- Official website
- Official application link
- FAQs
- Related government jobs

Omit unknown fields or show neutral states. Do not invent missing recruitment information.

## Job-To-Taxonomy Internal Linking

Every job page should automatically link to relevant taxonomy pages when data exists:

- State
- District
- City
- Qualification
- Department
- Organization
- Exam
- Post/designation
- Job type
- Application mode
- Related jobs

Example:

```text
Job
  -> Maharashtra Government Jobs
  -> Pune Government Jobs
  -> Graduate Government Jobs
  -> Railway Jobs
  -> RRB Jobs
  -> Similar closing-soon jobs
```

## Landing Page Requirements

Upgrade/create only pages supported by real data and real search intent.

State pages should include:

- Latest jobs in state
- State government jobs
- Central government jobs available in state
- District-wise jobs
- City-wise jobs
- Qualification-wise jobs
- Department-wise jobs
- Organization-wise jobs
- Popular exams
- Freshers jobs
- Closing-soon jobs
- FAQs
- Related states

District/city pages should include:

- Latest local jobs
- Local departments/organizations
- State and central jobs in that location
- Qualification links
- Department links
- Related locations
- FAQs

Qualification pages should include:

- Who can apply
- Typical job categories
- Departments
- Relevant exams
- Latest jobs
- Eligibility considerations
- Related qualifications
- FAQs

Department/organization/exam pages should include:

- Entity overview
- Latest jobs/notifications
- Eligibility and application guidance
- Related locations/qualifications/jobs
- FAQs

## Duplicate Content Rules

For each duplicate content group, classify as:

- Legitimate unique page
- Pagination variation
- Filter URL
- Parameter URL
- Accidental duplicate route
- Duplicate job page
- Duplicate taxonomy page
- Legacy URL

Then apply:

- Unique content
- Canonical
- 301 redirect
- Noindex where appropriate
- URL consolidation
- Proper pagination handling
- Parameter handling

Never delete first. Never create hundreds of near-identical landing pages.

## Low Word Count Rules

For the 19 low-word-count pages:

- Improve important indexable pages with meaningful unique content.
- Noindex/merge/canonicalize thin pages without durable SEO value.
- Do not add generic AI filler.
- Do not copy the same FAQ/content block to every page.

## Internal Linking Rules

For the 11 pages with only one incoming internal link:

- Add relevant contextual internal links from parent categories, hubs, related jobs, articles, taxonomy pages, and related resource pages.
- Use descriptive anchor text.
- Do not add random footer spam.

## Dynamic Data Rules

Do not hard-code:

- Job counts
- Vacancy counts
- Latest jobs
- Closing dates
- Status
- Statistics

Use real database/API fields.

Status must be generated from real dates/data:

- New
- Open
- Closing Soon
- Closed
- Result Available
- Admit Card Available
- Answer Key Available
- Updated

Do not show expired jobs as `Apply Now`.

Use timezone-aware date calculations.

## Empty State Rules

For a state/district/category with no current jobs:

- Do not publish fake jobs.
- Show a useful empty state.
- Link to latest jobs, parent category, nearby/relevant categories, or related states.
- Index only if the page has sufficient permanent useful content and a valid SEO purpose.

## Structured Data

Use accurate schema only:

- Organization
- WebSite
- BreadcrumbList
- ItemList
- JobPosting
- FAQPage where visible page content qualifies
- Article/BlogPosting where appropriate
- LocalBusiness only if legitimate business/address details exist

JobPosting schema must match visible job data.

Do not add fake schema to satisfy audit tools.

## Performance And GEO

Improve:

- Desktop PageSpeed
- Script completion time
- Rendered content percentage
- Server-rendered/crawlable important content
- Image optimization
- JS/CSS loading
- Caching

Important content and links should not depend entirely on client-side rendering.

## Security And DNS

Tasks:

- Investigate HSTS on affected subdomain.
- Add HSTS only after validating HTTPS support.
- Add SPF record only after confirming real mail provider.
- Preserve valid DMARC.
- Ensure HTTPS canonical host behavior is consistent.

## Mobile And Accessibility

Improve:

- Mobile/tablet/desktop layouts
- Filter drawer
- Search
- Job cards
- Tables
- Breadcrumbs
- Buttons
- Pagination
- FAQ accordions
- Content readability

Accessibility requirements:

- Semantic HTML
- Keyboard navigation
- Accessible forms
- Labels
- Alt text
- Visible focus states
- Sufficient contrast
- ARIA only where necessary
- Screen-reader-friendly status messages

## Final QA

Before deployment verify:

- HTTPS
- Canonicals
- Titles
- Meta descriptions
- H1/H2 hierarchy
- robots.txt
- sitemap.xml
- Structured data
- Breadcrumbs
- Internal links
- External links
- Image alt text
- URL structure
- Redirects
- 404 behavior
- Pagination
- Mobile viewport
- Language
- Charset
- Doctype
- Compression
- Caching
- JavaScript/CSS
- Server response
- Crawlability
- Indexability

## Post-Deployment Verification

Run complete crawl after deployment.

Target:

- 0 duplicate titles
- 0 duplicate meta descriptions
- 0 accidental duplicate content
- 0 important crawl failures
- 0 broken internal links
- 0 broken internal images
- 0 invalid canonical URLs
- 0 multiple canonical conflicts
- 0 missing critical metadata
- 0 missing sitemap
- 0 missing robots configuration
- 0 accidental noindex
- 0 accidental blocked pages
- 0 important orphan pages
- 0 inappropriate redirects
- 0 mixed-content issues
- 0 fake structured data

Run a new Semrush Site Audit and compare before/after numbers.

Do not claim 100% fixed unless the new crawl verifies it.

## Final Acceptance Criteria

The work is complete only when:

1. Existing jobs are preserved.
2. Existing important URLs are preserved.
3. Existing functionality is preserved.
4. Existing pagination works.
5. Existing search works.
6. Existing filters work.
7. Job detail pages work.
8. State pages work.
9. District pages work.
10. Qualification pages work.
11. Department pages work.
12. Organization pages work.
13. Exam pages work.
14. Related jobs work.
15. Internal linking is significantly improved.
16. Every important page has unique metadata.
17. Duplicate titles are resolved.
18. Duplicate meta descriptions are resolved.
19. Duplicate content is resolved appropriately.
20. Thin pages are improved with meaningful content or noindexed/merged.
21. Sitemap works.
22. Robots.txt works.
23. Canonicals are correct.
24. HTTPS is consistent.
25. HSTS issue is investigated and resolved where safe.
26. Crawl failure is investigated and fixed.
27. Structured data is valid.
28. JobPosting schema matches visible job data.
29. Mobile UX is strong.
30. Accessibility is improved.
31. Performance is improved.
32. No important existing data is deleted.
33. No fake content is introduced.
34. No mass low-quality programmatic SEO pages are created.
35. Final Semrush crawl is run.
36. Google Search Console is checked after deployment.

## Final Reminder

Do not stop after changing the homepage.

Audit the whole website, fix the whole website, add missing content, add missing information architecture, connect relevant pages, optimize important page types, run a complete post-deployment crawl, and verify the actual production domain:

`https://www.searchsarkarinaukri.com/`
