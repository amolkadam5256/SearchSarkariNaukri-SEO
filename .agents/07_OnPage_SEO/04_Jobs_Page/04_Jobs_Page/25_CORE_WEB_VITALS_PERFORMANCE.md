# 25 — CORE WEB VITALS PERFORMANCE

**Section:** Performance Optimization Implementation  
**Priority:** P2  
**Type:** Technical SEO  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides performance optimization without removing existing functionality.**

---

## Goal

Achieve "Good" Core Web Vitals scores for the /jobs page by optimizing Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS).

---

## Performance Targets

### Core Web Vitals Thresholds

| Metric | Target | Poor | Needs Improvement |
|--------|--------|------|------------------|
| LCP | ≤ 2.5s | > 4.0s | 2.5s - 4.0s |
| INP | ≤ 200ms | > 500ms | 200ms - 500ms |
| CLS | ≤ 0.1 | > 0.25 | 0.1 - 0.25 |

---

## LCP (Largest Contentful Paint) Optimization

### Current Potential Issues

**On /jobs page:**
- Large hero assets
- Unoptimized fonts
- Client-side rendering delay
- API-delayed first job list
- Heavy JavaScript bundles

### Optimization Strategies

#### 1. Server-Side Rendering (Critical)
**Implementation:**
- Server-render H1, intro, and first job cards
- Use Next.js SSR or equivalent
- Render initial HTML with job data
- Hydrate React client-side

**Target:** First paint shows actual job content, not loading state.

#### 2. Hero Asset Optimization
**Current Issue:** Large hero images delay LCP  
**Solution:**
- Compress hero image to < 200KB
- Use WebP/AVIF format
- Add preload for hero image
- Consider using CSS gradients instead of images
- Lazy load hero if below fold

**Implementation:**
```html
<link rel="preload" as="image" href="hero-image.webp" fetchpriority="high">
```

#### 3. Font Optimization
**Current Issue:** Font loading delays LCP  
**Solution:**
- Use font-display: swap
- Preload critical fonts
- Use system fonts where possible
- Subset fonts to include only needed characters
- Use font-display: optional for non-critical fonts

**Implementation:**
```css
@font-face {
  font-family: 'Inter';
  font-display: swap;
  src: url('/fonts/inter.woff2') format('woff2');
}
```

#### 4. JavaScript Optimization
**Current Issue:** Heavy JS blocks rendering  
**Solution:**
- Code-split JavaScript bundles
- Lazy load non-critical JavaScript
- Defer non-essential scripts
- Use dynamic imports for heavy components
- Remove unused JavaScript

#### 5. API Response Optimization
**Current Issue:** API delay blocks first paint  
**Solution:**
- Optimize database queries
- Add API response caching
- Implement progressive rendering
- Show skeleton loading state
- Use streaming SSR where possible

---

## INP (Interaction to Next Paint) Optimization

### Current Potential Issues

**On /jobs page:**
- Expensive filter recomputation
- Heavy search input handling
- JavaScript-heavy job cards
- No input debouncing
- Main thread blocking

### Optimization Strategies

#### 1. Input Debouncing
**Implementation:**
```javascript
// Debounce search input
const debouncedSearch = debounce(searchTerm => {
  performSearch(searchTerm);
}, 300);

searchInput.addEventListener('input', (e) => {
  debouncedSearch(e.target.value);
});
```

#### 2. Filter Optimization
**Implementation:**
- Use efficient filtering algorithms
- Cache filter results
- Virtualize long job lists
- Use Web Workers for heavy computations
- Implement incremental updates

#### 3. Event Handler Optimization
**Implementation:**
- Use passive event listeners where possible
- Avoid inline event handlers
- Use event delegation
- Throttle scroll events
- Optimize click handlers

**Example:**
```javascript
// Use passive listeners
window.addEventListener('scroll', handleScroll, { passive: true });
```

#### 4. Animation Optimization
**Implementation:**
- Use CSS animations instead of JavaScript
- Use transform and opacity
- Avoid layout-thrashing properties
- Use will-change sparingly
- Consider reduced motion preference

---

## CLS (Cumulative Layout Shift) Optimization

### Current Potential Issues

**On /jobs page:**
- Job cards loading without reserved dimensions
- Advertisements without reserved space
- Images without dimensions
- Fonts causing layout shift
- Dynamic content insertion

### Optimization Strategies

#### 1. Reserve Space for Job Cards
**Implementation:**
```css
.job-card {
  min-height: 200px;
  aspect-ratio: 16/9;
}
```

