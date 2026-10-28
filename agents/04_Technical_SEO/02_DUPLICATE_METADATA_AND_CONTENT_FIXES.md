# Duplicate Metadata And Content Fixes

## Required Inputs

Export from Semrush:

- URLs with duplicate title tags
- URLs with duplicate meta descriptions
- URLs with duplicate content
- URL of the uncrawlable page

Do not rely only on issue counts. Fixing requires the exact affected URLs.

## Duplicate Title Workflow

1. Crawl current titles.
2. Group exact duplicate titles.
3. Identify page intent and entity.
4. Write unique title.
5. Ensure only one title tag is emitted.
6. Re-crawl.

## Title Templates

Homepage:

`Sarkari Naukri 2026 - Govt Jobs in India`

Jobs hub:

`Latest Government Jobs 2026 - Sarkari Naukri`

Qualification:

`{Qualification} Government Jobs 2026 - Latest Vacancies`

State:

`Government Jobs in {State} 2026 - Latest Vacancies`

District/city:

`Government Jobs in {Location} 2026 - Apply Online`

Category:

`{Category} Jobs 2026 - Latest Recruitment Updates`

Exam:

`{Exam} Jobs 2026 - Notification, Eligibility & Dates`

Tool/resource:

`{Tool Name} - SearchSarkariNaukri`

Rules:

- Keep unique entity near the front.
- Avoid identical generic suffixes creating duplicates.
- Keep titles concise when possible.

## Duplicate Meta Description Workflow

1. Crawl current descriptions.
2. Group exact duplicates.
3. Write entity-specific descriptions.
4. Keep important pages around 120-160 characters.
5. Remove duplicate fallback descriptions from shared SEO components.
6. Re-crawl.

## Meta Description Templates

Homepage:

`Find Sarkari Naukri 2026, latest government jobs, MPSC, SSC, railway, banking and police recruitment updates with official apply links.`

Jobs hub:

`Find latest Government Jobs 2026 across India. Search Sarkari Naukri by qualification, state, district, department, exam and deadline.`

Qualification:

`Browse latest {Qualification} government jobs with vacancy, eligibility, location, deadline and official notification details.`

Location:

`Find latest government jobs in {Location}. Check active vacancies, qualifications, departments, deadlines and official recruitment links.`

Category:

`Explore latest {Category} recruitment updates with active vacancies, eligibility, last date, location and official notification links.`

Exam:

`Check latest {Exam} recruitment updates, eligibility, application dates, vacancies, syllabus resources and official notification links.`

## Duplicate Content Workflow

For each duplicate group, choose one:

### Canonical

Use when multiple URLs represent the same content and both must remain accessible.

Requirements:

- Primary page self-canonicalizes.
- Duplicate page canonicalizes to primary.
- Internal links point to primary where possible.

### 301 Redirect

Use when a duplicate URL has no independent user or SEO value.

Requirements:

- Redirect to most relevant equivalent URL.
- Update internal links.
- Keep redirect permanent and direct.

### Noindex

Use for thin filter/search result combinations that should exist for users but not search.

Requirements:

- Do not noindex valuable landing pages by accident.
- Keep page crawlable if internal links need discovery.

### Unique Content

Use when the page has independent intent and should rank.

Add:

- Unique intro tied to entity
- Relevant dynamic listings/data
- Useful FAQs or guidance
- Internal links to related pages
- Entity-specific metadata

Avoid:

- Repeating the same paragraph with entity swapped
- Keyword stuffing
- Thin doorway pages

## Pagination Duplicate Handling

For paginated lists:

- Each paginated URL should be crawlable if it exposes unique listings.
- Use sensible self-canonical or project-approved pagination canonical strategy.
- Preserve query parameters for filters.
- Do not canonicalize every paginated page to page 1 if it blocks discovery of deeper jobs.

Example:

- `/jobs` canonical -> `/jobs`
- `/jobs?page=2` canonical -> `/jobs?page=2`, if page 2 has distinct crawlable listings and should be indexed/discovered
- Thin filtered pages may canonicalize/noindex based on strategy

## QA Checklist

- [ ] Exact duplicate titles resolved
- [ ] Exact duplicate descriptions resolved
- [ ] Duplicate content groups resolved
- [ ] Shared SEO component does not emit generic duplicates
- [ ] Page-specific metadata is generated from real entity data
- [ ] Canonical strategy is documented
- [ ] Redirects are direct and relevant
- [ ] No valuable existing page accidentally noindexed
- [ ] No new thin pages created
