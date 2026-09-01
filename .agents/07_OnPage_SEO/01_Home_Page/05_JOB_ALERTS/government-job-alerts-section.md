# Government Job Alerts Section

## Section Placement

Place this section after:

```text
04_DIGITAL_LIBRARY
```

and before:

```text
06_EXAM_COUNTDOWN
```

---

## Section Goal

Help users subscribe to relevant government job alerts by channel,
qualification, exam type, and location.

This section should feel active and useful, not like a generic newsletter
block.

---

## Final Section Copy

### Eyebrow

```text
Never miss an important update
```

### Heading

```text
Government Job Alerts on WhatsApp & Telegram
```

### Description

```text
Get timely Sarkari Naukri updates for new vacancies, last dates, admit cards, results and exam alerts. Choose your preferred channel and follow jobs that match your profile.
```

### Supporting Line

```text
Set alerts by qualification, department, exam and location.
```

---

## Alert Cards

### WhatsApp Alerts

Title:

```text
WhatsApp Job Alerts
```

Description:

```text
Receive important vacancy updates, closing-soon reminders and exam notices directly on WhatsApp.
```

CTA:

```text
Join WhatsApp Alerts
```

Suggested URL:

```text
https://www.searchsarkarinaukri.com/job-alerts/whatsapp
```

### Telegram Alerts

Title:

```text
Telegram Job Alerts
```

Description:

```text
Follow fast updates for Sarkari Naukri, Maharashtra jobs, UPSC, MPSC, banking, railway and police recruitment.
```

CTA:

```text
Join Telegram Alerts
```

Suggested URL:

```text
https://www.searchsarkarinaukri.com/job-alerts/telegram
```

### Personalized Alerts

Title:

```text
Personalized Job Alerts
```

Description:

```text
Select your qualification, age range, state, district and preferred job category to see better-matched updates.
```

CTA:

```text
Set My Preferences
```

Suggested URL:

```text
https://www.searchsarkarinaukri.com/job-alerts/preferences
```

---

## Creative UX Direction

Use this exact UI pattern:

```text
┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
│      WhatsApp      │  │     Telegram       │  │    Personalised    │
│                    │  │                    │  │                    │
│       green dot    │  │       blue dot     │  │      purple dot    │
│                    │  │                    │  │                    │
│ WhatsApp Job       │  │ Telegram Job       │  │ Personalized Job   │
│ Alerts             │  │ Alerts             │  │ Alerts             │
│                    │  │                    │  │                    │
│ [Join WhatsApp]    │  │ [Join Telegram]    │  │ [Set Preferences]  │
└────────────────────┘  └────────────────────┘  └────────────────────┘

       ↓

┌─────────────────────────────────────────────────────────────────────┐
│ By Qualification │ By Location │ By Job Category                    │
│ 10th │ 12th │ Graduate │ Maharashtra │ Pune │ MPSC │ UPSC │ Railway│
└─────────────────────────────────────────────────────────────────────┘
```

Design notes:

- Use three equal-width cards on desktop.
- Each card should have a small top label, a large colored status dot,
  title text and one CTA.
- Use green for WhatsApp, blue for Telegram and purple for Personalized.
- Put the preference selector in one full-width strip below the cards.
- Keep the strip grouped by Qualification, Location and Job Category.
- Keep chips as real links where possible.
- Avoid fake subscriber counts unless backed by real data.

---

## Suggested Preference Chips

Qualification chips:

```text
10th Pass
12th Pass
Graduate
ITI
Diploma
Post Graduate
```

Location chips:

```text
Maharashtra
Pune
Mumbai
Nagpur
Nashik
All India
```

Category chips:

```text
MPSC
UPSC
Railway
Banking
Police
Defence
Teaching
```

Suggested chip links:

```text
/jobs?qualification=10th-pass
/jobs?qualification=graduate
/jobs?state=maharashtra
/jobs?city=pune
/jobs?category=railway
/jobs?category=police
```

---

## Desktop UX

Desktop can use either:

- 2-column layout: copy and preferences on the left, alert cards on the right.
- 3-card layout: WhatsApp, Telegram and Personalized Alerts in one row.

Recommended desktop layout:

```text
┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
│ WhatsApp card       │  │ Telegram card       │  │ Preferences card    │
└────────────────────┘  └────────────────────┘  └────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ Qualification chips | Location chips | Job category chips           │
└─────────────────────────────────────────────────────────────────────┘
```

If the existing site already has a design for this section, preserve that
UI and improve the content, links and animation within the same structure.

---

## Mobile UX

Mobile order:

```text
Eyebrow
Heading
Description
WhatsApp CTA
Telegram CTA
Personalized CTA
Qualification chips
Location chips
Category chips
```

Rules:

- CTAs must be large enough to tap comfortably.
- Keep chips horizontally scrollable if the list is long.
- Do not stack too many chips before the main alert CTAs.

---

## SEO Keyword Targeting

Primary keyword:

```text
government job alerts
```

Secondary keywords:

```text
Sarkari Naukri alerts
WhatsApp government job alerts
Telegram government job alerts
Maharashtra job alerts
MPSC job alerts
UPSC job alerts
railway job alerts
banking job alerts
police recruitment alerts
latest government vacancy alerts
```

Use keywords naturally in:

- heading
- alert card titles
- CTA titles
- internal link titles
- aria labels

Do not repeat the same keyword in every card.

---

## Scroll Animation

Add a lively but controlled scroll reveal animation.

Recommended behavior:

- Main copy fades in and moves up 12px.
- WhatsApp card enters first.
- Telegram card enters second.
- Personalized Alerts card enters third.
- Preference chip rows reveal with a short stagger.
- CTA buttons get a small hover lift.
- Animation runs once only.

