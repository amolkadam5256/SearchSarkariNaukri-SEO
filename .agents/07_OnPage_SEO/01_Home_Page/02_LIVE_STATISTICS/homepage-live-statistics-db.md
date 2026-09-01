# Homepage Live Statistics — Database-Driven Implementation

## Purpose

This file defines the exact requirements for the homepage statistics block:

- **Active Jobs**
- **Organizations**
- **Closing Soon**
- **Maharashtra Districts**

The values must be generated from the live database. Do **not** hard-code values such as `738`, `388`, or `262` in production HTML.

The existing homepage source currently shows `738 Active Jobs`, `388 Organizations`, `262 Closing Today`, and `212 Registered Users`; the jobs section separately shows `665` jobs. These figures must not be copied into the new implementation unless they are returned by the live database at request time. fileciteturn4file5L350-L378

---

# 1. Required Homepage Display

Use this exact semantic structure:

```text
738
Active Jobs

388
Organizations

262
Closing Soon

36
Maharashtra Districts
```

The numbers are examples of the current supplied page, **not fixed production values**.

Production values must come from the database.

---

# 2. Business Definitions

## 2.1 Active Jobs

Definition:

> Number of published recruitment/job records whose application status is currently open according to the site's database.

Recommended database logic:

```sql
COUNT(*) 
FROM jobs
WHERE status = 'active'
  AND is_published = true
```

If the database uses dates rather than a status field:

```sql
COUNT(*)
FROM jobs
WHERE is_published = true
  AND application_start_date <= CURRENT_TIMESTAMP
  AND (
    last_date IS NULL
    OR last_date >= CURRENT_DATE
  )
```

### Important

Do not count:

- drafts
- deleted jobs
- unpublished jobs
- test records
- duplicate jobs
- expired jobs
- jobs marked closed
- jobs that should not be publicly indexed

---

# 3. Organizations

Definition:

> Number of unique recruiting organizations associated with currently active published jobs.

Preferred query:

```sql
COUNT(DISTINCT organization_id)
FROM jobs
WHERE status = 'active'
  AND is_published = true
```

Do NOT use:

```sql
COUNT(*)
FROM jobs
```

because multiple jobs can belong to the same organization.

Example:

```text
Sahitya Akademi
├── Junior Clerk
├── Programme Assistant
├── Publication Assistant
└── Deputy Secretary
```

These are multiple jobs but one organization.

Therefore:

```text
4 jobs ≠ 4 organizations
```

---

# 4. Closing Soon

Definition:

> Number of active published jobs whose application deadline falls inside the site's defined closing-soon window.

Recommended production rule:

```text
Closing Soon = active jobs with last_date between today and today + 7 days
```

SQL:

```sql
COUNT(*)
FROM jobs
WHERE status = 'active'
  AND is_published = true
  AND last_date >= CURRENT_DATE
  AND last_date < CURRENT_DATE + INTERVAL '7 days'
```

## Important distinction

The existing page labels `262` as **"Closing Today"** in one location, while the requested homepage card is **"Closing Soon"**. fileciteturn4file5L362-L366

Do not mix these definitions.

If the card says:

```text
Closing Soon
```

use the 7-day window.

If the card says:

```text
Closing Today
```

use:

```sql
last_date = CURRENT_DATE
```

### Recommended homepage label

**Closing Soon**

because it is more useful to users.

---

# 5. Maharashtra Districts

Definition:

> Number of official Maharashtra districts represented in the site's district master data.

Do NOT calculate this by counting jobs.

Recommended:

```sql
SELECT COUNT(*)
FROM districts
WHERE state_code = 'MH'
  AND is_active = true
```

Expected current administrative count:

```text
36
```

But production should still read the district master table rather than hard-code `36`.

---

# 6. Important Data Integrity Rule

The four cards must use independent, correctly defined metrics.

```text
Active Jobs
    ↓
COUNT active published jobs

Organizations
    ↓
COUNT DISTINCT active-job organizations

Closing Soon
    ↓
COUNT active jobs with deadline inside closing window

Maharashtra Districts
    ↓
COUNT active Maharashtra districts
```

Do not derive one number from another.

---

# 7. Recommended API Response

Create one lightweight endpoint:

