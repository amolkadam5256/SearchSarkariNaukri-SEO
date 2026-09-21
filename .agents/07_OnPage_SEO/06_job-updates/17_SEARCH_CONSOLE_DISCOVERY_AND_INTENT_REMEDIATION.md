# 17 - SEARCH CONSOLE DISCOVERY AND INTENT REMEDIATION

**Section:** 21 September 2026 Search Console Follow-up  
**Priority:** P0  
**Type:** Developer + SEO Remediation Checklist  
**Status:** Addendum Required Before Next Deployment

---

## Current Search Console Status

`/job-updates` is not currently a Soft 404, robots, or noindex problem.

Search Console shows the URL is discovered from the sitemap, the live test on 21 September 2026 says the page can be indexed, Breadcrumbs are valid, and an indexing request has already been submitted. The normal inspection record still shows `Discovered - currently not indexed` with `Last crawl: N/A`, which means Google knows the URL but has not yet completed the normal indexing crawl.

- [ ] Do not repeatedly request indexing for `/job-updates`.
- [ ] Treat sitemap discovery as working.
- [ ] Treat the live indexability test as passing.
- [ ] Focus on high-level internal links, intent differentiation from `/jobs`, self-canonical verification, server-rendered content, and crawl health.

## P0 Remediation Items

### 1. Add Homepage Link to `/job-updates`

The homepage must link users and crawlers to the SEO landing page before sending them to WhatsApp or Telegram.

Required architecture:

```text
Homepage
  -> Free Government Job Alerts
  -> /job-updates
      -> WhatsApp
      -> Telegram
```

Do not keep this structure:

```text
Homepage
  -> WhatsApp external
  -> Telegram external
```

Implementation:

```html
<section>
  <h2>Free Government Job Alerts</h2>
  <a href="/job-updates">Latest Sarkari Naukri & Free Job Alerts</a>
  <a href="YOUR-WHATSAPP-URL">Join WhatsApp</a>
  <a href="YOUR-TELEGRAM-URL">Join Telegram</a>
</section>
```

For React Router:

```jsx
<Link to="/job-updates">Latest Sarkari Naukri & Free Job Alerts</Link>
```

Checklist:

- [ ] Homepage has a crawlable `<a href="/job-updates">` or framework link that renders an anchor.
- [ ] Anchor text is descriptive, not `click here`.
- [ ] WhatsApp and Telegram links remain working.
- [ ] Homepage no longer bypasses `/job-updates` as the only job-alert path.

### 2. Add a Real `/jobs` to `/job-updates` Link

The `/jobs` page should not merely mention the Job Updates page. It must contain a crawlable internal link.

Replace plain text such as:

> Join our WhatsApp Community and Telegram Channel from the Job Updates page.

With:

```jsx
Join our WhatsApp Community and Telegram Channel from the
<Link to="/job-updates">Government Job Alerts page</Link>.
```

Rendered HTML must include:

```html
<a href="/job-updates">Government Job Alerts</a>
```

Checklist:

- [ ] `/jobs` links to `/job-updates` with a crawlable anchor.
- [ ] Link appears in a relevant alert/deadline context.
- [ ] Anchor text differentiates alerts from general job browsing.

### 3. Add `/job-updates` to Main Navigation

`/job-updates` is important enough to be discoverable from primary or secondary navigation.

Recommended label:

```text
Job Alerts -> /job-updates
```

Suggested nav cluster:

```text
Jobs
Maharashtra Jobs
Job Alerts
Exams
Results
Admit Cards
Current Affairs
```

Checklist:

- [ ] Header or secondary navigation includes a crawlable link to `/job-updates`.
- [ ] Label is short and clear: `Job Alerts`.
- [ ] Link does not replace existing WhatsApp/Telegram functionality.

### 4. Add Contextual Links from Category Pages

Relevant category and qualification pages should link to `/job-updates` when alert intent is natural.

Examples:

