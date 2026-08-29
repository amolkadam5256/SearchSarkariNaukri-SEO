# 04 - Database Verification

**Project:** SearchSarkariNaukri.com

**Module:** Database Verification for Google Search Console 404 URLs

**Priority:** 🔴 Critical

**Status:** Investigation

---

# Purpose

This document defines the verification process for every URL reported in the **Google Search Console → Not Found (404)** report.

The purpose is to determine whether the reported URL still exists in the application's existing database.

This document is only for verification.

It does **not** include:

- Database modifications
- Record updates
- Record deletion
- Route changes
- Redirect implementation
- UI changes
- Content changes

The only objective is to verify the existence and status of every affected URL.

---

# Reference File

Use the Google Search Console export located in this folder.

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

Every URL from this report must be verified.

---

# Objective

For every URL reported in Google Search Console determine

- Does the record exist?
- Does the Job ID exist?
- Does the slug exist?
- Is the page active?
- Is the page archived?
- Has the page been deleted?
- Is there another URL for the same record?

No implementation should be performed during this stage.

---

# Scope

Included

- Existing database verification
- Job lookup
- Slug lookup
- Archive verification
- Existing record verification

Excluded

- Database updates
- Record creation
- Record deletion
- Route implementation
- Redirect creation
- API modification
- UI changes
- Content updates

---

# Verification Workflow

```
Google Search Console URL

↓

Extract URL

↓

Extract Job ID (if available)

↓

Extract Slug (if available)

↓

Search Existing Database

↓

Record Exists?

↓

Record Status

↓

Prepare Verification Result
```

---

# Verification Rules

Each URL should receive only one verification result.

---

## Result A

### Active Record

Description

The record exists.

The page should still exist.

Status

```
Active
```

Developer Action

Verification Complete

Continue to URL Mapping.

---

## Result B

### Archived Record

Description

The recruitment has ended.

Historical information still exists.

Status

```
Archived
```

Developer Action

Verification Complete

Continue to Archive Strategy.

---

## Result C

### Slug Changed

Description

The Job ID exists.

Current slug is different.

Status

```
Slug Changed
```

Developer Action

Verification Complete

Continue to Redirect Strategy.

---

## Result D

### Legacy URL

Description

Job exists.

Only URL structure changed.

Status

```
Legacy URL
```

Developer Action

Verification Complete

Continue to Redirect Strategy.

---

## Result E

### Record Not Found

Description

No matching record found.

Status

```
Not Found
```

Developer Action

Continue investigation.

Do not delete anything yet.

---

## Result F

### Permanently Removed

Description

Record intentionally removed.

No replacement exists.

Status

```
Deleted
```

Developer Action

Continue to URL Mapping.

---

# Verification Checklist

For every URL verify

| Item           | Required |
| -------------- | -------- |
| Original URL   | ✅       |
| Job ID         | ✅       |
| Slug           | ✅       |
| Record Exists  | ✅       |
| Current Status | ✅       |
| Archive Status | ✅       |
| Notes          | ✅       |

---

# Existing Database Checks

Verify only existing records.

Examples

```
Jobs

Archived Jobs

Categories

States

Districts

Cities
```

Do not create new records.

Do not delete records.

Do not rename records.

---

# Verification Notes

While verifying

Check

- Existing slug
- Existing Job ID
- Existing URL
- Existing page status

Do not assume the Google Search Console URL is the correct URL.

Always compare with the existing application data.

---

# Rules

During verification

DO

- Verify records.
- Compare IDs.
- Compare slugs.
- Record findings.

DO NOT

- Update database.
- Delete records.
- Restore records.
- Create redirects.
- Modify routing.
- Modify UI.
- Modify content.
- Modify metadata.
- Change application logic.
- Add new features.

---

# Verification Output

Every URL should receive one result.

| Verification Result | Meaning                      |
| ------------------- | ---------------------------- |
| Active              | Existing page                |
| Archived            | Historical page              |
| Slug Changed        | Existing record with new URL |
| Legacy URL          | Old URL format               |
| Deleted             | Permanently removed          |
| Not Found           | Requires investigation       |

---

# Developer Instructions

This stage is verification only.

Developers should not

- Update SQL
- Run migrations
- Edit seed data
- Modify Prisma schema
- Change database structure
- Change routing
- Create redirects
- Modify page layout
- Change frontend
- Update backend logic

Only verify the existing application data.

---

# Use Case

This document ensures that implementation decisions are based on verified data instead of assumptions.

Incorrect verification can result in

- Wrong redirects
- Duplicate pages
- Restoring deleted content
- Redirect loops
- Invalid archive pages

Verification prevents these issues.

---

# Success Criteria

Verification is complete when

- Every URL from the Google Search Console report has been checked.
- Every URL has a verification result.
- Existing records have been identified.
- Missing records have been documented.
- No code changes have been made.
- No database changes have been made.

---

# Next Document

```
05_URL_Mapping.md
```

Purpose

Create the final mapping for every verified URL.

Each URL will receive its implementation action.

- HTTP 200
- HTTP 301
- HTTP 410

This mapping will become the implementation guide for developers.