```text
GET /api/homepage/stats
```

Recommended JSON:

```json
{
  "activeJobs": 738,
  "organizations": 388,
  "closingSoon": 262,
  "maharashtraDistricts": 36,
  "closingSoonWindowDays": 7,
  "lastUpdated": "2026-08-28T00:18:00+05:30"
}
```

The numbers above are illustrative based on the supplied homepage data. The live API must return the actual database values.

---

# 8. Recommended Backend Response Contract

Use:

```json
{
  "data": {
    "activeJobs": 0,
    "organizations": 0,
    "closingSoon": 0,
    "maharashtraDistricts": 0
  },
  "meta": {
    "generatedAt": "ISO-8601 timestamp",
    "closingSoonWindowDays": 7,
    "timezone": "Asia/Kolkata"
  }
}
```

Use integer values only.

Do not return formatted strings such as:

```json
{
  "activeJobs": "738+"
}
```

Return:

```json
{
  "activeJobs": 738
}
```

and format the number in the frontend.

---

# 9. Frontend HTML

Use semantic HTML:

```html
<section class="homepage-stats" aria-labelledby="homepage-stats-title">
  <div class="container">

    <h2 id="homepage-stats-title" class="sr-only">
      Government Job Statistics
    </h2>

    <div class="stats-grid">

      <a class="stat-card" href="/jobs?status=active">
        <span class="stat-number" data-stat="activeJobs">—</span>
        <span class="stat-label">Active Jobs</span>
      </a>

      <a class="stat-card" href="/organizations">
        <span class="stat-number" data-stat="organizations">—</span>
        <span class="stat-label">Organizations</span>
      </a>

      <a class="stat-card" href="/jobs?status=closing-soon">
        <span class="stat-number" data-stat="closingSoon">—</span>
        <span class="stat-label">Closing Soon</span>
      </a>

      <a class="stat-card" href="/districts">
        <span class="stat-number" data-stat="maharashtraDistricts">—</span>
        <span class="stat-label">Maharashtra Districts</span>
      </a>

    </div>
  </div>
</section>
```

---

# 10. Frontend JavaScript

Use the API response rather than hard-coded numbers:

```html
<script>
async function loadHomepageStats() {
  const elements = {
    activeJobs: document.querySelector('[data-stat="activeJobs"]'),
    organizations: document.querySelector('[data-stat="organizations"]'),
    closingSoon: document.querySelector('[data-stat="closingSoon"]'),
    maharashtraDistricts:
      document.querySelector('[data-stat="maharashtraDistricts"]')
  };

  try {
    const response = await fetch('/api/homepage/stats', {
      headers: {
        'Accept': 'application/json'
      },
      credentials: 'same-origin'
    });

    if (!response.ok) {
      throw new Error('Unable to load homepage statistics');
    }

    const result = await response.json();
    const stats = result.data || result;

    const formatter = new Intl.NumberFormat('en-IN');

    if (elements.activeJobs) {
      elements.activeJobs.textContent =
        formatter.format(stats.activeJobs);
    }

    if (elements.organizations) {
      elements.organizations.textContent =
        formatter.format(stats.organizations);
    }

    if (elements.closingSoon) {
      elements.closingSoon.textContent =
        formatter.format(stats.closingSoon);
    }

    if (elements.maharashtraDistricts) {
      elements.maharashtraDistricts.textContent =
        formatter.format(stats.maharashtraDistricts);
    }

  } catch (error) {
    console.error('Homepage statistics error:', error);

    // Do not display fake/stale numbers.
    Object.values(elements).forEach((element) => {
      if (element) element.textContent = '—';
    });
  }
}

loadHomepageStats();
</script>
```

---

# 11. Better Implementation: Server-Side Rendering

For SEO and performance, preferably render these numbers on the server.

Recommended flow:

```text
Database
   ↓
Backend statistics service
   ↓
Homepage server render
   ↓
HTML contains current numbers
   ↓
Browser receives complete statistics
```

This is preferable to:

```text
Browser
   ↓
JavaScript
   ↓
API
   ↓
Database
```

for the initial homepage content.

The statistics are important visible content, so server-side rendering avoids a blank `—` state for normal users and crawlers.

---

# 12. Recommended Backend Service

