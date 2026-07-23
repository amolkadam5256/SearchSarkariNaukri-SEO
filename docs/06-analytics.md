# 06 — Analytics & Conversion Tracking

## 6.1 Tracking Stack Configuration

- **Google Analytics 4 (GA4):** Web Stream `G-XXXXXXXXXX` configured with 14-month data retention.
- **Google Tag Manager (GTM):** Container `GTM-XXXXXXX` handling all tag firing, dataLayer variables, and trigger groups.
- **Microsoft Clarity:** Tracking Project ID configured via GTM snippet (IP filters exclude internal team).
- **Looker Studio:** Automated executive dashboards pulling GSC & GA4 API streams.

---

## 6.2 Custom Event & DataLayer Implementation

### DataLayer Code Snippet: Job Page Load Event
```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'event': 'job_page_view',
  'job_title': 'SSC CGL Recruitment 2026',
  'job_department': 'SSC',
  'job_state': 'All India',
  'job_qualification': 'Graduate',
  'job_vacancies': 5000,
  'last_date': '2026-08-15',
  'page_type': 'job_listing'
});
```

### DataLayer Code Snippet: Outbound Apply Button Click
```javascript
document.querySelector('#apply-now-btn').addEventListener('click', function() {
  dataLayer.push({
    'event': 'apply_click',
    'job_title': 'SSC CGL Recruitment 2026',
    'official_apply_url': 'https://ssc.nic.in',
    'click_position': 'top_cta_bar'
  });
});
```

### DataLayer Code Snippet: Job Alert Form Subscription
```javascript
dataLayer.push({
  'event': 'alert_signup',
  'alert_channel': 'telegram', // 'whatsapp' or 'email'
  'candidate_state': 'Uttar Pradesh',
  'candidate_qualification': 'Graduate'
});
```

---

## 6.3 Conversion Goals & Value Matrix

| Conversion Event | Event Type | Target Conversion Rate | Estimated Unit Value | Conversion Category |
|------------------|------------|------------------------|----------------------|---------------------|
| `apply_click` | Primary Conversion | > 15% of job page views | ₹5 | Lead / Outbound Intent |
| `alert_signup` | Primary Conversion | > 8% of total sessions | ₹15 | Candidate Retention |
| `newsletter_signup` | Secondary Conversion | > 5% of blog views | ₹10 | Subscriber Acquisition |
| `download_click` | Micro Conversion | Tracked engagement | ₹2 | Engagement |
| `share_click` | Micro Conversion | > 3% of total sessions | ₹3 | Viral Growth |

---

## 6.4 Executive Looker Studio Dashboard Layout

```
Dashboard View 1: SEO Overview Dashboard (Weekly)
├── Header: Total Sessions | Total Clicks | Average CTR | Avg Position
├── Chart 1: Organic Sessions Trend (Line chart, 12-week comparison)
├── Chart 2: Top 20 Landing Pages by Organic Traffic (Table: Sessions, Bounce Rate, Apply Clicks)
├── Chart 3: Top 20 Search Queries (Table: Clicks, Impressions, CTR, Position)
└── Chart 4: Device Split (Mobile vs Desktop vs Tablet pie chart)

Dashboard View 2: Content & Conversion Performance (Monthly)
├── Chart 1: Organic Traffic by Category (Jobs vs Results vs Admit Cards vs Blog vs State pages)
├── Chart 2: Apply Click Conversion Rate by State Page
├── Chart 3: Top Growing Pages (MoM Click Growth)
└── Chart 4: Underperforming Pages (High Impressions, Low CTR targets)
```
