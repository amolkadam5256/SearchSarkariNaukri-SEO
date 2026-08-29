# SearchSarkariNaukri.com --- Homepage Hero Section Implementation Specification

**Purpose:** Final SEO + UX + accessibility + performance implementation
for the homepage Hero Section\
**Design reference:**
`01_Home_Page/01_HeroSection/Demo_ui_for_HeroSection.png` (the supplied
1364 px x 500 px PNG)\
**Status:** Ready for implementation\
**Constraint:** Do not change the approved Hero wording, hierarchy, CTA
destinations, or visual design direction defined in this document.

---

## 1. Implementation Rule

This document covers **ONLY the homepage Hero Section**.

Do not use this document to modify:

- Homepage Section 2
- Qualification section
- District section
- Department section
- Exam section
- Results
- Admit Cards
- News
- Blogs
- Current Affairs
- Study Material
- Footer
- Individual job pages
- District pages
- Qualification pages

Those sections will be handled separately.

The Hero must establish the homepage's broad search intent:

> **Sarkari Naukri 2026**

The Hero must not attempt to rank for every category, department,
qualification, district, or exam.

---

# 2. Approved Hero Content --- Use Exactly

## H1

**Sarkari Naukri 2026 -- Latest Government Jobs & Vacancies in India**

Do not change the wording, punctuation, or keyword order without a
separate SEO review.

## Supporting paragraph

**Find the latest Sarkari Naukri 2026 and government job vacancies
across India, including Maharashtra. Search jobs by qualification,
district, department and exam, check eligibility and important dates,
and verify the official recruitment notification before applying.**

Use this as normal HTML text. Do not convert it into an image.

## Search placeholder

**Search government jobs by keyword, department or location**

## Primary CTA

**Search Government Jobs**

Destination:

`/jobs`

## Secondary CTA

**Browse Maharashtra Jobs**

Destination:

`/districts`

## Small utility link

**Check Eligibility**

Destination:

`/eligibility-checker`

## Trust line

**Independent job information portal. Always verify vacancy details with
the official recruitment notification.**

---

# 3. Final Hero Layout

Implement the Hero in this order:

```text
TOP NEWS / JOB TICKER
        ↓
HERO BACKGROUND / VISUAL
        ↓
OPTIONAL STATUS / UPDATE BADGES
        ↓
H1
Sarkari Naukri 2026 – Latest Government Jobs & Vacancies in India
        ↓
SUPPORTING PARAGRAPH
        ↓
SEARCH BOX
Search government jobs by keyword, department or location
        ↓
PRIMARY CTA
Search Government Jobs
        ↓
SECONDARY CTA
Browse Maharashtra Jobs
        ↓
UTILITY LINK
Check Eligibility
        ↓
TRUST LINE
Independent job information portal...
        ↓
OPTIONAL TRUST / BENEFIT STRIP
```

The supplied PNG should be treated as the visual source of truth for the
Hero's overall composition, spacing, dark-blue background treatment,
orange accent, rounded search bar, CTA treatment, trust banner, and
bottom benefit strip.

---

# 4. Supplied Hero PNG --- Design Instruction

The supplied asset is:

`Demo_ui_for_HeroSection.png`

Dimensions:

`1364 px x 500 px`

Use the supplied PNG as the **Hero banner/background design reference**.

## Do not alter the approved visual direction

Do not:

- recolor the background
- replace the blue/orange visual system
- add unrelated graphics
- change the overall composition
- change the CTA style
- change the search-bar concept
- replace the Maharashtra visual treatment
- add a different hero illustration
- add a large video
- add an unnecessary carousel
- add visual clutter

## Important implementation rule

The PNG is a UI/design image containing text and interface elements. For
the production website, the SEO-critical text and controls must remain
**real HTML elements**, not text baked into the background image.

Therefore:

- use the PNG to reproduce the visual/background treatment;
- recreate H1, paragraph, search input, buttons, links, trust line and
  benefit items as live HTML;
- do not rely on image text for SEO, accessibility, or interaction;
- do not visually render the same text twice.

If the exact PNG is used literally as the CSS background, the
implementation must prevent duplicate visible text/UI from appearing
over the baked-in screenshot. Prefer using the PNG as the visual
design/background reference and reproduce the live Hero UI in HTML/CSS.

