# 24 — IMAGE / MEDIA / SOCIAL SEO

**Section:** Image and Social Media Optimization  
**Priority:** P2  
**Type:** Technical SEO  
**Status:** Implementation Ready

---

## Ground Rules Reminder

> **Follow the ground rules in `01_ground_rules_do_not_delete_UPDATED.md`. This provides image/social SEO without removing existing functionality.**

---

## Goal

Optimize images and social media assets for search engines, social platforms, and user experience while maintaining performance and accessibility.

---

## Image File Naming Conventions

### Good Filenames

**Recommended Format:**
```
government-jobs-2026-search-sarkarinaukri.webp
msrtc-recruitment-2026-solapur.jpg
maharashtra-government-jobs-pune.jpg
railway-recruitment-2026-rrb.jpg
12th-pass-government-jobs.jpg
```

### Bad Filenames

**Avoid:**
```
IMG_938472.jpg
image1.png
download.jpg
photo (1).jpg
DSC_0001.jpg
final-banner-v2.jpg
```

---

## Alt Text Guidelines

### Good Alt Text

**Descriptive and Contextual:**
```
Government Jobs 2026 on Search Sarkari Naukri homepage
MSRTC Solapur Recruitment 2026 - 306 vacancies
Maharashtra government jobs listing page
Railway recruitment notification image
```

### Bad Alt Text

**Avoid:**
```
image
photo
picture
government jobs government jobs government jobs
job recruitment job recruitment
sarkari naukri sarkari naukri
```

**Rules:**
- Be descriptive but concise
- Include relevant keywords naturally
- Don't repeat the same alt text on multiple images
- Don't keyword stuff
- Don't use "image of" or "picture of"

---

## Image Format and Performance

### Format Priority

**Use in Order:**
1. **WebP** - Modern format, excellent compression
2. **AVIF** - Even better compression, newer format
3. **JPEG** - Fallback for older browsers
4. **PNG** - Only for transparency requirements

### Compression Guidelines

**Target File Sizes:**
- Hero images: < 200KB
- Section images: < 100KB
- Thumbnails/Icons: < 50KB
- Logos: < 30KB

**Quality Settings:**
- WebP: Quality 80-85
- JPEG: Quality 80-85
- PNG: Use compression tools

---

## Image Dimensions and CLS Prevention

### Always Specify Dimensions

**HTML Attributes:**
```html
<img 
  src="government-jobs-2026.webp" 
  width="1200" 
  height="630" 
  alt="Government Jobs 2026 on Search Sarkari Naukri"
  loading="lazy"
>
```

**CSS Approach:**
```css
.hero-image {
  width: 1200px;
  height: 630px;
  aspect-ratio: 1200/630;
}
```

**Why:** Prevents Cumulative Layout Shift (CLS) by reserving space.

---

## Lazy Loading Implementation

### Below-the-Fold Images

**Add loading="lazy":**
```html
<img 
  src="category-image.webp" 
  alt="Railway government jobs" 
  loading="lazy"
  width="400" 
  height="300"
>
```

### Above-the-Fold Images

**Do NOT lazy load:**
- Hero images
- Logo
- Critical navigation images
- First screen content

---

## Social Media Images

### Open Graph Image

**Requirements:**
- **Size:** 1200x630 pixels (1.91:1 ratio)
- **Format:** JPG or PNG
- **File Size:** < 5MB
- **Content:** Page-relevant, branded

**Example:**
```html
<meta property="og:image" content="https://www.searchsarkarinaukri.com/og-government-jobs-2026.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Government Jobs 2026 - Search Sarkari Naukri">
```

### Twitter Card Image

**Requirements:**
- **Size:** 1200x600 pixels
- **Format:** JPG or PNG
- **File Size:** < 5MB
- **Content:** Page-relevant, branded

**Example:**
```html
<meta name="twitter:image" content="https://www.searchsarkarinaukri.com/twitter-government-jobs-2026.jpg">
<meta name="twitter:image:alt" content="Government Jobs 2026 - Search Sarkari Naukri">
```

---

## Favicon and Logo

### Favicon Requirements

**Standard Sizes:**
- 16x16 (favicon.ico)
- 32x32 (favicon.ico)
- 180x180 (Apple touch icon)
- 192x192 (Android Chrome)
- 512x512 (Windows tile)

**Implementation:**
```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png">
```

---

## Organization Logos

### Official Organisation Logos

**Usage on Job Pages:**
```html
<img 
  src="/logos/msrtc-logo.png" 
  alt="MSRTC - Maharashtra State Road Transport Corporation logo"
  width="200" 
  height="80"
  loading="lazy"
>
```

**Guidelines:**
- Use official logos where available
- Maintain aspect ratio
- Add descriptive alt text
- Don't hotlink from external sites
- Use optimized versions

