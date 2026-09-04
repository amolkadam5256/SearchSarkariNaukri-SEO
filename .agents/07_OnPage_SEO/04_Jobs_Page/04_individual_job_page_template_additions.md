# 04 — Individual Job Page (`/jobs/{slug}`): New Fields & Sections (Additive Only)

> Applies to every existing job detail page template. All current fields (organization, qualification, location, last date, etc.) stay exactly as they are — the items below are **new blocks added to the same template.**

## 1. New "Quick Information" table (add near the top, below H1)

```html
<h2>Quick Information</h2>
<table>
  <tr><td>Organization</td><td>{organization}</td></tr>
  <tr><td>Recruitment</td><td>{recruitment_name} {year}</td></tr>
  <tr><td>Post Name</td><td>{post_name}</td></tr>
  <tr><td>Total Vacancies</td><td>{vacancy_count}</td></tr>
  <tr><td>Qualification</td><td>{qualification_summary}</td></tr>
  <tr><td>Age Limit</td><td>{age_limit}</td></tr>
  <tr><td>Application Start</td><td>{start_date}</td></tr>
  <tr><td>Last Date</td><td>{last_date}</td></tr>
  <tr><td>Application Mode</td><td>Online</td></tr>
  <tr><td>Official Website</td><td>{official_site_link}</td></tr>
</table>
```

## 2. New status/freshness badges (add near the title, don't remove existing date field)

```html
<span class="badge">Status: {Open|Closed}</span>
<span class="badge">Last Updated: {date}</span>
```

## 3. New original-content sections (add below the quick info table)

Add these as new headed sections. Write genuinely original 1–3 sentence summaries per job rather than copying the notification PDF verbatim — see file 09 for why this matters for indexing.

```html
<h2>{Organization} Recruitment {Year}</h2>
<p>{2–4 sentence original overview}</p>

<h2>Vacancy Details</h2>
<h2>Eligibility Criteria</h2>
<h2>Educational Qualification</h2>
<h2>Age Limit</h2>
<h2>Application Fee</h2>
<h2>Selection Process</h2>
<h2>Important Dates</h2>
<h2>How to Apply</h2>
<h2>Documents Required</h2>
<h2>Official Notification</h2>
```

Only include a heading if you actually have real content for it — don't ship empty headings.

## 4. New "Source & Verification" block (trust signal, add near the top)

```html
<p>
Recruiting Organization: {organization} · Official Website: {domain} ·
Source: Official {organization} Notification · Verified: {date}
</p>
```

Only show "Verified" language when it has actually been checked against the official notification.

## 5. New FAQ block (add near the bottom, before related jobs)

```html
<h2>Frequently Asked Questions</h2>
<h3>What is the last date to apply?</h3>
<h3>What is the qualification required?</h3>
<h3>What is the selection process?</h3>
<h3>What is the official website?</h3>
```

## 6. New "Related Jobs" section (add at the bottom)

```html
<h2>Related Government Jobs</h2>
<ul>
  <li>More {category} Jobs</li>
  <li>More {qualification} Jobs</li>
  <li>More {state/district} Jobs</li>
  <li>More Jobs Closing Soon</li>
</ul>
```

Populate dynamically based on the job's own department/qualification/location — don't show random unrelated jobs.

## 7. New "Related Exam" section (add if the job maps to a known exam, e.g. IBPS PO, SSC CGL)

```html
<h2>Related Exam: {exam_name}</h2>
<ul>
  <li>{exam_name} Syllabus</li>
  <li>{exam_name} Exam Pattern</li>
  <li>{exam_name} Previous Papers</li>
  <li>{exam_name} Admit Card</li>
  <li>{exam_name} Result</li>
</ul>
```

Only add these links once the corresponding exam pages exist (see file 07/exam clusters) — don't link to pages that don't exist yet.

## 8. Expired job handling (do not delete the page)

When `last_date` passes:

- **Keep the URL live.** Do not 404/delete it unless it has genuinely zero historical value.
- Change the status badge to `Status: Closed / Recruitment Closed`.
- **Remove only the `JobPosting` schema block** (see file 06) — this is the one place where *removing* something is correct, because Google requires expired JobPosting markup to be taken down. Everything else on the page stays.
- Add a line: "You may also be interested in: [Latest {category} Jobs] · [Latest Government Jobs]"

## Checklist for this file

- [ ] Quick Information table added
- [ ] Status/Last Updated badges added
- [ ] Original-content headed sections added (no verbatim PDF copy-paste)
- [ ] Source & Verification block added
- [ ] FAQ block added
- [ ] Related Jobs section added
- [ ] Related Exam section added (where applicable)
- [ ] Expired-job flow implemented (schema removed, page kept live)
