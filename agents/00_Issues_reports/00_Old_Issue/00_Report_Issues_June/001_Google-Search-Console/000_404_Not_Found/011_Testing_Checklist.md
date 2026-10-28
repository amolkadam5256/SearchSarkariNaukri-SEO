# 12 - Testing Checklist

**Project:** SearchSarkariNaukri.com

**Module:** Testing Checklist for Google Search Console 404 Resolution

**Priority:** 🔴 Critical

**Status:** Pre-Deployment & Post-Deployment Verification

---

# Purpose

This document defines the testing process for all fixes implemented to resolve the **Google Search Console → Page Indexing → Not Found (404)** issue.

The objective is to verify that every implemented fix works correctly before and after deployment.

This document only covers testing related to the reported **607 Google Search Console 404 URLs**.

---

# Reference Files

## Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

Use this file to verify every affected URL.

---

# Objective

Confirm that every URL from the Google Search Console report now behaves exactly as expected.

Each URL should return only one valid response.

```
200 OK

301 Permanent Redirect

410 Gone
```

No unexpected HTTP 404 responses should remain.

---

# Scope

Included

- URL Testing
- Redirect Testing
- Archive Page Testing
- Routing Testing
- Internal Link Testing
- Sitemap Verification

Excluded

- UI Testing
- Design Testing
- Responsive Testing
- Performance Testing
- Accessibility Testing
- Feature Testing
- API Testing unrelated to 404
- Database Testing unrelated to 404

---

# Testing Workflow

```
Google Search Console Report

↓

URL Mapping

↓

Developer Implementation

↓

Manual Testing

↓

Fix Issues

↓

Regression Testing

↓

Deployment

↓

Production Verification

↓

Google Search Console Validation
```

---

# Test Case 1

## Active Page

Condition

Page should exist.

Expected Result

```
HTTP 200
```

Verify

- Page loads successfully
- Correct URL
- No unexpected redirect

---

# Test Case 2

## Legacy URL

Condition

Old URL exists.

Expected Result

```
HTTP 301
```

Verify

- Redirect works
- Redirect only once
- Final destination loads
- Correct destination

---

# Test Case 3

## Archived Recruitment

Condition

Archived page exists.

Expected Result

```
HTTP 200
```

Verify

- Archive page loads
- Existing content preserved
- Correct URL

---

# Test Case 4

## Permanently Removed

Condition

No replacement exists.

Expected Result

```
HTTP 410
```

Verify

- Correct HTTP response
- No unexpected redirect

---

# Test Case 5

## Invalid URL

Condition

Invalid URL requested.

Expected Result

Correct error response according to application routing.

Verify

- Application handles invalid requests correctly.
- No routing conflicts.

---

# Redirect Testing

Verify

- HTTP 301
- Correct destination
- No redirect loops
- No redirect chains
- Final URL loads successfully

---

# Routing Testing

Verify

- Existing URLs
- Legacy URLs
- Archived URLs
- Removed URLs

Confirm correct HTTP responses.

---

# Sitemap Testing

Verify

- No 404 URLs remain.
- No redirect URLs remain.
- Only valid URLs exist.

---

# Internal Link Testing

Verify

- Homepage
- Latest Jobs
- Related Jobs
- Categories
- State Pages
- District Pages
- City Pages

Confirm no internal links point to reported 404 URLs.

---

# Browser Testing

Verify

- URL opens correctly
- Redirect behavior
- Refresh works
- Direct URL access works

---

# Regression Testing

Verify that resolving the reported 404 URLs has not affected

- Existing pages
- Existing routes
- Existing navigation
- Existing functionality

---

# Testing Checklist

## URL Verification

- Active URLs return HTTP 200
- Legacy URLs return HTTP 301
- Archive pages return HTTP 200
- Removed pages return HTTP 410

---

## Redirect Verification

- Correct destination
- Single redirect
- No loops
- No chains

---

## Sitemap Verification

- Valid XML
- No broken URLs
- No redirect URLs
- No deleted URLs

---

## Internal Links

- No links to reported 404 URLs
- Links point directly to final URLs

---

## Production Verification

Verify after deployment

- URLs accessible
- Redirects active
- Sitemap available
- Internal links updated

---

# Developer Scope

Developers may

- Test implemented fixes
- Verify routing
- Verify redirects
- Verify HTTP responses
- Confirm deployment

Developers should not

- Modify UI
- Modify layouts
- Refactor unrelated code
- Add features
- Perform unrelated optimizations

---

# Not Allowed

Do not

- Skip testing.
- Test only sample URLs.
- Ignore redirect chains.
- Ignore failed URLs.
- Modify unrelated functionality during testing.

Every URL from the report should be considered within the testing scope.

---

# Completion Criteria

Testing is complete when

- All implemented fixes have been tested.
- Expected HTTP responses are confirmed.
- No reported URLs continue returning unexpected 404 responses.
- Internal links are verified.
- Sitemap is verified.
- No regressions are identified.

---

# Success Criteria

Testing is considered successful when

- All fixes pass manual verification.
- Production behaves as expected.
- Google Search Console validation can be started with confidence.
- No additional issues are introduced while resolving the reported 404 URLs.

---

# Important Developer Instructions

This document only covers testing related to the **Google Search Console 404 issue**.

Do not

- Modify UI
- Modify layouts
- Modify React components
- Modify business logic
- Add features
- Perform unrelated code refactoring

Only verify the fixes implemented for the reported **607 URLs**.

---

# Next Document

```
13_Developer_Action_Items.md
```

Purpose

Provide the final implementation checklist for developers, listing all required actions to complete the Google Search Console 404 resolution project before final verification and issue closure.
