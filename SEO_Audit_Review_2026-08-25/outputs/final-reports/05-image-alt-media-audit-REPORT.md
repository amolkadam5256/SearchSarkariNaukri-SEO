# 05 — Image, Alt Text & Media Audit — AUDIT REPORT
Site: https://www.searchsarkarinaukri.com/
Audit date: 25 August 2026
Auditor: Codex + custom Googlebot crawler + Lighthouse 13.4.1 + read-only source/server/database review
Checklist source: 05-image-alt-media-audit.md
Total items checked: 15
Total Pass: 8 | Total Warning: 1 | Total Fail: 6 | Total N/A: 0

| # | Checklist Item | Status | Evidence | Affected URL(s) | Severity | Recommended Fix | Effort (S/M/L) |
|---:|---|---|---|---|---|---|:---:|
| 1 | Crawl every `<img>` tag site-wide, export full list with: image URL, page it's on, current `alt` attribute value (or blank if missing) | ✅ Pass | `images-all.csv`: complete 67-image occurrence export with page, URL, alt, loading, srcset/sizes, width/height. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 2 | Report exact percentage of images with missing/empty `alt` attributes | ✅ Pass | 0/67 missing alt and 0/67 empty alt: 0.00%. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 3 | Report exact percentage of images with generic/non-descriptive alt text (e.g. `alt="image1.jpg"`, `alt="logo"`, `alt=""` on meaningful images) | ✅ Pass | Blog cover alt values are descriptive article titles; no generic `logo`/filename-only alt found in the crawler export. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 4 | Decorative images (icons, dividers) confirmed to correctly use `alt=""` (empty is correct for decorative — flag only meaningful images missing alt) | ✅ Pass | No decorative `<img>` occurrence was found in Googlebot HTML; UI icons are code/SVG, so empty decorative alt was not required in this set. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 5 | og:image (`/og-image.png`) has appropriate file — confirm dimensions match og:image:width/height meta values (1200x630 declared — verify actual file) | ✅ Pass | `image-dimension-evidence.csv`: actual og-image 1200×630, exactly matching declared metadata; 97,951 bytes. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 6 | Modern format usage (WebP/AVIF) vs legacy (JPEG/PNG) — report ratio | ❌ Fail | All 67 crawled editorial images are PNG: 0% WebP/AVIF, 100% legacy PNG. | site-wide | Medium | Serve WebP/AVIF with PNG/JPEG fallback and automate conversion on upload. | M |
| 7 | Responsive images (`srcset`/`sizes`) implemented for hero/banner images | ❌ Fail | 0/67 images use srcset; 0/67 use sizes. | site-wide media | Medium | Generate width variants and add accurate srcset/sizes to editorial and hero images. | M |
| 8 | Lazy-loading (`loading="lazy"`) implemented for below-the-fold images | ❌ Fail | 0/67 images declare loading=lazy. | site-wide media | Medium | Add loading=lazy and decoding=async below the fold; keep only the LCP image eager/high-priority. | M |
| 9 | Image file sizes audited — flag any image over 200KB without justification | ❌ Fail | `image-http-size-audit.csv`: all 67 exceed 200 KB; min 1.12 MB, median 2.66 MB, max 10.19 MB; total 339.52 MB. | site-wide media | High | Batch-convert/compress covers to WebP/AVIF, create responsive variants, enforce upload byte/dimension limits, and backfill existing assets. | M |
| 10 | CDN usage for image delivery confirmed or absent | ⚠️ Warning | All image URLs use the first-party www host served directly from the DigitalOcean origin; no image CDN/transform service observed. | site-wide media | Medium | Add an image/static CDN or edge cache with transforms while preserving canonical asset URLs and cache headers. | L |
| 11 | Image filenames reviewed for descriptiveness (not `IMG_2031.jpg` style) | ❌ Fail | All blog cover filenames contain timestamps/random IDs and Gemini_Generated_Image/ChatGPT_Image tokens rather than descriptive slugs. | site-wide media | Medium | Rename new uploads to concise article/topic slugs and migrate old assets with redirects or stable media mapping. | M |
| 12 | Images included in a dedicated Image Sitemap (recommended if site has meaningful editorial images, e.g. organization logos) — confirm presence/absence | ❌ Fail | No image sitemap child exists in the 11-file sitemap index. | site-wide / sitemap files | Medium | Regenerate sitemap children from current canonical 200 indexable records only; include missing self-canonical pages, remove 410s/empty files, and validate XSD before publish. | M |
| 13 | Logo image has proper alt text matching brand name | ✅ Pass | `Navbar.jsx` uses `alt="SearchSarkariNaukri"` for the logo. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 14 | Favicon present and renders correctly in browser tab + Google SERP | ✅ Pass | 16/32/192/512 favicon assets and favicon.ico exist; browser screenshot assets captured. | site-wide media | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |
| 15 | Apple touch icon / Android chrome icons present for PWA/bookmark use | ✅ Pass | 180×180 Apple touch icon plus 192/512 Android icons and manifest are present. | site-wide | Info | No remediation required; retain this behavior and regression-test after SEO changes. | S |

## Image headline

- Googlebot-visible images: 67 unique occurrences.
- Missing/empty alt: 0 (0.00%).
- Format: 67 PNG; 0 WebP/AVIF.
- Responsive/lazy attributes: 0 srcset, 0 sizes, 0 lazy.
- HTTP file sizes: all 67 over 200 KB; 1.12–10.19 MB, median 2.66 MB, aggregate 339.52 MB.

## Summary
- Critical issues: 0 — none
- High issues: 1 — 9
- Medium issues: 6 — 6, 7, 8, 10, 11, 12
- Low issues: 0 — none
- Top 3 priority fixes for this audit area:
  1. Item 9: Batch-convert/compress covers to WebP/AVIF, create responsive variants, enforce upload byte/dimension limits, and backfill existing assets.
  2. Item 6: Serve WebP/AVIF with PNG/JPEG fallback and automate conversion on upload.
  3. Item 7: Generate width variants and add accurate srcset/sizes to editorial and hero images.
