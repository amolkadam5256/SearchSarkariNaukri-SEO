# 19 — Core Web Vitals Performance Optimization

## 19.1 Target Thresholds Matrix

| Metric | Metric Full Name | Good Threshold | Needs Improvement | Poor Threshold | Our Target |
|--------|------------------|----------------|-------------------|----------------|------------|
| **LCP** | Largest Contentful Paint | <= 2.5s | 2.5s – 4.0s | > 4.0s | **< 2.0s** |
| **CLS** | Cumulative Layout Shift | <= 0.10 | 0.10 – 0.25 | > 0.25 | **< 0.05** |
| **INP** | Interaction to Next Paint | <= 200ms | 200ms – 500ms | > 500ms | **< 150ms** |
| **FCP** | First Contentful Paint | <= 1.8s | 1.8s – 3.0s | > 3.0s | **< 1.5s** |
| **TTFB** | Time to First Byte | <= 800ms | 800ms – 1800ms | > 1800ms | **< 200ms** |

---

## 19.2 Metric Optimization Levers

### LCP (Largest Contentful Paint) Levers
- Preload LCP hero image: `<link rel="preload" as="image" fetchpriority="high" href="...">`.
- Serve images in compressed WebP/AVIF formats.
- Enable Cloudflare HTML Edge Caching (Target TTFB < 200ms).
- Server-side render (SSR) critical hero elements in initial HTML response.

### CLS (Cumulative Layout Shift) Levers
- Reserve explicit `width` and `height` attributes on all `<img>` and `<iframe>` elements.
- Apply fixed `min-height` CSS rules on ad containers before ad scripts load.
- Use `font-display: swap` combined with size-matched fallback fonts (`font-technology`).

### INP (Interaction to Next Paint) Levers
- Split long JavaScript execution tasks into chunks < 50ms using `requestIdleCallback`.
- Defer non-critical third-party analytics and ad scripts via GTM.
- Use passive event listeners for scroll and touch handlers.

---

## 19.3 Technical Resource Hints Code Block

```html
<!-- Preconnect to critical external domains -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="preconnect" href="https://www.googletagmanager.com" />
<link rel="preconnect" href="https://pagead2.googlesyndication.com" />

<!-- Preload critical fonts & LCP images -->
<link rel="preload" as="font" type="font/woff2" href="/fonts/inter-var.woff2" crossorigin />
<link rel="preload" as="image" fetchpriority="high" href="/images/hero-banner.webp" />

<!-- DNS Prefetch for non-critical assets -->
<link rel="dns-prefetch" href="https://www.google-analytics.com" />
<link rel="dns-prefetch" href="https://clarity.microsoft.com" />
```