---

# 5. Hero H1 SEO Requirement

There must be exactly **one homepage H1**.

Use:

```text
Sarkari Naukri 2026 – Latest Government Jobs & Vacancies in India
```

The H1 must:

- exist in server-rendered HTML;
- be visible to users;
- be available without requiring JavaScript execution;
- not be hidden;
- not be duplicated;
- not be inside an image;
- not be replaced with an icon;
- not be visually replaced by pseudo-elements.

Do not add another H1 anywhere else in the Hero.

---

# 6. H1 Keyword Strategy

Primary keyword:

**Sarkari Naukri 2026**

Supporting topical terms:

- Latest Government Jobs
- Government Jobs
- Vacancies
- India

The Hero should not repeat `Sarkari Naukri 2026` multiple times in every
line.

The keyword should appear naturally in:

1.  Homepage title
2.  Homepage H1
3.  Hero paragraph
4.  relevant homepage content below the Hero

Do not force keyword density.

---

# 7. Hero Paragraph SEO Strategy

Use the approved paragraph exactly:

> Find the latest Sarkari Naukri 2026 and government job vacancies
> across India, including Maharashtra. Search jobs by qualification,
> district, department and exam, check eligibility and important dates,
> and verify the official recruitment notification before applying.

This paragraph establishes the semantic relationships:

```text
Sarkari Naukri 2026
        ↓
Government Job Vacancies
        ↓
India
        ↓
Maharashtra
        ↓
Qualification
        ↓
District
        ↓
Department
        ↓
Exam
        ↓
Eligibility
        ↓
Important Dates
        ↓
Official Recruitment Notification
```

Do not add a long keyword paragraph below it.

---

# 8. Hero Search Interface

The search interface is a core part of the Hero.

## Label

Use an accessible label:

**Search Government Jobs**

The label must exist even if it is visually hidden.

## Input placeholder

**Search government jobs by keyword, department or location**

## Search behavior

The form should send the user to the site's real job-search
functionality.

Primary destination:

`/jobs`

Do not create a fake search interaction.

Do not make the search box decorative.

---

# 9. Search Input Accessibility

Use a real:

```html
<input type="search" />
```

with an associated label.

Example implementation structure:

```html
<label for="hero-job-search"> Search Government Jobs </label>

<input
  id="hero-job-search"
  name="search"
  type="search"
  placeholder="Search government jobs by keyword, department or location"
/>
```

The actual query parameter must match the application's existing search
implementation.

Do not invent a new query parameter if the existing `/jobs` search
system already defines one.

---

# 10. Primary CTA

## Text

**Search Government Jobs**

## Destination

`/jobs`

Use a normal crawlable link or a real form submission depending on the
application's existing search implementation.

The visible CTA text must remain exactly:

**Search Government Jobs**

Avoid:

- Search Now
- Explore
- Find More
- Get Started
- Click Here

The approved CTA is more descriptive and directly communicates the
action.

---

# 11. Secondary CTA

## Text

**Browse Maharashtra Jobs**

## Destination

`/districts`

This is the main Hero path into the Maharashtra location architecture.

Do not change this to a search query URL.

Preferred:

`/districts`

Not:

`/jobs?search=Maharashtra`

The district hub should then connect users to individual Maharashtra
district pages.

---

# 12. Utility Link

## Text

**Check Eligibility**

## Destination

`/eligibility-checker`

This is a secondary utility, not the primary Hero conversion.

Visual hierarchy:

```text
Search Government Jobs       ← Primary
Browse Maharashtra Jobs      ← Secondary
Check Eligibility            ← Utility
```

Do not give all three identical visual weight.

---

# 13. Hero Trust Line

Use exactly:

**Independent job information portal. Always verify vacancy details with
the official recruitment notification.**

This should be visually smaller than the H1 and main paragraph.

The trust line must not claim:

- government ownership;
- government affiliation;
- official government status;
- government authorization;
- guaranteed recruitment information.

The site is an independent job-information portal.

---

# 14. Optional Top Ticker

The supplied Hero design contains a top orange/red job-update ticker.

If the existing homepage already has a live ticker, retain the design
concept.