- [ ] Police category page: `Get alerts for new Police Bharti vacancies`.
- [ ] Railway category page: `Get Railway job deadline alerts`.
- [ ] Banking category page: `Get banking recruitment alerts`.
- [ ] Maharashtra jobs/district pages: `Get daily Maharashtra government job alerts`.
- [ ] Qualification pages: `Get alerts for new 10th pass / 12th pass / ITI jobs`.

### 5. Differentiate `/job-updates` from `/jobs`

This is the biggest ranking-quality issue after discovery.

Primary intent map:

| URL | Primary intent |
| --- | --- |
| `/jobs` | Browse and search all active government vacancies |
| `/job-updates` | Daily job alerts, new notifications, closing deadlines, WhatsApp/Telegram alerts |
| `/news` | Recruitment/exam news and editorial news |
| `/results` | Government exam results |
| `/admit-cards` | Admit cards and hall tickets |
| `/districts` | District-based job discovery |

`/job-updates` should emphasize:

- New Today
- New This Week
- Closing Today
- Closing This Week
- Deadline Alerts
- Recently Updated
- WhatsApp Alerts
- Telegram Alerts
- Recruitment Notification Updates

`/job-updates` should not become another copy of `/jobs`.

Checklist:

- [ ] `/jobs` H1/title focuses on browsing/searching active jobs.
- [ ] `/job-updates` H1/title focuses on daily updates and alerts.
- [ ] `/job-updates` top sections prioritize new and closing-soon updates.
- [ ] Generic qualification/category/state content is concise.
- [ ] No large duplicated FAQ/content blocks between `/jobs` and `/job-updates`.

### 6. Recommended H1, Title, and Meta

Recommended H1:

```text
Daily Sarkari Naukri Updates & Free Government Job Alerts 2026
```

Alternative H1:

```text
Latest Government Job Alerts 2026 - Daily Sarkari Naukri Updates
```

Recommended title:

```html
<title>Daily Sarkari Naukri Updates 2026 - Free Government Job Alerts</title>
```

Recommended meta description:

```html
<meta
  name="description"
  content="Get daily Sarkari Naukri updates and free government job alerts for UPSC, SSC, Railway, Banking, MPSC, Police Bharti and more. Track new vacancies, closing dates, WhatsApp and Telegram alerts."
>
```

Checklist:

- [ ] Title is unique from `/jobs`.
- [ ] H1 is unique from `/jobs`.
- [ ] Meta description emphasizes daily alerts and deadlines.
- [ ] Metadata does not keyword-stuff.

### 7. Canonical Rules

For `/job-updates`:

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/job-updates">
```

Checklist:

- [ ] `/job-updates` self-canonical is exact.
- [ ] Canonical is not `/job-updates/`.
- [ ] Canonical is not `/jobs`.
- [ ] Canonical is not `/`.
- [ ] Internal links consistently use `/job-updates`.

Do not canonicalize `/job-updates` to `/jobs` unless the business decision is to remove `/job-updates` as an indexable page.

### 8. Sitemap and Freshness Rules

Sitemap discovery is working. Do not keep changing the sitemap to force indexing.

Correct sitemap entry:

```xml
<url>
  <loc>https://www.searchsarkarinaukri.com/job-updates</loc>
  <lastmod>2026-09-21</lastmod>
