# 22 — INDEXING / CRAWL CONTROL MATRIX

**Section:** URL Indexing Strategy  
**Priority:** P1  
**Type:** Technical SEO  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides indexing control without removing existing functionality.**

---

## Goal

Prevent URL duplication, manage crawl budget efficiently, and ensure only valuable pages are indexed while maintaining a clean URL structure.

---

## Indexing Control Matrix

### Core Pages (Always Index)

| URL Type | Index? | Canonical | Notes |
|----------|--------|-----------|-------|
| `/jobs` | ✅ YES | Self | Main hub page |
| `/` (Homepage) | ✅ YES | Self | Platform homepage |
| `/jobs/{id}/{slug}` | ✅ YES | Self | Individual job pages |
| `/government-jobs/10th-pass` | ✅ YES | Self | Qualification landing page |
| `/government-jobs/12th-pass` | ✅ YES | Self | Qualification landing page |
| `/government-jobs/graduate` | ✅ YES | Self | Qualification landing page |
| `/government-jobs/maharashtra` | ✅ YES | Self | State landing page |
| `/government-jobs/maharashtra/pune` | ✅ YES | Self | City landing page |
| `/government-jobs/railway` | ✅ YES | Self | Department landing page |
| `/government-jobs/police` | ✅ YES | Self | Department landing page |
| `/exams/upsc-cse` | ✅ YES | Self | Exam landing page |
| `/exams/mpsc-rajyaseva` | ✅ YES | Self | Exam landing page |
| `/districts` | ✅ YES | Self | District discovery hub |
| `/admit-cards` | ✅ YES | Self | Admit card hub |
| `/results` | ✅ YES | Self | Results hub |
| `/eligibility-checker` | ✅ YES | Self | Tool page |
| `/age-calculator` | ✅ YES | Self | Tool page |

---

### Conditional Pages (Index with Criteria)

| URL Type | Index? | Criteria | Notes |
|----------|--------|----------|-------|
| `/government-jobs/{other-qualification}` | ✅ Condition | 10+ active jobs + unique content | Only if sufficient inventory |
| `/government-jobs/{other-state}` | ✅ Condition | 10+ active jobs + unique content | Only if sufficient inventory |
| `/government-jobs/{other-city}` | ✅ Condition | 5+ active jobs + unique content | Only if sufficient inventory |
| `/government-jobs/{other-department}` | ✅ Condition | 10+ active jobs + unique content | Only if sufficient inventory |
| `/exams/{other-exam}` | ✅ Condition | Exam is active/upcoming | Only if relevant |

---

### Pagination Pages

| URL Type | Index? | Canonical | Notes |
|----------|--------|-----------|-------|
| `/jobs?page=2` | ✅ YES | Self | Self-referencing canonical |
| `/jobs?page=3` | ✅ YES | Self | Self-referencing canonical |
| `/jobs?page=N` | ✅ YES | Self | Self-referencing canonical |

**Rule:** Each paginated URL gets self-referencing canonical, not canonical back to page 1.

---

### NEVER Index (Explicitly Noindex)

| URL Type | Index? | Robots Tag | Notes |
|----------|--------|------------|-------|
| `/jobs?qualification=12th&location=pune` | ❌ NO | noindex,follow | Random filter combinations |
| `/jobs?department=railway&sort=deadline` | ❌ NO | noindex,follow | Sort parameters |
| `/jobs?utm_source=newsletter` | ❌ NO | noindex,follow | Tracking parameters |
| `/jobs?campaign=google-ads` | ❌ NO | noindex,follow | Campaign parameters |
| `/jobs?fbclid=*` | ❌ NO | noindex,follow | Facebook parameters |
| `/jobs?gclid=*` | ❌ NO | noindex,follow | Google Ads parameters |
| Internal search results | ❌ NO | noindex,follow | User-generated searches |
| Empty filter results | ❌ NO | noindex,follow | No results pages |
| Duplicate job URLs | ❌ NO | 301 redirect | Consolidate duplicates |

---

### Special Cases

| URL Type | Index? | Strategy | Notes |
|----------|--------|----------|-------|
| Expired individual job | ✅ Keep | Self | Keep page live, update status to "Closed" |
| Permanently closed recruitment | ✅ Keep | Self | Keep for historical reference |
| Temporarily unavailable jobs | ✅ Keep | Self | Keep page, show unavailable status |
| Deleted/error jobs | ❌ Remove | 410/404 | Remove from index entirely |

---

## Robots.txt Implementation

### Allow Important Sections

```
User-agent: *
Allow: /jobs
Allow: /government-jobs
Allow: /exams
Allow: /districts
Allow: /admit-cards
Allow: /results
Allow: /eligibility-checker
Allow: /age-calculator
```

### Block Unnecessary Sections

```
Disallow: /jobs?
Disallow: /search?
Disallow: /filter?
Disallow: /admin/
Disallow: /api/
Disallow: /private/
```

### Sitemap Directive

```
Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml
```

---

## Canonical URL Strategy

### Self-Referencing Canonicals

**Standard Pages:**
```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">
```

**Pagination:**
```html
<!-- On /jobs?page=2 -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs?page=2">
```

**Individual Jobs:**
```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/123/msrtc-recruitment">
```

---

### Redirect Strategy

### 301 Redirects (Permanent)

**Duplicate Content:**
- Old job URL → New job URL
- URL variations → Canonical version
- HTTP → HTTPS
- Non-www → www (or vice versa)

**Moved Content:**
- Old recruitment → New recruitment
- Deleted category → Relevant category
- Obsolete page → Related active page

### 410 Gone (Permanently Removed)

**Truly Deleted:**
- Fake/erroneous job postings
- Test/sample data
- Expired spam content

