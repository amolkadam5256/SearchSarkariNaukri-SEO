# 08_CONVERSIONS.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Conversion Tracking Specification
>
> **Purpose:** Define all GA4 Key Events (Conversions), Google Ads Conversions, Meta Pixel Conversions, and business goals for SearchSarkariNaukri.com.
>
> **Audience:** Developers, GTM Engineers, Analytics Engineers, SEO Team, Marketing Team
>
> **Priority:** Critical
>
> **Status:** Required Before GTM Export
>
> **Version:** 1.0

---

# 1. Overview

This document defines every conversion that should be measured across the website.

All conversions must originate from

```
Website

↓

Data Layer

↓

Google Tag Manager

↓

Google Analytics 4

↓

Google Ads

↓

Meta Pixel

↓

Looker Studio
```

No conversion should be fired directly from application code.

---

# 2. Conversion Objectives

Measure

- Job Applications
- User Registrations
- User Login
- Newsletter Signups
- Contact Form Submission
- WhatsApp Clicks
- Telegram Joins
- Resume Downloads
- PDF Downloads
- Outbound Clicks
- Search Engagement

---

# 3. Primary Conversions

## Job Apply

Priority

★★★★★

GA4 Event

```
job_apply
```

Google Ads

Yes

Meta Pixel

Lead

Value

1

---

## Registration

GA4 Event

```
register
```

Value

1

---

## Login

GA4 Event

```
login
```

---

## Contact Form

GA4 Event

```
contact_submit
```

---

## Newsletter

GA4 Event

```
newsletter_signup
```

---

## WhatsApp

GA4 Event

```
whatsapp_click
```

---

## Telegram

GA4 Event

```
telegram_click
```

---

# 4. Secondary Conversions

- bookmark_job
- share_job
- search
- download
- outbound_click
- file_download
- scroll_depth
- session_engaged

These should remain Events until promoted to Key Events.

---

# 5. GA4 Key Events

Mark as Key Events

```
job_apply

register

login

contact_submit

newsletter_signup

whatsapp_click

telegram_click
```

---

# 6. Google Ads Conversions

Create

```
Job Apply

Registration

Contact Form

WhatsApp

Telegram
```

Import from

```
Google Analytics 4
```

Do not duplicate tracking.

---

# 7. Meta Pixel Conversions

Fire

```
Lead

CompleteRegistration

Contact

Subscribe
```

Mapped through GTM.

Never install Meta Pixel directly in website code.

---

# 8. Event Parameters

Every conversion should include

```
page_title

page_url

page_path

page_type

user_type

device_type

environment

language
```

---

# 9. Job Apply Parameters

```
job_id

job_title

organization

department

category

state

district

employment_type

apply_url
```

---

# 10. Registration Parameters

```
method

user_type

page_url
```

---

# 11. Contact Parameters

```
form_name

form_type

page_path
```

---

# 12. Download Parameters

```
file_name

file_type

file_url
```

---

# 13. Attribution

Default

```
Cross-channel

Data Driven Attribution
```

Lookback Window

```
30 Days
```

---

# 14. Deduplication

Conversions can be double-counted when the same business action is measurable from more than one signal (e.g., a GA4 Key Event and a server-side/Google Ads import of the same event). Apply the following rules:

| Risk | Rule |
|------|------|
| GA4 Key Event vs Google Ads import | Google Ads imports GA4 Key Events directly — do not also create a separate `awct` (Google Ads Conversion Tracking) tag for the same action unless Ads import is explicitly disabled for that event. |
| Client-side vs Server-side (future) | If server-side GTM is introduced, use `transaction_id` / a stable `event_id` data-layer field and enable deduplication on the destination platform (GA4 `event_id`, Meta `event_id` for CAPI). |
| Duplicate Tag firing | Every conversion Tag must use `tagFiringOption: ONCE_PER_EVENT` (already enforced in the exported container) so a single Data Layer push cannot fire the same Tag twice. |
| Multiple triggers on one Tag | Do not attach more than one Trigger to a conversion Tag unless the Triggers are provably mutually exclusive. |

Developers must verify in GA4 DebugView and Google Ads "Diagnose issues" that each conversion action produces exactly one hit per real user action before sign-off.

