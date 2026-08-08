# 01 - Overview

**Project:** SearchSarkariNaukri.com

**Module:** Google Search Console - Page Indexing - Not Found (404)

**Priority:** 🔴 Critical

**Status:** Investigation & Implementation

**Issue Type:** Technical SEO

---

# Objective

The objective of this document is to investigate and resolve all URLs reported under **Google Search Console → Page Indexing → Not Found (404)**.

This documentation provides the implementation plan for resolving the reported **607 affected URLs** while preserving the existing application behavior, routing, UI, and data.

---

# Current Issue

Google Search Console has identified multiple URLs returning **HTTP 404 (Not Found)**.

These URLs are currently excluded from Google's index because the requested pages cannot be found.

Some URLs may represent:

- Existing jobs with changed URLs
- Legacy URL structures
- Archived recruitment pages
- Deleted pages
- Incorrect internal links
- Outdated sitemap entries

Each URL must be verified individually before implementation.

---

# Reference File

The primary reference for this investigation is the Google Search Console export located in this folder.

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

This file contains all **607 affected URLs** reported by Google Search Console.

Every implementation decision should be verified against this report.

---

# Scope

This investigation only covers URLs reported in the Google Search Console **Not Found (404)** report.

Included:

- Google Search Console 404 URLs
- Route verification
- Redirect implementation
- Archive restoration
- Sitemap cleanup
- Internal link corrections
- HTTP response validation

Excluded:

- General SEO improvements
- Website redesign
- UI changes
- Content modifications
- Performance optimization
- Database redesign
- API redesign
- New feature development

---

# Expected Outcome

Each affected URL should receive one final action.

| Condition                       | Action                   |
| ------------------------------- | ------------------------ |
| Page exists                     | Return HTTP 200          |
| URL changed                     | Return HTTP 301          |
| Valuable historical recruitment | Restore as Archive (200) |
| Permanently removed             | Return HTTP 410          |

No URL should remain without a documented resolution.

---

# Investigation Process

The investigation should follow this sequence.

```
Google Search Console Export

↓

Identify URL

↓

Classify URL Type

↓

Verify Existing Record

↓

Determine Correct Action

↓

Implement Fix

↓

Test

↓

Validate in Google Search Console
```

---

# URL Types

During the investigation, URLs may belong to one of the following groups.

- Numeric Job URLs
- SEO-Friendly Job URLs
- Archived Recruitment Pages
- Category Pages
- State Pages
- District Pages
- City Pages
- Permanently Deleted Pages

Each type follows a different resolution strategy documented in this folder.

---

# Implementation Principles

The implementation must follow these principles.

## Verify Before Fixing

Every URL must be verified before any implementation.

Do not assume that every reported URL should be restored.

---

## Preserve Valuable Content

Historical government recruitment pages should be preserved whenever possible.

Avoid deleting content that may still have search value.

---

## Use Appropriate HTTP Responses

Only use:

- 200 OK
- 301 Permanent Redirect
- 410 Gone

Avoid unnecessary redirects or incorrect status codes.

---

## Maintain Existing Functionality

This implementation must not change:

- Website layout
- User interface
- Existing workflows
- Business logic
- Existing data

The goal is only to resolve reported 404 URLs.

---

# Developer Notes

While implementing fixes:

- Keep changes as small as possible.
- Avoid modifying unrelated files.
- Preserve existing routing where applicable.
- Follow the documented resolution strategy.
- Record every implemented change for QA verification.

---

# Success Criteria

This phase is complete when:

- Every URL from the Google Search Console report has been reviewed.
- Every URL has a documented action.
- Valid pages return HTTP 200.
- Redirects return HTTP 301.
- Permanently removed pages return HTTP 410.
- Sitemap no longer references invalid URLs.
- Internal links do not point to broken pages.
- Google Search Console validation completes successfully.

---

# Related Documents

Continue with the following documents in order:

```
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
