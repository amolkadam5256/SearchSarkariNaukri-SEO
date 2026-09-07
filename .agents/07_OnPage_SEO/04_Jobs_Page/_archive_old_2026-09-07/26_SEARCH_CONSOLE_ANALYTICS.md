# 26 — SEARCH CONSOLE + SEO MEASUREMENT

**Section:** Analytics and Performance Tracking  
**Priority:** P1  
**Type:** Strategic Documentation  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides measurement strategy without removing existing functionality.**

---

## Goal

Set up comprehensive SEO measurement and monitoring using Google Search Console and analytics to track performance, identify opportunities, and optimize continuously.

---

## Search Console Configuration

### Property Setup

**Required Properties:**
1. **Domain Property:** `https://www.searchsarkarinaukri.com/`
2. **URL Prefix Property:** `https://www.searchsarkarinaukri.com/jobs` (optional)
3. **Sitemap Submission:** Submit main sitemap
4. **International Targeting:** Set to India (if applicable)

### Verification Methods
- HTML file upload
- DNS TXT record
- Google Analytics
- Google Tag Manager

---

## Key Query Tracking

### Primary Keywords to Monitor

**High Priority Queries:**
- Government Jobs
- Sarkari Naukri
- Govt Jobs
- Government Jobs 2026
- Latest Government Jobs
- Government Jobs in India

**Secondary Keywords:**
- Government Jobs in Maharashtra
- Government Jobs for 10th Pass
- Government Jobs for 12th Pass
- Government Jobs for Graduates
- Railway Jobs
- Police Jobs
- Banking Jobs
- Government Jobs in Pune
- Government Jobs in Mumbai

**Long-Tail Keywords:**
- [Organisation] recruitment 2026
- government jobs closing soon
- government jobs for freshers
- government jobs last date
- government job notifications

---

## Search Console Monitoring

### Weekly Monitoring Tasks

**1. Performance Report**
- [ ] Check average position
- [ ] Monitor impressions
- [ ] Track click-through rate (CTR)
- [ ] Identify pages gaining impressions
- [ ] Identify pages losing impressions

**2. Index Coverage Report**
- [ ] Check total indexed pages
- [ ] Monitor excluded pages
- [ ] Track "Crawled - currently not indexed"
- [ ] Monitor "Valid with warnings"
- [ ] Check for coverage errors

**3. URL Inspection**
- [ ] Inspect /jobs page weekly
- [ ] Inspect sample job pages
- [ ] Inspect category landing pages
- [ ] Check for mobile usability issues
- [ ] Verify AMP (if implemented)

**4. Manual Actions**
- [ ] Check for security issues
- [ ] Monitor for spam reports
- [ ] Check for hacked content
- [ ] Review any manual penalties

---

## Monthly Optimization Loop

### Monthly Process

**Week 1: Query Analysis**
1. Export top 1000 queries
2. Group by intent (informational, navigational, transactional)
3. Identify high-impression, low-click queries
4. Find new keyword opportunities
5. Track keyword ranking changes

**Week 2: Content Optimization**
1. Optimize titles and descriptions for low-CTR pages
2. Improve content for high-impression, low-click queries
3. Add internal links to underperforming pages
4. Update outdated content
5. Add FAQ content for question queries

**Week 3: Technical Review**
1. Check for crawl errors
2. Review coverage issues
3. Check for mobile usability problems
4. Review structured data errors
5. Fix any 404 or redirect issues

**Week 4: Performance Review**
1. Review Core Web Vitals
2. Check page load times
3. Monitor bounce rate changes
4. Track conversion metrics
5. Plan next month's optimization

---

## Key Performance Indicators

### SEO KPIs

**Organic Performance:**
- Total organic impressions
- Total organic clicks
- Average CTR
- Average position
- Total indexed pages
- Organic traffic

**Keyword Performance:**
- Number of keywords ranking
- Keywords in top 10
- Keywords in top 3
- New keywords gained
- Keywords lost rankings

**Page Performance:**
- Pages with impressions
- Pages with clicks
- Average CTR by page
- Top performing pages
- Underperforming pages

---

## Analytics Setup

### Google Analytics 4 Configuration

**Required Events:**
- page_view
- job_view
- job_apply_click
- search_performed
- filter_used
- job_save
- external_link_click

**Custom Dimensions:**
- job_category
- qualification
- location
- department
- job_status

**Conversion Tracking:**
- Apply online click
- Official notification download
- Job save/bookmark
- Resource page visit
- Tool usage (eligibility checker, age calculator)

---

## Measurement Dashboard