Create a reusable function:

```text
getHomepageStats()
```

Return:

```text
activeJobs
organizations
closingSoon
maharashtraDistricts
generatedAt
```

Pseudo-code:

```javascript
async function getHomepageStats(db) {
  const activeJobs = await db.jobs.count({
    where: {
      status: 'active',
      isPublished: true
    }
  });

  const organizations = await db.jobs.countDistinct({
    column: 'organization_id',
    where: {
      status: 'active',
      isPublished: true
    }
  });

  const closingSoon = await db.jobs.count({
    where: {
      status: 'active',
      isPublished: true,
      lastDate: {
        gte: today(),
        lt: addDays(today(), 7)
      }
    }
  });

  const maharashtraDistricts = await db.districts.count({
    where: {
      stateCode: 'MH',
      isActive: true
    }
  });

  return {
    activeJobs,
    organizations,
    closingSoon,
    maharashtraDistricts,
    generatedAt: new Date().toISOString()
  };
}
```

Adapt the syntax to the project's actual ORM/database layer.

---

# 13. Database Indexes

Because these metrics run on the homepage, indexes are important.

Recommended indexes:

```sql
CREATE INDEX idx_jobs_homepage_active
ON jobs (status, is_published);

CREATE INDEX idx_jobs_homepage_deadline
ON jobs (status, is_published, last_date);

CREATE INDEX idx_jobs_organization
ON jobs (organization_id);

CREATE INDEX idx_districts_state_active
ON districts (state_code, is_active);
```

Only add indexes that match your actual schema and existing indexes. Check the database before creating duplicates.

---

# 14. Timezone Requirement

The website is India-focused.

Use:

```text
Asia/Kolkata
```

for deadline calculations.

Do not calculate "Closing Today" using the server's arbitrary timezone.

Example:

```text
Application deadline:
27 Aug 2026 23:59 IST
```

should be evaluated against:

```text
Asia/Kolkata
```

not UTC alone.

---

# 15. Deadline Status Logic

Use a single centralized status calculation.

Recommended:

```text
ACTIVE
CLOSING_TODAY
CLOSING_SOON
CLOSED
UPCOMING
```

Example:

```javascript
function getJobStatus(lastDate, nowIST) {
  if (!lastDate) return 'ACTIVE';

  if (lastDate < nowIST) {
    return 'CLOSED';
  }

  if (sameCalendarDate(lastDate, nowIST)) {
    return 'CLOSING_TODAY';
  }

  if (lastDate <= addDays(nowIST, 7)) {
    return 'CLOSING_SOON';
  }

  return 'ACTIVE';
}
```

Do not maintain separate conflicting rules in different homepage components.

---

# 16. Avoid the Existing Statistics Conflict

The supplied page currently has:

```text
738 Active Jobs
388 Organizations
262 Closing Today
212 Registered Users
```

and then:

```text
All Jobs 665
Central Government 69
State Government (Maharashtra) 19
Banking & Finance 57
Railway 31
Defence 15
Medical & Health 55
Education & Research 187
PSU & Corporations 141
Police 11
Other 257
```

fileciteturn4file5L350-L378

This requires reconciliation.

Possible reasons include:

- different datasets
- filters
- active vs displayed jobs
- pagination
- cached counts
- category overlap

But production must make the definitions clear.

---

# 17. Category Counts

If category filters are shown on the homepage, calculate them from the same canonical jobs dataset.

Do not manually maintain:

```text
Central Government 69
Railway 31
Police 11
...
```

Recommended API:

```text
GET /api/homepage/job-categories
```

Response:

```json
{
  "categories": [
    {
      "slug": "central-government",
      "name": "Central Government",
      "count": 69
    },
    {
      "slug": "state-government-maharashtra",
      "name": "State Government (Maharashtra)",
      "count": 19
    }
  ]
}
```

Counts should use the same active/published rules.

---

# 18. Do Not Hard-Code "36"

Although Maharashtra currently has 36 districts in the supplied site architecture, use the database:

```sql
SELECT COUNT(*)
FROM districts
WHERE state_code = 'MH'
AND is_active = true;
```

The existing homepage explicitly links users to all 36 Maharashtra districts. fileciteturn4file1L62-L72

---

