# 07_EVENTS.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Event Specification
>
> **Purpose:** Define every analytics event required for SearchSarkariNaukri.com. This document serves as the implementation contract between Developers, Google Tag Manager, Google Analytics 4, Microsoft Clarity, Meta Pixel, and future marketing platforms.
>
> **Audience:** Developers, GTM Engineers, SEO Engineers, Analytics Engineers
>
> **Priority:** Critical
>
> **Status:** Required Before GTM Export
>
> **Version:** 1.0

---

# 1. Overview

This document defines every event that must be implemented.

Every event follows the architecture

```
Website

↓

Data Layer

↓

Google Tag Manager

↓

Google Analytics 4

↓

Marketing Platforms
```

No platform should receive events directly from website code.

---

# 2. Developer Responsibilities

Developers must

- Push Data Layer events
- Use documented event names
- Include required parameters
- Never duplicate events
- Test every event
- Validate in GTM Preview
- Validate in GA4 DebugView

Developers must NOT

- Fire GA4 directly
- Fire Meta Pixel directly
- Rename event names
- Skip required parameters
- Push incomplete event objects

---

# 3. Event Naming Standard

Use

```
snake_case
```

Examples

```
page_view

job_view

job_apply

search

download

contact_submit

newsletter_signup
```

Never use

```
PageView

Job View

JobView

Job_View
```

---

# 4. Global Events

## page_view

Purpose

Every page load.

Trigger

```
TR - Page View
```

Parameters

```
page_title

page_url

page_path

page_type

template_type

language
```

---

# 5. Job Events

## job_view

Purpose

User opens Job Details page.

Parameters

```
job_id

job_title

department

organization

state

district

category

employment_type
```

---

## job_apply

Purpose

User clicks Apply.

Parameters

```
job_id

job_title

destination_url

organization
```

---

## bookmark_job

Purpose

User saves a job.

---

## share_job

Purpose

User shares a job.

---

## job_expired_view

Purpose

User views expired job.

---

# 6. Search Events

## search

Parameters

```
search_term

result_count

filters

sort_order
```

---

## filter_apply

Parameters

```
filter_type

filter_value
```

---

## pagination_click

Parameters

```
page_number
```

---

# 7. Download Events

## download

Track

- Notification PDF
- Admit Card
- Result PDF
- Answer Key
- Syllabus

Parameters

```
file_name

file_type

file_url
```

---

# 8. Click Events

## outbound_click

Parameters

```
link_url

link_text

page_path
```

---

## whatsapp_click

Track

WhatsApp buttons.

---

## telegram_click

Track

Telegram Join buttons.

---

## email_click

Track

Email links.

---

## phone_click

Track

Phone links.

---

# 9. Form Events

## contact_submit

Parameters

```
form_name

status
```

---

## newsletter_signup

---

## register

---

## login

---

# 10. Engagement Events

## scroll_depth

Values

```
25

50

75

90

100
```

---

## session_engaged

Trigger

Timer

---

## video_start

Reserved

---

## video_complete

Reserved

---

# 11. Error Events

## javascript_error

Parameters

```
message

filename

line

page_url
```

---

## api_error

Parameters

```
endpoint

status

message
```

---

## page_not_found

Trigger

404

---

## server_error

Trigger

500

---

# 12. SEO Events

Track

```
canonical_loaded

schema_loaded

robots_loaded

sitemap_loaded
```

Reserved for future implementation.

---

# 13. AI Search Events

Reserved

```
ai_referral

llm_referral

chatgpt_referral

gemini_referral

copilot_referral

perplexity_referral
```

---

# 14. Marketing Events

Reserved

```
lead

generate_lead

purchase

conversion
```

---

# 15. Event Parameters

Every event should include where applicable

```
page_title

page_url

page_path

page_type

language

device_type

environment
```

---

# 16. Event Flow

```
User

↓

Website

↓

Data Layer

↓

Trigger

↓

Tag

↓

GA4
```

---

# 17. Event Folder Structure

Events must be organized across the standard 20-folder GTM structure:

```
01 - Configuration

02 - Variables

03 - Triggers

04 - GA4

05 - Google Ads

06 - Meta Pixel

07 - Microsoft Clarity

08 - SEO Events

09 - Job Tracking

10 - Forms

11 - Engagement

12 - Search

13 - Scroll

14 - Outbound Links

15 - Downloads

16 - Debug

17 - Consent

18 - Utilities

19 - Archived

20 - Testing
```

Event sub-categories within `04 - GA4`:

```
Page Events

Job Events

Search Events

Download Events

Click Events

Forms

Engagement

Errors

SEO

Marketing

AI Search
```

---

# 18. QA Checklist

Developer must verify

- Correct event name
- Correct parameters
- No duplicate events
- Data Layer push successful
- GTM Trigger fired
- GTM Tag fired
- GA4 DebugView received event
- Event visible in Realtime

---

# 19. Acceptance Criteria

Implementation is complete when

- Every documented event exists
- Every event pushes required parameters
- GTM receives every event
- GA4 receives every event
- No duplicate firing
- Naming convention followed
- Testing completed
- Documentation updated

---

# 20. Deliverables

Developer must provide

- Event Documentation
- Data Layer Examples
- GTM Export JSON
- Event Validation Report
- QA Report
- Preview Screenshots
- DebugView Screenshots

---

# 21. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

05_TRIGGERS.md

06_TAGS.md

08_CONVERSIONS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 22. Developer Notes

- Every event must originate from the Data Layer.
- Never hardcode analytics events in React or Next.js components.
- Every event must be reusable across GA4, Meta Pixel, Google Ads, Clarity, and future platforms.
- Validate every event using GTM Preview Mode and GA4 DebugView before publishing.
- Keep event names stable after production deployment to avoid breaking dashboards and reports.

---

# 23. Implementation Sequence

Developers must implement in this order

1. Data Layer Event
2. GTM Variable Mapping
3. GTM Trigger
4. GTM Tag
5. Preview Testing
6. GA4 DebugView
7. Production Validation
8. GTM Export