---

## Parameter Handling

### Google-Specific Parameters

**Noindex These Parameters:**
```
utm_source
utm_medium
utm_campaign
fbclid
gclid
msclkid
campaign
source
ref
```

**Implementation:**
```html
<meta name="robots" content="noindex, follow">
```
Or configure in robots.txt for patterns.

---

## Duplicate URL Normalization

### Trailing Slash Consistency

**Choose One Convention:**
- Either: `https://www.searchsarkarinaukri.com/jobs/`
- Or: `https://www.searchsarkarinaukri.com/jobs`

**Rule:** Redirect one to the other (301) to avoid duplication.

### Case Sensitivity

**URLs are case-insensitive:** Ensure server handles this consistently.

### URL Encoding

**Handle special characters:** Use proper URL encoding for spaces, special characters.

---

## Crawl Budget Management

### Prioritize Crawl Order

**High Priority:**
1. `/jobs` hub page
2. Individual job pages (especially active ones)
3. Major qualification landing pages
4. Maharashtra state pages
5. Major department pages

**Medium Priority:**
6. Other state pages
7. Other qualification pages
8. Exam pages
9. District pages

**Low Priority:**
10. Tool pages
11. Archive pages
12. Low-traffic category pages

---

## XML Sitemap Strategy

### Sitemap Structure

**Main Sitemap Index:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-jobs.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-qualification.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-location.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-department.xml</loc>
  </sitemap>
</sitemapindex>
```

### Content Sitemaps

**Jobs Sitemap:**
- Only include 200-status URLs
- Only include indexable job pages
- Include lastmod for each URL
- Exclude expired jobs (or update status)

**Category Sitemaps:**
- Only include qualification/location/department pages with real inventory
- Exclude pages with < 5 jobs
- Include lastmod timestamps

---

## Lastmod Rules

### When to Update lastmod

**Update When:**
- Page content changes significantly
- Job information is updated
- New jobs are added to category pages
- Status changes (Open → Closed)
- Editorial updates are made

**Do NOT Update:**
- For minor cosmetic changes
- For page view counts
- For automated cache refreshes
- For unrelated system updates

---

## Orphan Page Detection

### Regular Checks

**Identify Orphan Pages:**
- Pages with no internal links
- Pages not in navigation
- Pages not in sitemap
- Pages with zero traffic

**Action:**
- Add internal links to valuable orphan pages
- Remove/noindex useless orphan pages
- Fix broken internal links

---

## Index Coverage Monitoring

### Regular Monitoring

**Check Weekly:**
- Indexed pages count
- Excluded pages count
- Valid with warnings
- Excluded by canonical
- Excluded by noindex
- Crawled - currently not indexed

**Action:**
- Investigate sudden drops in indexed pages
- Fix "Crawled - currently not indexed" issues
- Remove accidental noindex tags
- Fix canonical issues

---

## Implementation Steps

### Step 1: Robots.txt Setup
1. Create/update robots.txt
2. Allow important sections
3. Block unnecessary parameters
4. Add sitemap directive
5. Test with Google robots.txt tester

### Step 2: Canonical Implementation
1. Add self-referencing canonicals to all pages
2. Implement pagination canonical strategy
3. Handle HTTP/HTTPS canonicals
4. Handle www/non-www canonicals
5. Test canonical implementation

### Step 3: Parameter Handling
1. Identify all URL parameters
2. Configure noindex for tracking parameters
3. Allow important parameters (pagination)
4. Test parameter handling
5. Monitor parameter usage

### Step 4: Sitemap Setup
1. Create sitemap index
2. Create child sitemaps by category
3. Include only indexable URLs
4. Implement lastmod logic
5. Submit to Search Console

### Step 5: Monitoring Setup
1. Set up Search Console monitoring
2. Configure index coverage reports
3. Set up crawl error monitoring
4. Create weekly review process
5. Set up alerts for issues

---

## Validation Checklist

### Robots.txt
- [ ] Important sections allowed
- [ ] Unnecessary parameters blocked
- [ ] Sitemap directive present
- [ ] Syntax validated
- [ ] Tested with Google tool

### Canonical Tags
- [ ] All pages have canonicals
- [ ] Pagination canonicals correct
- [ ] HTTP/HTTPS canonicals correct
- [ ] www/non-www canonicals correct
- [ ] No canonical loops

### Sitemap
- [ ] Sitemap index created
- [ ] Child sitemaps organized
- [ ] Only indexable URLs included
- [ ] lastmod implemented correctly
- [ ] Submitted to Search Console

### Parameter Handling
- [ ] Tracking parameters noindexed
- [ ] Important parameters allowed
- [ ] Filter combinations noindexed
- [ ] Sort parameters noindexed
- [ ] Tested parameter URLs

### Monitoring
- [ ] Search Console monitoring setup
- [ ] Index coverage reports reviewed
- [ ] Crawl errors monitored
- [ ] Weekly review process established
- [ ] Alerts configured

---

## Developer Notes

1. **Crawl Budget:** Prioritize important pages for crawling
2. **Sitemap Automation:** Automate sitemap generation
3. **Canonical Consistency:** Ensure canonicals are always correct
4. **Monitoring:** Set up automated monitoring and alerts
5. **Testing:** Test all indexing rules before deployment

---

## Success Metrics

- [ ] Reduced duplicate content issues
- [ ] Improved crawl budget efficiency
- [ ] Higher index coverage for important pages
- [ ] Fewer "Crawled - not indexed" pages
- [ ] Better sitemap coverage
- [ ] Zero canonical errors

---

**Last Updated:** 4 September 2026  
**Dependencies:** 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md  
**Status:** Implementation Ready