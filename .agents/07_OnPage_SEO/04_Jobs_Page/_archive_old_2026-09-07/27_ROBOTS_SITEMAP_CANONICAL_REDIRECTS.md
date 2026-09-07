# 27 — ROBOTS / SITEMAP / CANONICAL / REDIRECTS

**Section:** Technical SEO Foundation  
**Priority:** P1  
**Type:** Technical Implementation  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides technical foundation without removing existing functionality.**

---

## Goal

Implement comprehensive technical SEO foundation including robots.txt, XML sitemaps, canonical URLs, and redirect policies for optimal search engine crawling and indexing.

---

## Robots.txt Implementation

### Complete Robots.txt

```txt
User-agent: *
Allow: /
Allow: /jobs
Allow: /government-jobs
Allow: /exams
Allow: /districts
Allow: /admit-cards
Allow: /results
Allow: /eligibility-checker
Allow: /age-calculator
Allow: /career-guidance
Allow: /current-affairs
Allow: /quiz

# Block unnecessary parameters
Disallow: /jobs?
Disallow: /search?
Disallow: /filter?
Disallow: /admin/
Disallow: /api/
Disallow: /private/
Disallow: /temp/
Disallow: /test/

# Allow important bots
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# Sitemap
Sitemap: https://www.searchsarkarinaukri.com/sitemap.xml
```

### Testing
- [ ] Test with Google robots.txt tester
- [ ] Verify sitemap directive
- [ ] Check blocked sections
- [ ] Validate syntax

---

## XML Sitemap Architecture

### Sitemap Index Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-main.xml</loc>
    <lastmod>2026-09-04</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-jobs.xml</loc>
    <lastmod>2026-09-04</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-qualification.xml</loc>
    <lastmod>2026-09-04</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-location.xml</loc>
    <lastmod>2026-09-04</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-department.xml</loc>
    <lastmod>2026-09-04</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.searchsarkarinaukri.com/sitemap-exam.xml</loc>
    <lastmod>2026-09-04</lastmod>
  </sitemap>
</sitemapindex>
```

### Jobs Sitemap Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.searchsarkarinaukri.com/jobs</loc>
    <lastmod>2026-09-04</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.searchsarkarinaukri.com/jobs?page=2</loc>
    <lastmod>2026-09-04</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.searchsarkarinaukri.com/jobs/123/msrtc-solapur-recruitment</loc>
    <lastmod>2026-09-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
```

### Lastmod Rules

**Update lastmod when:**
- Page content changes significantly
- New jobs added to category pages
- Job information updated
- Status changes (Open → Closed)
- Editorial updates made

**Do NOT update lastmod for:**
- Minor cosmetic changes
- Page view count changes
- Automated cache refreshes
- Unrelated system updates

---

## Canonical URL Strategy

### Self-Referencing Canonicals

**Standard Pages:**
```html
<!-- On /jobs -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">
```

**Pagination:**
```html
<!-- On /jobs?page=2 -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs?page=2">
```

**Individual Jobs:**
```html
<!-- On /jobs/123/msrtc-recruitment -->
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs/123/msrtc-recruitment">
```

**Canonical Rules:**
- Every indexable page has self-referencing canonical
- Pagination pages self-canonicalize (not back to page 1)
- No rel="next"/rel="prev" (deprecated by Google)
- Canonical URLs are absolute (not relative)

---

## HTTP/HTTPS Consistency

### Enforce HTTPS

**Implementation:**
```html
<link rel="canonical" href="https://www.searchsarkarinaukri.com/jobs">
```

**Redirect HTTP to HTTPS:**
```
http://www.searchsarkarinaukri.com/jobs → https://www.searchsarkarinaukri.com/jobs
http://searchsarkarinaukri.com/jobs → https://www.searchsarkarinaukri.com/jobs
```

**Implementation:** 301 redirect from all HTTP to HTTPS

---

## WWW/Non-WWW Consistency

### Choose One Preferred Version

**Option 1: WWW Preferred**
```
https://searchsarkarinaukri.com/jobs → https://www.searchsarkarinaukri.com/jobs
http://searchsarkarinaukri.com/jobs → https://www.searchsarkarinaukri.com/jobs
```

**Option 2: Non-WWW Preferred**
```
https://www.searchsarkarinaukri.com/jobs → https://searchsarkarinaukri.com/jobs
http://www.searchsarkarinaukri.com/jobs → https://searchsarkarinaukri.com/jobs
```

**Implementation:** 301 redirect to preferred version, set canonical accordingly

---

## Redirect Policy

### 301 Redirects (Permanent)

**Use Cases:**
- URL structure changes
- Content moved to new URL
- HTTP to HTTPS
- WWW/non-WWW canonicalization
- Duplicate content consolidation
- Old recruitment → new recruitment

**Implementation:**
```javascript
// Example redirect configuration
301 Redirect: /old-jobs/msrec-2026 → /jobs/123/msrtc-recruitment
```

