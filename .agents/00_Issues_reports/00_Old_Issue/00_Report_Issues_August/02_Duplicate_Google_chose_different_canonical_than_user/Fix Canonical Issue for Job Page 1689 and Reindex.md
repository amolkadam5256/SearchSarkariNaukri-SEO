# Fix Canonical Issue for Job Page 1689 and Reindex

## Issue
Google Search Console reports:

**Duplicate, Google chose different canonical than user**

Affected URL:

`https://www.searchsarkarinaukri.com/jobs/1689`

Status: Not Indexed

---

## Technical Audit

### 1. Verify Canonical Tag

Check page source for:

```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/1689" />
```

Verify there are no conflicting canonical tags.

---

### 2. Verify Next.js Metadata

Check page metadata configuration.

Expected:

```tsx
alternates: {
  canonical: "https://www.searchsarkarinaukri.com/jobs/1689"
}
```

---

### 3. Check Google Selected Canonical

Using Google Search Console URL Inspection:

- Inspect `/jobs/1689`
- Record Google-selected canonical URL
- Compare with user-declared canonical

---

### 4. Check Duplicate URLs

Search for alternative versions:

- `/jobs/1689/`
- `/job/1689`
- `/jobs?id=1689`
- Any parameterized URLs
- HTTP version
- WWW version

Action:

- Apply 301 redirects to canonical URL.
- Ensure only one URL returns HTTP 200.

---

### 5. Internal Linking Audit

Verify all internal links point to:

`https://www.searchsarkarinaukri.com/jobs/1689`

Remove references to alternate versions.

---

### 6. Sitemap Verification

Check sitemap entry.

Only include:

```xml
<loc>https://www.searchsarkarinaukri.com/jobs/1689</loc>
```

No duplicate URLs should exist in any sitemap.

---

### 7. Structured Data Audit

Verify JobPosting schema.

Expected:

```json
{
  "@type": "JobPosting",
  "url": "https://www.searchsarkarinaukri.com/jobs/1689"
}
```

---

### 8. Indexing Controls

Confirm:

- No `noindex` tag
- No X-Robots-Tag blocking
- Not blocked in robots.txt
- Returns HTTP 200

---

## Content Improvement

If technical implementation is correct and page content is thin, expand content by adding:

### Job Overview
- Organization Name
- Post Name
- Number of Vacancies

### Eligibility Criteria
- Educational Qualification
- Age Limit
- Age Relaxation

### Selection Process
- Exam Details
- Interview Details
- Merit Process

### Salary Details
- Pay Scale
- Allowances

### Important Dates
- Notification Date
- Start Date
- Last Date

### Application Process
- Step-by-step application instructions

### Important Links
- Official Notification
- Apply Online
- Official Website

### FAQ Section
Add at least 5–10 FAQs related to the recruitment.

---

## After Fixes

### Revalidate

- Clear cache
- Regenerate sitemap
- Deploy production build

### Google Search Console

1. URL Inspection
2. Test Live URL
3. Request Indexing

### Sitemap Submission

Resubmit:

- sitemap.xml
- jobs sitemap
- sitemap index

Monitor for 7–14 days.

---

## Success Criteria

- Only one canonical URL exists.
- No duplicate accessible versions.
- Page returns HTTP 200.
- Canonical, sitemap, schema, and internal links match exactly.
- Expanded unique content added.
- URL successfully indexed by Google.