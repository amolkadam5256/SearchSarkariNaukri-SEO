# 02_TRACKING_REQUIREMENTS.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Tracking Requirements
>
> **Purpose:** Define the complete tracking requirements for SearchSarkariNaukri.com before creating the Google Tag Manager container, GA4 configuration, Meta Pixel implementation, and future marketing integrations.
>
> **Audience:** Developers, SEO Engineers, Analytics Engineers, GTM Specialists, QA Team
>
> **Priority:** Critical
>
> **Status:** Required Before GTM Implementation
>
> **Version:** 1.0

---

# 1. Overview

This document defines every tracking requirement that must be implemented on SearchSarkariNaukri.com.

The purpose of this document is to ensure:

- Every important user interaction is measurable.
- SEO performance can be monitored.
- User behaviour can be analyzed.
- Conversion funnels can be optimized.
- AI Search traffic can be measured.
- Future advertising platforms can be integrated without modifying website code.

This document must be completed before creating the GTM Export Container.

---

# 2. Developer Scope

## Developers MUST

- Install Google Tag Manager
- Implement Data Layer
- Push Data Layer Events
- Add Required Page Variables
- Maintain Existing UI
- Maintain Existing SEO
- Keep Website Performance Stable
- Test Every Event
- Deploy to Production
- Support Future GTM Updates

---

## Developers MUST NOT

- Hardcode GA4 Events
- Hardcode Meta Pixel
- Hardcode Google Ads Events
- Fire Analytics Directly
- Modify Page Design
- Change Existing UI
- Change Existing Layout
- Modify Metadata
- Remove Existing SEO Code
- Break Core Web Vitals

---

# 3. Tracking Architecture

The website must follow this architecture.

```
User

↓

Website

↓

Data Layer

↓

Google Tag Manager

↓

GA4

↓

Meta Pixel

↓

Google Ads

↓

Looker Studio

↓

BigQuery
```

All tracking starts from the Data Layer.

No tracking should bypass GTM.

---

# 4. Tracking Objectives

The tracking system must measure:

## SEO

- Organic Landing Pages
- Organic Sessions
- Search Console Performance
- AI Search Traffic
- Index Coverage
- Page Engagement

---

## User Behaviour

- Page Views
- Scroll Depth
- Session Duration
- Returning Users
- Internal Search
- Navigation Flow
- Exit Pages

---

## Recruitment Funnel

- Job View
- Notification View
- Admit Card View
- Result View
- Apply Button Click
- Official Website Click
- Download Notification
- Share Job
- Save Job

---

## Engagement

- WhatsApp Click
- Telegram Join
- Social Share
- Newsletter Signup
- Contact Form
- Feedback Submission

---

## Performance

- Core Web Vitals
- JavaScript Errors
- API Failures
- Slow Pages
- Broken Links

---

# 5. Page Types

Tracking must work on every page.

## Homepage

```
/
```

Track

- Page View
- Scroll
- Search
- Featured Jobs
- Categories

---

## Jobs Listing

```
/jobs
```

Track

- Filters
- Pagination
- Search
- Sort
- Category Click

---

## Job Details

```
/jobs/:id
```

Track

- Job View
- Apply Click
- Download Notification
- Share
- Bookmark
- Related Job Click

---

## State Pages

```
/state/*
```

Track

- Page View
- Search
- District Click

---

## District Pages

```
/district/*
```

Track

- Page View
- Job Click

---

## Department Pages

```
/department/*
```

Track

- Department Selection
- Job Click

---

## Admit Cards

Track

- Admit Card View
- Download
- Official Link

---

## Results

Track

- Result View
- Download
- Official Website

---

## Answer Key

Track

- Download
- Official Link

---

## Syllabus

Track

- PDF Download

---

## Static Pages

Track

- Page View
- CTA Clicks

---

# 6. Required Data Layer

Every tracked interaction must push a Data Layer event.

Example:

```javascript
window.dataLayer.push({
event: "job_view",
job_id: "3553",
job_title: "SSC CGL Recruitment",
department: "SSC",
state: "Maharashtra"
});
```

Developers must NEVER send events directly to GA4.

---

# 7. Required Event Naming Standard

All events must use snake_case.

Correct

```
page_view

job_view

job_apply

search_submit

download_pdf

whatsapp_click
```

Incorrect

```
PageView

Job View

jobView

JOB_VIEW
```

---

# 8. Required Page Information

Every page must expose:

```
Page URL

Page Path

Page Title

Canonical URL

Language

Template Type

Author

Publish Date

Modified Date
```

---

# 9. Job Information

Job pages must expose

```
Job ID

Job Title

Department

Organization

State

District

Qualification

Category

Application Start Date

Application End Date

Official Website

Official Notification

Application Mode

Status
```

---

# 10. Search Tracking

Track

```
Search Term

Result Count

Search Category

Filters

Search Source
```

---

# 11. Click Tracking

Track

- Apply Button
- Official Website
- Notification PDF
- WhatsApp
- Telegram
- Share
- Download
- Internal Navigation
- External Links

---

# 12. Scroll Tracking

Fire events at

- 25%
- 50%
- 75%
- 90%
- 100%

Only fire once per page load.

---

# 13. File Download Tracking

Track

```
Notification PDF

Answer Key

Result PDF

Syllabus

Advertisement PDF

ZIP Files
```

Capture

- File Name
- File Type
- URL
- Page

---

# 14. Outbound Link Tracking

Track

- Official Recruitment Website
- Apply Online
- Official Notification
- External Resources

Capture

- Destination URL
- Anchor Text
- Page URL

---

# 15. Form Tracking

Track

- Contact Form
- Newsletter
- Registration
- Login
- Feedback

Capture

- Success
- Failure
- Validation Errors

---

# 16. Error Tracking

Automatically capture

- JavaScript Errors
- API Errors
- 404 Pages
- 500 Pages
- Network Errors

---

# 17. Consent Requirements

Tracking must support:

- Google Consent Mode v2
- Analytics Consent
- Ad Storage
- Ad User Data
- Ad Personalization

Consent settings must be configurable through GTM.

---

# 18. Future Platform Support

The implementation must support future integrations with:

- Google Ads
- Meta Pixel
- Microsoft Clarity
- LinkedIn Insight Tag
- Pinterest Tag
- X Pixel
- Hotjar
- Microsoft Ads
- BigQuery
- Looker Studio

No website code changes should be required to add these platforms.

---

# 19. GTM Folder Structure

Developers must organize the GTM container using folders.

Required folders:

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

# 20. QA Requirements

Before deployment verify:

- GTM Installed
- Preview Mode Passed
- GA4 Receiving Events
- DebugView Working
- Data Layer Valid
- No Duplicate Events
- No Missing Parameters
- No Console Errors
- No Performance Issues
- No Layout Changes

---

# 21. Acceptance Criteria

Implementation is complete only when:

- Every required event fires correctly.
- Every required parameter is populated.
- GTM Preview passes without errors.
- GA4 DebugView receives all events.
- SEO performance is unaffected.
- Website UI is unchanged.
- Core Web Vitals are not degraded.
- Documentation is updated.
- GTM Container Export (.json) is generated and tested.

---

# 22. Deliverables

The developer must provide:

- GTM Container Export (.json)
- Data Layer Documentation
- Event Documentation
- Variables List
- Triggers List
- Tags List
- Testing Report
- QA Checklist
- Release Notes
- Implementation Summary

---

# 23. Developer Sign-off Checklist

Before handing over the implementation, confirm:

- [ ] GTM code installed correctly
- [ ] Container ID matches **GTM-TC789H5W**
- [ ] GA4 Measurement ID matches **G-GGE1EC2V8F**
- [ ] Data Layer implemented
- [ ] All required events pushed
- [ ] GTM Preview passed
- [ ] GA4 DebugView verified
- [ ] No duplicate tracking
- [ ] No JavaScript errors
- [ ] No UI or layout changes
- [ ] No SEO metadata changes
- [ ] Website performance unchanged
- [ ] Production deployment completed
- [ ] GTM Export JSON delivered
- [ ] Documentation updated

---

# 24. Related Documents

This document must be implemented together with:

```
01_PROJECT_OVERVIEW.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

05_TRIGGERS.md

06_TAGS.md

07_EVENTS.md

08_CONVERSIONS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 25. Implementation Sequence

Developers must follow this exact order:

1. Read Project Overview
2. Install GTM
3. Implement Data Layer
4. Create Variables
5. Create Triggers
6. Create Tags
7. Configure GA4
8. Configure Consent Mode
9. Configure Conversions
10. Test in Preview Mode
11. Verify in GA4 DebugView
12. Publish GTM Container
13. Export GTM Container (.json)
14. Deliver documentation and testing report

---

**End of Document**