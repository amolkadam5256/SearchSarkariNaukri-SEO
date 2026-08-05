# 01_404_Not_Found

## Overview

This folder contains the complete documentation, implementation plan, validation process, and developer tasks for resolving the **Google Search Console – Page Indexing → Not Found (404)** issue on **SearchSarkariNaukri.com**.

The current Google Search Console report contains **607 affected URLs** that are returning **HTTP 404 (Not Found)**. These URLs are currently excluded from Google's index and require investigation before any implementation begins.

The objective of this folder is to provide a structured workflow for identifying the cause of each URL, deciding the correct action, implementing the fix, validating the result, and ensuring the issue does not reoccur.

---

# Scope

This documentation only covers the following issue:

```
Google Search Console

↓

Page Indexing

↓

Not Found (404)
```

This folder **does not** include:

- General SEO audits
- Technical SEO improvements unrelated to 404 errors
- Website redesign
- UI/UX improvements
- Content rewriting
- Performance optimization
- Core Web Vitals optimization
- API refactoring
- Database redesign
- New feature development
- Business logic changes
- Metadata optimization unrelated to 404 pages

The implementation should focus only on resolving URLs reported under the Google Search Console 404 report.

---

# Goal

The goal is **not** to restore every reported URL.

Each affected URL should first be audited and then assigned one of the following actions.

- Restore existing page
- Redirect to the correct URL
- Convert into an archived page
- Return HTTP 410 if permanently removed

Every action should be based on the existing data available in the project.

---

# Primary Reference File

All investigations must begin using the Google Search Console export located in this folder.

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

This Excel file contains all **607 URLs** reported by Google Search Console.

It is the primary source of truth for the entire implementation.

Do not skip any URL contained within this report.

---

# Documentation Structure

This folder contains the following implementation documents.

```
README.md

01_Overview.md

02_GSC_404_Report_Analysis.md

03_URL_Classification.md

04_Database_Verification.md

05_URL_Mapping.md

06_Redirect_Strategy.md

07_Archive_Expired_Jobs.md

08_NextJS_404_Routing.md

09_Sitemap_Cleanup.md

10_Internal_Links_Fix.md

11_GSC_Validation_Process.md

12_Testing_Checklist.md

13_Developer_Action_Items.md

14_Final_Verification.md
```

Each document represents one stage of the implementation process.

---

# Implementation Principles

Before making any changes, follow these principles.

## Do not restore every URL automatically.

Every URL should first be verified.

---

## Do not delete valuable government recruitment pages.

If historical information still exists, preserve it as an archive page instead of returning 404.

---

## Do not redirect unrelated pages.

Redirects should only point to the most relevant destination.

Avoid redirecting everything to the homepage.

---

## Do not modify existing UI.

No layout changes.

No component redesign.

No styling updates.

No frontend redesign.

---

## Do not change business logic.

The purpose is only to fix URL handling.

Existing application functionality should remain unchanged.

---

## Do not modify database data unnecessarily.

Only verify records.

Do not update existing job data unless required to resolve the specific 404 issue.

---

## Do not rename routes unless required.

Use the existing routing structure wherever possible.

---

## Do not remove pages without verification.

Every page must first be classified before removal.

---

# Expected Developer Workflow

Step 1

Open the Google Search Console Excel report.

↓

Step 2

Classify every affected URL.

↓

Step 3

Verify whether the page still exists.

↓

Step 4

Determine the appropriate action.

- Restore
- Redirect
- Archive
- Remove

↓

Step 5

Implement the fix.

↓

Step 6

Update sitemap if necessary.

↓

Step 7

Verify internal links.

↓

Step 8

Run testing.

↓

Step 9

Deploy.

↓

Step 10

Validate in Google Search Console.

---

# Allowed Changes

Developers may only perform changes directly related to resolving the reported 404 URLs.

Examples include:

- Route handling
- Redirect implementation
- Legacy URL handling
- Archive page restoration
- Sitemap cleanup
- Internal link correction
- HTTP response correction

---

# Not Allowed

The following changes are outside the scope of this task.

- UI redesign
- Component redesign
- CSS changes
- Database restructuring
- API redesign
- Feature additions
- Content rewriting
- SEO improvements unrelated to 404
- Performance optimization
- Authentication changes
- Dashboard modifications
- Admin panel changes

---

# Success Criteria

The implementation will be considered complete when:

- Every URL from the Google Search Console report has been reviewed.
- Every URL has a documented action.
- Valid pages return HTTP 200.
- Redirects return HTTP 301.
- Permanently removed pages return HTTP 410 where applicable.
- Invalid URLs are removed from the sitemap.
- Internal links no longer point to broken URLs.
- Google Search Console validation completes successfully.
- No unintended UI, data, or business logic changes have been introduced.

---

# Notes for Developers

This documentation is intended to resolve **only** the Google Search Console 404 issue.

Avoid making unrelated improvements during implementation.

If additional issues are discovered during development, document them separately rather than including them in this implementation.

The objective is to fix the reported 404 errors with the minimum necessary code changes while preserving the existing application behavior, user interface, routing structure, and data integrity.
