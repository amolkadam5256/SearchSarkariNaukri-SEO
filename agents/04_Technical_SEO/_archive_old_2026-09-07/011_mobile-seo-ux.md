# 11. Mobile SEO & UX

This file keeps the useful mobile guidance from the older audit and aligns it with the newer August 8, 2026 fix pack.

## The problem

The site appears to have a responsive foundation, but mobile SEO still depends on the rendered experience Googlebot Smartphone and real users receive. The main risks are:

- Touch targets and spacing may be inconsistent on job cards, navigation, filters, and form controls.
- Some mobile text may render below the practical 16px readability baseline.
- Push notification prompts and third-party scripts can hurt INP and LCP on mobile.
- Images need responsive sizes, explicit dimensions, modern formats, and lazy loading below the fold.
- Forms such as eligibility checkers should use mobile keyboard hints (`inputmode`, `type`, `autocomplete`) and accessible labels.
- Primary navigation and important crawl links need to exist in raw/prerendered HTML, not only after client JavaScript.

## Fix checklist

- [ ] Confirm `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is present on every indexable template.
- [ ] Keep tap targets at least 44px by 44px with enough spacing to avoid accidental taps.
- [ ] Use mobile-readable font sizes for body copy, filters, job metadata, and form labels.
- [ ] Defer non-essential third-party scripts on mobile until after the main content is interactive.
- [ ] Delay OneSignal or similar permission prompts until after a user action; never show them immediately on first paint.
- [ ] Add explicit `width` and `height` to images to reduce CLS.
- [ ] Serve responsive images with `srcset`/`sizes` and WebP or AVIF where possible.
- [ ] Lazy-load below-the-fold images and avoid lazy-loading the LCP image.
- [ ] Add `inputmode`, semantic `type`, and `autocomplete` values to mobile forms.
- [ ] Confirm hamburger menus, filters, pagination, breadcrumbs, and key category/district links work with touch.
- [ ] Confirm important links are present in server-rendered or prerendered HTML.

## Implementation notes

Use CSS similar to:

```css
button,
a,
input,
select,
textarea,
.clickable,
.nav-link,
.job-card {
  min-height: 44px;
}

button,
a,
input,
select,
textarea {
  touch-action: manipulation;
}
```

Use mobile form attributes similar to:

```html
<input type="number" inputmode="numeric" min="18" max="65" autocomplete="off" aria-label="Age">
<input type="tel" inputmode="tel" autocomplete="tel" aria-label="Mobile number">
<input type="email" inputmode="email" autocomplete="email" aria-label="Email address">
<input type="date" autocomplete="bday" aria-label="Date of birth">
```

For images:

```html
<picture>
  <source type="image/avif" srcset="/images/job-400.avif 400w, /images/job-800.avif 800w" sizes="(max-width: 640px) 100vw, 50vw">
  <source type="image/webp" srcset="/images/job-400.webp 400w, /images/job-800.webp 800w" sizes="(max-width: 640px) 100vw, 50vw">
  <img src="/images/job-800.jpg" width="800" height="450" alt="Government job update" loading="lazy">
</picture>
```

## Verification

Run these after deployment:

```bash
# Mobile Lighthouse check
npx lighthouse https://www.searchsarkarinaukri.com/ --form-factor=mobile --screenEmulation.mobile=true

# Confirm raw HTML exposes key mobile/crawl links
curl -s https://www.searchsarkarinaukri.com/ | grep -Ei "viewport|/jobs|/department|/district|canonical"
```

Also verify in Search Console:

- Mobile usability issues stay at zero.
- Core Web Vitals mobile field data improves.
- Googlebot Smartphone can access primary content and links without blocked resources.
