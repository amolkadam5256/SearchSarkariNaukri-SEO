# 06_TAGS.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Google Tag Manager Tags Specification
>
> **Purpose:** Define every Google Tag Manager Tag required for SearchSarkariNaukri.com. This document serves as the implementation blueprint for developers to build a production-ready GTM container.
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

Tags are responsible for sending collected data from the website to analytics and marketing platforms.

All Tags must:

- Use Data Layer values
- Use approved GTM Variables
- Use approved GTM Triggers
- Never duplicate events
- Be organized into folders
- Be documented
- Be tested before publishing

---

# 2. Developer Responsibilities

Developers must

- Create Tags exactly as documented
- Never hardcode tracking scripts
- Use GTM Variables
- Use GTM Triggers
- Test every Tag
- Verify in Preview Mode
- Verify GA4 DebugView
- Export GTM JSON

Developers must NOT

- Fire duplicate events
- Fire GA4 directly
- Fire Meta Pixel directly
- Modify Tag names
- Skip QA testing

---

# 3. Tag Naming Convention

Use

```
TAG - Platform - Event
```

Examples

```
TAG - GA4 - Configuration

TAG - GA4 - Page View

TAG - GA4 - Job View

TAG - GA4 - Job Apply

TAG - Meta - Page View

TAG - Clarity - Install
```

---

# 4. GA4 Configuration Tag

Name

```
TAG - GA4 - Configuration
```

Type

```
Google Analytics: Google Tag
```

Measurement ID

```
G-GGE1EC2V8F
```

Trigger

```
Initialization - All Pages
```

Purpose

Loads GA4 once on every page.

---

# 5. GA4 Page View

Trigger

```
TR - Page View
```

Event

```
page_view
```

Parameters

```
page_title

page_location

page_path

page_type

template_type
```

---

# 6. GA4 Job View

Trigger

```
TR - Job View
```

Event

```
job_view
```

Parameters

```
job_id

job_title

department

organization

state

district

category
```

---

# 7. GA4 Job Apply

Trigger

```
TR - Job Apply
```

Event

```
job_apply
```

Parameters

```
job_id

job_title

destination_url
```

---

# 8. GA4 Search

Trigger

```
TR - Search
```

Event

```
search
```

Parameters

```
search_term

result_count

filters
```

---

# 9. GA4 Download

Trigger

```
TR - Download
```

Event

```
download
```

Parameters

```
file_name

file_type

file_url
```

---

# 10. GA4 Outbound Click

Trigger

```
TR - Outbound Click
```

Event

```
click
```

Parameters

```
link_url

link_text

page_path
```

---

# 11. GA4 WhatsApp Click

Trigger

```
TR - WhatsApp Click
```

Event

```
whatsapp_click
```

---

# 12. GA4 Telegram Click

Trigger

```
TR - Telegram Click
```

Event

```
telegram_click
```

---

# 13. GA4 Share Job

Trigger

```
TR - Share Job
```

Event

```
share_job
```

---

# 14. GA4 Bookmark Job

Trigger

```
TR - Bookmark Job
```

Event

```
bookmark_job
```

---

# 15. GA4 Registration

Trigger

```
TR - Registration
```

Event

```
register
```

---

# 16. GA4 Login

Trigger

```
TR - Login
```

Event

```
login
```

---

# 17. GA4 Contact Form

Trigger

```
TR - Contact Form
```

Event

```
contact_submit
```

---

# 18. GA4 Newsletter

Trigger

```
TR - Newsletter Signup
```

Event

```
newsletter_signup
```

---

# 19. GA4 Scroll Tracking

Create five Tags

```
25%

50%

75%

90%

100%
```

Each fires only once.

---

# 20. GA4 Error Tracking

Create Tags

```
JavaScript Error

API Error

404 Error

500 Error
```

---

# 21. Google Ads

Reserved Tags

```
Google Ads Conversion

Remarketing

Enhanced Conversion
```

Disabled until Ads implementation.

---

# 22. Meta Pixel

Reserved Tags

```
Meta Base Code

PageView

ViewContent

Search

Lead

CompleteRegistration
```

Disabled until Meta Pixel ID is available.

---

# 23. Microsoft Clarity

Tag

```
Microsoft Clarity Install
```

Trigger

Initialization

---

# 24. Consent Mode

Create

```
Google Consent Default

Google Consent Update
```

Must load before GA4.

---

# 25. Folder Structure

Create GTM folders

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

---

# 26. Developer Validation

Verify

- Tags fire correctly
- No duplicates
- Correct Variables
- Correct Triggers
- Correct Parameters
- DebugView receives data
- Preview Mode passes

---

# 27. Acceptance Criteria

Implementation is complete only if

✓ All Tags created

✓ Naming standards followed

✓ Folder structure completed

✓ GTM Preview passes

✓ GA4 DebugView passes

✓ No duplicate firing

✓ No UI changes

✓ GTM Export JSON generated

---

# 28. Deliverables

Developer must provide

- GTM Container (.json)
- Tag List
- Variable List
- Trigger List
- Testing Report
- Preview Screenshots
- DebugView Screenshots
- Release Notes

---

# 29. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

05_TRIGGERS.md

07_EVENTS.md

08_CONVERSIONS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 30. Developer Notes

- Use the **Google Tag** for GA4 Configuration.
- Fire the Configuration Tag only once using the **Initialization** trigger.
- All Event Tags must use Custom Event Triggers.
- All parameters must come from GTM Variables.
- Do not hardcode Measurement IDs or event values outside GTM Constants.
- Publish only after Preview Mode and DebugView validation.
- Export the final GTM Container JSON and include it in the implementation handoff.

---

# 31. Implementation Order

Developers must follow this order

1. GTM Installation
2. Data Layer
3. Variables
4. Triggers
5. Tags
6. Events
7. Conversions
8. Consent Mode
9. QA Testing
10. Publish
11. Export GTM JSON