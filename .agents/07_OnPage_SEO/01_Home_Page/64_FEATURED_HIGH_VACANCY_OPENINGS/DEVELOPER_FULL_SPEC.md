# Section 64 — Featured high-vacancy openings (developer full spec)

## Placement

Before “Latest Government Jobs” long list OR after urgent strip — competitor-style “Featured Sarkari Openings”.

## H2

Featured Sarkari openings 2026

## Subhead

Prominent recruitments with larger vacancy counts — central and state.

## Query

Top 4–6 jobs: `ORDER BY vacancies DESC`, active only, prefer mix of sectors (not all same org).

## Card copy pattern (reuse job card component)

| Element | Source | Label for user |
|---------|--------|----------------|
| Title | job.title | H3 link to detail |
| Location | job.city/state | Plain text |
| Vacancies | job.vacancy_count | “283 posts” |
| Teaser | first 120 chars of summary | Plain `<p>` |
| Last date | job.last_date | “Last date: 16 Oct 2026” |
| PDF | job.notification_url | **Official PDF** |
| Apply | job.application_url | **Apply on official site** |

## Footer link

“View all central government jobs →” use best live hub: `/central-government-jobs` or `/category/central-government-jobs` or `/jobs` with verified filter.

## Messaging on buttons

- PDF button: `Official notification (PDF)`  
- Apply button: `Apply on official portal` — opens external with `rel="noopener noreferrer"`

## Schema

`ItemList` of job detail URLs optional; JobPosting only on detail pages.

## QA

- [ ] No expired jobs in featured set  
- [ ] Vacancy count matches detail page  
