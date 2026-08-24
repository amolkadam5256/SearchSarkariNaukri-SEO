# 06 — Individual Job Page: `JobPosting` JSON-LD (New Addition)

> Add to every `/jobs/{slug}` page. This is the one schema type that belongs on individual job pages, **not** on `/jobs` itself (see file 05).

## 1. Full JobPosting template

```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "{post_name} – {organization} Recruitment {year}",
  "description": "{unique_150_300_word_description}",
  "identifier": {
    "@type": "PropertyValue",
    "name": "{organization}",
    "value": "{internal_job_id}"
  },
  "datePosted": "{ISO_date_posted}",
  "validThrough": "{ISO_last_date}",
  "employmentType": "FULL_TIME",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "{organization}",
    "sameAs": "{official_organization_url}"
  },
  "jobLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "{district}",
      "addressRegion": "{state}",
      "addressCountry": "IN"
    }
  },
  "educationRequirements": "{qualification_summary}",
  "totalJobOpenings": "{vacancy_count}",
  "url": "https://www.searchsarkarinaukri.com/jobs/{slug}"
}
```

### Field notes

- `description` must be genuinely unique per job — not a copy-pasted template with only the organization swapped. Use the original-content sections from file 04 as the source text.
- `validThrough` is required and time-critical — Google actively checks this against the current date and can suppress stale postings from job-related search features.
- Only populate `baseSalary` if the notification actually states a figure. Don't estimate or invent one.
- Use real data only — no placeholder/fake values, per Google's structured data guidelines.

## 2. Expiration handling (the one approved "removal")

When a job's `last_date` passes:

1. Remove the `JobPosting` `<script>` block from the page (do not remove any other content, per file 04 §8).
2. Update the visible status badge to "Closed".
3. Keep the page live and indexable unless it is genuinely thin/duplicate, in which case follow file 09's classification process — don't delete on a schedule.
4. If you have Indexing API access set up (see §3), send a `URL_UPDATED` notification when the schema changes.

## 3. Indexing API (optional, for eligible JobPosting pages only)

Google's Indexing API is scoped to JobPosting and BroadcastEvent pages — it is **not** a general bulk-indexing tool, and it should not be pointed at category/district/result pages (see file 09 §26 context).

Suggested flow, purely additive to your publishing pipeline:

```
New job published
   → generate JobPosting JSON-LD
   → add page to jobs sitemap (file 08)
   → call Indexing API: URL_UPDATED

Job closes
   → remove JobPosting JSON-LD
   → call Indexing API: URL_UPDATED (or URL_DELETED if page is actually removed)
```

## 4. BreadcrumbList for individual job pages

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.searchsarkarinaukri.com/" },
    { "@type": "ListItem", "position": 2, "name": "Government Jobs", "item": "https://www.searchsarkarinaukri.com/jobs" },
    { "@type": "ListItem", "position": 3, "name": "{post_name}", "item": "https://www.searchsarkarinaukri.com/jobs/{slug}" }
  ]
}
```

## Checklist for this file

- [ ] JobPosting schema added to every job page with real, unique field values
- [ ] `validThrough` kept accurate and current
- [ ] Schema removed (only) when job closes, page otherwise kept live
- [ ] Indexing API wired for JobPosting create/update/expire events (optional)
- [ ] BreadcrumbList added per job page
- [ ] Validated in Rich Results Test on a sample of pages
