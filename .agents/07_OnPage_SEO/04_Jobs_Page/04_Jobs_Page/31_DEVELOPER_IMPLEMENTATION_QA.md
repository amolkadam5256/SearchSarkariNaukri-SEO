# 31 — DEVELOPER IMPLEMENTATION QA

**Section:** Quality Assurance Checklist  
**Priority:** P1  
**Type:** Developer Handoff  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides QA checklist without removing existing functionality.**

---

## Goal

Provide a comprehensive quality assurance checklist for developers to ensure all SEO, AEO, GEO, and technical requirements are correctly implemented before deployment.

---

## Pre-Implementation Checklist

### Environment Setup
- [ ] Development environment configured
- [ ] Staging environment available
- [ ] Database migrations prepared
- [ ] Code repository ready
- [ ] Deployment pipeline tested

### Dependencies
- [ ] React/Next.js version compatible
- [ ] SEO libraries installed (react-helmet, next-seo, etc.)
- [ ] Schema markup library installed
- [ ] Image optimization configured
- [ ] Performance monitoring set up

---

## Metadata Implementation QA

### Title Tags
- [ ] Dynamic title generation working
- [ ] Title length 50-60 characters
- [ ] Primary keyword in title
- [ ] No duplicate titles across pages
- [ ] Titles update correctly with content changes

### Meta Descriptions
- [ ] Dynamic meta description working
- [ ] Description length 150-160 characters
- [ ] Keywords included naturally
- [ ] Call-to-action included
- [ ] No duplicate descriptions

### Canonical Tags
- [ ] Self-referencing canonical on all pages
- [ ] Pagination canonical strategy correct
- [ ] HTTP/HTTPS canonicals consistent
- [ ] www/non-www canonicals consistent
- [ ] No canonical loops

### Robots Meta Tags
- [ ] Index, follow on important pages
- [ ] Noindex on filter/parameter pages
- [ ] Noindex on internal search results
- [ ] No accidental noindex on hub pages
- [ ] Meta tags render correctly

---

## Content Implementation QA

### H1 and Headings
- [ ] H1 present on all pages
- [ ] Only one H1 per page
- [ ] Heading hierarchy logical (H1-H6)
- [ ] Headings contain relevant keywords
- [ ] No skipped heading levels

### Section Content
- [ ] All required sections present
- [ ] Content length appropriate
- [ ] Keywords used naturally
- [ ] No keyword stuffing
- [ ] Content is accurate and helpful

### FAQ Content
- [ ] FAQ section implemented
- [ ] Questions are clear and direct
- [ ] Answers are factual and concise
- [ ] Q&A format followed
- [ ] Schema markup added (if eligible)

---

## Structured Data QA

### JobPosting Schema
- [ ] Only on individual job pages
- [ ] Not on /jobs hub page
- [ ] All required fields present
- [ ] Optional fields only when data available
- [ ] No fabricated information
- [ ] Validated with Rich Results Test

### BreadcrumbList Schema
- [ ] Implemented on all pages
- [ ] Correct item hierarchy
- [ ] Accurate URLs
- [ ] Proper position values
- [ ] Validated with testing tools

### WebPage Schema
- [ ] Implemented on hub pages
- [ ] Accurate page information
- [ ] Publisher information correct
- [ ] Date information accurate
- [ ] No schema errors

### FAQ Schema
- [ ] Only implemented when eligible
- [ ] Questions and answers accurate
- [ ] Proper schema structure
- [ ] Validated with Rich Results Test
- [ ] No schema warnings

---

## Technical SEO QA

### URL Structure
- [ ] URLs are clean and descriptive
- [ ] Hyphens used in URLs
- [ ] No special characters in URLs
- [ ] Lowercase URLs only
- [ ] Trailing slash consistent

### Redirects
- [ ] HTTP to HTTPS redirects working
- [ ] www/non-www redirects working
- [ ] 301 redirects for moved content
- [ ] No redirect chains (>1 hop)
- [ ] 404 pages handled correctly

### Robots.txt
- [ ] Robots.txt accessible
- [ ] Important sections allowed
- [ ] Unnecessary parameters blocked
- [ ] Sitemap directive present
- [ ] Tested with Google tool

### Sitemap
- [ ] Sitemap accessible
- [ ] Sitemap index created
- [ ] Child sitemaps organized
- [ ] Only indexable URLs included
- [ ] Submitted to Search Console

---

## Performance QA

### Core Web Vitals
- [ ] LCP under 2.5s
- [ ] INP under 200ms
- [ ] CLS under 0.1
- [ ] Tested with PageSpeed Insights
- [ ] Field data monitored

### Image Optimization
- [ ] Images compressed (WebP/AVIF)
- [ ] Image dimensions specified
- [ ] Lazy loading implemented
- [ ] Alt text added to all images
- [ ] No layout shift from images

### JavaScript Optimization
- [ ] Code splitting implemented
- [ ] Lazy loading for non-critical JS
- [ ] Debounced input handlers
- [ ] No render-blocking scripts
- [ ] Bundle size optimized

### Server-Side Rendering
- [ ] SSR implemented for /jobs
- [ ] Critical content server-rendered
- [ ] Hydration working correctly
- [ ] No flash of unstyled content
- [ ] SEO metadata server-rendered

---

## Accessibility QA

### Semantic HTML
- [ ] Semantic elements used (main, section, article)
- [ ] Landmark regions defined
- [ ] Proper heading structure
- [ ] Lists used correctly
- [ ] Tables used appropriately

### Keyboard Navigation
- [ ] All interactive elements keyboard accessible
- [ ] Tab order logical
- [ ] Focus indicators visible
- [ ] No keyboard traps
- [ ] Skip links implemented

