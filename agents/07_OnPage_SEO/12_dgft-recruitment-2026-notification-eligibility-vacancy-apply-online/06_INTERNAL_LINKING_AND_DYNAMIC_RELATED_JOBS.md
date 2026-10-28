# 06 — INTERNAL LINKING & DYNAMIC RELATED JOBS SPECIFICATION

**Target Canonical URL:** `https://www.searchsarkarinaukri.com/jobs/dgft-dgft-2026--2030`  
**Focus:** Link Equity, Contextual Discovery & Dynamic Database Filtering  
**Audit Date:** 18 October 2026 (IST)  
**Priority:** P1 Internal Linking & UX Routing

---

## 1. Confirmed Existing URLs (100% Safe to Render)

The following URLs are verified 200-status destinations on SearchSarkariNaukri and are approved for hardcoded editorial linking:

| Anchor Text | Destination Canonical URL | Page Placement | Context & Linking Rationale |
|---|---|---|---|
| **Latest Sarkari Naukri 2026** | `https://www.searchsarkarinaukri.com/` | Top banner, how-to-check, footer | Primary fallback for finding active employment. |
| **Maharashtra Government Jobs 2026** | `https://www.searchsarkarinaukri.com/jobs-in-maharashtra` | Related guides section | State-level job discovery without misclassifying DGFT. |
| **District-wise Government Jobs in Maharashtra** | `https://www.searchsarkarinaukri.com/blogs/district-wise-government-jobs-maharashtra-guide` | Related guides section | Comprehensive district career guidance. |
| **Government Jobs in Pune 2026** | `https://www.searchsarkarinaukri.com/blogs/government-jobs-in-pune-2026` | Related guides section | Major administrative & educational employment guide. |
| **Government Jobs in Pune — Current Listings** | `https://www.searchsarkarinaukri.com/districts/pune` | Related guides section | Direct live listings for Pune district. |

---

## 2. Dynamic Section 1: Latest Central Government Jobs Widget

To ensure that candidates landing on this expired DGFT archive find immediate value, render a dynamic server-side component querying currently open Central Government jobs.

### Widget Specifications
- **Component Identifier:** `<DynamicRelatedJobsWidget />`
- **Section Heading (H2):** `Latest Central Government Jobs — Currently Accepting Applications`
- **Display Count:** 3 to 6 active job cards.

### Strict Database Query & Filtering Criteria
```sql
SELECT 
    id, slug, title, hiring_organization, vacancies_count,
    job_location, application_end_date, source_verified_at,
    application_status, canonical_url
FROM recruitment_records
WHERE 
    category_or_type = 'CENTRAL_GOVERNMENT'
    AND application_status = 'OPEN'
    AND application_end_date >= CURRENT_DATE
    AND source_verified = TRUE
    AND id != 'dgft-dgft-2026--2030' -- Exclude self-reference
ORDER BY application_end_date ASC, source_verified_at DESC
LIMIT 6;
```

### Card Rendering Specifications
Each rendered card must display:
1. **Job Designation / Title** (e.g., `SSC CGL 2026 Inspector / Assistant Posts`)
2. **Hiring Authority** (e.g., `Staff Selection Commission`)
3. **Reported Vacancies** (e.g., `14,582 Posts`)
4. **Verified Deadline** (e.g., `Last Date: 15 November 2026`)
5. **Call to Action Link:** `<a href="/jobs/{slug}" class="btn-card">View Recruitment Details</a>`

### Zero-Result Graceful Fallback
If the database query returns 0 matching active central government jobs, do NOT render an empty container. Render the following fallback block:
```html
<div class="no-related-fallback">
  <p>There are no active central government vacancies closing this week. Check our complete repository for newly announced opportunities.</p>
  <a href="https://www.searchsarkarinaukri.com/" class="btn btn-primary">Browse All Active Government Jobs</a>
</div>
```

---

## 3. Dynamic Section 2: More Government Job Guides & Recruitment Updates

Render an editorial cards section linking directly to the verified career guides:

```html
<section id="related-guides" class="related-guides-block">
  <h2>More Government Job Guides and Recruitment Updates</h2>
  <div class="guides-grid">
    <div class="guide-card">
      <h3><a href="https://www.searchsarkarinaukri.com/jobs-in-maharashtra">Maharashtra Government Jobs 2026</a></h3>
      <p>Explore current state department openings, MPSC exam schedules, and department-wise vacancy reports across Maharashtra.</p>
    </div>
    <div class="guide-card">
      <h3><a href="https://www.searchsarkarinaukri.com/blogs/district-wise-government-jobs-maharashtra-guide">District-wise Government Jobs Guide</a></h3>
      <p>Detailed breakdown on how to navigate district collectorate, Zilla Parishad, and municipal corporation recruitment drives.</p>
    </div>
    <div class="guide-card">
      <h3><a href="https://www.searchsarkarinaukri.com/blogs/government-jobs-in-pune-2026">Government Jobs in Pune 2026</a></h3>
      <p>Targeted career handbook for central and state public sector jobs located in Pune district and surrounding regions.</p>
    </div>
  </div>
</section>
```

---

## 4. Dynamic Section 3: Other DGFT Notifications

- **Section Heading (H2):** `Other DGFT Notifications`
- **Database Query:** Query `recruitment_records` where `employer_name ILIKE '%Directorate General of Foreign Trade%' OR employer_name = 'DGFT'`, excluding the current post (`id != 'dgft-dgft-2026--2030'`).
- **Conditional Logic:**
  - If verified records exist, display them prioritized by status: `OPEN` first, followed by `CLOSED` (clearly labeled with a closed pill).
  - If **no other records exist**, display:
    ```html
    <div class="dgft-empty-state">
      <p>No other verified DGFT recruitment notices are currently listed in our repository.</p>
      <a href="https://www.dgft.gov.in/" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
        Visit Official DGFT Website for Latest Circulars
      </a>
    </div>
    ```

---

## 5. Developer Link Integrity Contract

Every dynamic card rendered on the page must fulfill the following contract to prevent broken links and search penalties:

```typescript
interface RelatedLinkContract {
  target_url: string;              // Must be absolute or valid root-relative path
  target_title: string;            // Plain text designation, no HTML
  target_status: 'OPEN' | 'CLOSED';// Status flag
  target_last_date: string;        // ISO 8601 date string
  target_source_verified_at: string;
  http_status: 200;                // Never render 404, 301 loop, or 500 links
}
```

### Safety Rules:
- **No Self-Links:** The current page URL (`/jobs/dgft-dgft-2026--2030`) must be explicitly excluded from related job queries.
- **No Expired Jobs in "Active" Blocks:** Any job whose `application_end_date < CURRENT_DATE` must never appear under the "Currently Accepting Applications" heading.
- **Cache Refresh:** Dynamic queries must be cached using Next.js `revalidate = 86400` (daily cache revalidation) or invalidated instantly via webhook on new job publication.