Recommended purpose:

- latest active job
- application deadline
- recruitment update

The ticker must contain only current/valid data.

## Critical rule

Never display:

- expired jobs as active;
- closed applications as new;
- duplicate jobs;
- fake urgency;
- permanently hard-coded old dates.

If a job expires, it must be removed or updated automatically.

---

# 15. Ticker SEO Rule

The ticker is secondary content.

It must never replace the Hero H1.

Correct:

```text
Ticker
↓
H1
↓
Paragraph
↓
Search
```

Incorrect:

```text
Ticker
↓
Large job title as H1
↓
Sarkari Naukri content
```

The homepage's broad intent must remain:

**Sarkari Naukri 2026**

---

# 16. Top Status Badge

The supplied design contains:

**#1 Career Platform in Maharashtra**

and:

**LAST UPDATED: 27 AUGUST 2026**

These are visual design elements.

## Recommendation

Do not make unsupported superlative claims.

If the site cannot substantiate:

> #1 Career Platform in Maharashtra

do not publish that claim as factual SEO content.

If retained as a design badge, it must be replaced with a truthful,
supportable statement.

A safer version is:

**#1 Career Platform in Maharashtra**

or:

**#1 Career Platform in Maharashtra**

For the date badge, make the date dynamic.

Do not hard-code a date that becomes stale.

---

# 17. Hero Benefit Strip

The supplied design includes:

- 10th Pass to Graduation
- 500+ Exams Tracked
- Daily Job Updates
- Official Notifications
- 100% Free to Use

These can remain as supporting UX signals **only when factually
accurate**.

## Important

Every number must be dynamically derived from the application/database
where possible.

Do not hard-code:

`500+ Exams Tracked`

unless the site's actual inventory supports it.

Do not claim:

`100% Free to Use`

if any required feature or service has a paid component.

The most important benefit is:

**Official Notifications**

but the wording should not imply that SearchSarkariNaukri itself is the
recruiting authority.

---

# 18. Recommended Benefit Strip

If the existing facts are verified, use:

```text
10th Pass to Graduation
500+ Exams Tracked
Daily Job Updates
Official Notifications
100% Free to Use
```

Keep the wording concise.

Do not turn these into keyword blocks.

---

# 19. Hero Visual Hierarchy

The supplied design should follow this hierarchy:

```text
1. H1
2. Supporting paragraph
3. Search interface
4. Primary CTA
5. Maharashtra CTA
6. Eligibility utility
7. Trust statement
8. Supporting benefit badges
```

The background must remain subordinate to the content.

The background must never make the H1 difficult to read.

---

# 20. Hero Desktop Layout

Target structure:

```text
-----------------------------------------------------
Top update ticker
-----------------------------------------------------

             status / update badges

     Sarkari Naukri 2026 –
     Latest Government Jobs &
     Vacancies in India

      supporting paragraph

  [ 🔍 Search ...                  ]
  [                     Search Government Jobs ]

      [ Browse Maharashtra Jobs ]
      [ Check Eligibility ]

 [ Independent job information portal... ]

 [10th] [500+ Exams] [Daily Updates]
 [Official] [Free]
-----------------------------------------------------
```

Use the supplied PNG as the visual composition reference.

---

# 21. Hero Mobile Layout

Mobile order must be:

```text
Ticker
↓
Status badge
↓
H1
↓
Paragraph
↓
Search input
↓
Search Government Jobs
↓
Browse Maharashtra Jobs
↓
Check Eligibility
↓
Trust line
↓
Benefit strip
```

Do not place a large image above the H1.

Do not allow the background artwork to push the H1 below the first
viewport unnecessarily.

---

# 22. Mobile Performance Requirement

The previous audit identified poor mobile performance:

- Mobile Performance: 42
- Mobile LCP: 8.54 seconds
- Mobile TBT: 714 ms

Therefore the Hero must be implemented as a lightweight component.

Avoid loading unnecessary JavaScript before the Hero becomes
interactive.

Do not add:

- video backgrounds;
- large animation libraries;
- unnecessary sliders;
- social embeds;
- YouTube embeds;
- heavy third-party widgets;
- unnecessary tracking scripts inside the Hero.

---

