# Daily UPSC & MPSC Assessment Section

## Section Placement

Place this section after:

```text
02_LIVE_STATISTICS
```

and before:

```text
04_DIGITAL_LIBRARY
```

---

## Final Section Copy

### Eyebrow

```text
A smarter daily study habit
```

### Heading

```text
Daily UPSC & MPSC Assessment
```

### Description

```text
Solve 10 AI-generated questions every day - 5 from last week's current affairs and 5 from the exam syllabus. No repeated questions for you.
```

### Feature Points

```text
Only 10 questions
New questions every day
Results on your dashboard
```

### CTA

```text
Start today's assessment
```

CTA URL:

```text
https://www.searchsarkarinaukri.com/daily-assessment
```

---

## SEO Keyword Targeting

Primary keyword:

```text
Daily UPSC MPSC assessment
```

Secondary keywords:

```text
UPSC daily current affairs quiz
MPSC daily current affairs quiz
UPSC practice questions
MPSC practice questions
government exam daily test
daily exam preparation quiz
AI generated exam questions
current affairs assessment for UPSC
current affairs assessment for MPSC
```

Use keywords naturally in:

- heading
- short description
- CTA `aria-label`
- internal link title
- image alt text if a meaningful section image is used

Do not keyword-stuff the visible section copy.

Recommended hidden/accessibility label for CTA:

```html
<a
  href="https://www.searchsarkarinaukri.com/daily-assessment"
  aria-label="Start today's Daily UPSC and MPSC Assessment with current affairs and syllabus questions"
>
  Start today's assessment
</a>
```

---

## Scrolling Animation

Add a soft scroll reveal animation when this section enters the viewport.

Recommended behavior:

- Eyebrow fades in first.
- Heading slides up 10-14px.
- Description fades in after the heading.
- Feature points stagger one by one.
- CTA appears last with a small upward movement.
- Animation should run once only.

Recommended CSS:

```css
.daily-assessment [data-scroll-reveal] {
  opacity: 0;
  transform: translateY(12px);
  transition:
    opacity 360ms ease,
    transform 360ms ease;
}

.daily-assessment.is-visible [data-scroll-reveal] {
  opacity: 1;
  transform: translateY(0);
}

.daily-assessment.is-visible [data-scroll-reveal="eyebrow"] {
  transition-delay: 0ms;
}

.daily-assessment.is-visible [data-scroll-reveal="heading"] {
  transition-delay: 90ms;
}

.daily-assessment.is-visible [data-scroll-reveal="description"] {
  transition-delay: 170ms;
}

.daily-assessment.is-visible [data-scroll-reveal="feature-1"] {
  transition-delay: 250ms;
}

.daily-assessment.is-visible [data-scroll-reveal="feature-2"] {
  transition-delay: 330ms;
}

.daily-assessment.is-visible [data-scroll-reveal="feature-3"] {
  transition-delay: 410ms;
}

.daily-assessment.is-visible [data-scroll-reveal="cta"] {
  transition-delay: 500ms;
}
```

Recommended JavaScript:

```js
const assessmentSection = document.querySelector('.daily-assessment');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (assessmentSection && !reduceMotion) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      assessmentSection.classList.add('is-visible');
      observer.disconnect();
    });
  }, { threshold: 0.25 });

  observer.observe(assessmentSection);
}
```

Reduced motion:

```css
@media (prefers-reduced-motion: reduce) {
  .daily-assessment [data-scroll-reveal] {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## Suggested HTML Structure

```html
<section class="daily-assessment" aria-labelledby="daily-assessment-title">
  <p data-scroll-reveal="eyebrow">A smarter daily study habit</p>

  <h2 id="daily-assessment-title" data-scroll-reveal="heading">
    Daily UPSC &amp; MPSC Assessment
  </h2>

  <p data-scroll-reveal="description">
    Solve 10 AI-generated questions every day - 5 from last week's current
    affairs and 5 from the exam syllabus. No repeated questions for you.
  </p>

  <ul>
    <li data-scroll-reveal="feature-1">Only 10 questions</li>
    <li data-scroll-reveal="feature-2">New questions every day</li>
    <li data-scroll-reveal="feature-3">Results on your dashboard</li>
  </ul>

  <a
    href="https://www.searchsarkarinaukri.com/daily-assessment"
    data-scroll-reveal="cta"
    aria-label="Start today's Daily UPSC and MPSC Assessment with current affairs and syllabus questions"
  >
    Start today's assessment
  </a>
</section>
```

---

## Universal Developer Guardrail

Apply this rule before using this file for implementation:

1. Audit the existing homepage/component first.
2. Do not delete existing sections, components, internal links, SEO copy, metadata, schema, job data, or URLs without explicit approval.
3. Preserve approved Sections `01-10`; patch only verified issues.
4. If this section already exists in code, improve the existing component instead of rebuilding it unnecessarily.
5. Never invent vacancies, dates, salary, eligibility, age limits, selection process, official links, job counts, subscriber counts, exam dates, or government approval.
6. Verify every internal URL and official external URL before publishing.
7. Remove or replace links to true `404`/`410` pages; keep those URLs out of sitemap, schema, breadcrumbs, related links, and internal-link hubs.
8. Use one-hop `301` only when there is a close relevant replacement.
9. Do not create thin doorway pages, duplicate SEO pages, keyword-stuffed sections, or fake urgency.
10. Do not change navbar, footer, header, logo, global menu, global styles, analytics, tracking, or unrelated routes unless a documented bug requires it and regression QA is completed.
11. SearchSarkariNaukri must be described as an independent information portal, not an official government website.
12. Final signoff requires audit, implementation, live URL/status checks, sitemap/canonical/robots/schema validation, mobile QA, accessibility QA, and performance QA.