### Screen Reader Support
- [ ] Alt text descriptive
- [ ] ARIA labels where needed
- [ ] Form labels visible
- [ ] Status announcements
- [ ] Tested with screen readers

### Color and Contrast
- [ ] Sufficient color contrast (4.5:1)
- [ ] Color not sole indicator
- [ ] Text readable without zooming
- [ ] Focus states visible
- [ ] Tested with contrast checker

---

## Mobile QA

### Responsive Design
- [ ] Layout works on mobile
- [ ] Touch targets 44x44px minimum
- [ ] Horizontal scrolling minimal
- [ ] Text readable without zooming
- [ ] Images responsive

### Mobile Performance
- [ ] Fast load on mobile networks
- [ ] No large downloads on mobile
- [ ] Touch gestures work correctly
- [ ] Mobile-specific features tested
- [ ] Tested on real devices

---

## Content QA

### Accuracy
- [ ] All information accurate
- [ ] No factual errors
- [ ] Links point to correct destinations
- [ ] Contact information correct
- [ ] Dates and times accurate

### Currency
- [ ] Content is up-to-date
- [ ] Expired content updated/removed
- [ ] New content added regularly
- [ ] Outdated links fixed
- [ ] Seasonal content updated

### Consistency
- [ ] Naming conventions consistent
- [ ] Style guide followed
- [ ] Formatting consistent
- [ ] Terminology consistent
- [ ] Brand guidelines followed

---

## Security QA

### Input Validation
- [ ] User input sanitized
- [ ] XSS protection implemented
- [ ] SQL injection prevention
- [ ] CSRF protection
- [ ] Output encoding

### External Links
- [ ] External links safe
- [ ] No unsafe injection
- [ ] rel="noopener noreferrer" on external links
- [ ] No mixed content
- [ ] HTTPS only

### Data Protection
- [ ] Sensitive data protected
- [ ] No internal IDs exposed
- [ ] Secure authentication
- [ ] Proper session management
- [ ] Compliance with regulations

---

## SEO-Specific QA

### Internal Linking
- [ ] Internal links working
- [ ] Anchor text descriptive
- [ ] No broken internal links
- [ ] Link hierarchy logical
- [ ] No orphan pages

### External Linking
- [ ] External links relevant
- [ ] Official source links present
- [ ] No broken external links
- [ ] Link attributes correct
- [ ] No excessive external links

### Keyword Placement
- [ ] Primary keyword in title
- [ ] Primary keyword in H1
- [ ] Keywords used naturally
- [ ] No keyword stuffing
- [ ] Keyword cannibalisation prevented

---

## Integration QA

### Search Console
- [ ] Property verified
- [ ] Sitemap submitted
- [ ] No coverage errors
- [ ] No security issues
- [ ] Data flowing correctly

### Analytics
- [ ] Tracking installed
- [ ] Events firing correctly
- [ ] Custom dimensions working
- [ ] Conversion tracking working
- [ ] Data accurate

### Third-Party Tools
- [ ] No conflicts with other tools
- [ ] Performance monitoring working
- [ ] Error tracking working
- [ ] A/B testing compatible
- [ ] CDN integration working

---

## Pre-Deployment Checklist

### Code Review
- [ ] Code reviewed by peer
- [ ] SEO requirements verified
- [ ] Performance validated
- [ ] Accessibility checked
- [ ] Security reviewed

### Testing
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] E2E tests passing
- [ ] Manual testing completed
- [ ] Performance testing completed

### Documentation
- [ ] Code documented
- [ ] API documentation updated
- [ ] SEO documentation updated
- [ ] Deployment guide updated
- [ ] Rollback plan documented

---

## Post-Deployment Checklist

### Immediate Checks
- [ ] Site accessible
- [ ] No 500 errors
- [ ] Metadata rendering correctly
- [ ] Schema validation passed
- [ ] Performance acceptable

### Search Console Validation
- [ ] URL inspection for /jobs
- [ ] URL inspection for sample job
- [ ] Coverage report checked
- [ ] Mobile usability checked
- [ ] Structured data tested

### Monitoring Setup
- [ ] Error tracking enabled
- [ ] Performance monitoring active
- [ ] Uptime monitoring working
- [ ] Alerts configured
- [ ] Dashboard updated

---

## Developer Notes

1. **Testing:** Test thoroughly on staging before production
2. **Monitoring:** Set up comprehensive monitoring immediately
3. **Rollback:** Have rollback plan ready before deployment
4. **Documentation:** Document all changes and configurations
5. **Communication:** Notify relevant teams of deployment

---

## Success Criteria

### Implementation Complete When:
- [ ] All QA checks passed
- [ ] No critical bugs found
- [ ] Performance targets met
- [ ] SEO requirements satisfied
- [ ] Stakeholder approval received

---

## Common Issues to Watch

### Issue 1: Schema Errors
**Problem:** Schema validation failing  
**Solution:** Check all required fields, validate with testing tools

### Issue 2: Performance Regression
**Problem:** Slower page load after deployment  
**Solution:** Check bundle size, image optimization, server response time

### Issue 3: Missing Metadata
**Problem:** Title/meta not rendering  
**Solution:** Check SSR, verify metadata component configuration

### Issue 4: Broken Links
**Problem:** Internal/external links broken  
**Solution:** Run link checker, update broken URLs

### Issue 5: Accessibility Issues
**Problem:** Screen reader or keyboard issues  
**Solution:** Test with accessibility tools, fix ARIA labels

---

**Last Updated:** 4 September 2026  
**Dependencies:** All implementation files  
**Status:** Implementation Ready