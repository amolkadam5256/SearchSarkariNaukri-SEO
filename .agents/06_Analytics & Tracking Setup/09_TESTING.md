# 09_TESTING.md

> **Project:** SearchSarkariNaukri
>
> **Document:** GTM, GA4 & Tracking Testing Guide
>
> **Purpose:** Complete QA process for validating every tag, trigger, variable, event, conversion, and tracking implementation before publishing the GTM container.
>
> **Audience:** Developers, GTM Engineers, QA Team, SEO Team, Analytics Team
>
> **Priority:** Critical
>
> **Status:** Required Before Production Deployment
>
> **Version:** 1.0

---

# 1. Overview

This document defines the complete testing and quality assurance process for all tracking implementations on SearchSarkariNaukri.com.

No GTM container should be published until every test in this document has passed.

---

# 2. Testing Objectives

Verify

- GTM Installation
- Data Layer
- Variables
- Triggers
- Tags
- GA4 Events
- Google Ads Conversions
- Meta Pixel Events
- Microsoft Clarity
- Search Console
- Cross Browser Compatibility
- Cross Device Compatibility

---

# 3. Testing Environment

Production

```
https://www.searchsarkarinaukri.com
```

Development

```
Local Environment
```

Preview

```
Google Tag Manager Preview Mode
```

---

# 4. Required Testing Tools

Google Tag Manager Preview

Google Analytics DebugView

Google Tag Assistant

Meta Pixel Helper

Meta Test Events

Microsoft Clarity

Chrome Developer Tools

Google Search Console

Lighthouse

PageSpeed Insights

---

# 5. GTM Installation Test

Verify

- GTM Script exists inside HEAD
- GTM Noscript exists after BODY
- GTM Container loads successfully

Expected

```
Container Loaded Successfully
```

---

# 6. GTM Preview Test

Open

```
Google Tag Manager

↓

Preview
```

Enter

```
https://www.searchsarkarinaukri.com
```

Verify

Container Connected

Expected

```
Connected Successfully
```

---

# 7. Data Layer Test

Developer Console

```
window.dataLayer
```

Verify

- Exists
- Array
- Events pushed correctly

Expected

```
Array with Events
```

---

# 8. Variable Testing

Verify every variable

Examples

```
Page URL

Page Path

Page Hostname

Click URL

Click Text

Job ID

Department

District

State

User Type
```

Expected

Correct values

---

# 9. Trigger Testing

Verify

Page View

DOM Ready

Window Loaded

Click Trigger

Form Submit

Custom Events

History Change

Scroll

Expected

Only required triggers fire

---

# 10. Tag Testing

Verify

GA4 Configuration

GA4 Events

Google Ads

Meta Pixel

Conversion Linker

Clarity

Expected

No duplicate firing

---

# 11. GA4 DebugView

Open

```
Google Analytics

↓

Admin

↓

DebugView
```

Visit website

Verify

Events appear instantly

Expected

Every event visible

---

# 12. Realtime Report

Open

```
GA4

↓

Realtime
```

Visit website

Verify

```
1 Active User
```

Expected

Realtime updates within seconds

---

# 13. Meta Test Events

Open

```
Meta Events Manager

↓

Test Events
```

Verify

PageView

Lead

CompleteRegistration

Contact

Subscribe

Expected

All events received

---

# 14. Google Ads Testing

Verify

Conversion Tags

Conversion Linker

Imported Conversions

Expected

Conversions recorded correctly

---

# 15. Microsoft Clarity Testing

Verify

Session Recording

Heatmaps

Dead Clicks

JavaScript Errors

Expected

Sessions visible

---

# 16. Search Console Verification

Verify

Property Verified

Pages Indexed

Sitemap Submitted

Coverage

Enhancements

Expected

No critical errors

---

# 17. Browser Testing

Test

Chrome

Firefox

Edge

Safari

Expected

Tracking identical

---

# 18. Device Testing

Desktop

Tablet

Mobile

Expected

Tracking consistent

---

# 19. Event Testing

Verify

page_view

scroll

search

job_search

job_view

job_apply

register

login

contact_submit

newsletter_signup

bookmark_job

share_job

download

Expected

Each event fires once

---

# 20. Conversion Testing

Verify

Registration

Login

Job Apply

WhatsApp

Telegram

Contact

Newsletter

Expected

Every conversion tracked

---

# 21. Duplicate Event Testing

Check

Duplicate Tags

Duplicate Events

Duplicate Page Views

Expected

Zero duplicates

---

# 22. SEO Testing

Verify

Canonical

Robots

Meta Tags

Structured Data

Title

Description

No JavaScript Errors

Expected

No SEO impact

---

# 23. Performance Testing

Run

PageSpeed

Lighthouse

Core Web Vitals

Expected

No tracking-related performance issues

---

# 24. Error Testing

Verify

404 Pages

500 Pages

Redirect Pages

Offline Pages

Expected

Tracking still functional

---

# 25. Consent Testing

Verify

Consent Mode

Cookie Banner

Analytics Consent

Ads Consent

Expected

Tracking follows consent settings

---

# 26. Security Testing

Verify

No API Keys Exposed

No Secrets in Data Layer

HTTPS Only

Secure Cookies

Expected

No security risks

---

# 27. GTM Workspace QA

Verify

No unpublished changes

No broken tags

No broken variables

Folders organized

Naming conventions followed

Expected

Clean workspace

---

# 28. Final QA Checklist

Developer Checklist

- GTM Installed
- Data Layer Working
- Variables Working
- Triggers Working
- Tags Working
- Events Working
- Conversions Working

Analytics Checklist

- GA4 Receiving Data
- DebugView Working
- Realtime Working
- Key Events Configured

Marketing Checklist

- Google Ads Connected
- Meta Connected
- Conversion Linker Active

SEO Checklist

- Search Console Verified
- No SEO Issues
- Structured Data Valid

---

# 29. Deployment Checklist

Before Publish

- GTM Preview Passed
- QA Completed
- Analytics Verified
- Meta Verified
- Google Ads Verified
- Clarity Verified
- Search Console Verified

After Publish

- Verify Live Tags
- Verify Live Events
- Verify Live Conversions
- Monitor Errors

---

# 30. Developer Sign-Off

Developer confirms

- Implementation Complete
- All Tests Passed
- No Console Errors
- No Duplicate Events
- Production Ready

Developer Name

```
_____________________
```

Date

```
_____________________
```

---

# 31. SEO Team Approval

SEO Engineer

```
_____________________
```

Status

```
Approved / Rejected
```

---

# 32. Analytics Team Approval

Analytics Engineer

```
_____________________
```

Status

```
Approved / Rejected
```

---

# 33. Final Deliverables

Developer must submit

- GTM Export JSON
- QA Report
- Testing Screenshots
- GA4 DebugView Screenshots
- Meta Test Event Screenshots
- Google Ads Verification
- Clarity Verification
- Deployment Report

---

# 34. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

05_TRIGGERS.md

06_TAGS.md

07_EVENTS.md

08_CONVERSIONS.md

10_GTM_EXPORT_GUIDE.md
```

---

# 35. Acceptance Criteria

This project is considered complete only when

- GTM Container Published
- All Tags Working
- All Variables Valid
- All Triggers Verified
- All Events Verified
- All Conversions Verified
- GA4 Receiving Data
- Google Ads Receiving Data
- Meta Receiving Data
- Clarity Recording Sessions
- QA Approved
- SEO Approved
- Analytics Approved
- Production Verified
- Documentation Updated