# 23. Hero Background Performance

If the supplied PNG is used as a background asset, optimize the
production asset.

Do not serve an unnecessarily large image if a smaller responsive asset
provides the same visual result.

Preferred strategy:

```text
Desktop:
appropriate desktop background

Tablet:
appropriately sized background

Mobile:
mobile-optimized background if required
```

If a mobile-specific crop is necessary, create it as an optimized
production asset while preserving the approved design.

Do not load the full 1364 px x 500 px source at excessive byte size on
every mobile device.

---

# 24. LCP Rule

Determine whether the Hero background or another Hero element becomes
the Largest Contentful Paint element.

If the background is LCP-critical:

- optimize it aggressively;
- preload only when justified;
- avoid late-loading the primary visual;
- ensure text is immediately available.

If the background is not LCP-critical, do not prioritize it above the
HTML Hero content.

The H1 and primary content must be available immediately.

---

# 25. Do Not Lazy-Load Critical Hero Content

Do not lazy-load:

- H1;
- paragraph;
- search input;
- primary CTA;
- critical Hero background if it is the LCP asset.

Lazy loading is for below-the-fold content, not the core Hero.

---

# 26. Accessibility

The Hero must pass WCAG-oriented accessibility checks.

Required:

- one H1;
- accessible search label;
- visible keyboard focus;
- descriptive CTA names;
- sufficient color contrast;
- semantic links;
- semantic form controls;
- no text embedded only in images;
- no inaccessible icon-only buttons;
- no keyboard trap;
- no content obscured by notification UI.

---

# 27. Icon Rules

Icons shown in the supplied design are decorative unless they
communicate unique information.

Use:

```html
aria-hidden="true"
```

for purely decorative icons.

Do not use an icon as the only accessible name of:

- Search
- Browse Maharashtra Jobs
- Check Eligibility

The text must remain available.

---

# 28. Focus States

Every interactive Hero element must have a clear keyboard focus state:

- search input;
- search button;
- Maharashtra link;
- eligibility link;
- ticker links if clickable.

Do not remove browser focus outlines without replacing them with an
equally visible focus indicator.

---

# 29. Color / Contrast

The supplied design uses:

- dark blue background;
- white typography;
- orange CTA;
- light borders;
- green status accents.

Maintain the design direction but verify contrast programmatically.

Do not sacrifice accessibility for visual similarity.

The H1 must remain clearly readable against the background.

---

# 30. No Overlay Obstruction

The previous audit identified a mobile notification/onboarding layer.

The Hero must remain usable when such UI exists.

The following must never be covered:

- H1;
- search field;
- primary CTA;
- Maharashtra CTA;
- eligibility link.

Any notification prompt should appear outside the critical interaction
path.

---

# 31. SEO-Critical HTML

The production Hero must render the following as real HTML:

```text
H1
Paragraph
Search input
Search button
Browse Maharashtra Jobs link
Check Eligibility link
Trust statement
```

Do not make these elements part of a single image.

---

# 32. Suggested Semantic HTML

Recommended conceptual structure:

```html
<header>
  <div class="hero-ticker">...</div>

  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-content">
      <div class="hero-status">...</div>

      <h1 id="hero-title">
        Sarkari Naukri 2026 – Latest Government Jobs & Vacancies in India
      </h1>

      <p>
        Find the latest Sarkari Naukri 2026 and government job vacancies across
        India, including Maharashtra. Search jobs by qualification, district,
        department and exam, check eligibility and important dates, and verify
        the official recruitment notification before applying.
      </p>

      <form>...</form>

      <nav aria-label="Hero actions">
        <a href="/districts"> Browse Maharashtra Jobs </a>

        <a href="/eligibility-checker"> Check Eligibility </a>
      </nav>

      <p class="hero-trust">
        Independent job information portal. Always verify vacancy details with
        the official recruitment notification.
      </p>
    </div>
  </section>
</header>
```

Adapt the exact JSX/component structure to the existing Next.js
architecture.

Do not delete or rewrite unrelated working components.

---

# 33. Existing Features Must Not Be Broken

This Hero update must be additive and controlled.

Do not break:

