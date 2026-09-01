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
