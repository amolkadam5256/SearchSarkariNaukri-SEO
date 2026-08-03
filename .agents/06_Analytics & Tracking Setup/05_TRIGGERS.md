# 05_TRIGGERS.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Google Tag Manager Trigger Specification
>
> **Purpose:** Define every GTM Trigger required for SearchSarkariNaukri.com. This document serves as the implementation guide for developers and GTM engineers to create consistent, reusable, and scalable triggers.
>
> **Audience:** Frontend Developers, GTM Developers, Analytics Engineers, SEO Engineers
>
> **Priority:** Critical
>
> **Status:** Required Before GTM Tag Creation
>
> **Version:** 1.0

---

# 1. Overview

Triggers determine **when Tags fire**.

No Tag should fire without an approved Trigger.

Every Trigger must:

- Use standardized naming
- Be reusable
- Use Data Layer whenever possible
- Avoid duplicate firing
- Be tested in GTM Preview Mode

---

# 2. Developer Responsibilities

Developers must:

- Push Data Layer events correctly
- Ensure events fire only once where required
- Prevent duplicate events
- Validate Trigger conditions
- Test every Trigger before production

Developers must NOT:

- Hardcode event firing
- Fire analytics manually
- Create duplicate Triggers
- Modify existing production Triggers without approval

---

# 3. Trigger Naming Convention

Use the following format:

```
TR - Event Name
```

Examples:

```
TR - Page View

TR - Job View

TR - Job Apply

TR - Search

TR - Download

TR - WhatsApp Click
```

---

# 4. Page View Trigger

Name

```
TR - Page View
```

Type

```
Custom Event
```

Event Name

```
page_view
```

Used By

- GA4 Page View
- Clarity
- Future Platforms

---

# 5. Job View Trigger

Name

```
TR - Job View
```

Type

```
Custom Event
```

Event

```
job_view
```

Fire

Every Job Detail Page

---

# 6. Job Apply Trigger

Name

```
TR - Job Apply
```

Type

```
Custom Event
```

Event

```
job_apply
```

---

# 7. Search Trigger

Event

```
search
```

Fire

Every Internal Search

---

# 8. Download Trigger

Event

```
download
```

Track

- PDF
- Notification
- Admit Card
- Result
- Answer Key
- Syllabus

---

# 9. Outbound Click Trigger

Event

```
outbound_click
```

Track

- Official Website
- Apply Online
- External Resources

---

# 10. WhatsApp Trigger

Event

```
whatsapp_click
```

---

# 11. Telegram Trigger

Event

```
telegram_click
```

---

# 12. Share Trigger

Event

```
share_job
```

---

# 13. Bookmark Trigger

Event

```
bookmark_job
```

---

# 14. Contact Form Trigger

Event

```
contact_submit
```

Fire

Only on Successful Submission

---

# 15. Registration Trigger

Event

```
register
```

---

# 16. Login Trigger

Event

```
login
```

---

# 17. Newsletter Trigger

Event

```
newsletter_signup
```

---

# 18. Scroll Triggers

Create individual Triggers

```
TR - Scroll 25

TR - Scroll 50

TR - Scroll 75

TR - Scroll 90

TR - Scroll 100
```

Fire Once Per Page

---

# 19. Timer Trigger

Used for

- Engagement Time
- Active Reading
- Future CRO

Intervals

```
30 Seconds

60 Seconds

120 Seconds
```

---

# 20. JavaScript Error Trigger

Event

```
javascript_error
```

---

# 21. API Error Trigger

Event

```
api_error
```

---

# 22. 404 Trigger

Condition

```
Page Type = 404
```

---

# 23. 500 Trigger

Condition

```
Page Type = 500
```

---

# 24. Trigger Folder Structure

Organize GTM using folders

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

# 25. Trigger Dependencies

| Trigger | Requires |
|----------|----------|
| Page View | page_view event |
| Job View | job_view event |
| Job Apply | job_apply event |
| Search | search event |
| Download | download event |
| WhatsApp | whatsapp_click |
| Telegram | telegram_click |
| Contact | contact_submit |

---

# 26. QA Checklist

Developer must verify:

- Trigger fires correctly
- Fires only once
- No duplicate firing
- Correct Event Name
- Correct Parameters
- GTM Preview Passes
- GA4 Receives Event
- No JavaScript Errors

---

# 27. Acceptance Criteria

Implementation is complete only if:

- Every Trigger exists
- Every Trigger is documented
- Every Trigger has a valid Event
- No duplicate Triggers
- GTM Preview passes
- Events appear in GA4 DebugView
- Production tested successfully

---

# 28. Deliverables

Developer must provide:

- GTM Trigger Configuration
- GTM Export (.json)
- Trigger Documentation
- Preview Screenshots
- QA Report
- Event Validation Report

---

# 29. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

06_TAGS.md

07_EVENTS.md

08_CONVERSIONS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 30. Developer Notes

- Always use **Custom Event Triggers** for Data Layer events.
- Avoid using Click Triggers where a Data Layer event is available.
- Configure Triggers before creating Tags.
- Every Trigger must have a clear purpose and documentation.
- Keep naming consistent across all GTM assets.
- Test every Trigger in GTM Preview and GA4 DebugView before publishing.
- Organize Triggers into the defined GTM folder structure before exporting the container.

---

# 31. Implementation Order

Developers must follow this sequence:

1. Verify Data Layer Events
2. Create GTM Variables
3. Create GTM Triggers
4. Test Triggers
5. Create Tags
6. Link Tags with Triggers
7. Validate in Preview Mode
8. Validate in GA4 DebugView
9. Publish Container
10. Export GTM JSON

---

**Next Document**

```
06_TAGS.md
```

This document will define **every GTM Tag** (GA4 Configuration, Event Tags, Google Ads, Meta Pixel, Clarity, Consent Mode, etc.) that uses these Triggers and Variables.