- existing search;
- existing authentication;
- saved jobs;
- job alerts;
- reminders;
- analytics;
- existing routing;
- existing accessibility features;
- existing mobile navigation;
- existing notification system.

Only modify the Hero-specific presentation and SEO content.

---

# 34. Existing Search URL Handling

Before implementation, inspect the current `/jobs` search
implementation.

The Hero form must use the site's existing search contract.

Do not assume a parameter such as:

`?search=`

unless that is already how the application works.

The final Hero search must produce the same valid results as the
existing job-search interface.

---

# 35. Internal Linking From Hero

Only these three primary internal destinations should be used:

Hero element Destination

---

Search Government Jobs `/jobs`
Browse Maharashtra Jobs `/districts`
Check Eligibility `/eligibility-checker`

Do not add all districts, all qualifications, all departments and all
exams inside the Hero.

Those will be connected in later homepage sections.

---

# 36. Hero → Homepage Architecture

The Hero establishes three main paths:

```text
HOME HERO
│
├── Search Government Jobs
│       ↓
│      /jobs
│
├── Browse Maharashtra Jobs
│       ↓
│    /districts
│
└── Check Eligibility
        ↓
 /eligibility-checker
```

Later homepage sections will expand:

```text
Home
 ↓
Qualification
 ↓
District
 ↓
Department
 ↓
Exam
 ↓
Location + Qualification
 ↓
Individual Jobs
```

Do not overload Section 1 with this entire architecture.

---

# 37. Metadata Relationship

Hero content must align with the homepage metadata.

## Homepage title

**Sarkari Naukri 2026 -- Latest Government Jobs in India**

## Homepage H1

**Sarkari Naukri 2026 -- Latest Government Jobs & Vacancies in India**

## Homepage meta description

**Search the latest Sarkari Naukri 2026, government jobs, MPSC, SSC,
Railway, Banking and Police Bharti vacancies with official links.**

The Hero should not introduce a different primary keyword.

---

# 38. Primary Keyword Placement

Use the primary keyword in:

```text
Title
↓
H1
↓
Hero paragraph
↓
Later homepage sections
```

Do not repeat it in:

- every CTA;
- every icon;
- every badge;
- every image alt;
- every paragraph.

---

# 39. Image Alt Text

If the background image is purely decorative:

```text
alt=""
```

or use it as a CSS background without an image alt attribute.

Do not write a keyword-stuffed alt such as:

> Sarkari Naukri 2026 latest government jobs Maharashtra India
> government job banner

That is unnecessary.

If any separate meaningful image is used in the Hero, its alt text must
describe the actual image content.

---

# 40. Structured Data

Do not add a special Hero schema.

The Hero's SEO signals should come from:

- page title;
- H1;
- visible content;
- internal links;
- WebSite schema;
- Organization schema.

The homepage's other structured data should remain in their appropriate
sections.

Do not add duplicate WebSite or Organization schema while implementing
the Hero.

---

# 41. AEO Requirement

The Hero should give a concise answer to:

> What does SearchSarkariNaukri provide?

The paragraph already does this:

- government jobs;
- India;
- Maharashtra;
- qualification;
- district;
- department;
- exam;
- eligibility;
- dates;
- official notification verification.

Do not turn the Hero into a long FAQ.

---

# 42. Trust Requirement

The Hero must clearly avoid implying government affiliation.

Correct:

> Independent job information portal.

Incorrect:

> Official Government Job Portal.

Incorrect:

> Government Authorized Job Portal.

Incorrect:

> Official Government Recruitment Website.

The official recruiting authority remains the final source.

---

# 43. Mobile Typography

Use responsive typography.

The H1 must remain prominent but should not consume the entire mobile
screen.

Recommended implementation principle:

```text
Desktop:
large display heading

Tablet:
medium display heading

Mobile:
large but controlled heading
```

Do not hard-code the desktop font size for mobile.

The exact pixel values should follow the existing design system.

---

# 44. Hero Width

Use a constrained content container.

The supplied design demonstrates a centered content layout.

Recommended principle:

```text
full-width background
        ↓
centered max-width content
        ↓
H1 / paragraph / search
```

Do not let the paragraph become an extremely long single line on
desktop.

---

# 45. Paragraph Width

Keep the Hero paragraph readable.

Target:

