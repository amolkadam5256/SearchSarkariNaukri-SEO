# 06 - Redirect Strategy

**Project:** SearchSarkariNaukri.com

**Module:** Redirect Strategy for Google Search Console 404 URLs

**Priority:** 🔴 Critical

**Status:** Planning

---

# Purpose

This document defines the redirect strategy for URLs reported in **Google Search Console → Page Indexing → Not Found (404)**.

The objective is to restore SEO value wherever possible while maintaining a clean URL structure.

This document only explains **when a redirect should be used** and **when it should not**.

It does not contain actual redirect implementation code.

---

# Reference File

Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

All redirect decisions should be based on verified URLs from this report.

---

# Objective

Every URL should receive the correct HTTP response.

Possible responses

```
200 OK

301 Permanent Redirect

410 Gone
```

Do not use redirects unless they are the correct solution.

---

# Redirect Workflow

```
Google Search Console URL

↓

Database Verification

↓

URL Mapping

↓

Determine Redirect Requirement

↓

Developer Implementation

↓

Testing

↓

Google Search Console Validation
```

---

# Redirect Rules

## Rule 1

### Existing Active Page

Condition

- Correct URL already exists
- Page loads successfully

Action

```
No Redirect
```

Response

```
HTTP 200
```

---

## Rule 2

### Legacy Numeric URL

Example

```
/jobs/855
```

Current URL

```
/jobs/staff-selection-commission-ssc-je-2026-855
```

Action

```
301 Permanent Redirect
```

---

## Rule 3

### Old SEO Slug

Example

Old

```
/jobs/barc-technical-officer-855
```

Current

```
/jobs/bhabha-atomic-research-centre-technical-officer-855
```

Action

```
301 Permanent Redirect
```

---

## Rule 4

### Archived Recruitment

Condition

Recruitment closed

Historical page still exists

Action

```
Do NOT Redirect
```

Return

```
HTTP 200
```

Display archive page.

---

## Rule 5

### Permanently Deleted

Condition

- No replacement
- No archive
- No SEO value

Action

```
No Redirect
```

Return

```
HTTP 410 Gone
```

---

# Redirect Decision Matrix

| Situation             | Action |
| --------------------- | ------ |
| Active page           | 200    |
| Legacy numeric URL    | 301    |
| Old slug              | 301    |
| Canonical URL changed | 301    |
| Archived page         | 200    |
| Permanently removed   | 410    |

---

# Redirect Principles

Always redirect

- Old URL
- Duplicate URL
- Legacy URL

Never redirect

- To homepage
- To unrelated pages
- To category pages unless it is the correct replacement
- To search pages
- To random pages

---

# Redirect Requirements

Every redirect should

- Have one destination
- Use HTTP 301
- Avoid redirect chains
- Avoid redirect loops
- Point to the most relevant page

---

# Redirect Validation Checklist

Verify

- Correct source URL
- Correct destination URL
- HTTP 301 response
- Single redirect only
- Destination loads correctly
- Canonical is correct

---

# Developer Scope

Developers may

- Add redirect rules
- Update routing for legacy URLs
- Configure permanent redirects
- Validate redirect responses

Developers should not

- Change UI
- Change layout
- Change page design
- Modify content
- Modify metadata unrelated to redirects
- Update business logic
- Change application functionality
- Modify unrelated routes

---

# Not Allowed

Do not

- Redirect every 404 page
- Redirect deleted pages to homepage
- Redirect unrelated jobs
- Redirect all old jobs to one page
- Create redirect chains
- Create multiple redirects for one URL

---

# Testing

Verify

- HTTP Status
- Destination URL
- Canonical URL
- Browser redirect
- Internal links
- Google Search Console validation

---

# Deliverables

After this phase

- Redirect list finalized
- Redirect rules prepared
- Legacy URLs mapped
- Deleted URLs excluded
- Archive pages identified

---

# Success Criteria

The redirect strategy is complete when

- Every redirect has a valid destination.
- No unnecessary redirects exist.
- No redirect loops exist.
- No redirect chains exist.
- Homepage redirects are avoided.
- Every redirect follows the URL Mapping document.

---

# Important Developer Instructions

This document only defines the redirect strategy.

Do not

- Modify UI
- Modify layouts
- Modify frontend components
- Change page content
- Change application logic
- Update database records
- Add new features

Only implement redirect behavior for verified URLs identified in previous documents.

---

# Next Document

```
07_Archive_Expired_Jobs.md
```

Purpose

Define how expired government recruitment pages should be handled, when they should remain accessible as archived pages, and when they should return HTTP 200 instead of becoming 404 pages, without changing the existing UI, application flow, or business logic.
