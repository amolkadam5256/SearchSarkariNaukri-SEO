# SearchSarkariNaukri.com — Homepage Section 3: Closing Soon Jobs Specification

**Section Name:** `03_Closing_Soon`  
**Page:** Homepage `/` only  
**Section Position:** Immediately after `02_Latest_Jobs` and before `04_Qualification`  
**Purpose:** Highlight recruitment notifications with upcoming application deadlines (closing within 24h, 48h, 7 days) to create high-urgency conversion and maximize user action.  
**Status:** Ready for Implementation  

---

## 1. Scope & Placement

This specification applies exclusively to:
```text
Homepage /
├── 01_Hero
├── 02_Latest_Jobs
└── 03_Closing_Soon (THIS SECTION)
```

---

## 2. SEO & User Intent Strategy

### Primary & Secondary Keywords
- **Primary Keywords:** `Sarkari Naukri Last Date Today`, `Government Jobs Closing Soon 2026`, `Sarkari Result Apply Online Last Date`
- **Secondary Keywords:** `Recruitment Application Deadline 2026`, `Jobs Expiring This Week`, `Last Chance Government Vacancies`
- **Intent Type:** Commercial & Actionable Navigation (Users with high intent looking for immediate application opportunities before deadlines close).

---

## 3. UX & UI Requirements

### Key Features
1. **Urgency Filter Tabs:** `Closing in 24 Hours`, `Closing in 48 Hours`, `Closing This Week (7 Days)`.
2. **Visual Urgency Badges:**
   - 🔴 **Red Badge:** "Ends Today / < 24 hrs" (High Urgency)
   - 🟠 **Amber Badge:** "Ends in 2 Days"
   - 🟡 **Yellow Badge:** "Ends This Week"
3. **Card Content Structure:**
   - Organization Name & Logo
   - Post Name & Vacancy Count
   - Qualification Required
   - Application End Date & Live Countdown
   - Direct "Apply Online" and "View Notification" CTAs

---

## 4. Semantic HTML Structure

```html
<section id="closing-soon-jobs" class="section-closing-soon" aria-labelledby="closing-soon-heading">
  <div class="container">
    <div class="section-header">
      <h2 id="closing-soon-heading">Closing Soon — Last Chance to Apply for Sarkari Jobs</h2>
      <p>Don't miss out on top government recruitment deadlines ending in the next 24 to 72 hours.</p>
    </div>

    <!-- Filter Buttons -->
    <div class="urgency-filter-group" role="tablist" aria-label="Closing Soon Filter">
      <button role="tab" aria-selected="true" class="tab-btn active" data-filter="24h">Ending Today (24h)</button>
      <button role="tab" aria-selected="false" class="tab-btn" data-filter="48h">Ending in 48h</button>
      <button role="tab" aria-selected="false" class="tab-btn" data-filter="7d">Ending This Week</button>
    </div>

    <!-- Dynamic Jobs Grid -->
    <div class="closing-soon-grid" id="closingSoonContainer">
      <!-- Cards rendered via DB -->
    </div>

    <div class="section-footer-cta">
      <a href="/jobs/closing-soon" class="btn btn-outline">View All Closing Soon Jobs →</a>
    </div>
  </div>
</section>
```

---

## 5. Database & API Requirements

```sql
-- Query active jobs closing within 7 days sorted by end_date ASC
SELECT id, title, organization, vacancies, qualification, end_date, slug
FROM jobs
WHERE status = 'ACTIVE' 
  AND end_date >= NOW() 
  AND end_date <= DATE_ADD(NOW(), INTERVAL 7 DAY)
ORDER BY end_date ASC
LIMIT 8;
```

---

## 6. Schema.org Structured Data (ItemList)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Government Jobs Closing Soon 2026",
  "description": "Latest government vacancies with upcoming application deadlines.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "url": "https://www.searchsarkarinaukri.com/jobs/mpsc-civil-services-2026"
    }
  ]
}
```
