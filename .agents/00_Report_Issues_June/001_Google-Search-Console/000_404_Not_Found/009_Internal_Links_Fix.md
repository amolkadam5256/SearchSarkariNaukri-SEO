# 10 - Internal Links Fix

**Project:** SearchSarkariNaukri.com

**Module:** Internal Link Verification & Fix for Google Search Console 404 URLs

**Priority:** 🔴 Critical

**Status:** Planning

---

# Purpose

This document defines the process for identifying and fixing **internal links** that point to URLs reported under **Google Search Console → Page Indexing → Not Found (404)**.

Even after restoring or redirecting pages, internal links pointing to broken URLs should be updated to point directly to the correct destination.

The goal is to improve crawling efficiency and eliminate internal 404 errors.

---

# Reference File

## Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

Use this report together with the URL Mapping document to identify all broken internal links.

---

# Objective

Ensure that no page on the website contains an internal link pointing to a URL reported in the Google Search Console 404 report.

Internal links should always point directly to the final valid URL.

---

# Scope

Included

- Navigation links
- Job cards
- Related jobs
- Latest jobs
- Featured jobs
- Category pages
- State pages
- District pages
- City pages
- Footer links
- Header links
- Breadcrumb links
- Search results
- Pagination

Only if they contain URLs reported in the current 404 report.

Excluded

- External links
- UI redesign
- Navigation redesign
- Content rewriting
- SEO optimization unrelated to 404

---

# Internal Link Review Workflow

```
Google Search Console Report

↓

Broken URL

↓

Search Website

↓

Locate Internal Links

↓

Verify Correct Destination

↓

Update Link

↓

Testing
```

---

# Internal Link Rules

## Rule 1

### Valid Page

Condition

Destination returns

```
HTTP 200
```

Action

Keep the internal link.

---

## Rule 2

### Redirected Page

Condition

Destination returns

```
HTTP 301
```

Action

Update the internal link to point directly to the final destination.

Do not rely on redirects for internal navigation.

---

## Rule 3

### Deleted Page

Condition

Destination returns

```
HTTP 410
```

Action

Remove or replace the internal link.

---

## Rule 4

### Broken Page

Condition

Destination returns

```
HTTP 404
```

Action

Update or remove the internal link.

---

# Areas to Verify

Check internal links in

## Homepage

Verify

- Latest Jobs
- Featured Jobs
- Trending Jobs

---

## Job Details

Verify

- Related Jobs
- Similar Jobs
- Recommended Jobs

---

## Category Pages

Verify

- Job listings
- Pagination
- Featured sections

---

## State Pages

Verify

- Job links
- District links

---

## District Pages

Verify

- Job links
- Nearby districts

---

## City Pages

Verify

- Job links
- Related cities

---

## Search Results

Verify

- Job URLs
- Category URLs

---

## Breadcrumbs

Verify every breadcrumb destination.

---

## Header

Verify navigation links.

---

## Footer

Verify footer links.

---

# Internal Link Checklist

Verify

- URL exists
- Destination is correct
- No redirect
- No 404
- No duplicate links

---

# Common Issues

Examples

- Old numeric URLs
- Old slug URLs
- Deleted jobs
- Mistyped URLs
- Legacy routes

These should be updated using the URL Mapping document.

---

# Developer Scope

Developers may

- Update internal links
- Replace outdated URLs
- Remove links to deleted pages
- Update navigation references

Developers should not

- Redesign navigation
- Change page layouts
- Add new navigation items
- Remove existing features
- Modify unrelated links

---

# Not Allowed

Do not

- Redesign Header
- Redesign Footer
- Modify page layout
- Change React components
- Change application flow
- Change menus
- Change content
- Add new internal linking features

Only update links related to the reported 404 URLs.

---

# Validation

Verify

- No internal links point to HTTP 404.
- No internal links point to HTTP 410.
- Internal links do not rely on redirects.
- Navigation works correctly.
- Breadcrumbs are valid.
- Search results use valid URLs.

---

# QA Checklist

- Homepage links verified
- Job page links verified
- Related jobs verified
- Latest jobs verified
- Breadcrumbs verified
- Footer links verified
- Header links verified
- Search result links verified
- No internal 404 links remain

---

# Success Criteria

Internal link verification is complete when

- Every internal link related to the 607 Google Search Console URLs has been reviewed.
- No internal links point to broken URLs.
- Internal links point directly to the final destination.
- Navigation continues to function correctly.
- No UI or functionality has changed.

---

# Important Developer Instructions

This document only covers internal links related to the reported Google Search Console 404 URLs.

Do not

- Modify UI
- Modify layouts
- Modify React components
- Change navigation design
- Change application logic
- Rewrite content
- Add new features

Only update internal links that reference URLs reported in the Google Search Console 404 report.

---

# Next Document

```
11_GSC_Validation_Process.md
```

Purpose

Verify the completed fixes in Google Search Console, submit validation, monitor the validation progress, and confirm that the reported 404 URLs have been successfully resolved without introducing new indexing issues.
