# 08 - Routing & 404 Handling

**Project:** SearchSarkariNaukri.com

**Module:** Routing & 404 URL Handling

**Priority:** 🔴 Critical

**Status:** Planning

---

# Purpose

This document defines how the application's existing routing should handle URLs reported in the Google Search Console **Not Found (404)** report.

The objective is to ensure that verified URLs return the correct HTTP response without changing the application's routing architecture or introducing unrelated changes.

This document only covers routing behavior related to the reported 404 URLs.

---

# Reference File

Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

All routing verification should be based on URLs contained in this report.

---

# Objective

Verify that the application's routing correctly handles:

- Existing URLs
- Legacy URLs
- Changed URLs
- Archived URLs
- Permanently removed URLs

without affecting unrelated routes.

---

# Scope

Included

- Existing routing
- Legacy URL handling
- URL parameter validation
- Slug matching
- Route matching
- 404 handling
- Redirect routing

Excluded

- UI redesign
- Navigation changes
- Component redesign
- Route restructuring
- Feature development
- Performance optimization

---

# Routing Verification Workflow

```
Google Search Console URL

↓

Match Existing Route

↓

Verify URL Parameters

↓

Verify Existing Record

↓

Determine Correct Response

↓

Implementation
```

---

# Routing Rules

## Existing URL

Condition

The requested URL exists.

Expected Response

```
HTTP 200
```

---

## Legacy URL

Condition

Legacy URL matches an existing page.

Expected Response

```
HTTP 301
```

---

## Changed Slug

Condition

Only the slug has changed.

Expected Response

```
HTTP 301
```

---

## Archived Page

Condition

Archived recruitment exists.

Expected Response

```
HTTP 200
```

---

## Permanently Removed

Condition

No replacement exists.

Expected Response

```
HTTP 410
```

---

# Route Validation

Verify

- Route exists
- URL parameters are valid
- Slug parsing works correctly
- Existing page is returned
- Invalid URLs return the correct response

---

# URL Parameter Validation

Verify

- Missing ID
- Missing slug
- Invalid slug
- Invalid ID
- Malformed URL

Only verified URLs should be handled.

---

# Existing Routing

Review only the routing required for resolving the reported 404 URLs.

Do not modify unrelated application routes.

---

# Redirect Handling

Verify

- Legacy URLs
- Old slugs
- Numeric URLs

Ensure redirects follow the URL Mapping document.

---

# Error Handling

Verify

- Invalid URLs
- Missing records
- Deleted pages

Ensure the correct HTTP response is returned.

---

# Developer Scope

Developers may

- Update routing for verified URLs
- Implement approved redirects
- Correct route matching
- Handle legacy URLs

Developers should not

- Redesign routing
- Change application architecture
- Rename routes unnecessarily
- Modify navigation
- Change business logic

---

# Not Allowed

Do not

- Change URL structure
- Rename existing routes
- Modify page layout
- Change components
- Change page content
- Add new routing features
- Refactor unrelated routes

---

# Testing Checklist

Verify

- Existing routes load correctly
- Legacy URLs redirect correctly
- Archived pages load
- Deleted pages return correct status
- No routing conflicts
- No redirect loops

---

# Success Criteria

Routing verification is complete when

- All verified URLs resolve correctly.
- Legacy URLs redirect correctly.
- Archived pages remain accessible.
- Deleted pages return the correct response.
- Existing routing continues to work without regression.

---

# Important Developer Instructions

This document only covers routing behavior required to resolve the Google Search Console 404 report.

Do not

- Modify UI
- Modify layouts
- Modify React components
- Refactor routing architecture
- Change application flow
- Add new features

Only implement routing changes required for the verified 404 URLs.

---

# Next Document

```
09_Sitemap_Cleanup.md
```

Purpose

Review and clean the XML sitemap by removing invalid 404 URLs, ensuring only valid, crawlable URLs remain. This document is limited to sitemap updates related to the Google Search Console 404 report and does not include other SEO improvements.
