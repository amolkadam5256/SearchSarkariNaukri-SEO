# 04_VARIABLES.md

> **Project:** SearchSarkariNaukri
>
> **Document:** GTM Variables Specification
>
> **Purpose:** Define all Google Tag Manager Variables required for SearchSarkariNaukri.com. Every Trigger and Tag must use these standardized variables. No custom variable naming should be introduced outside this specification.
>
> **Audience:** Frontend Developers, GTM Developers, SEO Engineers, Analytics Engineers
>
> **Priority:** Critical
>
> **Status:** Required Before GTM Container Creation
>
> **Version:** 1.0

---

# 1. Overview

Variables are the foundation of every GTM implementation.

They store values from

- Data Layer
- Browser
- Page
- URL
- Clicks
- Forms
- JavaScript

Every Tag and Trigger will consume these Variables.

Developers must ensure all required values are available before GTM is configured.

---

# 2. Developer Responsibilities

Developers must

- Populate Data Layer variables
- Keep naming consistent
- Never hardcode values
- Keep variables reusable
- Test every variable
- Verify variables in GTM Preview

Developers must NOT

- Rename variables
- Duplicate variables
- Store business logic inside GTM
- Push incomplete values

---

# 3. Variable Naming Convention

Use

```
DLV - Data Layer Variable

URL - URL Variable

JS - JavaScript Variable

CJS - Custom JavaScript

CONST - Constant

AUTO - Auto Event Variable
```

Example

```
DLV - Job ID

DLV - Job Title

URL - Page Path

JS - Device Type

CONST - GA4 Measurement ID
```

---

# 4. Constant Variables

## CONST - GA4 Measurement ID

```
Type

Constant
```

Value

```
G-GGE1EC2V8F
```

---

## CONST - GTM Container

```
GTM-TC789H5W
```

---

## CONST - Website URL

```
https://www.searchsarkarinaukri.com
```

---

## CONST - Environment

```
Production
```

---

# 5. Data Layer Variables

These variables are mandatory.

## Page Variables

```
DLV - Page Title

DLV - Page URL

DLV - Page Path

DLV - Canonical URL

DLV - Page Type

DLV - Template Type

DLV - Language

DLV - Publish Date

DLV - Modified Date
```

---

## Job Variables

```
DLV - Job ID

DLV - Job Title

DLV - Organization

DLV - Department

DLV - State

DLV - District

DLV - City

DLV - Qualification

DLV - Employment Type

DLV - Category

DLV - Salary

DLV - Vacancy Count

DLV - Job Status

DLV - Notification URL

DLV - Apply URL

DLV - Start Date

DLV - End Date
```

---

## Search Variables

```
DLV - Search Term

DLV - Search Result Count

DLV - Search Category

DLV - Filter State

DLV - Filter Department

DLV - Sort Order
```

---

## User Variables

```
DLV - User ID

DLV - Login Status

DLV - User Role

DLV - Membership

DLV - Device Type
```

Never expose

- Email
- Mobile Number
- Password
- Personal Information

---

# 6. URL Variables

Create GTM URL Variables

```
URL - Hostname

URL - Path

URL - Full URL

URL - Query

URL - Fragment
```

---

# 7. Built-in Variables

Enable

```
Click URL

Click Text

Click Classes

Click ID

Click Element

Page URL

Page Hostname

Page Path

Referrer

Event
```

---

# 8. Auto Event Variables

Create

```
AUTO - Click URL

AUTO - Click Text

AUTO - Link Domain

AUTO - Form ID

AUTO - Form Classes

AUTO - Form Target
```

---

# 9. JavaScript Variables

## JS - Device Type

Returns

```
Desktop

Tablet

Mobile
```

---

## JS - Screen Resolution

Returns

```
Width × Height
```

---

## JS - Current Timestamp

Returns

```
ISO Timestamp
```

---

# 10. Custom JavaScript Variables

## CJS - Logged In

Returns

```
true

false
```

---

## CJS - Is Job Page

Returns

```
true

false
```

---

## CJS - Is Search Page

Returns

```
true

false
```

---

## CJS - Is Download Link

Returns

```
true

false
```

---

# 11. Variable Folder Structure

Variables must be organized within the GTM container's standard 20-folder structure:

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

Variable sub-grouping within the `02 - Variables` folder:

```
Constants

Data Layer

Page Variables

Job Variables

Search Variables

User Variables

URL Variables

JavaScript

Custom JavaScript

Auto Event
```

---

# 12. Variable Mapping

| Variable | Source |
|------------|------------|
| Job ID | Data Layer |
| Job Title | Data Layer |
| Department | Data Layer |
| State | Data Layer |
| Search Term | Data Layer |
| URL | Browser |
| Page Path | Browser |
| Device | JavaScript |
| Click URL | Auto Event |

---

# 13. Developer Checklist

Verify

- Every variable returns a value
- No undefined values
- No null values
- Correct naming
- No duplicates
- GTM Preview shows variables
- Variables update dynamically
- Variables match Data Layer

---

# 14. QA Validation

Before publishing

- All Data Layer Variables available
- All URL Variables working
- All Click Variables working
- All Form Variables working
- All JS Variables working
- No console errors
- GTM Preview passes

---

# 15. Acceptance Criteria

Implementation is complete when

- Every required GTM Variable exists
- Variables return correct values
- Tags can consume variables
- Triggers can consume variables
- No hardcoded values remain
- Variable documentation is complete

---

# 16. Deliverables

Developer must provide

- GTM Variables configured
- GTM Export (.json)
- Variable mapping sheet
- Preview screenshots
- QA report

---

# 17. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

05_TRIGGERS.md

06_TAGS.md

07_EVENTS.md

08_CONVERSIONS.md

09_TESTING.md

10_GTM_EXPORT_GUIDE.md
```

---

# 18. Developer Notes

- Every GTM Variable must have a single responsibility.
- Use Data Layer Variables wherever possible.
- Avoid unnecessary Custom JavaScript Variables.
- Constants must be used for IDs, URLs, and environment values.
- Organize all Variables into GTM folders before exporting the container.
- Test every Variable in GTM Preview Mode before creating Tags or Triggers.
- Do not change variable names after publishing, as they may be referenced by Tags, Triggers, Looker Studio, BigQuery, and future tracking implementations.

---

**Next Document**

```
05_TRIGGERS.md
```

This document will define every Trigger that uses these Variables.