---

## Image Sitemap

### Create Image Sitemap

**When to Use:**
- Large number of images
- Important images for search visibility
- Images in structured data

**Example:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://www.searchsarkarinaukri.com/jobs/123/msrtc-recruitment</loc>
    <image:image>
      <image:loc>https://www.searchsarkarinaukri.com/images/ms-recruitment.jpg</image:loc>
      <image:title>MSRTC Recruitment 2026</image:title>
      <image:caption>MSRTC Solapur recruitment banner</image:caption>
    </image:image>
  </url>
</urlset>
```

---

## Decorative Images

### Accessibility Handling

**Decorative Images:**
```html
<img src="decorative-pattern.png" alt="" role="presentation" loading="lazy">
```

**Background Images:**
```css
.hero-section {
  background-image: url('hero-bg.jpg');
  background-size: cover;
  background-position: center;
}
```

**Rule:** Add `role="presentation"` and empty alt for decorative images.

---

## Job Card Images

### Recommendation

**For Government Jobs:**
- **Primary Approach:** No individual job card images
- **Secondary Approach:** Use organisation logos only
- **Benefits:** Faster page load, cleaner design, better performance

**If Using Job Images:**
- Use organisation logos or category icons
- Keep file sizes minimal (< 20KB)
- Use consistent dimensions
- Lazy load all card images

---

## Image Optimization Checklist

### File Optimization
- [ ] Images compressed (WebP/AVIF preferred)
- [ ] File sizes within target ranges
- [ ] Proper dimensions specified
- [ ] Lazy loading implemented for below-fold images
- [ ] No decorative images blocking critical resources

### Alt Text
- [ ] All images have descriptive alt text
- [ ] Alt text includes relevant keywords naturally
- [ ] No keyword stuffing in alt text
- [ ] Decorative images marked properly
- [ ] Alt text varies across images

### Social Media
- [ ] OG image implemented (1200x630)
- [ ] Twitter card image implemented
- [ ] OG image alt text provided
- [ ] File sizes under 5MB
- [ ] Images tested with social media debuggers

### Performance
- [ ] CLS prevented by dimensions
- [ ] LCP not blocked by large images
- [ ] Images served from CDN (if available)
- [ ] Image HTTP/2 or HTTP/3
- [ ] No unnecessary image redirects

---

## Implementation Steps

### Step 1: Image Audit
1. Audit all existing images
2. Identify large images
3. Check for missing alt text
4. Identify non-optimized formats
5. Check for CLS issues

### Step 2: Image Optimization
1. Convert to WebP/AVIF format
2. Compress images to target sizes
3. Add proper dimensions
4. Implement lazy loading
5. Add CDN if available

### Step 3: Alt Text Implementation
1. Add descriptive alt text to all images
2. Remove keyword stuffing
3. Ensure alt text variety
4. Mark decorative images properly
5. Test with accessibility tools

### Step 4: Social Media Images
1. Create OG image (1200x630)
2. Create Twitter card image
3. Add proper meta tags
4. Test with social media debuggers
5. Validate image requirements

### Step 5: Monitoring
1. Monitor image performance
2. Track CLS issues
3. Check social media previews
4. Monitor image load times
5. Audit new images regularly

---

## Developer Notes

1. **Format Conversion:** Use image optimization tools for batch conversion
2. **CDN:** Implement CDN for image delivery if available
3. **Responsive Images:** Use srcset for responsive images if needed
4. **Alt Text:** Create guidelines for content writers
5. **Testing:** Test image optimization with PageSpeed Insights

---

## Success Metrics

- [ ] Improved Core Web Vitals (CLS)
- [ ] Faster page load times
- [ ] Better social media previews
- [ ] Higher image search visibility
- [ ] Improved accessibility scores
- [ ] Reduced bandwidth usage

---

## Common Image SEO Mistakes

### Mistake 1: No Alt Text
**Problem:** Missing alt text on images  
**Solution:** Add descriptive alt text to all images

### Mistake 2: Keyword Stuffing
**Problem:** "government jobs government jobs sarkari naukri"  
**Solution:** Use natural, descriptive alt text

### Mistake 3: No Dimensions
**Problem:** Images without width/height causing CLS  
**Solution:** Always specify image dimensions

### Mistake 4: Large File Sizes
**Problem:** Images > 500KB slowing page load  
**Solution:** Compress images to target sizes

### Mistake 5: Wrong Format
**Problem:** Using PNG when JPEG would suffice  
**Solution:** Use appropriate format for image type

---

**Last Updated:** 4 September 2026  
**Dependencies:** 15_TECHNICAL_SEO_GEO_AEO_CHECKLIST.md  
**Status:** Implementation Ready