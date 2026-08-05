# 10_GTM_EXPORT_GUIDE.md

> **Project:** SearchSarkariNaukri
>
> **Document:** Google Tag Manager Export Guide
>
> **Purpose:** Define the complete GTM container architecture, export structure, versioning standards, folder organization, import workflow, and deployment process for SearchSarkariNaukri.com.
>
> **Audience:** Developers, GTM Engineers, Analytics Team, SEO Team
>
> **Priority:** Critical
>
> **Status:** Required Before Production Deployment
>
> **Version:** 1.0

---

# 1. Objective

This document explains how the complete Google Tag Manager container should be built, organized, exported, version-controlled, and deployed.

The final GTM Export JSON should be production-ready and importable without requiring manual configuration.

---

# 2. Project Information

Website

```
https://www.searchsarkarinaukri.com
```

Project

```
SearchSarkariNaukri
```

Framework

```
Next.js App Router
```

Container Name

```
www.searchsarkarinaukri.com
```

Container ID

```
GTM-TC789H5W
```

GA4

```
G-GGE1EC2V8F
```

---

# 3. Export Goals

The exported container must include

- Complete Folder Structure
- Variables
- Triggers
- Tags
- Built-in Variables
- Custom Templates
- Event Tracking
- Conversion Tracking
- SEO Tracking
- Debug Configuration

No manual setup should be required after import except connecting platform IDs where necessary.

---

# 4. GTM Folder Structure

Inside GTM create folders exactly as below

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

# 5. Variables Included

Container Export must include

```
Page URL

Page Hostname

Page Path

Page Title

Referrer

Click URL

Click Text

Click Classes

Click ID

Form ID

Form Classes

Search Query

Job ID

Job Title

Department

Category

District

State

Application Mode

Source Website

Login Status

User Type

Device Type

Language

Traffic Source

Campaign

UTM Source

UTM Medium

UTM Campaign
```

---

# 6. Triggers Included

Include

```
Initialization

Consent Initialization

Page View

DOM Ready

Window Loaded

History Change

Element Visibility

Form Submit

Outbound Link

Scroll

Timer

Custom Events

Click Trigger

File Download

Search

Video

YouTube

WhatsApp

Telegram
```

---

# 7. Tags Included

GA4

```
GA4 Configuration

page_view

scroll

search

job_search

job_view

job_apply

download

share

bookmark

login

register

newsletter_signup

contact_submit
```

---

Google Ads

```
Google Tag

Conversion Linker

Remarketing

Conversions
```

---

Meta

```
Base Pixel

PageView

ViewContent

Lead

Contact

CompleteRegistration

Search

Subscribe
```

---

Microsoft Clarity

```
Clarity Base Tag
```

---

Custom

```
DataLayer Logger

Debug Events

Console Logger (Development Only)
```

---

# 8. Naming Convention

Variables

```
V - Page URL

V - Job ID

V - Department
```

Triggers

```
T - Page View

T - Job Apply

T - Scroll
```

Tags

```
GA4 - Page View

GA4 - Job View

GA4 - Job Apply

META - Lead

ADS - Conversion

CLARITY - Base
```

Folders

```
01 - Configuration

02 - Variables

03 - Triggers
```

---

# 9. Export File Naming

Every export should follow

```
SearchSarkariNaukri_GTM_v1.0.json
```

Future versions

```
SearchSarkariNaukri_GTM_v1.1.json

SearchSarkariNaukri_GTM_v2.0.json
```

> **Note:** The delivered container in `11_GTM_Container_Export/` is named `SearchSarkariNaukri-GTM-v1.json` (hyphens), matching `01_PROJECT_OVERVIEW.md` Section 22 and Section 27. This document originally specified underscores. Hyphenated naming is the standard going forward — do not rename the delivered file; update future exports to match it instead.

---

# 10. Version Control

Every export must include

Version Number

Created Date

Developer Name

Changes

Example

```
Version

1.0

Changes

Initial Production Release
```

---

# 11. Import Procedure

Developer

Open

```
Google Tag Manager
```

↓

Select Container

↓

Admin

↓

Import Container

↓

Select

```
SearchSarkariNaukri_GTM_v1.0.json
```

↓

Choose

```
Merge
```

↓

Overwrite Conflicting

```
No
```

↓

Review

↓

Import

---

# 12. Validation After Import

Verify

Folders

Variables

Triggers

Tags

Templates

No Errors

---

# 13. Preview Testing

Run

```
Preview Mode
```

Verify

Every page

Homepage

Jobs

Job Details

Departments

States

Districts

Admit Cards

Results

Answer Keys

Blogs

Search

Forms

---

# 14. Publishing Workflow

Step 1

Import

↓

Step 2

Preview

↓

Step 3

Fix Errors

↓

Step 4

QA Approval

↓

Step 5

SEO Approval

↓

Step 6

Analytics Approval

↓

Step 7

Publish

---

# 15. Rollback Strategy

If deployment fails

Restore previous version

```
Version History

↓

Restore

↓

Publish
```

---

# 16. Export Validation Checklist

Developer must verify

- No Missing Variables
- No Broken Tags
- No Broken Triggers
- No Duplicate Tags
- No Duplicate Events
- No Invalid IDs
- No Console Errors
- No Template Errors

---

# 17. Required Deliverables

Developer must submit

- GTM Export JSON
- Version History
- QA Report
- Debug Screenshots
- Preview Screenshots
- Published Version Screenshot

---

# 18. Future Container Updates

Every new feature must

- Use Existing Naming Convention
- Be Added to Correct Folder
- Update Documentation
- Update Version Number
- Be Tested Before Publish

---

# 19. Developer Instructions

Developer must

- Never edit tags directly in Production.
- Use Workspace for every change.
- Export container before every deployment.
- Create a backup before importing a new version.
- Test every event using Preview Mode.
- Validate all events in GA4 DebugView.
- Verify Meta Pixel Test Events.
- Verify Google Ads Conversions.
- Confirm Microsoft Clarity sessions.
- Update documentation after every container change.

---

# 20. Final Acceptance Criteria

The GTM Export is considered production-ready only if

- Container Imports Successfully
- No Import Errors
- All Variables Available
- All Triggers Working
- All Tags Firing Correctly
- GA4 Receiving Events
- Meta Receiving Events
- Google Ads Receiving Conversions
- Clarity Recording Sessions
- SEO Team Approved
- Analytics Team Approved
- Developer Approved
- Documentation Updated

---

# 21. Related Documents

```
01_PROJECT_OVERVIEW.md

02_TRACKING_REQUIREMENTS.md

03_DATALAYER_ARCHITECTURE.md

04_VARIABLES.md

05_TRIGGERS.md

06_TAGS.md

07_EVENTS.md

08_CONVERSIONS.md

09_TESTING.md

11_GTM_Container_Export/README.md
(consolidated: container specification, import checklist, versioning, and release checklist for this specific export — see this document for the general procedures and 04-08 for the source specification)

11_GTM_Container_Export/SearchSarkariNaukri-GTM-v1.json
```