#### 2. Image Dimensions
**Implementation:**
```html
<img 
  src="job-image.webp" 
  width="400" 
  height="300" 
  alt="Job description"
  loading="lazy"
>
```

#### 3. Advertisement Space
**Implementation:**
```css
.ad-container {
  min-height: 250px;
  width: 300px;
}
```

#### 4. Font Optimization
**Implementation:**
```css
@font-face {
  font-display: swap;
}
```

#### 5. Dynamic Content
**Implementation:**
- Reserve space for dynamic content
- Use skeleton screens
- Avoid inserting content above existing content
- Use CSS transitions for smooth changes

---

## Page-Specific Performance Map

### /jobs Page Performance Issues

**LCP Problems:**
- Hero image too large → Compress image, use WebP
- Client-side rendering → Implement SSR
- API delay → Add caching, optimize queries

**INP Problems:**
- Filter recomputation → Add debouncing, virtualization
- Search input → Debounce input, optimize handlers
- Job card interactions → Optimize event handlers

**CLS Problems:**
- Job card dimensions → Reserve space with CSS
- Images without dimensions → Add width/height
- Dynamic content → Reserve space, use skeletons

---

## Implementation Steps

### Phase 1: Critical Performance Issues
1. Implement SSR for /jobs page
2. Optimize hero image (compress, WebP)
3. Add font optimization
4. Reserve space for job cards
5. Optimize API responses

### Phase 2: JavaScript Optimization
1. Implement input debouncing
2. Optimize filter algorithms
3. Code-split JavaScript bundles
4. Add virtual scrolling for long lists
5. Optimize event handlers

### Phase 3: Advanced Optimization
1. Implement Web Workers for heavy tasks
2. Add service worker for caching
3. Optimize bundle size
4. Add performance monitoring
5. Implement progressive rendering

---

## Validation and Testing

### Testing Tools
- [ ] Google PageSpeed Insights (Mobile + Desktop)
- [ ] Lighthouse
- [ ] Chrome DevTools Performance
- [ ] WebPageTest
- [ ] Field Data (Real User Monitoring)

### Validation Checklist

**LCP:**
- [ ] LCP under 2.5s
- [ ] Hero image optimized
- [ ] Fonts optimized
- [ ] SSR implemented
- [ ] API responses optimized

**INP:**
- [ ] INP under 200ms
- [ ] Input debouncing implemented
- [ ] Filters optimized
- [ ] Event handlers optimized
- [ ] Main thread not blocked

**CLS:**
- [ ] CLS under 0.1
- [ ] Job card space reserved
- [ ] Image dimensions set
- [ ] Ad space reserved
- [ ] Font shift minimized

---

## Monitoring

### Continuous Monitoring
1. Set up Google PageSpeed Insights API
2. Monitor Core Web Vitals in Search Console
3. Track performance over time
4. Set up performance budgets
5. Alert on performance degradation

### Key Metrics to Track
- LCP: 75th percentile
- INP: 75th percentile
- CLS: 75th percentile
- First Contentful Paint (FCP)
- Time to Interactive (TTI)
- Total Blocking Time (TBT)

---

## Developer Notes

1. **SSR Priority:** SSR is critical for LCP on /jobs page
2. **Image Optimization:** Compress all images, use modern formats
3. **JavaScript:** Debounce inputs, optimize event handlers
4. **Testing:** Test on real devices, not just lab data
5. **Monitoring:** Monitor real user performance continuously

---

## Success Metrics

- [ ] LCP under 2.5s (75th percentile)
- [ ] INP under 200ms (75th percentile)
- [ ] CLS under 0.1 (75th percentile)
- [ ] Improved PageSpeed Insights score
- [ ] Better user engagement metrics
- [ ] Reduced bounce rate

---

## Common Performance Issues

### Issue 1: Client-Side Only Rendering
**Problem:** Empty initial HTML, slow LCP  
**Solution:** Implement SSR for critical content

### Issue 2: Large Images
**Problem:** Hero image > 500KB  
**Solution:** Compress to < 200KB, use WebP

### Issue 3: No Input Debouncing
**Problem:** Every keystroke triggers expensive operation  
**Solution:** Debounce search/filter inputs

### Issue 4: Layout Shift
**Problem:** Content jumps as it loads  
**Solution:** Reserve space, add dimensions

### Issue 5: Heavy JavaScript
**Problem:** Large bundle blocks main thread  
**Solution:** Code-split, lazy load, optimize

---

**Last Updated:** 4 September 2026  
**Dependencies:** 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md  
**Status:** Implementation Ready