### 302 Redirects (Temporary)

**Use Cases:**
- Temporary content moves
- A/B testing
- Seasonal redirects
- Maintenance pages

**Implementation:** Use sparingly, only for temporary situations

### 410 Gone (Permanently Removed)

**Use Cases:**
- Deleted fake/spam job postings
- Test/sample data removed
- Permanently closed pages (no redirect destination)

**Implementation:**
```http
Status: 410 Gone
```

### 404 Not Found

**Use Cases:**
- genuinely missing pages
- Broken links
- User errors

**Implementation:** Return proper 404 status, provide helpful error page

---

## Trailing Slash Consistency

### Choose One Convention

**Option 1: With Trailing Slash**
```
https://www.searchsarkarinaukri.com/jobs/
https://www.searchsarkarinaukri.com/jobs?page=2/
```

**Option 2: Without Trailing Slash**
```
https://www.searchsarkarinaukri.com/jobs
https://www.searchsarkarinaukri.com/jobs?page=2
```

**Implementation:** Redirect one convention to the other (301)

---

## URL Normalization

### Handle Special Characters

**URL Encoding:**
- Spaces → `-` (hyphens) or `%20`
- Special characters → proper encoding
- Unicode characters → proper encoding

**Example:**
```
/government-jobs-12th-pass (not /government jobs 12th pass)
/government-jobs/pune-solapur (not /government jobs?city=pune,solapur)
```

---

## Implementation Steps

### Step 1: Robots.txt Setup
1. Create comprehensive robots.txt
2. Allow important sections
3. Block unnecessary parameters
4. Add sitemap directive
5. Test with Google robots.txt tester

### Step 2: Sitemap Setup
1. Create sitemap index
2. Create child sitemaps by category
3. Include only indexable URLs
4. Implement lastmod logic
5. Submit to Search Console

### Step 3: Canonical Implementation
1. Add canonical tags to all pages
2. Implement pagination canonical strategy
3. Handle HTTP/HTTPS canonicals
4. Handle www/non-www canonicals
5. Test canonical implementation

### Step 4: Redirect Setup
1. Implement 301 redirects for URL changes
2. Configure HTTP to HTTPS redirects
3. Configure www/non-www redirects
4. Handle trailing slash consistency
5. Test redirect chains

### Step 5: Monitoring
1. Monitor robots.txt for errors
2. Monitor sitemap coverage
3. Check canonical coverage
4. Monitor redirect chains
5. Check for 404/410 errors

---

## Validation Checklist

### Robots.txt
- [ ] Important sections allowed
- [ ] Unnecessary parameters blocked
- [ ] Sitemap directive present
- [ ] Syntax validated
- [ ] Tested with Google tool

### Sitemap
- [ ] Sitemap index created
- [ ] Child sitemaps organized
- [ ] Only indexable URLs included
- [ ] lastmod implemented correctly
- [ ] Submitted to Search Console

### Canonical
- [ ] All pages have canonicals
- [ ] Pagination canonicals correct
- [ ] HTTP/HTTPS canonicals correct
- [ ] www/non-www canonicals correct
- [ ] No canonical loops

### Redirects
- [ ] HTTP to HTTPS redirects working
- [ ] www/non-www redirects working
- [ ] Trailing slash consistency
- [ ] No redirect chains > 1 hop
- [ ] 404/410 pages handled correctly

---

## Developer Notes

1. **Robots.txt:** Keep it simple, test changes before deploying
2. **Sitemap:** Automate sitemap generation for accuracy
3. **Canonical:** Use absolute URLs, not relative
4. **Redirects:** Use 301 for permanent, 302 for temporary
5. **Testing:** Test all technical implementations thoroughly

---

## Success Metrics

- [ ] Zero robots.txt errors
- [ ] High sitemap coverage
- [ ] Zero canonical errors
- [ ] No redirect chains
- [ ] Zero duplicate content issues
- [ ] Better crawl efficiency

---

## Common Technical Issues

### Issue 1: Blocking Important Content
**Problem:** Robots.txt blocks important sections  
**Solution:** Review robots.txt, allow important sections

### Issue 2: Duplicate Canonicals
**Problem:** Multiple pages with same canonical  
**Solution:** Ensure each page has unique, self-referencing canonical

### Issue 3: Redirect Chains
**Problem:** Page → redirect → redirect → destination  
**Solution:** Reduce redirects to single hop (301)

### Issue 4: Mixed HTTP/HTTPS
**Problem:** Both HTTP and HTTPS accessible  
**Solution:** 301 redirect all HTTP to HTTPS

### Issue 5: Missing Sitemap
**Problem:** Sitemap not submitted or outdated  
**Solution:** Submit updated sitemap, automate generation

---

**Last Updated:** 4 September 2026  
**Dependencies:** 22_INDEXING_CRAWL_CONTROL.md  
**Status:** Implementation Ready