# 19. Cache Strategy

These statistics do not need a database query on every request if traffic becomes significant.

Recommended:

```text
Database
   ↓
Stats service
   ↓
Cache: 1–5 minutes
   ↓
Homepage
```

For example:

```text
homepage_stats
TTL = 300 seconds
```

However, when a job changes status from active to closed, invalidate or refresh the cache.

---

# 20. Do Not Use Fake Fallback Numbers

Bad:

```javascript
activeJobs || 738
```

Bad:

```javascript
const activeJobs = apiData.activeJobs || 738;
```

This can cause incorrect statistics.

Use:

```javascript
activeJobs ?? null
```

or show:

```text
—
```

until real data is available.

---

# 21. No "500+" Unless It Is a Real Metric

The current homepage says:

> MPSC, Police, ZP, Talathi & 500+ exams tracked

fileciteturn4file6L419-L429

If this is not backed by a real database count, replace it with a factual statement.

For example:

> MPSC, Police, Railway, SSC, Banking and other government recruitment updates.

---

# 22. Accessibility Requirements

Each statistic must have:

```html
<span class="stat-number">738</span>
<span class="stat-label">Active Jobs</span>
```

The number alone is not sufficient.

Use:

```html
aria-label="738 active government jobs"
```

only when it improves the accessible name.

Do not use icon-only cards.

---

# 23. Animation Requirements

Add subtle motion to make the live statistics feel active without making
the section distracting.

Recommended animation behavior:

- Fade the statistics block in when it first enters the viewport.
- Stagger each card by 80-120ms.
- Count numbers up from 0 to the server-rendered value only once.
- Use a soft upward movement of 8-12px for each card.
- Add a quiet pulse or shimmer only to the "last updated" indicator, not
  to every number.

Recommended CSS:

```css
.live-stat-card {
  opacity: 0;
  transform: translateY(10px);
  transition:
    opacity 320ms ease,
    transform 320ms ease,
    box-shadow 220ms ease;
}

.live-stat-card.is-visible {
  opacity: 1;
  transform: translateY(0);
}

.live-stat-card:hover {
  transform: translateY(-2px);
}

.live-stat-updated-dot {
  animation: live-stat-pulse 1.8s ease-in-out infinite;
}

@keyframes live-stat-pulse {
  0%, 100% {
    opacity: 0.55;
    transform: scale(1);
  }

  50% {
    opacity: 1;
    transform: scale(1.18);
  }
}
```

Recommended JavaScript behavior:

```js
const prefersReducedMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)'
).matches;

if (!prefersReducedMotion) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.25 });

  document.querySelectorAll('.live-stat-card').forEach((card, index) => {
    card.style.transitionDelay = `${index * 90}ms`;
    observer.observe(card);
  });
}
```

Number count-up rules:

- Use the real server-rendered value as the final number.
- Do not animate to fake or rounded values.
- Do not repeat the count-up animation every time the user scrolls.
- Keep total duration below 900ms.

Reduced motion rule:

```css
@media (prefers-reduced-motion: reduce) {
  .live-stat-card,
  .live-stat-updated-dot {
    animation: none;
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

# 24. SEO Requirements

The statistics are supporting homepage content.

Do not try to rank for:

```text
738 active jobs
388 organizations
262 closing soon
```

These are dynamic values.

Primary SEO target remains:

```text
Latest Sarkari Naukri 2026
Government Jobs 2026
Maharashtra Government Jobs 2026
```

The existing site already positions itself around current vacancies, qualification, department and district filtering. fileciteturn4file0L19-L31

---

# 25. Recommended Card Links

### Active Jobs

```text
/jobs?status=active
```

### Organizations

Prefer a real organization index:

```text
/organizations
```

### Closing Soon

```text
/jobs?status=closing-soon
```

### Maharashtra Districts

```text
/districts
```

If your actual application uses different routes, use those existing canonical routes.

---

# 25. Important URL Rule

Do not create hundreds of indexable combinations from these filters.

For example:

```text
/jobs?status=active
/jobs?status=active&sort=latest
/jobs?status=active&district=pune
/jobs?status=active&qualification=graduate
```

These can remain functional filter URLs, while dedicated SEO pages should use clean URLs.

Examples:

```text
/graduate-government-jobs
/jobs-in-pune
/maharashtra-government-jobs
```

---

# 26. Data Validation Tests

Before deployment, test:

### Test 1 — Active Jobs

```text
Database active count
=
API activeJobs
=
Homepage Active Jobs
```

### Test 2 — Organizations

```text
COUNT(DISTINCT organization_id)
=
API organizations
=
Homepage Organizations
```

### Test 3 — Closing Soon

```text
7-day database count
=
API closingSoon
=
Homepage Closing Soon
```

### Test 4 — Maharashtra Districts

```text
active MH district count
=
API maharashtraDistricts
=
Homepage Maharashtra Districts
```

---

# 27. Edge Cases

Test:

- job closes at midnight
- job closes today
- deadline extended
- corrigendum changes deadline
- job is unpublished
- duplicate job
- organization deleted
- district renamed
- district disabled
- no closing date
- upcoming recruitment
- timezone conversion
- database temporarily unavailable

The site's editorial process already states that corrigenda, extensions and revisions should trigger updates. fileciteturn4file7L510-L520

The statistics must reflect those changes.

---

# 28. Monitoring

Log:

```text
homepage_stats_generated_at
active_jobs_count
organizations_count
closing_soon_count
maharashtra_district_count
query_duration_ms
cache_hit
```

Alert if:

```text
activeJobs = 0
```

or:

```text
organizations = 0
```

unexpectedly.

Do not alert simply because `closingSoon = 0`; zero can be legitimate.

---

# 29. Admin / Developer Debug Endpoint

Optional but strongly recommended:

```text
/api/homepage/stats?debug=1
```

or an internal admin dashboard showing:

```text
Active Jobs: 738
Organizations: 388
Closing Soon: 262
Maharashtra Districts: 36

Generated: 28 Aug 2026 00:18 IST
Cache: HIT
```

Do not expose internal database/query details publicly.

---

# 30. Final Production Acceptance Checklist

## Database

- [ ] Active job definition finalized
- [ ] Organization definition finalized
- [ ] Closing-soon window finalized
- [ ] Maharashtra district master table exists
- [ ] Duplicate jobs excluded
- [ ] Deleted jobs excluded
- [ ] Draft jobs excluded
- [ ] Expired jobs excluded from active count

## Backend

- [ ] `/api/homepage/stats` implemented
- [ ] Single statistics service
- [ ] Asia/Kolkata timezone
- [ ] Correct DISTINCT organization count
- [ ] Correct closing-date calculation
- [ ] Error handling
- [ ] Cache
- [ ] Cache invalidation/update strategy

## Frontend

- [ ] No hard-coded production numbers
- [ ] Server-rendered preferred
- [ ] Accessible labels
- [ ] Correct links
- [ ] Mobile responsive
- [ ] Loading state
- [ ] Error state
- [ ] No fake fallback values

## SEO

- [ ] Numbers are factual
- [ ] Labels match definitions
- [ ] No keyword stuffing
- [ ] No hidden SEO text
- [ ] Dynamic values do not alter title/meta
- [ ] Homepage remains focused on latest government jobs

## QA

- [ ] Compare DB vs API
- [ ] Compare API vs rendered HTML
- [ ] Test today's deadline
- [ ] Test tomorrow's deadline
- [ ] Test 7-day deadline
- [ ] Test expired jobs
- [ ] Test extended deadline
- [ ] Test duplicate organization
- [ ] Test Maharashtra district count

---

# 31. Final Recommended Display

When the database actually returns the current values, the homepage should render:

```text
┌────────────────────┬────────────────────┬────────────────────┬────────────────────────┐
│       738          │        388         │        262         │          36            │
│    Active Jobs     │   Organizations    │   Closing Soon     │ Maharashtra Districts  │
└────────────────────┴────────────────────┴────────────────────┴────────────────────────┘
```

The important rule is:

> **738 / 388 / 262 / 36 are not constants. They are database results.**

This resolves the current homepage's static-statistics problem and prevents the numbers becoming stale. The existing page already has a strong source-verification philosophy—official notification, recruiting organization, vacancy, eligibility, dates, official source and corrections—which should also apply to the data powering these public statistics. fileciteturn4file7L474-L520