Recommended CSS:

```css
.government-job-alerts [data-scroll-reveal] {
  opacity: 0;
  transform: translateY(12px);
  transition:
    opacity 360ms ease,
    transform 360ms ease,
    box-shadow 220ms ease;
}

.government-job-alerts.is-visible [data-scroll-reveal] {
  opacity: 1;
  transform: translateY(0);
}

.government-job-alerts.is-visible [data-scroll-reveal="copy"] {
  transition-delay: 0ms;
}

.government-job-alerts.is-visible [data-scroll-reveal="whatsapp"] {
  transition-delay: 120ms;
}

.government-job-alerts.is-visible [data-scroll-reveal="telegram"] {
  transition-delay: 220ms;
}

.government-job-alerts.is-visible [data-scroll-reveal="preferences"] {
  transition-delay: 320ms;
}

.government-job-alerts.is-visible [data-scroll-reveal="chip-strip"] {
  transition-delay: 430ms;
}

.government-job-alerts .alert-card {
  min-height: 220px;
  display: grid;
  justify-items: center;
  align-content: center;
  gap: 14px;
  text-align: center;
}

.government-job-alerts .alert-status-dot {
  width: 44px;
  height: 44px;
  border-radius: 999px;
  display: inline-block;
}

.government-job-alerts .alert-status-dot--whatsapp {
  background: #16a34a;
}

.government-job-alerts .alert-status-dot--telegram {
  background: #2563eb;
}

.government-job-alerts .alert-status-dot--personalized {
  background: #7c3aed;
}

.government-job-alerts .alert-preference-strip {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.government-job-alerts .alert-card:hover,
.government-job-alerts .alert-cta:hover {
  transform: translateY(-3px);
}

@media (max-width: 767px) {
  .government-job-alerts .alert-preference-strip {
    grid-template-columns: 1fr;
  }
}
```

Recommended JavaScript:

```js
const alertsSection = document.querySelector('.government-job-alerts');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (alertsSection && !reduceMotion) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      alertsSection.classList.add('is-visible');
      observer.disconnect();
    });
  }, { threshold: 0.25 });

  observer.observe(alertsSection);
}
```

Reduced motion:

```css
@media (prefers-reduced-motion: reduce) {
  .government-job-alerts [data-scroll-reveal],
  .government-job-alerts .alert-card:hover,
  .government-job-alerts .alert-cta:hover {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## Suggested HTML Structure

```html
<section class="government-job-alerts" aria-labelledby="job-alerts-title">
  <div data-scroll-reveal="copy">
    <p>Never miss an important update</p>
    <h2 id="job-alerts-title">Government Job Alerts on WhatsApp &amp; Telegram</h2>
    <p>
      Get timely Sarkari Naukri updates for new vacancies, last dates, admit
      cards, results and exam alerts. Choose your preferred channel and follow
      jobs that match your profile.
    </p>
    <p>Set alerts by qualification, department, exam and location.</p>
  </div>

  <div class="alert-card-grid">
    <article class="alert-card" data-scroll-reveal="whatsapp">
      <p>WhatsApp</p>
      <span class="alert-status-dot alert-status-dot--whatsapp" aria-hidden="true"></span>
      <h3>WhatsApp Job Alerts</h3>
      <a
        class="alert-cta"
        href="https://www.searchsarkarinaukri.com/job-alerts/whatsapp"
        aria-label="Join WhatsApp government job alerts"
      >
        Join WhatsApp Alerts
      </a>
    </article>

    <article class="alert-card" data-scroll-reveal="telegram">
      <p>Telegram</p>
      <span class="alert-status-dot alert-status-dot--telegram" aria-hidden="true"></span>
      <h3>Telegram Job Alerts</h3>
      <a
        class="alert-cta"
        href="https://www.searchsarkarinaukri.com/job-alerts/telegram"
        aria-label="Join Telegram government job alerts"
      >
        Join Telegram Alerts
      </a>
    </article>

    <article class="alert-card" data-scroll-reveal="preferences">
      <p>Personalised</p>
      <span class="alert-status-dot alert-status-dot--personalized" aria-hidden="true"></span>
      <h3>Personalized Job Alerts</h3>
      <a
        class="alert-cta"
        href="https://www.searchsarkarinaukri.com/job-alerts/preferences"
        aria-label="Set personalized Sarkari Naukri alert preferences"
      >
        Set My Preferences
      </a>
    </article>
  </div>

  <div class="alert-preference-strip" data-scroll-reveal="chip-strip">
    <div>
      <p>By Qualification</p>
      <a href="/jobs?qualification=10th-pass">10th</a>
      <a href="/jobs?qualification=12th-pass">12th</a>
      <a href="/jobs?qualification=graduate">Graduate</a>
    </div>

    <div>
      <p>By Location</p>
      <a href="/jobs?state=maharashtra">Maharashtra</a>
      <a href="/jobs?city=pune">Pune</a>
    </div>

    <div>
      <p>By Job Category</p>
      <a href="/jobs?category=mpsc">MPSC</a>
      <a href="/jobs?category=upsc">UPSC</a>
      <a href="/jobs?category=railway">Railway</a>
    </div>
  </div>
</section>
```

---

## Quality Checklist

- [ ] Section is focused on Government Job Alerts, not exam countdown.
- [ ] WhatsApp and Telegram actions are visually clear.
- [ ] Preference chips are useful internal links.
- [ ] Copy avoids fake urgency or unverifiable claims.
- [ ] Scroll animation runs once.
- [ ] Reduced-motion users get static content.
- [ ] All CTAs are crawlable anchor links.
