# Requirements

## Functional requirements

### Job listing and detail pages

1. Every listing must identify the recruiting authority, title, category, location or applicable district, key dates, source URL, and current status where known.
2. A job-detail page must prominently link to the official notice and/or official application destination when available.
3. Dates must show an unambiguous format and time zone where the source specifies one.
4. Expired, withdrawn, and corrected listings must be visibly labelled rather than silently presented as active.
5. Search, category, and district paths must return useful empty states when no active listings match.

### Content utilities

1. Admit cards, results, and calendar entries must name the related exam/body and link to the official source.
2. Eligibility guidance must clearly state that final eligibility is determined by the official notification.
3. Study material and current-affairs content must show publication or update dates.

## Data and editorial requirements

1. Record a source URL and source-check date for every recruitment record.
2. Define an owner and review cadence for high-change content (deadlines, admit cards, results, and active jobs).
3. Preserve a correction trail internally for material factual edits.
4. Do not invent vacancy counts, fees, dates, qualifications, or official links.
5. Maintain a controlled taxonomy for category, department, exam, state, district, qualification, and status.

## Quality requirements

### SEO

- Each indexable page needs a unique, accurate title, primary heading, meta description, canonical URL, and internal links.
- XML sitemap URLs must be valid, indexable pages only.
- Use structured data only when the page content supports it and it follows current search-engine guidelines.
- Paginated, filtered, and expired-content URL policies must be documented before scale-up.

### Accessibility and usability

- Support keyboard navigation, semantic headings, visible focus, sufficient colour contrast, descriptive links, and mobile-first layouts.
- Do not make deadline, status, or validation information dependent on colour alone.
- Keep application links clear and distinguish external official destinations.

### Performance and security

- Optimize for Core Web Vitals on mobile.
- Use HTTPS, secure headers, dependency updates, backups, monitoring, and least-privilege administrative access.
- Validate and sanitize all user-controlled input, including search and eligibility-checker fields.

## Measurement requirements

Track, with consent and privacy requirements respected:

- Job-detail views.
- Search/filter and district/category navigation.
- Official-notice and apply-link outbound clicks.
- Eligibility-checker start and completion.
- Admit-card, result, calendar, and study-material engagement.
- Content freshness, crawl/index coverage, and technical errors.

## Acceptance criteria for a published job

- Source verified and stored.
- Status and deadline checked.
- Essential fields populated or clearly marked unavailable.
- Official destination tested.
- Mobile layout and page metadata reviewed.
- Internal links and sitemap eligibility confirmed.
