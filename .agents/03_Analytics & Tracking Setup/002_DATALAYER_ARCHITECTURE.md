# 03_DATALAYER_ARCHITECTURE.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Data Layer Architecture
>
> **Purpose:** Define the complete Data Layer architecture for SearchSarkariNaukri.com. Every tracking event, SEO event, marketing event, and conversion must originate from the Data Layer before being processed by Google Tag Manager.
>
> **Audience:** Frontend Developers, Backend Developers, GTM Developers, SEO Engineers, Analytics Engineers
>
> **Priority:** Critical
>
> **Status:** Required Before GTM Container Creation
>
> **Version:** 1.0

---

# 1. Overview

This document defines the complete Data Layer implementation for SearchSarkariNaukri.com.

The Data Layer is the single source of truth for all analytics, SEO tracking, conversion tracking, and future marketing integrations.

The developer must implement every required Data Layer object before creating any GTM tags.

No analytics platform should directly access page data.

Everything must flow through

Website

↓

Data Layer

↓

Google Tag Manager

↓

Analytics Platforms

---

# 2. Objectives

The Data Layer must support

- Google Analytics 4
- Google Tag Manager
- Google Ads
- Microsoft Clarity
- Meta Pixel
- LinkedIn Insight
- Future Marketing Platforms
- Looker Studio
- BigQuery

without changing website code.

---

# 3. Developer Responsibilities

Developers must

✓ Create a global Data Layer

✓ Populate page information

✓ Populate job information

✓ Populate search information

✓ Push events

✓ Push user interactions

✓ Push conversions

✓ Keep values accurate

✓ Keep event names consistent

✓ Test every Data Layer push

---

Developers MUST NOT

❌ Fire GA4 directly

❌ Fire Meta Pixel directly

❌ Fire Google Ads directly

❌ Duplicate events

❌ Push incomplete objects

❌ Rename standard events

❌ Modify GTM-generated events

---

# 4. Global Data Layer

Every page must initialize

```javascript
window.dataLayer = window.dataLayer || [];
```

Only initialize once.

Never overwrite

```javascript
window.dataLayer = [];
```

This will erase existing events.

---

# 5. Required Global Variables

Every page must expose

```javascript
page_title

page_url

page_path

canonical_url

language

template_type

page_type

page_category

publish_date

modified_date

author

user_type

environment
```

---

# 6. Job Page Variables

Every Job Detail page must expose

```javascript
job_id

job_title

organization

department

employment_type

qualification

state

district

city

salary

vacancies

application_start_date

application_end_date

notification_date

official_notification_url

official_apply_url

job_status

category
```

---

# 7. Search Variables

Search pages must expose

```javascript
search_term

search_type

result_count

filter_state

filter_department

filter_category

sort_order
```

---

# 8. User Variables

Future ready

```javascript
user_id

login_status

user_role

membership

device_type
```

Do not expose sensitive user information.

---

# 9. Required Page View Event

Every page load

```javascript
window.dataLayer.push({

event:"page_view",

page_title:"",

page_url:"",

page_type:"",

template_type:""

});
```

---

# 10. Job View Event

Whenever a Job Detail page loads

```javascript
window.dataLayer.push({

event:"job_view",

job_id:"",

job_title:"",

organization:"",

department:"",

state:"",

district:""

});
```

---

# 11. Apply Button Event

When user clicks Apply

```javascript
window.dataLayer.push({

event:"job_apply",

job_id:"",

job_title:"",

destination_url:""

});
```

---

# 12. Search Event

Whenever search is performed

```javascript
window.dataLayer.push({

event:"search",

search_term:"",

result_count:"",

filters:""

});
```

---

# 13. Download Event

```javascript
window.dataLayer.push({

event:"download",

file_name:"",

file_type:"",

file_url:""

});
```

---

# 14. Outbound Click Event

```javascript
window.dataLayer.push({

event:"outbound_click",

link_url:"",

link_text:""

});
```

---

# 15. WhatsApp Event

```javascript
window.dataLayer.push({

event:"whatsapp_click"

});
```

---

# 16. Telegram Event

```javascript
window.dataLayer.push({

event:"telegram_click"

});
```

---

# 17. Contact Form Event

```javascript
window.dataLayer.push({

event:"contact_submit",

status:"success"

});
```

---

# 18. Scroll Event

Push only once

```javascript
25

50

75

90

100
```

---

# 19. Error Event

```javascript
window.dataLayer.push({

event:"javascript_error",

message:"",

page_url:""

});
```

---

# 20. Naming Convention

All event names

snake_case

Examples

```
page_view

job_view

job_apply

download

search

scroll_depth

contact_submit
```

Never use

```
PageView

JobView

Job View
```

---

# 21. Developer Testing

Before GTM implementation

Open browser console

Run

```javascript
dataLayer
```

Developer must verify

✓ Variables exist

✓ Events appear

✓ Values populated

✓ No duplicates

✓ Correct sequence

---

# 22. QA Checklist

Developer must confirm

- Global Data Layer initialized
- No overwrite
- All page variables available
- All job variables available
- Search variables available
- Events fire correctly
- No duplicate pushes
- No JavaScript errors
- GTM Preview receives all events
- GA4 DebugView receives events

---

# 23. Acceptance Criteria

The implementation is complete only if

✓ Every page initializes Data Layer

✓ Every page pushes page_view

✓ Every Job page pushes job_view

✓ Every Apply button pushes job_apply

✓ Every Search pushes search event

✓ Every Download pushes download event

✓ GTM can read every variable

✓ No tracking is hardcoded

✓ Future platforms can reuse the same Data Layer

---

# 24. Developer Deliverables

Developers must provide

- Data Layer implementation
- Source code commit
- Pull Request
- Testing screenshots
- GTM Preview screenshots
- GA4 DebugView screenshots
- Event validation report
- Variable mapping document

---

# 25. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

04_VARIABLES.md

05_TRIGGERS.md

06_TAGS.md

07_EVENTS.md

08_CONVERSIONS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 26. Implementation Order

Developers must follow this sequence

1. Install GTM
2. Implement Data Layer
3. Validate Data Layer
4. Create GTM Variables
5. Create GTM Triggers
6. Create GTM Tags
7. Configure GA4
8. Configure Conversions
9. Test in Preview
10. Verify in DebugView
11. Publish GTM
12. Export GTM Container

---

# 27. Notes for Developers

- Never modify the website UI during Data Layer implementation.
- Never hardcode analytics scripts inside components.
- Keep all tracking platform-agnostic so the same Data Layer supports GA4, Meta Pixel, Google Ads, Clarity, LinkedIn, and future tools.
- Every new feature added to SearchSarkariNaukri must include a corresponding Data Layer event before release.
- All future GTM tags must consume data only from the Data Layer.
