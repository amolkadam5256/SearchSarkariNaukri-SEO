# Digital Library Section

## Section Placement

Place this section after:

```text
03_DAILY_ASSESSMENT
```

and before:

```text
05_JOB_ALERTS
```

---

## Final Section Copy

### Eyebrow

```text
Free Study Material
```

### Heading

```text
Prepare for MPSC & UPSC with our Digital Library
```

### Description

```text
Open useful study material and previous question papers in one place. Select your exam and start reading instantly.
```

### Supporting Line

```text
Read and download free
```

---

## Library Cards

### MPSC Study Material

Description:

```text
Maharashtra competitive-exam books, practice material and previous question papers.
```

CTA:

```text
View Study Material
```

URL:

```text
https://www.searchsarkarinaukri.com/digital-library?category=mpsc#books
```

### UPSC Study Material

Description:

```text
Civil Services study resources, subject papers and previous question papers.
```

CTA:

```text
View Study Material
```

URL:

```text
https://www.searchsarkarinaukri.com/digital-library?category=upsc#books
```

---

## Improved UX Direction

Use a clean two-card layout:

- Header content on top.
- MPSC and UPSC cards below.
- Each card should include a clear title, one short description, and one CTA.
- Use an icon or small subject marker for each card if the design system supports it.
- Keep the section compact so it does not feel like a separate landing page.

Recommended card labels:

```text
MPSC
UPSC
Books
Question Papers
Practice Material
```

Do not show too many tags. Two or three labels per card are enough.

---

## SEO Keyword Targeting

Primary keyword:

```text
MPSC UPSC study material
```

Secondary keywords:

```text
free MPSC study material
free UPSC study material
MPSC books PDF
UPSC previous question papers
MPSC previous question papers
competitive exam study material
government exam preparation material
digital library for government exams
```

Use these naturally in headings, link titles, and card descriptions.

Do not keyword-stuff the visible copy.

Recommended link attributes:

```html
<a
  href="https://www.searchsarkarinaukri.com/digital-library?category=mpsc#books"
  title="Free MPSC study material, books and previous question papers"
>
  View Study Material
</a>
```

```html
<a
  href="https://www.searchsarkarinaukri.com/digital-library?category=upsc#books"
  title="Free UPSC study material, books and previous question papers"
>
  View Study Material
</a>
```

---

## Scroll Animation

Add a smooth scroll reveal animation for the section.

Recommended behavior:

- Eyebrow fades in first.
- Heading slides upward 12px.
- Description fades in after heading.
- Supporting line appears with a short delay.
- MPSC card slides from the left.
- UPSC card slides from the right.
- CTAs fade in after their cards.
- Animation runs once only.

Recommended CSS:

```css
.digital-library [data-scroll-reveal] {
  opacity: 0;
  transform: translateY(12px);
  transition:
    opacity 360ms ease,
    transform 360ms ease;
}

.digital-library [data-scroll-reveal="mpsc-card"] {
  transform: translateX(-16px);
}

.digital-library [data-scroll-reveal="upsc-card"] {
  transform: translateX(16px);
}

.digital-library.is-visible [data-scroll-reveal] {
  opacity: 1;
  transform: translate(0, 0);
}

.digital-library.is-visible [data-scroll-reveal="eyebrow"] {
  transition-delay: 0ms;
}

.digital-library.is-visible [data-scroll-reveal="heading"] {
  transition-delay: 90ms;
}

.digital-library.is-visible [data-scroll-reveal="description"] {
  transition-delay: 170ms;
}

.digital-library.is-visible [data-scroll-reveal="supporting-line"] {
  transition-delay: 240ms;
}

.digital-library.is-visible [data-scroll-reveal="mpsc-card"] {
  transition-delay: 330ms;
}

.digital-library.is-visible [data-scroll-reveal="upsc-card"] {
  transition-delay: 420ms;
}

.digital-library .library-card:hover {
  transform: translateY(-3px);
}
```

Recommended JavaScript:

```js
const librarySection = document.querySelector(".digital-library");
const reduceMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)",
).matches;

if (librarySection && !reduceMotion) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;

        librarySection.classList.add("is-visible");
        observer.disconnect();
      });
    },
    { threshold: 0.25 },
  );

  observer.observe(librarySection);
}
```

Reduced motion:

```css
@media (prefers-reduced-motion: reduce) {
  .digital-library [data-scroll-reveal],
  .digital-library .library-card:hover {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## Suggested HTML Structure

```html
<section class="digital-library" aria-labelledby="digital-library-title">
  <p data-scroll-reveal="eyebrow">Free Study Material</p>

  <h2 id="digital-library-title" data-scroll-reveal="heading">
    Prepare for MPSC &amp; UPSC with our Digital Library
  </h2>

  <p data-scroll-reveal="description">
    Open useful study material and previous question papers in one place. Select
    your exam and start reading instantly.
  </p>

  <p data-scroll-reveal="supporting-line">Read and download free</p>

  <div class="library-card-grid">
    <article class="library-card" data-scroll-reveal="mpsc-card">
      <p>MPSC</p>
      <h3>MPSC Study Material</h3>
      <p>
        Maharashtra competitive-exam books, practice material and previous
        question papers.
      </p>
      <a
        href="https://www.searchsarkarinaukri.com/digital-library?category=mpsc#books"
        title="Free MPSC study material, books and previous question papers"
      >
        View Study Material
      </a>
    </article>

    <article class="library-card" data-scroll-reveal="upsc-card">
      <p>UPSC</p>
      <h3>UPSC Study Material</h3>
      <p>
        Civil Services study resources, subject papers and previous question
        papers.
      </p>
      <a
        href="https://www.searchsarkarinaukri.com/digital-library?category=upsc#books"
        title="Free UPSC study material, books and previous question papers"
      >
        View Study Material
      </a>
    </article>
  </div>
</section>
```

---

## Quality Checklist

- [ ] Section appears immediately after Daily Assessment.
- [ ] MPSC CTA goes to `/digital-library?category=mpsc#books`.
- [ ] UPSC CTA goes to `/digital-library?category=upsc#books`.
- [ ] Visible copy remains concise.
- [ ] Scroll animation runs once.
- [ ] Reduced-motion users see static content.
- [ ] Links are crawlable anchor tags.
- [ ] Card titles use real text, not image text.