- approximately 2--4 lines on desktop;
- approximately 4--7 lines on mobile depending on viewport width.

Do not make it a full-width paragraph across the screen.

---

# 46. Search Bar Width

The supplied design shows a wide centered search bar.

Retain that concept.

Desktop:

```text
wide search field + primary button
```

Mobile:

```text
search field
↓
full-width Search Government Jobs button
```

Avoid horizontal overflow.

---

# 47. CTA Touch Targets

All mobile interactive elements should have sufficiently large tap
areas.

Especially:

- Search Government Jobs
- Browse Maharashtra Jobs
- Check Eligibility

The original audit identified mobile tap-target issues, so this must be
explicitly regression-tested.

---

# 48. No Horizontal Overflow

Test:

- 320px
- 360px
- 375px
- 390px
- 414px

The Hero must not create horizontal scrolling.

The ticker should be clipped or horizontally scrolling in a controlled
way without expanding the page width.

---

# 49. Ticker Accessibility

If the ticker is animated:

- do not make it too fast;
- provide accessible links;
- respect `prefers-reduced-motion`;
- ensure keyboard users can access the content;
- do not cause layout shifts.

If it is not necessary, a static latest-job strip is preferable for
performance.

---

# 50. Performance Rule for Ticker

Do not fetch a large amount of data solely for the Hero ticker.

Only retrieve the minimum current records required.

Recommended:

```text
1–3 current job records
```

rather than loading the entire jobs dataset into the Hero.

---

# 51. Dynamic Data

The following can be dynamic:

- latest update date;
- current ticker jobs;
- benefit counts where factually measurable.

The following should remain stable SEO content:

- H1;
- Hero paragraph;
- CTA labels;
- trust statement.

Do not make the H1 dynamically change every day.

---

# 52. Do Not Put Current Job Titles in H1

The H1 must remain:

**Sarkari Naukri 2026 -- Latest Government Jobs & Vacancies in India**

Do not change it dynamically to a job title.

The ticker can show individual jobs.

---

# 53. Do Not Put District Name in H1

The homepage H1 should not become:

> Government Jobs in Pune

That belongs to the Pune page.

Homepage:

**Sarkari Naukri 2026**

District page:

**Government Jobs in Pune 2026**

This protects keyword ownership.

---

# 54. Do Not Put Qualification in H1

Likewise:

Homepage:

**Sarkari Naukri 2026**

Qualification page:

**12th Pass Government Jobs 2026**

This prevents cannibalization.

---

# 55. Do Not Put Department in H1

Homepage:

**Sarkari Naukri 2026**

MPSC page:

**MPSC Bharti 2026**

SSC page:

**SSC Recruitment 2026**

Railway page:

**Railway Jobs 2026**

The Hero must own the broad query.

---

# 56. Hero Content Density

Target:

- one H1;
- one supporting paragraph;
- one search interface;
- 2--3 actions;
- one trust line;
- optional compact benefits.

This is enough.

Do not add another 500 words.

---

# 57. Final Visual Design Direction

The supplied image should guide:

- dark blue background;
- subtle Maharashtra/India visual motif;
- orange primary CTA;
- white H1;
- orange primary keyword emphasis if consistent with the supplied
  design;
- rounded search box;
- rounded CTA buttons;
- subtle borders;
- compact trust banner;
- compact benefit strip.

Do not introduce a different visual system.

---

# 58. Important: Orange H1 Keyword

The supplied design visually emphasizes:

**Sarkari Naukri 2026 --**

in orange.

This can be retained.

The remaining H1 can remain white.

This is a visual styling choice and does not change the H1 semantics.

The H1 remains one HTML element:

```html
<h1>
  <span>Sarkari Naukri 2026 –</span>
  <span>Latest Government Jobs & Vacancies in India</span>
</h1>
```

Do not create two H1 elements.

---

# 59. Recommended H1 Markup

Conceptually:

```html
<h1>
  <span>Sarkari Naukri 2026 –</span>
  <span>Latest Government Jobs &amp; Vacancies in India</span>
</h1>
```

Both spans are part of the same H1.

The visual line break should be controlled with CSS, not a second
heading.

---

# 60. Recommended Search Markup

Conceptually:

