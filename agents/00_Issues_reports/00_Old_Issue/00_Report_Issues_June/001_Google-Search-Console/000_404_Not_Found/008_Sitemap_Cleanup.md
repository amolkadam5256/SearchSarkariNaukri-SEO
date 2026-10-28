# 09 - Sitemap Cleanup

**Project:** SearchSarkariNaukri.com

**Module:** Sitemap Cleanup for Google Search Console 404 URLs

**Priority:** 🔴 Critical

**Status:** Planning

---

# Purpose

This document defines the process for reviewing and cleaning all XML sitemaps after resolving the **Google Search Console → Page Indexing → Not Found (404)** issue.

The objective is to ensure that search engines only discover valid and accessible URLs.

Only URLs affected by the current **404 report** are included in this document.

---

# Reference File

## Google Search Console Export

```
https___www.searchsarkarinaukri.com_-Coverage-Drilldown-2026-08-05.xlsx
```

Use this report to identify URLs that should be removed or retained in the sitemap.

---

# Objective

The sitemap should contain only URLs that:

- Return HTTP 200
- Are intended to be indexed
- Exist on the website
- Are the canonical version

Invalid URLs should not remain in any sitemap.

---

# Scope

Included

- XML Sitemap
- Sitemap Index
- Job Sitemap
- Category Sitemap
- State Sitemap
- District Sitemap
- City Sitemap

Only if they contain URLs reported in the 404 report.

Excluded

- Sitemap redesign
- Sitemap structure changes
- New sitemap generation logic
- SEO optimization unrelated to 404
- Robots.txt optimization

---

# Sitemap Review Workflow

```
Google Search Console Report

↓

Identify 404 URL

↓

Locate URL in Sitemap

↓

Verify Current Status

↓

Remove / Keep URL

↓

Regenerate Sitemap

↓

Validate Sitemap
```

---

# Sitemap Rules

## Rule 1

### Valid Page

Condition

Page exists.

Returns

```
HTTP 200
```

Action

Keep URL in sitemap.

---

## Rule 2

### Redirect URL

Condition

URL redirects.

Returns

```
HTTP 301
```

Action

Remove redirected URL.

Only include the final destination.

---

## Rule 3

### Deleted Page

Condition

Returns

```
HTTP 410
```

Action

Remove from sitemap.

---

## Rule 4

### 404 Page

Condition

Returns

```
HTTP 404
```

Action

Remove immediately.

---

## Rule 5

### Archive Page

Condition

Returns

```
HTTP 200
```

Action

Keep in sitemap if intended for indexing.

---

# Sitemap Verification Checklist

Verify

- URL exists
- HTTP 200
- Canonical URL
- No duplicate entries
- No redirected URLs
- No deleted URLs
- No broken URLs

---

# URLs That Must Be Removed

Remove

- 404 URLs
- 410 URLs
- Redirect source URLs
- Duplicate URLs
- Invalid URLs
- Mistyped URLs

---

# URLs That Must Remain

Keep

- Active Job Pages
- Archive Pages
- Category Pages
- State Pages
- District Pages
- City Pages

Only if they return

```
HTTP 200
```

---

# Common Sitemap Issues

Examples

- Old numeric URLs
- Old slug URLs
- Deleted jobs
- Duplicate URLs
- Redirect URLs
- Invalid URLs

These should not remain in the sitemap.

---

# Developer Scope

Developers may

- Remove invalid URLs
- Update sitemap entries
- Regenerate sitemap
- Validate sitemap output

Developers should not

- Change sitemap format
- Modify sitemap architecture
- Add unrelated URLs
- Modify indexing strategy

---

# Not Allowed

Do not

- Include 404 URLs
- Include redirected URLs
- Include duplicate URLs
- Include deleted pages
- Include invalid pages

Do not redesign the sitemap structure during this task.

---

# Validation

After regeneration verify

- Sitemap loads successfully
- No 404 URLs remain
- No redirect URLs remain
- Only canonical URLs exist
- XML format is valid

---

# QA Checklist

Verify

- Every sitemap URL returns HTTP 200
- No duplicate URLs
- No redirect URLs
- No broken URLs
- XML validation passes
- Google Search Console accepts the sitemap

---

# Success Criteria

Sitemap cleanup is complete when

- All 404 URLs reported in Google Search Console are removed.
- Redirect source URLs are removed.
- Deleted pages are removed.
- Archive pages remain if applicable.
- Only valid canonical URLs remain.
- Updated sitemap is ready for submission to Google Search Console.

---

# Important Developer Instructions

This document only covers sitemap cleanup related to the reported 404 URLs.

Do not

- Modify UI
- Modify layouts
- Modify React components
- Change business logic
- Change page content
- Change routing structure
- Implement unrelated SEO improvements

Only update sitemap entries necessary to resolve the Google Search Console 404 issue.

---

# Next Document

```
10_Internal_Links_Fix.md
```

Purpose

Review and fix all internal links pointing to URLs reported in the Google Search Console 404 report. Ensure internal navigation points directly to valid pages without changing the existing UI, design, page content, or application functionality.
