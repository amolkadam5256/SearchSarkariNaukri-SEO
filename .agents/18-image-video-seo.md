# 18 — Image & Video SEO Standards

## 18.1 Image Optimization Technical Standards

- **Format:** WebP primary format (AVIF where supported; JPEG/PNG legacy fallback).
- **Naming Rule:** Lowercase, hyphenated, descriptive file names including target keyword (`ssc-cgl-2026-eligibility-table.webp`).
- **ALT Attributes:** Mandatory descriptive `alt` attribute on 100% of images.
- **Explicit Dimensions:** Mandatory `width` and `height` attributes on HTML `<img>` elements to avoid Cumulative Layout Shift (CLS).
- **Lazy Loading:** `loading="lazy"` on all below-fold content images; `fetchpriority="high"` on LCP hero image.

### Image Compression Standards Matrix

| Image Type | Max File Size Target | Target Dimensions | Primary Format |
|------------|----------------------|-------------------|----------------|
| **Hero / Featured Image** | < 150KB | 1200 × 630 px | WebP / AVIF |
| **Content Body Images** | < 80KB | 800 × 600 px | WebP |
| **Thumbnails** | < 30KB | 300 × 200 px | WebP |
| **Open Graph Images** | < 100KB | 1200 × 630 px | WebP / JPEG |
| **Icons & Logos** | < 20KB | Various | SVG / WebP |

---

## 18.2 Video SEO & Schema Protocol

- **Hosting Platform:** YouTube embedded videos providing exam prep, syllabus analysis, or application walkthroughs.
- **On-Page Optimization:** Descriptive video titles, 200-word summary description, timestamps/chapters, closed captions SRT files.

### VideoObject Schema JSON-LD Syntax
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to Apply for SSC CGL 2026 — Step by Step Guide",
  "description": "Watch this complete video guide to fill out the SSC CGL 2026 application form online...",
  "thumbnailUrl": "https://www.searchsarkarinaukri.com/images/thumbs/ssc-cgl-video.webp",
  "uploadDate": "2026-07-20T10:00:00+05:30",
  "duration": "PT5M30S",
  "contentUrl": "https://www.youtube.com/watch?v=XXXXXXXXXXX",
  "embedUrl": "https://www.youtube.com/embed/XXXXXXXXXXX"
}
```