```html
<form action="/jobs" method="GET">
  <label for="hero-job-search"> Search Government Jobs </label>

  <input
    id="hero-job-search"
    name="search"
    type="search"
    placeholder="Search government jobs by keyword, department or location"
  />

  <button type="submit">Search Government Jobs</button>
</form>
```

**Important:** confirm the real query parameter before implementation.
If the application uses a different search parameter, use the existing
implementation rather than inventing `name="search"`.

---

# 61. Link Markup

Conceptually:

```html
<a href="/districts"> Browse Maharashtra Jobs </a>

<a href="/eligibility-checker"> Check Eligibility </a>
```

These must be real links.

Do not use:

```html
<div onclick="..."></div>
```

for SEO navigation.

---

# 62. Hero Background CSS Principle

Conceptually:

```css
.hero {
  background-image: url("...");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
```

Adapt to the existing design system.

Do not inline a massive base64 image into the HTML.

Do not create a huge CSS payload.

---

# 63. Background Overlay

If the supplied background requires an overlay for text readability, use
a lightweight CSS overlay.

Do not bake additional text into the image.

Do not add a heavy image-processing library.

---

# 64. Production Asset Rule

The source PNG is a design asset.

For production:

1.  inspect actual file size;
2.  optimize it;
3.  generate an appropriate web format;
4.  provide responsive dimensions if needed;
5.  verify visual fidelity;
6.  test mobile LCP.

Do not ship an unnecessarily large original design file if it is several
megabytes.

---

# 65. No Unnecessary Third-Party Scripts

Do not initialize additional third-party scripts from the Hero
component.

Analytics, ads, notification services and other integrations should
follow the site's global loading strategy.

The Hero should remain as close to static HTML/CSS as practical.

---

# 66. Hero Rendering Parity

The Hero must be equivalent for:

- normal users;
- Googlebot;
- other search crawlers.

Do not change the H1, paragraph, links, canonical, schema, or core
content based on user-agent.

The previous audit identified rendering differences, so this must be
explicitly tested.

---

# 67. SSR / Initial HTML

The following must appear in the initial server-rendered HTML:

```text
Sarkari Naukri 2026 – Latest Government Jobs & Vacancies in India
Find the latest Sarkari Naukri 2026...
Search Government Jobs
Browse Maharashtra Jobs
Check Eligibility
Independent job information portal...
```

Do not require a client-side API call before the H1 appears.

---

# 68. Hydration Rule

The Hero may hydrate for search interaction and dynamic elements.

However:

- H1 should not wait for hydration;
- paragraph should not wait for hydration;
- internal links should not wait for hydration;
- trust statement should not wait for hydration.

---

# 69. Regression Test --- SEO

After implementation:

- [ ] Fetch homepage as normal browser
- [ ] Fetch homepage with Googlebot user agent
- [ ] Compare H1
- [ ] Compare Hero paragraph
- [ ] Compare links
- [ ] Compare canonical
- [ ] Compare title
- [ ] Compare meta description
- [ ] Confirm no duplicate H1
- [ ] Confirm no hidden SEO text

---

# 70. Regression Test --- Accessibility

Run:

- Lighthouse Accessibility
- axe
- keyboard navigation
- screen-reader check
- focus visibility
- mobile tap-target audit

Expected:

- no critical accessibility errors;
- no inaccessible Hero controls;
- no hidden focus state;
- no blocked search.

---

# 71. Regression Test --- Performance

Run mobile Lighthouse after implementation.

Focus on:

- LCP
- TBT / INP
- Speed Index
- CLS
- total transfer size
- JavaScript execution
- background image cost

The Hero implementation should improve or at least not worsen the
previous mobile performance baseline.

---

# 72. Regression Test --- Responsive

Test at:

```text
320px
360px
375px
390px
414px
768px
1024px
1280px
1440px
1536px
```

Check:

- H1 wrapping;
- search bar;
- buttons;
- ticker;
- background;
- trust line;
- benefit strip;
- no horizontal overflow.

---

# 73. Final Approved Hero Content Table

---

Element Final value

---

H1 **Sarkari Naukri 2026 -- Latest
Government Jobs & Vacancies in
India**

