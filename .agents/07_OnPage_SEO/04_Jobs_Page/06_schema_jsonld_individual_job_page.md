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
  "employmentType": "{ACTUAL_EMPLOYMENT_TYPE_OR_OMIT}",
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
- `validThrough` is required and time-critical — Google actively checks this against the current date and can suppress stale postings from job-related search features. **`validThrough` must come only from the actual official application deadline stated in the recruitment notification.** Never calculate, estimate, default, or auto-generate this date (e.g. "posted date + 30 days") — a fabricated deadline is worse than no deadline, since it can misrepresent the recruitment and get the page penalized for inaccurate structured data.
- **`employmentType` must reflect the actual type stated in the notification** (`FULL_TIME`, `PART_TIME`, `CONTRACTOR`, `TEMPORARY`, etc. — see schema.org's `EmploymentType` enum for valid values). Do **not** hardcode `FULL_TIME` as a default. If the notification doesn't specify an employment type, **omit the field entirely** rather than guessing — an omitted optional field is safe; an incorrect one is inaccurate structured data.
- Only populate `baseSalary` if the notification actually states a figure. Don't estimate or invent one.
- Use real data only — no placeholder/fake values, per Google's structured data guidelines. This applies to every field in this template, not just the two called out above — if a value isn't confirmed from the source notification, omit the field rather than filling in a plausible-looking placeholder.

## 2. Expiration handling — two distinct cases, do not conflate them

A closed job and a removed job are **not the same thing**. Implement them as two clearly separate states so the "keep pages live" rule and the "clean up genuinely dead content" rule don't get tangled together.

### Case A — Job closed, page stays live (the default, expected case)

This is what should happen for the overwhelming majority of expired jobs.

1. Remove the `JobPosting` `<script>` block from the page (this is the one schema removal this file set calls for — everything else on the page, per file 04 §8, stays).
2. Update the visible status badge to "Closed" / "Recruitment Closed".
3. Page remains live, indexable, and reachable via internal links and the sitemap — it retains historical/informational value, may hold backlinks, and can still rank for the organization/post name.
4. If Indexing API is wired up (§3), send `URL_UPDATED` — not `URL_DELETED` — because the URL still exists and now has different (schema-less, "closed") content.

### Case B — Page actually removed (rare, deliberate, separately reviewed)

Only applies when a page is genuinely thin, duplicate, or has no standalone value even after the content upgrades in file 09 — this is a judgment call made per file 09's classification process, never an automatic side effect of a job closing.

1. If the decision is to remove the page: return an appropriate status (`410 Gone` is preferable to `404` for a deliberately retired job page) and add `noindex` if the route is being kept alive for any short-term reason.
2. Send `URL_DELETED` via the Indexing API if wired up.
3. This is the one place in the entire doc set where a page's indexability is intentionally reduced — it should be a rare, reviewed, logged decision, not the default expiration behavior.

**Do not use Case B as the standard flow.** The default for every expiring job is Case A.

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
