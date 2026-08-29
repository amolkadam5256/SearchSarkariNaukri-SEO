# 05 — Image, Alt Text & Media Audit

Output file: `outputs/final-reports/05-image-alt-media-audit-REPORT.md`

## A. Alt Text Coverage (explicitly requested — check ALL images)
- [ ] Crawl every `<img>` tag site-wide, export full list with: image URL, page
  it's on, current `alt` attribute value (or blank if missing)
- [ ] Report exact percentage of images with missing/empty `alt` attributes
- [ ] Report exact percentage of images with generic/non-descriptive alt text
  (e.g. `alt="image1.jpg"`, `alt="logo"`, `alt=""` on meaningful images)
- [ ] Decorative images (icons, dividers) confirmed to correctly use `alt=""`
  (empty is correct for decorative — flag only meaningful images missing alt)
- [ ] og:image (`/og-image.png`) has appropriate file — confirm dimensions
  match og:image:width/height meta values (1200x630 declared — verify actual file)

## B. Image Performance
- [ ] Modern format usage (WebP/AVIF) vs legacy (JPEG/PNG) — report ratio
- [ ] Responsive images (`srcset`/`sizes`) implemented for hero/banner images
- [ ] Lazy-loading (`loading="lazy"`) implemented for below-the-fold images
- [ ] Image file sizes audited — flag any image over 200KB without justification
- [ ] CDN usage for image delivery confirmed or absent

## C. Image SEO
- [ ] Image filenames reviewed for descriptiveness (not `IMG_2031.jpg` style)
- [ ] Images included in a dedicated Image Sitemap (recommended if site has
  meaningful editorial images, e.g. organization logos) — confirm presence/absence
- [ ] Logo image has proper alt text matching brand name

## D. Favicon & App Icons
- [ ] Favicon present and renders correctly in browser tab + Google SERP
- [ ] Apple touch icon / Android chrome icons present for PWA/bookmark use
