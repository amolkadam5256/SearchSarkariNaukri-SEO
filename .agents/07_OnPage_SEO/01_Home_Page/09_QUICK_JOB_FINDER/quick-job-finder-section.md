# Quick Job Finder Section

## Section Placement

Place this section after:

```text
08_EXISTING_TALATHI_FEATURED_RECRUITMENT
```

and before:

```text
10_LATEST_SARKARI_NAUKRI
```

---

## Section Goal

Help users quickly find government jobs by qualification, Maharashtra city
or district, recruiting organization, exam authority and latest updates.

This section should work like a compact internal-link hub, not a long SEO
block.

---

## Final UI Content

Section label:

```text
Quick Links
```

Heading/supporting line:

```text
Find government jobs faster by qualification, location & exam
```

---

## Creative UI Format

Use this exact 4-card layout:

```text
┌─────────────────────────────────────────────────────────────────────┐
│                         QUICK LINKS                                 │
│     Find government jobs faster by qualification, location & exam    │
│                                                                     │
│  ┌─────────────────────┐  ┌─────────────────────┐                  │
│  │ Qualification       │  │ Maharashtra Jobs     │                  │
│  │                     │  │                     │                  │
│  │ 10th Pass           │  │ Mumbai   Pune       │                  │
│  │ 12th Pass           │  │ Nagpur   Nashik     │                  │
│  │ Graduate            │  │ Latur    Thane      │                  │
│  │ Post Graduate       │  │ Beed     Solapur    │                  │
│  │                     │  │                     │                  │
│  │ View All            │  │ All Districts        │                  │
│  └─────────────────────┘  └─────────────────────┘                  │
│                                                                     │
│  ┌─────────────────────┐  ┌─────────────────────┐                  │
│  │ Organizations       │  │ Latest Updates       │                  │
│  │                     │  │                     │                  │
│  │ MPSC   UPSC   SSC   │  │ Latest Govt Job      │                  │
│  │ Railway  Banking    │  │ Notifications        │                  │
│  │ Police  ZP Jobs     │  │                     │                  │
│  │ DRDO   RRB   BARC   │  │ UPSC Updates         │                  │
│  │                     │  │                     │                  │
│  │ Explore Jobs        │  │ Read Updates         │                  │
│  └─────────────────────┘  └─────────────────────┘                  │
└─────────────────────────────────────────────────────────────────────┘
```

Design direction:

- Use a clean quick-access panel with 4 equal cards.
- Use real icons or small category markers for each card.
- Keep text short and scannable.
- Make every item a crawlable internal link where possible.
- Keep card radius modest and consistent with the homepage UI.
- Avoid a giant keyword list.

---

## Card 1: Qualification

Title:

```text
Qualification
```

Links:

```text
10th Pass
12th Pass
Graduate
Post Graduate
View All
```

Recommended URLs:

```text
/jobs?qualification=10th-pass
/jobs?qualification=12th-pass
/jobs?qualification=graduate
/jobs?qualification=post-graduate
/jobs-by-qualification
```

SEO intent:

```text
government jobs by qualification
10th pass government jobs
12th pass government jobs
graduate government jobs
```

---

## Card 2: Maharashtra Jobs

Title:

```text
Maharashtra Jobs
```

Links:

```text
Mumbai
Pune
Nagpur
Nashik
Latur
Thane
Beed
Solapur
All Districts
```

Recommended URLs:

```text
/jobs?city=mumbai
/jobs?city=pune
/jobs?city=nagpur
/jobs?city=nashik
/jobs?city=latur
/jobs?city=thane
/jobs?district=beed
/jobs?district=solapur
/maharashtra-government-jobs
```

SEO intent:

```text
Maharashtra government jobs
government jobs in Mumbai
government jobs in Pune
district wise government jobs Maharashtra
```

---

## Card 3: Organizations

Title:

```text
Organizations
```

Links:

```text
MPSC
UPSC
SSC
Railway
Banking
Police
ZP Jobs
DRDO
RRB
BARC
Explore Jobs
```

Recommended URLs:

```text
/jobs?organization=mpsc
/jobs?organization=upsc
/jobs?organization=ssc
/jobs?category=railway
/jobs?category=banking
/jobs?category=police
/jobs?category=zp-jobs
/jobs?organization=drdo
/jobs?organization=rrb
/jobs?organization=barc
/organizations
```

SEO intent:

```text
MPSC jobs
UPSC recruitment
SSC government jobs
Railway recruitment
Police recruitment
ZP jobs Maharashtra
```

---

## Card 4: Latest Updates

Title:

```text
Latest Updates
```

Links:

```text
Latest Govt Job Notifications
UPSC Updates
Read Updates
```

Recommended URLs:

```text
/latest-government-jobs
/upsc-updates
/job-news
```

SEO intent:

```text
latest government job notifications
latest Sarkari Naukri updates
UPSC latest updates
government job news
```

---

## Responsive UI Direction

Desktop:

```text
2 x 2 card grid
Each card contains title, compact links and footer CTA
```

Tablet:

```text
2 x 2 card grid
Reduce link spacing
Keep card heights balanced
```

Mobile:

```text
Single-column card stack
Qualification
Maharashtra Jobs
Organizations
Latest Updates
```

Mobile rules:

- Keep link groups easy to tap.
- Use 2-column mini link grids inside long cards.
- Avoid horizontal overflow.
- Keep the section heading short.
- Do not use large hero-style typography.

---

## Scroll Animation Direction

Use a soft scroll reveal:

```text
Section title appears first
Card 1 appears second
Card 2 appears third
Card 3 appears fourth
Card 4 appears fifth
```

Motion rules:

- Cards should move upward slightly.
- Stagger cards by 80-100ms.
- Add a small hover lift for cards.
- Underline or highlight links on hover.
- Run animation once only.
- Respect reduced-motion settings.

---

## Keyword Targeting

Primary keyword:

```text
find government jobs
```

Secondary keywords:

```text
government jobs by qualification
Maharashtra government jobs
latest government job notifications
MPSC jobs
UPSC updates
SSC recruitment
Railway jobs
Police recruitment
ZP jobs Maharashtra
government jobs in Pune
government jobs in Mumbai
```

Use keywords naturally through card titles, link text and link destinations.

Do not add paragraph-heavy SEO content inside this section.

---

## Internal Linking Rules

- Every visible item should be a real link where a relevant destination exists.
- Use short anchor text.
- Avoid duplicate anchors pointing to unrelated pages.
- Prefer filtered job pages for city, qualification and category links.
- Use `/organizations` for the full organization directory.
- Use `/job-news` for the broader update/news destination.

---

## Quality Checklist

- [ ] Section is small and scannable.
- [ ] Layout uses 4 cards in a 2 x 2 grid on desktop.
- [ ] Cards stack cleanly on mobile.
- [ ] All links are crawlable internal links.
- [ ] Keywords are present through natural link text.
- [ ] Section does not become a long SEO paragraph.
- [ ] Hover and scroll animation are subtle.
- [ ] Reduced-motion users are respected.

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