### Essential Metrics Dashboard

**Weekly Report:**
- Total impressions
- Total clicks
- Average CTR
- Average position
- Top 10 queries
- Top 10 pages
- Index coverage status

**Monthly Report:**
- Keyword ranking changes
- New keywords gained
- Traffic by device
- Traffic by location
- Traffic by query category
- Conversion metrics

---

## Query Intent Analysis

### Intent Classification

**Informational Queries:**
- what are government jobs
- how to apply for government jobs
- government job eligibility
- government job qualifications

**Navigational Queries:**
- searchsarkarinaukri
- government jobs
- sarkari naukri official

**Commercial Investigation:**
- best government jobs
- highest paying government jobs
- government job vs private job

**Transactional:**
- apply online for railway recruitment
- MPSC application form
- SSC registration

**Freshness/Deadline:**
- government jobs closing today
- latest recruitment this week
- government jobs last date

---

## Query Expansion Tracking

### Identify Query Expansion

**Monitor for:**
- Queries gaining impressions but no clicks
- Queries with high impressions but low CTR
- New queries appearing in Search Console
- Queries with position changes
- Queries with seasonal patterns

**Action Items:**
- Optimize titles/meta for low-CTR queries
- Create content for new query opportunities
- Add FAQ content for question queries
- Improve internal linking for relevant queries

---

## Competitor Monitoring

### Track Competitor Performance

**Identify Competitors:**
- Major government job portals
- Government official websites
- Leading job aggregators

**Monitor:**
- Competitor keyword rankings
- Competitor content strategies
- Competitor technical SEO
- Competitor link building
- Market share changes

---

## Implementation Steps

### Step 1: Search Console Setup
1. Verify Search Console property
2. Submit sitemap
3. Set international targeting
4. Configure email forwarding
5. Set up mobile usability tracking

### Step 2: Analytics Setup
1. Install GA4 tracking
2. Configure custom events
3. Set up conversion tracking
4. Configure custom dimensions
5. Test tracking implementation

### Step 3: Baseline Measurement
1. Export initial Search Console data
2. Establish baseline metrics
3. Set up tracking dashboards
4. Configure alerts and notifications
5. Document baseline performance

### Step 4: Monitoring System
1. Set up weekly monitoring schedule
2. Configure automated alerts
3. Create monthly report templates
4. Set up query expansion tracking
5. Configure competitor monitoring

### Step 5: Optimization Process
1. Implement monthly optimization loop
2. Create content optimization calendar
3. Set up technical review schedule
4. Configure performance review process
5. Document optimization results

---

## Validation Checklist

### Search Console
- [ ] Property verified
- [ ] Sitemap submitted
- [ ] International targeting set
- [ ] Email forwarding configured
- [ ] Mobile usability tracking active

### Analytics
- [ ] GA4 tracking installed
- [ ] Custom events configured
- [ ] Conversion tracking set up
- [ ] Custom dimensions configured
- [ ] Tracking tested and validated

### Monitoring
- [ ] Weekly monitoring established
- [ ] Monthly optimization loop created
- [ ] Alerts configured
- [ ] Dashboards set up
- [ ] Baseline metrics documented

---

## Developer Notes

1. **GA4 Migration:** Ensure proper GA4 implementation (not UA)
2. **Event Tracking:** Use meaningful event names and parameters
3. **Data Privacy:** Ensure compliance with privacy regulations
4. **Regular Review:** Review Search Console data weekly
5. **Continuous Optimization:** SEO is an ongoing process

---

## Success Metrics

- [ ] Increased organic impressions
- [ ] Improved click-through rates
- [ ] Better average position
- [ ] More keywords ranking
- [ ] Higher indexed page count
- [ ] Improved conversion rates

---

## Common Measurement Issues

### Issue 1: No Search Console Data
**Problem:** Property not verified or no data  
**Solution:** Verify property, check sitemap, wait for data

### Issue 2: Low CTR
**Problem:** High impressions, low clicks  
**Solution:** Optimize titles/meta, improve content

### Issue 3: "Crawled - Not Indexed"
**Problem:** Pages discovered but not indexed  
**Solution:** Improve content, check canonical, add internal links

### Issue 4: Position Drop
**Problem:** Rankings declining  
**Solution:** Analyze competitor changes, improve content, check technical issues

### Issue 5: Zero Impressions
**Problem:** New pages not getting impressions  
**Solution:** Check indexing, add internal links, verify content quality

---

**Last Updated:** 4 September 2026  
**Dependencies:** 14_KEYWORD_MAP.md  
**Status:** Implementation Ready