---

# 15. BigQuery Export

GA4 supports a daily (and optionally streaming) export to BigQuery. This is not yet enabled for this project but the architecture must not block it.

| Item | Requirement |
|------|-------------|
| Linking | Configure via GA4 Admin → BigQuery Links (outside GTM scope; requires a GCP project and billing account). |
| Event naming | All events must keep `snake_case` naming exactly as defined in `07_EVENTS.md` — BigQuery table/column names are derived directly from GA4 event and parameter names. |
| Parameter limits | Keep custom event parameters within GA4's limit (25 per event) — see `07_EVENTS.md` Section 15 for the approved parameter set per event. |
| PII | Never pass email, mobile number, or password as an event parameter (see `04_VARIABLES.md` Section 5, "Never expose"), since BigQuery export is raw and unfiltered. |
| Retention | BigQuery export is independent of GA4's UI data-retention setting; align retention with the organization's data policy before enabling. |
| Status | Not enabled. Enabling this is a GA4 Admin task for the Analytics team, not a GTM/developer deliverable, and does not require a new container version. |

---

# 16. Conversion Value

| Conversion | Value |
|------------|-------|
| Job Apply | 1 |
| Registration | 1 |
| Login | 1 |
| Contact | 1 |
| Newsletter | 1 |
| WhatsApp | 1 |
| Telegram | 1 |

---

# 17. GTM Folder Structure

All conversion tags must be organized within the standard 20-folder GTM container:

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

Conversion tags placement by folder:

- GA4 Conversion Tags → `04 - GA4`
- Google Ads Tags → `05 - Google Ads`
- Meta Pixel Tags → `06 - Meta Pixel`
- Conversion Linker → `05 - Google Ads`

---

# 18. Trigger Mapping

| Event | Trigger |
|--------|----------|
| job_apply | Click |
| register | Success |
| login | Success |
| contact_submit | Form Submit |
| newsletter_signup | Form Submit |
| whatsapp_click | Link Click |
| telegram_click | Link Click |

---

# 19. Developer Responsibilities

Developers must

- Push Data Layer Events
- Include all required parameters
- Avoid duplicate firing
- Keep event names unchanged
- Validate every conversion

---

# 20. GTM Responsibilities

GTM should

- Listen for Data Layer Events
- Fire GA4 Event Tags
- Fire Google Ads Conversion Tags
- Fire Meta Pixel Tags
- Pass parameters correctly

---

# 21. GA4 Responsibilities

Analytics Team should

- Mark Key Events
- Verify DebugView
- Verify Realtime
- Verify Reports
- Verify Attribution

---

# 22. QA Checklist

Developer must verify

- Data Layer Push
- Trigger Fired
- Tag Fired
- GA4 Received
- Google Ads Received
- Meta Received
- No Duplicate Events

---

# 23. Testing

Use

- GTM Preview
- GA4 DebugView
- Meta Test Events
- Google Ads Tag Assistant
- Chrome DevTools

---

# 24. Deliverables

Developer must provide

- GTM Container Export
- GA4 Screenshots
- Meta Test Event Screenshots
- Google Ads Conversion Verification
- QA Report
- Testing Report

---

# 25. Acceptance Criteria

Project is complete when

- All Key Events fire correctly
- No duplicate conversions exist
- GA4 receives every conversion
- Google Ads imports successfully
- Meta Test Events pass
- QA completed
- Production verified

---

# 26. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

05_TRIGGERS.md

06_TAGS.md

07_EVENTS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 27. Developer Notes

- Never hardcode conversion tracking in Next.js components.
- All conversions must be initiated through the Data Layer.
- Keep conversion names consistent across GA4, Google Ads, and Meta.
- Validate every conversion in GTM Preview before publishing.
- Document any custom conversion logic for future maintenance.

---

# 28. Implementation Sequence

Developers must complete in this order

1. Data Layer Event
2. GTM Variables
3. GTM Trigger
4. GA4 Event Tag
5. Google Ads Conversion Tag
6. Meta Pixel Tag
7. GTM Preview Testing
8. GA4 DebugView Verification
9. Production Deployment
10. Final GTM Export