Paragraph **Find the latest Sarkari Naukri
2026 and government job vacancies
across India, including
Maharashtra. Search jobs by
qualification, district, department
and exam, check eligibility and
important dates, and verify the
official recruitment notification
before applying.**

Search placeholder **Search government jobs by
keyword, department or location**

Primary CTA **Search Government Jobs**

Primary URL `/jobs`

Secondary CTA **Browse Maharashtra Jobs**

Secondary URL `/districts`

Utility link **Check Eligibility**

Utility URL `/eligibility-checker`

Trust line **Independent job information
portal. Always verify vacancy
details with the official
recruitment notification.**

Primary keyword **Sarkari Naukri 2026**

Page intent **Broad government-job search /
discovery**

---

---

# 74. What Must Remain Unchanged

The approved Hero wording must remain unchanged:

```text
Sarkari Naukri 2026 – Latest Government Jobs & Vacancies in India

Find the latest Sarkari Naukri 2026 and government jobs across India and Maharashtra. Search by qualification, location, department or exam, and check eligibility and important dates.

Search government jobs by keyword, department or location

Search Government Jobs

Browse Maharashtra Jobs

Check Eligibility

Independent job information portal. Always verify vacancy details with the official recruitment notification.
```

Do not substitute alternate SEO copy during implementation.

---

# 75. What Developers Must NOT Do

Do not:

- create two H1 tags;
- hide duplicate SEO text;
- place all Hero text inside the PNG;
- keyword stuff;
- add invisible text;
- add hidden links;
- use an image as the only H1;
- make CTA links JavaScript-only;
- add unsupported government-affiliation claims;
- add fake review/trust numbers;
- hard-code expired ticker jobs;
- load the entire job database into the Hero;
- add a video background;
- add unnecessary animation;
- add a huge unoptimized image;
- block the search field with a popup;
- create new query URLs without checking the existing search contract;
- modify other homepage sections as part of this task.

---

# 76. Final Acceptance Criteria

The Hero is complete only when all of the following are true:

### SEO

- [ ] Exact approved H1 is implemented
- [ ] One H1 only
- [ ] Primary keyword is clear
- [ ] Supporting paragraph is implemented
- [ ] No keyword stuffing
- [ ] Core Hero text is server-rendered

### UX

- [ ] Search works
- [ ] `/jobs` CTA works
- [ ] `/districts` CTA works
- [ ] `/eligibility-checker` works
- [ ] Hero is visually consistent with supplied PNG
- [ ] Mobile layout works
- [ ] No overlay blocks Hero

### Accessibility

- [ ] Search has accessible label
- [ ] Buttons/links have descriptive names
- [ ] Keyboard focus works
- [ ] Contrast passes
- [ ] Decorative icons are not announced unnecessarily
- [ ] No tap-target failures

### Performance

- [ ] Background optimized
- [ ] No unnecessary Hero JavaScript
- [ ] No large video
- [ ] No unnecessary third-party scripts
- [ ] Mobile LCP does not regress
- [ ] No layout shift caused by Hero

### Technical

- [ ] Normal-user HTML contains Hero
- [ ] Googlebot HTML contains equivalent Hero
- [ ] No duplicate H1
- [ ] No duplicate visible text from PNG + HTML
- [ ] Internal links are crawlable
- [ ] Existing search implementation remains functional

---

# 77. Final Developer Instruction

Implement **only the homepage Hero Section** according to this document.

Use the supplied:

`Demo_ui_for_HeroSection.png`

as the exact visual/design reference for the Hero banner/background
treatment.

Use the approved copy exactly.

Keep the H1, paragraph, search, CTAs, trust statement, visual hierarchy,
dark-blue/orange design direction, rounded search interface and
responsive behavior consistent with the supplied design.

**Do not modify other homepage sections in this task.**

The Hero must be implemented as real, accessible, server-rendered
HTML/CSS rather than depending on text embedded in an image.

After implementation, run:

1.  HTML/SSR check
2.  Googlebot rendering comparison
3.  Lighthouse mobile
4.  Lighthouse desktop
5.  axe accessibility
6.  responsive viewport test
7.  search-form test
8.  internal-link test

Only after this Hero passes QA should the implementation proceed to
Homepage Section 2.
