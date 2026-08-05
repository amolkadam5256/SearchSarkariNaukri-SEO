---

# 19. Document Approval

This document defines the official implementation standard for Google Tag Manager (GTM), Google Analytics 4 (GA4), and Data Layer tracking for SearchSarkariNaukri.

No implementation should begin until this document has been reviewed and approved.

| Role | Responsibility | Status |
|------|----------------|--------|
| SEO Lead | Defines tracking architecture and SEO requirements | Pending |
| Developer | Reviews implementation feasibility | Pending |
| QA Engineer | Validates tracking implementation | Pending |
| Project Owner | Final approval for production deployment | Pending |

---

# 20. Project Scope

This implementation covers the complete analytics and tracking architecture for SearchSarkariNaukri.

## Included

- Google Tag Manager
- Google Analytics 4
- Google Search Console Integration
- Google Ads Ready Architecture
- Microsoft Clarity Integration
- Meta Pixel Ready Architecture
- Data Layer Architecture
- Event Tracking
- Conversion Tracking
- SEO Tracking
- AI Search Tracking
- Core Web Vitals Tracking
- User Behaviour Tracking
- Server-side Tracking Ready Structure
- GTM Container Export

## Not Included

The following items are outside the scope of this implementation:

- UI Changes
- Page Layout Changes
- CSS Changes
- Database Modifications
- Backend Business Logic
- SEO Metadata Changes
- Content Writing
- Schema Changes (unless separately documented)

---

# 21. Implementation Scope

This document is the foundation for every analytics implementation.

Developers must implement:

- GTM Installation
- GA4 Configuration
- Data Layer
- Variables
- Triggers
- Tags
- Event Tracking
- Conversion Tracking
- Debug Configuration
- Production Validation
- GTM Export Container

Every implementation must be completed before the GTM container is exported.

---

# 22. Analytics Project Folder Structure

```
06_Analytics & Tracking Setup

01_PROJECT_OVERVIEW.md
02_TRACKING_REQUIREMENTS.md
03_DATALAYER_ARCHITECTURE.md
04_VARIABLES.md
05_TRIGGERS.md
06_TAGS.md
07_EVENTS.md
08_CONVERSIONS.md
09_TESTING.md
10_GTM_EXPORT_GUIDE.md

11_GTM_Container_Export
    SearchSarkariNaukri-GTM-v1.json
```

Developers must follow the documentation in the above order.

Do not skip documents.

---

# 23. GTM Workspace Strategy

Workspace Name

```
Production
```

Container

```
www.searchsarkarinaukri.com
```

Container ID

```
GTM-TC789H5W
```

Environment

```
Production
```

Developers must work only in the approved GTM workspace.

Do not publish directly without completing Preview Mode validation.

Every publish must create a new GTM Version.

---

# 24. GTM Naming Convention

Maintain consistent naming throughout the container.

## Folder

```
01 Configuration
02 GA4
03 Jobs
04 Search
05 User
06 Engagement
07 Conversions
08 Performance
09 Errors
10 Debug
11 Utilities
```

## Tags

```
TAG - GA4 Configuration

TAG - Page View

TAG - Job View

TAG - Job Apply

TAG - Search

TAG - Scroll

TAG - WhatsApp

TAG - Telegram

TAG - File Download
```

## Triggers

```
TR - All Pages

TR - Job View

TR - Job Apply

TR - Search

TR - Scroll

TR - Outbound Click
```

## Variables

```
DLV - Job ID

DLV - Job Title

DLV - Department

DLV - State

DLV - District

CONST - GA4 Measurement ID
```

Developers must follow the naming convention exactly.

---

# 25. Deployment Workflow

Implementation must follow this sequence.

1. Read all documentation.
2. Install GTM on the website.
3. Verify GTM installation.
4. Implement Data Layer.
5. Verify Data Layer.
6. Create Variables.
7. Create Triggers.
8. Create Tags.
9. Configure GA4.
10. Configure Conversions.
11. Test in GTM Preview Mode.
12. Validate in GA4 DebugView.
13. Validate in Google Tag Assistant.
14. Deploy to Production.
15. Verify Production Tracking.
16. Export GTM Container JSON.
17. Update Release Notes.
18. Submit for QA Review.

Do not skip any step.

---

# 26. Rollback Policy

If the deployment fails or tracking issues are detected:

1. Restore the previous GTM Version.
2. Roll back the Git commit if required.
3. Redeploy the previous stable version.
4. Validate GA4 tracking.
5. Validate GTM Preview.
6. Confirm production stability.
7. Document the issue.
8. Create a new implementation plan before republishing.

Never leave production with broken tracking.

---

# 27. Developer Deliverables

The developer must provide the following after implementation:

- Updated Source Code
- Git Commit Hash
- Production Deployment URL
- GTM Container Version
- GTM Container Export (.json)
- GTM Preview Screenshot
- GA4 DebugView Screenshot
- Google Tag Assistant Screenshot
- GA4 Realtime Screenshot
- Testing Report
- Validation Report
- Release Notes

Implementation is not considered complete until all deliverables have been submitted.

---

# 28. Acceptance Criteria

Implementation will be accepted only if all of the following are verified:

- GTM installed correctly
- GA4 Configuration working
- Data Layer available on every required page
- Variables populated correctly
- Triggers firing correctly
- Tags firing correctly
- Events visible in GA4 DebugView
- Realtime reporting working
- No duplicate events
- No JavaScript errors
- No Console errors
- No impact on Core Web Vitals
- GTM Container successfully exported
- GTM Container successfully imported into a test workspace

---

# 29. Developer Sign-off

Developer Name

```
______________________
```

Implementation Date

```
______________________
```

Git Commit

```
______________________
```

Container Version

```
______________________
```

Developer Signature

```
______________________
```

---

# 30. QA Sign-off

QA Engineer

```
______________________
```

Validation Date

```
______________________
```

Testing Status

```
Pass / Fail
```

QA Signature

```
______________________
```

---

# 31. SEO Sign-off

SEO Lead

```
______________________
```

Review Date

```
______________________
```

Production Approval

```
Approved / Rejected
```

Comments

```
__________________________________________
```

Signature

```
______________________
```

---

# 32. Final Notes for Developers

This document is the primary implementation guide for SearchSarkariNaukri analytics.

All tracking must be implemented using Google Tag Manager.

Do not hardcode Google Analytics, Meta Pixel, or other marketing scripts directly into the application unless explicitly approved.

The final deliverable must include a production-ready GTM container export (`SearchSarkariNaukri-GTM-v1.json`) that can be imported into another GTM container without additional configuration.

Every change must be validated using:

- GTM Preview Mode
- Google Tag Assistant
- GA4 DebugView
- GA4 Realtime Reports

No production deployment should occur until QA and SEO approvals have been completed.


 Paste this code as high in the <head> of the page as possible:
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TC789H5W');</script>
<!-- End Google Tag Manager -->



 Paste this code immediately after the opening <body> tag:
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TC789H5W"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->