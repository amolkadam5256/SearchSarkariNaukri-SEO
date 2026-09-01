# Latest Sarkari Naukri 2026 Section

## Section Placement

Place this section after:

```text
09_QUICK_JOB_FINDER
```

and before:

```text
11_CAREER_COMMAND_CENTER
```

---

## Section Goal

Show the newest government job notifications from the live jobs database.
This section should help users scan recent Sarkari Naukri updates by
category, qualification, state and recruiting organization.

Keep the homepage view short. Show only the latest 4 jobs, then link to
the full jobs page.

---

## Final UI Content

Section heading:

```text
Latest Sarkari Naukri 2026
```

Top CTA:

```text
View All Jobs
```

Top CTA link:

```text
/jobs
```

Description:

```text
New government jobs & recruitment notifications
```

Bottom CTA:

```text
View All Latest Jobs
```

Bottom CTA link:

```text
/latest-government-jobs
```

---

## Creative UI Format

Use this compact job-listing section:

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ Latest Sarkari Naukri 2026                              View All Jobs      │
│ New government jobs & recruitment notifications                            │
│                                                                            │
│ [All Jobs] [Maharashtra] [10th] [12th] [Graduate]                          │
│ [MPSC] [UPSC] [Railway] [Banking]                                          │
│                                                                            │
│ ┌──────────────────────────────┐ ┌──────────────────────────────┐          │
│ │ NEW                          │ │ NEW                          │          │
│ │ Job title                    │ │ Job title                    │          │
│ │ Recruiting organization      │ │ Recruiting organization      │          │
│ │ Location | Qualification     │ │ Location | Qualification     │          │
│ │ Posts                        │ │ Posts                        │          │
│ │ Last Date                    │ │ Last Date                    │          │
│ │ View Details                 │ │ View Details                 │          │
│ └──────────────────────────────┘ └──────────────────────────────┘          │
│                                                                            │
│ ┌──────────────────────────────┐ ┌──────────────────────────────┐          │
│ │ RECENT                       │ │ RECENT                       │          │
│ │ Job title                    │ │ Job title                    │          │
│ │ Recruiting organization      │ │ Recruiting organization      │          │
│ │ Location | Qualification     │ │ Location | Qualification     │          │
│ │ Posts                        │ │ Posts                        │          │
│ │ Last Date                    │ │ Last Date                    │          │
│ │ View Details                 │ │ View Details                 │          │
│ └──────────────────────────────┘ └──────────────────────────────┘          │
│                                                                            │
│                         [View All Latest Jobs]                             │
└────────────────────────────────────────────────────────────────────────────┘
```

Design direction:

- Use a clean job-board style, not a blog-card layout.
- Use green status for "NEW" jobs.
- Use blue status for "RECENT" jobs.
- Keep filters as horizontal chips.
- On mobile, make chips horizontally scrollable.
- Keep job cards equal height on desktop.
- Keep every card CTA aligned at the bottom.

---

## Filter Chips

Visible chips:

```text
All Jobs
Maharashtra
10th
12th
Graduate
MPSC
UPSC
Railway
Banking
```

Recommended URLs:

```text
/jobs
/jobs?state=maharashtra
/jobs?qualification=10th-pass
/jobs?qualification=12th-pass
/jobs?qualification=graduate
/jobs?category=mpsc
/jobs?category=upsc
/jobs?category=railway
/jobs?category=banking
```

---

## Job Card Fields From Database

Each job card must use live database fields:

```text
status label
job title
recruiting organization
location or state
qualification
number of posts
last date
job detail URL
```

Database sorting rule:

```text
Sort by published date or updated date, newest first.
```

Fallback sorting rule:

```text
If published date is missing, sort by job ID descending.
```

Status rules:

```text
NEW = published or updated within the last 72 hours
RECENT = published or updated within the last 14 days
```

Do not show expired jobs in this section unless the site explicitly marks
them as archived.

---

## Real Job Examples From Current Crawl

These examples are from crawled production job URLs found in the project
audit data. Use them only as fallback examples. The final homepage should
pull current data from the live jobs database.

Job 1:

```text
AAI Bagdogra Airport Apprentice Recruitment 2026 | Apply Online
URL: /jobs/aai-bagdogra-airport-apprentice-recruitment-2026-apply-online--3864
```

Job 2:

```text
AAI Bhubaneswar Airport Apprentice Recruitment 2026 - Apply Online
URL: /jobs/aai-bhubaneswar-airport-apprentice-recruitment-2026-apply-online--3869
```

Job 3:

```text
AAI Junior Executive Finance Recruitment 2026 Apply Online for 36 Posts
URL: /jobs/aai-junior-executive-finance-recruitment-2026-apply-online-for-36-posts--3669
```

Job 4:

```text
AAI Junior Executive Operations Recruitment 2026 Apply Online for 79 Posts
URL: /jobs/aai-junior-executive-operations-recruitment-2026-apply-online-for-79-posts--3671
```

---

## Keyword Targeting

Primary keyword:

```text
Latest Sarkari Naukri 2026
```

Secondary keywords:

```text
latest government jobs
new government job notifications
latest Sarkari job vacancy
Maharashtra government jobs
10th pass government jobs
12th pass government jobs
graduate government jobs
MPSC recruitment
UPSC recruitment
Railway recruitment
Banking recruitment
```

Use keywords naturally through:

- section heading
- description
- filter chip anchor text
- job card titles
- CTA labels
- internal link titles

Do not add a long SEO paragraph inside this section.

---

## Internal Link Strategy

Primary links:

```text
/jobs
/latest-government-jobs
```

Category links:

```text
/jobs?category=mpsc
/jobs?category=upsc
/jobs?category=railway
/jobs?category=banking
```

Qualification links:

```text
/jobs?qualification=10th-pass
/jobs?qualification=12th-pass
/jobs?qualification=graduate
```

Location link:

```text
/jobs?state=maharashtra
```

Every job title and "View Details" CTA must link to the real job detail
page.

---

## Responsive UI Direction

Desktop:

```text
Header row with View All Jobs CTA
Filter chips in 1-2 lines
2 x 2 latest job card grid
Centered bottom CTA
```

Tablet:

```text
2-column card grid
Filter chips wrap naturally
Keep cards equal height
```

Mobile:

```text
Header stacked
Filter chips horizontal scroll
Job cards single column
Bottom CTA full width
```

Mobile rules:

- Keep job titles readable and clamp to 2-3 lines.
- Avoid horizontal overflow in card text.
- Keep metadata labels short.
- Make the whole card scannable, but keep links explicit.

---

## Scroll Animation Direction

Use subtle section reveal:

```text
Header appears first
Filter chips appear second
Job card 1 appears third
Job card 2 appears fourth
Job card 3 appears fifth
Job card 4 appears sixth
Bottom CTA appears last
```

Motion rules:

- Use small upward movement.
- Stagger cards by 80-100ms.
- Add soft hover lift on job cards.
- Do not animate numbers aggressively.
- Run animation once only.
- Respect reduced-motion settings.

---

## Data And Verification Rules

- Use real jobs from the live jobs database.
- Do not hard-code sample jobs in production.
- Exclude expired jobs unless clearly marked.
- Ensure last date matches the job detail page.
- Ensure post count matches the official notification.
- Ensure organization name matches the official recruiter.
- If a field is missing, omit that row instead of showing a fake value.

---

## Quality Checklist

- [ ] Section uses real database jobs.
- [ ] Homepage shows only 4 latest jobs.
- [ ] Filter chips are crawlable links.
- [ ] Job cards link to real job detail pages.
- [ ] No placeholder organization names remain.
- [ ] No fake post counts or last dates are shown.
- [ ] Cards are responsive on mobile.
- [ ] Mobile chips scroll horizontally.
- [ ] Keywords are present through natural UI text.
- [ ] Animation is subtle and accessible.
