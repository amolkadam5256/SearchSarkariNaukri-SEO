# 07 - Archive Expired Jobs

**Project:** SearchSarkariNaukri.com

**Module:** Archive Strategy for Expired Government Recruitment Pages

**Priority:** 🔴 High

**Status:** Planning

---

# Purpose

This document defines how expired government recruitment pages should be handled when they appear in the **Google Search Console → Page Indexing → Not Found (404)** report.

Many government recruitment pages continue to receive organic traffic even after the recruitment process has ended.

Instead of deleting these pages and returning **404 Not Found**, they should be evaluated to determine whether they should remain available as archived pages.

This document only defines the decision-making process.

It does not include implementation details.

---

# Reference File

Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

Use this report together with the previous verification documents to identify expired recruitment pages.

---

# Objective

Determine whether an expired recruitment page should

- Continue as an archive page
- Be redirected
- Be permanently removed

The decision should always be based on the existing data.

---

# Scope

Included

- Expired recruitment pages
- Historical government jobs
- Previous notifications
- Archive eligibility

Excluded

- Active jobs
- UI redesign
- Content rewriting
- New archive templates
- Database modifications
- Feature development

---

# Why Archive?

Government recruitment pages often continue receiving traffic for searches such as

- Previous Notification
- Previous Vacancy
- Official PDF
- Previous Recruitment
- Salary
- Eligibility
- Selection Process
- Previous Year Recruitment

Deleting these pages may result in

- Loss of organic traffic
- Loss of backlinks
- Loss of indexed pages
- Poor user experience

---

# Archive Decision Workflow

```
Google Search Console URL

↓

Database Verification

↓

Recruitment Exists?

↓

Recruitment Closed?

↓

Historical Value?

↓

Archive Decision
```

---

# Archive Decision Rules

## Rule 1

### Recruitment Still Active

Condition

Recruitment is active.

Action

```
HTTP 200
```

No archive required.

---

## Rule 2

### Recruitment Closed

Condition

Recruitment has ended.

Historical information still exists.

Action

```
Archive Page

HTTP 200
```

---

## Rule 3

### Recruitment Replaced

Condition

A newer recruitment exists.

Action

Keep the previous recruitment available if it still contains useful historical information.

Do not remove solely because a newer recruitment has been published.

---

## Rule 4

### Permanently Removed

Condition

- No record
- No archive
- No historical value
- No replacement

Action

```
HTTP 410
```

---

# Archive Eligibility Checklist

Before deciding

Verify

- Recruitment exists
- Notification existed
- Organization exists
- Historical value exists
- Previous searches exist
- Existing backlinks (if known)

---

# Pages Commonly Suitable for Archive

Examples

```
SSC

UPSC

MPSC

IBPS

BARC

Railway

Bank Recruitment

DRDO

ISRO

NIELIT

NTPC

PSU Recruitment
```

These pages are often searched even after recruitment closes.

---

# Pages Usually Not Archived

Examples

- Invalid URLs
- Test URLs
- Duplicate URLs
- Incorrect URLs
- Empty pages
- Temporary pages
- Mistyped URLs

---

# Archive Principles

Preserve

- Historical recruitment information
- Existing URLs where appropriate
- Organic search value

Avoid

- Removing valuable pages
- Redirecting archived pages to unrelated pages
- Returning 404 for useful historical content

---

# Developer Scope

Developers may

- Verify archive eligibility
- Preserve existing archive pages
- Ensure archived pages return the correct HTTP response

Developers should not

- Redesign archive pages
- Modify UI
- Rewrite page content
- Add new archive functionality
- Change existing business logic

---

# Not Allowed

Do not

- Delete valuable recruitment pages
- Redirect archived pages to homepage
- Redirect archived jobs to unrelated jobs
- Remove historical information without verification
- Modify archive content during this task

---

# Validation Checklist

Verify

- Recruitment status
- Archive eligibility
- Existing URL
- HTTP response
- Existing routing

---

# Deliverables

After this phase

- Archive candidates identified
- Non-archive pages identified
- Historical pages preserved
- Permanent removals documented

---

# Success Criteria

This stage is complete when

- Every expired recruitment page has been reviewed.
- Archive candidates have been identified.
- Valuable historical pages are preserved.
- No useful recruitment page is unnecessarily removed.
- Permanently removed pages are clearly documented.

---

# Important Developer Instructions

This document is only for deciding whether pages should remain available as archives.

Do not

- Modify UI
- Modify layouts
- Change frontend components
- Rewrite page content
- Modify application logic
- Update database records
- Add archive features
- Change unrelated functionality

Only determine archive eligibility for URLs reported in the Google Search Console 404 report.

---

# Next Document

```
08_Routing_404_Handling.md
```

Purpose

Review the existing Next.js routing only where it affects the reported 404 URLs. Ensure legacy URLs, dynamic routes, slug resolution, and `notFound()` behavior correctly handle verified URLs without introducing UI changes, new features, or unrelated routing modifications.