</url>
```

Only update `<lastmod>` when meaningful page or data changes occur.

Checklist:

- [ ] `/job-updates` exists in XML sitemap.
- [ ] Sitemap `lastmod` reflects real page/data changes.
- [ ] Visible `Last updated` and `Last refreshed` use real dataset update time.
- [ ] Code does not use `new Date()` on every request to fake freshness.

### 9. Schema Rules

- [ ] Use `WebPage`.
- [ ] Use `BreadcrumbList`.
- [ ] Use `ItemList` for visible job-list links when useful.
- [ ] Use `FAQPage` only if visible FAQ content qualifies.
- [ ] Do not use `JobPosting` on `/job-updates`.
- [ ] Use `JobPosting` only on individual job detail pages.

### 10. Job Table Quality

The current job table is crawlable and useful. Keep job titles as links to job detail pages.

Improve listing readability:

- [ ] Keep qualification snippets short in listing tables.
- [ ] Put detailed eligibility on the individual job detail page.
- [ ] Validate `active listings` count is actual open jobs only.
- [ ] Exclude expired jobs from active counts.
- [ ] Deduplicate jobs by recruiting authority, notice number, post, deadline, and official PDF where possible.
- [ ] Avoid duplicate pages for Marathi/English versions of the same notification unless each page has a clear independent purpose.

### 11. Closing-Soon and Update Sections

The closing-soon section is one of the strongest differentiators from `/jobs`.

Add or prioritize:

- [ ] New Today.
- [ ] New This Week.
- [ ] Closing Today.
- [ ] Closing This Week.
- [ ] Recently Updated.
- [ ] Deadline Alerts.

Each section must be based on real data.

### 12. SSR, Prerender, and API-Failure Protection

Important SEO content should be visible in initial HTML where practical.

Developer must verify View Source/server response contains:

- [ ] `<title>`.
- [ ] `<meta name="description">`.
- [ ] `<link rel="canonical">`.
- [ ] `<meta name="robots" content="index,follow">` if robots meta is present.
- [ ] H1.
- [ ] Breadcrumb.
- [ ] Core explanation.
- [ ] Job links or useful fallback links.

Do not render the whole SEO page as:

```html
<div id="root"></div>
```

Do not make API failure produce a thin page:

```jsx
if (jobsApiError) {
  return <div>No jobs found</div>;
}
```

Use a resilient structure:

```jsx
<>
  <SEOContent />
  <JobAlertExplanation />
  <WhatsAppTelegram />
  {jobsError ? <p>Live vacancies are temporarily unavailable.</p> : <JobsTable />}
  <QualificationLinks />
  <FAQ />
  <OfficialSources />
</>
```

### 13. Real 404 and Crawl Health Checks

Site-wide crawler health still matters.

- [ ] Random nonexistent URLs return real HTTP 404, not HTTP 200 with a React "Page Not Found" view.
- [ ] Server logs show legitimate Googlebot can fetch pages with 200 responses.
- [ ] No recurring Googlebot 429 responses.
- [ ] No recurring Googlebot 5xx responses.
- [ ] Cloudflare/WAF/bot protection does not challenge legitimate Googlebot with CAPTCHA, 403, or 429.

### 14. Core Web Vitals

Measure separately; URL Inspection does not test Core Web Vitals.

- [ ] LCP is at or below 2.5 seconds.
- [ ] INP is below 200 ms.
- [ ] CLS is below 0.1.
- [ ] Job tables do not cause layout shifts.
- [ ] Fonts and dynamic alert widgets reserve stable space.

## Final Developer Checklist

| # | Check | Priority |
| --- | --- | --- |
| 1 | URL live and returns HTTP 200 | Critical |
| 2 | Live test says page can be indexed | Critical |
| 3 | Sitemap discovery confirmed | Critical |
| 4 | Index request submitted once | Critical |
| 5 | Homepage links to `/job-updates` | Critical |
| 6 | Main navigation links to `/job-updates` | High |
| 7 | `/jobs` links to `/job-updates` with crawlable anchor | Critical |
| 8 | Category/qualification pages link to `/job-updates` where relevant | Medium |
| 9 | Title, H1, and content intent differ from `/jobs` | Critical |
| 10 | Self-canonical points exactly to `/job-updates` | Critical |
| 11 | Robots allows indexing | Critical |
| 12 | No `JobPosting` schema on `/job-updates` | Critical |
| 13 | `JobPosting` exists only on single-job pages | Critical |
| 14 | Active count excludes expired jobs | High |
| 15 | Duplicate job records are controlled | High |
| 16 | Closing-soon and daily update sections are prominent | High |
| 17 | Initial HTML contains key SEO content | High |
| 18 | API failure leaves a useful page | High |
| 19 | Unknown URLs return real 404 | Critical |
| 20 | Googlebot logs do not show frequent 429/5xx/challenges | Critical |
| 21 | Core Web Vitals measured | High |
| 22 | Search Console Performance monitored after indexing | Medium |

---

**Last Updated:** 21 September 2026  
**Status:** Required Addendum
